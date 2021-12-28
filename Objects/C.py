from Objects.ElementBase import ElementBase
import sympy as sp
import numpy as np


class C(ElementBase):
    def __init__(self, loc, C):
        super().__init__()

        # numeric parameters
        self.C = C

        self.loc = loc
        self.name = "C"
        self.order = 2
        self.description = "Capacitor"

        self.complex = False

    def get_equation(self):
        k1, k2 = self.data_index

        self.check_contacts(k1, k2)

        time = sp.symbols("t")
        I_n = self.var_current()

        if k1 == 0 or k2 == 0:
            kn = k1 + k2
            y_kn = sp.Indexed(sp.symbols("y"), kn)

            Ic = self.symbol_attribute('C') * sp.Derivative(y_kn, time)

            final_equation = sp.Eq(I_n, Ic if k2 == 0 else -Ic)
        else:
            y_kn1 = sp.Indexed(sp.symbols("y"), k1)
            y_kn2 = sp.Indexed(sp.symbols("y"), k2)

            Ic = self.symbol_attribute('C') * (sp.Derivative(y_kn1, time) - sp.Derivative(y_kn2, time))

            final_equation = sp.Eq(I_n, Ic)

        return final_equation

    def get_data(self, kind, t, y):
        if kind in ['P', 'V']:
            return super().get_data(kind, t, y)
        elif kind == 'I':
            n = y.shape[1] // 2

            data1 = t
            if self.data_index[0] != 0 and self.data_index[1] != 0:
                pre_data_1 = y[:, n + self.data_index[0] - 1] - y[:, n + self.data_index[1] - 1]
            else:
                if self.data_index[0] == 0:
                    pre_data_1 = y[:, n + self.data_index[1] - 1]
                else:
                    pre_data_1 = y[:, n + self.data_index[0] - 1]

            dt = data1[1] - data1[0]
            pre_data_2 = np.zeros_like(t)

            for j in range(1, len(t)):
                pre_data_2[j] = (pre_data_1[j] - pre_data_1[j]) / dt

            values = self.C * pre_data_2

            return np.column_stack((t, values))
