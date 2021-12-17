import sympy as sp
from copy import deepcopy


class FunctionCompiler:
    def __init__(self, object_list, fixed_parameter):
        self.object_list = object_list
        self.fixed_parameter = fixed_parameter

        self.object_dict = {obj.name: obj for obj in object_list}

    # assigns names and variable indices to objects
    def _assign_indices(self):
        self.indices = []
        N = 0

        for i, obj in enumerate(self.object_list):
            obj.name = f"{obj.name}{i+1}"  # make one-based numbering
            obj.data_index = obj.loc
            obj.init_object()

            if N < max(obj.loc):
                N = max(obj.loc)

        self.N = N

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

            self._substitute_element_currents()

    def print_equations(self, eqns):
        for eqn in eqns:
            print(eqn)
