import sympy as sp
import numpy as np
from scipy.integrate import odeint


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

        for i, obj in enumerate(self.object_list):
            obj.name = f"{obj.name}{i+1}"  # make one-based numbering
            obj.data_index = obj.loc
            obj.init_object()

            if N < max(obj.loc):
                N = max(obj.loc)

        self.N = N
        self.object_dict = {obj.name: obj for obj in self.object_list}
        self._assigned = True

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
        # sLin TODO
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

        # self.lin_eq = ... TODO: sLin
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

    def compile(self):
        self._assign_indices()
        # TODO: add complex object initialization support

        s_pre = [obj.get_equation() for obj in self.object_list]
        S = [sp.sympify(0)] * self.N

        ode_eq_o1 = []
        ode_eq_1 = []
        ode_eq_2 = []
        ind_order1 = []

        # write equations for network nodes
        for i in range(1, self.N + 1):  # loc==0 means a ground, don't consider it as a node
            SLinPre = []
            order = 0

            for k, obj in enumerate(self.object_list):
                if obj.data_index[0] == i:
                    S[i - 1] -= obj.var_current()
                    if obj.order == 0 and order == 0:
                        pass  # TODO: SLinPre = ...
                    elif obj.order == 1 and order == 0:
                        order = 1
                        # TODO: SLinPre = ...
                    elif obj.order == 2:
                        order = 2
                        # TODO SLinPre = ...

                elif len(obj.data_index) > 1 and obj.data_index[1] == i:
                    S[i - 1] += obj.var_current()
                    if obj.order == 0 and order == 0:
                        pass  # TODO: SLinPre = ...
                    elif obj.order == 1 and order == 0:
                        order = 1
                    elif obj.order == 2:
                        order = 2

            N_ = sp.symbols("N")
            y_i = sp.Indexed(sp.symbols("y"), i)
            y_Ni = sp.Indexed(sp.symbols("y"), N_ + i)
            time = sp.symbols("t")

            if order == 0:
                pass  # TODO complete

            elif order == 1:
                ode_eq_o1.append(sp.Eq(sp.Derivative(y_i, time), sp.Derivative(y_i, time) + S[i - 1]))
                ind_order1.append(i)

            elif order == 2:
                ode_eq_1.append(sp.Eq(sp.Derivative(y_i, time), y_Ni))
                ode_eq_2.append(sp.Eq(sp.Derivative(y_Ni, time), sp.Derivative(y_Ni, time) + S[i - 1]))

            # All equations
            # ode_eq = s_pre + ode_eq_o1 + ode_eq_1 + ode_eq_2
            # self.ode_eq = ode_eq
            self.current_eq = s_pre
            self.another_eq = ode_eq_o1 + ode_eq_1 + ode_eq_2

        self.ind_order1 = ind_order1

        self._substitute_element_currents()
        self._prepair_matrix()
        self._fix_param()

    def solve(self, t, y0):
        # input values:
        # OdeEq -> diff_eq
        # OdeEq2 -> (A, X, B)
        # LinEqS -> TODO
        # N -> N
        # P -> fix param values, already in equations

        def _extract_number_from_deriv_term(term):
            return int(term.args[0].args[1]) - 1  # return zero-based index

        def _odeint_kernel(y, t):
            N = len(y)
            y_result = [sp.sympify(0)] * N
            var_y = sp.symbols("y")
            time = sp.symbols("t")

            def _substitute(expr):
                # substitute all y_i and d(y_i) variables
                # all y_i are the input
                # and d(y_i) are output array
                for i in range(N):
                    y_i = sp.Indexed(var_y, i+1)
                    expr = expr.subs(sp.Derivative(y_i, time), y_result[i])
                    expr = expr.subs(y_i, y[i])

                return float(expr)

            # parse equations like dy(...) = y(...)
            for eqn in self.diff_eq:
                lside = eqn.lhs
                rside = eqn.rhs
                n_var_deriv = _extract_number_from_deriv_term(lside)
                result_rhs = _substitute(rside)
                y_result[n_var_deriv] = result_rhs

            # parse another equations
            A = self.out_A
            B = self.out_B
            B_final = [_substitute(b) for b in B]
            A_final = np.zeros((A.rows, A.cols))
            for i in range(A.rows):
                for j in range(A.cols):
                    A_final[i, j] = _substitute(A[i,j])
            X = np.linalg.solve(A_final, B_final)

            for i, xi in enumerate(self.out_X):  # go over second derivatives
                n_var_deriv = _extract_number_from_deriv_term(xi)
                y_result[n_var_deriv] = X[i]

            return y_result

        return odeint(_odeint_kernel, y0, t)

    def print_equations(self, eqns):
        for eqn in eqns:
            print(eqn)
