import sympy as sp
import numpy as np
from scipy.integrate import odeint
import Functions


class FunctionCompiler:
    def __init__(self, object_list, fixed_parameter, fixed_param_val):
        self.object_list = object_list
        self._assigned = False

        # if fixed_parameter is not a list, make it a list
        if not isinstance(fixed_parameter, list):
            fixed_parameter = [fixed_parameter]
        self.fixed_parameter = fixed_parameter
        if not isinstance(fixed_param_val, list):
            fixed_param_val = [fixed_param_val]
        self.fixed_param_val = fixed_param_val
        self.fixed_param_dict = {name: val for name, val in zip(fixed_parameter, fixed_param_val)}

    # assigns names and variable indices to objects
    def _assign_indices(self):
        if self._assigned:
            return

        self.indices = []
        N = 0

        index_dict = {}

        for obj in self.object_list:
            # make an unique number sequence for each object type
            if obj.name in index_dict:
                index_dict[obj.name] += 1
                numb = index_dict[obj.name]
            else:
                index_dict[obj.name] = 1
                numb = 1

            obj.name = f"{obj.name}{numb}"  # make one-based numbering
            obj.data_index = obj.loc
            obj.init_object()

            if N < max(obj.loc):
                N = max(obj.loc)

        self.N = N
        self.object_dict = {obj.name: obj for obj in self.object_list}
        self._assigned = True

        print('Generated objects are:', " ".join(self.object_dict.keys()))

        # TODO: add complex object initialization support

    # substitutes expressions for currents, like I_JJ1, into another equations
    def _substitute_element_currents(self):
        new_eq = []

        for eqn in self.another_eq:
            for curr_eqn in self.current_eq:
                curr_sym, curr_val = curr_eqn.lhs, curr_eqn.rhs
                eqn = eqn.subs(curr_sym, curr_val)
            new_eq.append(eqn)

        self.final_system = new_eq

    def _fix_param(self):
        # uses:
        # self.needed_eqns
        # MATRIX: A, X, B
        # self.s_lin
        # self.ind_order1
        # object list
        # number od objects
        # fixed parameter
        A = self.A
        mas_a = sp.Matrix()
        size_a = A.cols

        for k in range(size_a):
            mas_a = mas_a.col_join(A.col(k))
        mas_a = list(mas_a)

        def process_equations(sys_eq):
            sys_eq_new = [None] * len(sys_eq)
            # substitute P(i) instead of fixed parameters
            p = sp.symbols("P")
            for i, par in enumerate(self.fixed_parameter):
                par_symbol = sp.sympify(self.fixed_param_dict[par]) # sp.Indexed(p, i + 1)
                for j, eqn in enumerate(sys_eq):
                    sys_eq_new[j] = eqn.subs(sp.symbols(par), par_symbol)

            # substitute object parameters and N
            obj_dict = self.object_dict
            n = sp.symbols('N')
            for i in range(len(sys_eq_new)):
                eqn = sys_eq_new[i]
                for sym in eqn.free_symbols:
                    strsym = str(sym)
                    if '.' in strsym:
                        obj, prop = strsym.split('.')
                        obj = obj_dict[obj]
                        eqn = eqn.subs(sym, getattr(obj, prop))
                eqn = eqn.subs(n, self.N)
                sys_eq_new[i] = eqn

            return sys_eq_new

        self.lin_eq = process_equations(self.s_lin)
        self.diff_eq = process_equations(self.needed_eqns)
        self.out_B = process_equations(self.B)
        self.out_X = process_equations(self.X)  # substitute N
        out_mas_a = process_equations(mas_a)

        # make a new A matrix
        out_A = []
        for i in range(size_a):
            out_A.append(out_mas_a[i*size_a: (i+1)*size_a])
        out_A = sp.Matrix(out_A)

        self.out_A = out_A

    def _prepair_matrix(self):
        def is_base_equation(eqn):
            left_part = eqn.lhs
            right_part = eqn.rhs

            if left_part.args[0].args[1].func == sp.core.add.Add:
                return True  # if '+' in index

            # if not, find te right part
            # if see 'd' operation, this equation is needed
            def find_d(expr):
                if expr.func == sp.core.function.Derivative:
                    return True
                else:
                    for arg in expr.args:
                        if find_d(arg):
                            return True
                return False
            return find_d(right_part)

        X = []
        B = []

        eqns_for_second_derivative = []
        base_eqns_idx = []
        # Find equations only of type dy(N+1) = ... or d(...)=d(...)

        for i, eqn in enumerate(self.final_system):
            if not is_base_equation(eqn):
                eqns_for_second_derivative.append(eqn)
            else:
                X.append(eqn.lhs)
                base_eqns_idx.append(i)

        n_eqns = len(X)
        A = sp.eye(n_eqns, n_eqns)

        # walk over selected equations and make a matrix row for it
        for i, n_eqn in enumerate(base_eqns_idx):
            eqn = self.final_system[n_eqn].rhs

            # find coefficients before all possible terms
            for j, term in enumerate(X):
                coef = eqn.coeff(term)
                A[i, j] += coef

            # make residual term (B), without terms which are multipliers of X
            for term in X:
                eqn = eqn.subs(term, 0)
            B.append(eqn)

        # save results
        self.X = X
        self.A = A
        self.B = B
        self.needed_eqns = eqns_for_second_derivative

    def _kill_lin_pins(self, eq):
        y = sp.symbols("y")
        psi = sp.symbols('psi')

        subs_list = []

        for idx in self.k_lin:
            symb_old = sp.Indexed(y, idx)
            symb_new = sp.Indexed(psi, idx)
            subs_list.append((symb_old, symb_new))

        eq_new = [eqi.subs(subs_list) for eqi in eq]
        return eq_new

    def _get_coef(self, equation, psi_vars):
        # uses:
        # KLin -> self.k_lin

        coef = []
        all_not_coef = sp.sympify(0)

        for var in psi_vars:
            now_coef = equation.coeff(var)
            coef.append(now_coef)
            all_not_coef += now_coef * var

        free_term = equation - all_not_coef

        return coef, -free_term

    def _form_lin_matrix(self):
        # uses:
        # LinEq -> self.lin_eq
        # KLin -> self.k_lin
        # N - self.N

        # substitute currents from equations like 'I_'=...

        # is expression like 'I_...', for example, I_1 or I_JJ4
        def is_curr_symbol(s):
            return s.func == sp.tensor.indexed.Indexed and str(s.args[0]) == 'I'

        # does expression contain terms like I_...
        def is_curr_in_equation(s):
            for smb in s.free_symbols:
                if is_curr_symbol(smb):
                    return True
            return False

        lin_eq = self._kill_lin_pins(self.lin_eq)
        lin_eq_2 = []
        list_to_replace = []

        for eqn in lin_eq:
            if is_curr_symbol(eqn.lhs) and not is_curr_in_equation(eqn.rhs) and eqn.rhs != 0:
                list_to_replace.append((eqn.lhs, eqn.rhs))
            else:
                lin_eq_2.append(eqn)

        lin_eq2 = [i.subs(list_to_replace) for i in lin_eq_2]

        A_lin = []
        B_lin = []

        psi = sp.symbols("psi")
        psi_vars = [sp.Indexed(psi, i) for i in self.k_lin]

        for eqn in lin_eq2:
            coeffs, free_term = self._get_coef(eqn.lhs, psi_vars)
            A_lin.append(coeffs)
            B_lin.append(free_term)

        self.A_lin = A_lin
        self.B_lin = B_lin
        self.x_lin = psi_vars

    def compile(self):
        self._assign_indices()
        # TODO: add complex object initialization support

        s_pre = [obj.get_equation() for obj in self.object_list]
        S = [sp.sympify(0)] * self.N

        ode_eq_o1 = []
        ode_eq_1 = []
        ode_eq_2 = []
        ind_order1 = []
        s_lin = []
        k_lin = []

        # write equations for network nodes
        for i in range(1, self.N + 1):  # loc==0 means a ground, don't consider it as a node
            s_lin_pre = []
            order = 0

            for k, obj in enumerate(self.object_list):
                if obj.data_index[0] == i:
                    S[i - 1] -= obj.var_current()
                    if obj.order == 0 and order == 0:
                        s_lin_pre.append(s_pre[k])
                    elif obj.order == 1 and order == 0:
                        order = 1
                        s_lin_pre = []
                    elif obj.order == 2:
                        order = 2
                        s_lin_pre = []

                elif len(obj.data_index) > 1 and obj.data_index[1] == i:
                    S[i - 1] += obj.var_current()
                    if obj.order == 0 and order == 0:
                        s_lin_pre.append(s_pre[k])
                    elif obj.order == 1 and order == 0:
                        order = 1
                    elif obj.order == 2:
                        order = 2

            N_ = sp.symbols("N")
            y_i = sp.Indexed(sp.symbols("y"), i)
            y_Ni = sp.Indexed(sp.symbols("y"), N_ + i)
            time = sp.symbols("t")

            if order == 0 and len(s_lin_pre) != 0:
                S[i - 1] = sp.Eq(S[i - 1], 0)
                s_lin.extend(s_lin_pre)
                s_lin.append(S[i - 1])
                k_lin.append(i)

            elif order == 1:
                ode_eq_o1.append(sp.Eq(sp.Derivative(y_i, time), sp.Derivative(y_i, time) + S[i - 1]))
                ind_order1.append(i)

            elif order == 2:
                ode_eq_1.append(sp.Eq(sp.Derivative(y_i, time), y_Ni))
                ode_eq_2.append(sp.Eq(sp.Derivative(y_Ni, time), sp.Derivative(y_Ni, time) + S[i - 1]))

        # All equations
        # ode_eq = s_pre + ode_eq_o1 + ode_eq_1 + ode_eq_2
        # self.ode_eq = ode_eq
        self.k_lin = k_lin
        self.s_lin = s_lin
        self.ind_order1 = ind_order1

        if len(k_lin) != 0:
            s_pre = self._kill_lin_pins(s_pre)
            ode_eq_2 = self._kill_lin_pins(ode_eq_2)
            ode_eq_o1 = self._kill_lin_pins(ode_eq_o1)

        # originally - one array OdeEq
        self.current_eq = s_pre
        self.another_eq = ode_eq_o1 + ode_eq_1 + ode_eq_2

        self._substitute_element_currents()
        self._prepair_matrix()
        self._fix_param()
        self._form_lin_matrix()

    def solve(self, t, y0):
        # input values:
        # OdeEq -> diff_eq
        # OdeEq2 -> (A, X, B)
        # LinEqS -> (x_lin, A_lin, B_lin)
        # N -> N
        # P -> fix param values, already in equations

        def _extract_number_from_deriv_term(term):
            return int(term.args[0].args[1]) - 1  # return zero-based index

        var_y = sp.symbols("y")
        time = sp.symbols("t")
        N = len(y0)

        # arguments for lambdify
        args_eq = []
        # functions
        for i in range(N):
            y_i = sp.Indexed(var_y, i + 1)
            args_eq.append(y_i)
        # derivatives
        for i in range(N):
            y_i = sp.Indexed(var_y, i + 1)
            args_eq.append(sp.Derivative(y_i, time))
        # time
        args_eq.append(time)
        # psi_i variables from linear equations
        for psii in self.x_lin:
            args_eq.append(psii)

        # custom functions for lambdify
        # all functions must be in the Functions module
        # and be numpy-functions (recieving numbers, not symbols, as arguments)
        # it is required to prepair a dictionary: {'function_name': implementation}
        custom_func_dict = {}
        for func in dir(Functions):
            if not func.startswith('__'):
                custom_func_dict[func] = getattr(Functions, func)

        diff_eq_lmbd = {}

        # parse equations like dy(...) = y(...)
        # TODO add custom function evaluation
        for eqn in self.diff_eq:
            lside = eqn.lhs
            rside = eqn.rhs
            n_var_deriv = _extract_number_from_deriv_term(lside)
            diff_eq_lmbd[n_var_deriv] = sp.lambdify(args_eq, rside, modules=custom_func_dict)

        # parse another equations
        # TODO add custom function evaluation
        A = self.out_A
        B = self.out_B
        B_final = [sp.lambdify(args_eq, b, modules=custom_func_dict) for b in B]
        A_final = np.zeros((A.rows, A.cols), dtype=object)
        for i in range(A.rows):
            for j in range(A.cols):
                A_final[i, j] = sp.lambdify(args_eq, A[i, j], modules=custom_func_dict)

        def _odeint_kernel(y, t):
            N = len(y)
            y_result = [0] * N
            var_y = sp.symbols("y")
            time = sp.symbols("t")

            # process linear equations and find Psi_... variables
            # evaluate numeric values of A and B matrices
            # by substitution of y_i which can be here
            # TODO add custom function evaluation
            if len(self.A_lin) != 0:
                subst_list = []
                for i in range(N):
                    y_i = sp.Indexed(var_y, i + 1)
                    subst_list.append((y_i, y[i]))
                A_lin = [[float(elem.subs(subst_list)) for elem in row] for row in self.A_lin]
                B_lin = [float(i.subs(subst_list)) for i in self.B_lin]

                psix = np.linalg.solve(A_lin, B_lin)
            else:
                psix = []

            for n_deriv, eq in diff_eq_lmbd.items():
                args = np.hstack((y, y_result, [t], psix))
                y_result[n_deriv] = eq(*args)

            args = np.hstack((y, y_result, [t]))
            B_now = [i(*args) for i in B_final]
            A_now = np.zeros((A.rows, A.cols))
            for i in range(A.rows):
                for j in range(A.cols):
                    A_now[i, j] = A_final[i, j](*args)

            X = np.linalg.solve(A_now, B_now)

            for i, xi in enumerate(self.out_X):  # go over second derivatives
                n_var_deriv = _extract_number_from_deriv_term(xi)
                y_result[n_var_deriv] = X[i]

            return y_result

        return odeint(_odeint_kernel, y0, t)

    def print_equations(self, eqns):
        for eqn in eqns:
            print(eqn)
