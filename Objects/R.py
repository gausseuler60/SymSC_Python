from Objects.ElementBase import *


class R(ElementBase):
    def __init__(self, loc, alR):
        super().__init__()

        # numeric parameters
        self.alR = alR

        self.loc = loc
        self.name = "R"
        self.order = 1
        self.description = "Resistor"

        self.complex = False

    def get_equation(self):
        k1, k2 = self.data_index

        if k1 < 0 or k2 < 0:
            self.error("is connected to a node with a negative index")

        if k1 + k2 == 0:
            self.warning("is grounded at both outputs")

        time = sp.symbols("t")
        I_n = self.var_current()

        if k1 == 0 or k2 == 0:
            kn = k1 + k2
            y_kn = sp.Indexed(sp.symbols("y"), kn)

            Ir = self.symbol_attribute("alR") * sp.Derivative(y_kn, time)

            final_equation = sp.Eq(I_n, Ir if k2 == 0 else -Ir)

        else:
            y_kn1 = sp.Indexed(sp.symbols("y"), k1)
            y_kn2 = sp.Indexed(sp.symbols("y"), k2)

            Ir = self.symbol_attribute("alR") * (sp.Derivative(y_kn1, time) - sp.Derivative(y_kn2, time))

            final_equation = sp.Eq(I_n, Ir)

        return final_equation

    def get_data(self, kind, t, y):
        if kind == 'P':
            return super().get_data(kind, t, y)

        elif kind == 'V':
            data1 = t
            if self.data_index[0] != 0 and self.data_index[1] != 0:
                pre_data_0 = y[:, self.data_index[0] - 1] - y[:, self.data_index[1] - 1]
            else:
                if self.data_index[0] == 0:
                    pre_data_0 = y[:, self.data_index[1] - 1]
                else:
                    pre_data_0 = y[:, self.data_index[0] - 1]

            dt = data1[1] - data1[0]
            pre_data_1 = np.zeros_like(t)

            for j in range(1, len(t)):
                pre_data_1[j] = (pre_data_0[j] - pre_data_1[j]) / dt

            return np.column_stack((t, pre_data_1))

        elif kind == 'I':
            t, data = self.get_data('V', t, y)
            return np.column_stack((t, data * self.alR))
