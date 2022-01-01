import numpy as np
from scipy.integrate import quad

from Objects.ElementBase import *


class JJ(ElementBase):
    def __init__(self, loc, A=1, B=0, al=1):
        super().__init__()

        # object numeric parameters
        self.A = A
        self.B = B
        self.al = al

        self.loc = loc
        self.order = 2
        self.description = "Josephson junction"
        self.name = "JJ"

        self.complex = False

    def get_equation(self):
        k1, k2 = self.data_index

        self.check_contacts(k1, k2)

        N_ = sp.symbols("N")
        time = sp.symbols("t")

        if k1 == 0 or k2 == 0:
            # only one variable will be
            k = k1 + k2
            kn = N_ + k
            y_kn = sp.Indexed(sp.symbols("y"), kn)
            y_k = sp.Indexed(sp.symbols("y"), k)
            Ic = sp.Derivative(y_kn, time)
            Ir = self.symbol_attribute('al') * sp.Derivative(y_k, time)
            Is = (self.symbol_attribute('A') * sp.sin(y_k) if self.A != 0 else 0) + \
                 (self.symbol_attribute('B') * sp.sin(2 * y_k) if self.B != 0 else 0)
        else:
            # two variables will be
            kn1 = N_ + k1
            kn2 = N_ + k2
            y_kn1 = sp.Indexed(sp.symbols("y"), kn1)
            y_kn2 = sp.Indexed(sp.symbols("y"), kn2)
            y_k1 = sp.Indexed(sp.symbols("y"), k1)
            y_k2 = sp.Indexed(sp.symbols("y"), k2)
            Ic = sp.Derivative(y_kn1, time) - sp.Derivative(y_kn2, time)
            diff_deriv = sp.Derivative(y_k1, time) - sp.Derivative(y_k2, time)
            diff_y = y_k1 - y_k2
            Ir = self.symbol_attribute('al') * diff_deriv
            Is = (self.symbol_attribute('A') * sp.sin(diff_y) if self.A != 0 else 0) + \
                 (self.symbol_attribute('B') * sp.sin(2 * diff_y) if self.B != 0 else 0)

        symbol_current = self.var_current()
        final_equation = sp.Eq(symbol_current, Ic + Ir + Is)

        return final_equation

    def get_data(self, kind, t, y):
        if kind == 'I':
            n = y.shape[1] // 2

            data1 = t
            if self.data_index[0] != 0 and self.data_index[1] != 0:
                pre_data_0 = y[:, self.data_index[0] - 1] - y[:, self.data_index[1] - 1]
                pre_data_1 = y[:, n + self.data_index[0] - 1] - y[:, n + self.data_index[1] - 1]
            else:
                if self.data_index[0] == 0:
                    pre_data_0 = y[:, self.data_index[1] - 1]
                    pre_data_1 = y[:, n + self.data_index[1] - 1]
                else:
                    pre_data_0 = y[:, self.data_index[0] - 1]
                    pre_data_1 = y[:, n + self.data_index[0] - 1]

            dt = data1[1] - data1[0]
            pre_data_2 = np.zeros_like(t)

            pre_data_2[0] = pre_data_1[0] / dt
            for j in range(1, len(t)):
                pre_data_2[j] = (pre_data_1[j] - pre_data_1[j]) / dt

            values = pre_data_2 + self.al * pre_data_1 + self.A * np.sin(pre_data_0) + self.B * np.sin(pre_data_0)

            return np.column_stack((t, values))

        elif kind == 'Edis':
            data1 = t
            if self.data_index[0] != 0 and self.data_index[1] != 0:
                pre_data_2 = self.al * (y[:, self.data_index[0] - 1] - y[:, self.data_index[1] - 1]) ** 2
            else:
                if self.data_index[0] == 0:
                    pre_data_2 = self.al * (y[:, self.data_index[1] - 1]) ** 2
                else:
                    pre_data_2 = self.al * (y[:, self.data_index[1] - 1]) ** 2

            data = np.zeros_like(data1)
            data[0] = pre_data_2[0]
            for k in range(1, len(data1)):
                data[k] = quad(t[:k], pre_data_2[:k])[0]

            return np.column_stack((t, data))

        else:  # 'P', 'V'
            return super().get_data(kind, t, y)
