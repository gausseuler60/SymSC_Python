from Objects.ElementBase import *


class GenI(ElementBase):
    def __init__(self, loc, A, B, w, d, alR):
        super().__init__()

        # numeric parameters
        self.A = A
        self.B = B
        self.w = w
        self.d = d
        self.alR = alR

        self.loc = loc
        self.name = "GenI"
        self.order = 1
        self.description = "Current generator"

        self.complex = False

    def get_equation(self):
        sA = self.symbol_attribute('A')
        sB = self.symbol_attribute('B')
        sw = self.symbol_attribute('w')
        sd = self.symbol_attribute('d')
        salR = self.symbol_attribute('alR')

        k1, k2 = self.data_index

        time = sp.symbols("t")
        I_n = self.var_current()

        I = sA * sp.sin(sw * time + sd) + sB

        self.check_contacts(k1, k2)

        if k1 == 0 or k2 == 0:
            kn = k1 + k2
            y_kn = sp.Indexed(sp.symbols("y"), kn)

            Ir = salR * sp.Derivative(y_kn, time)

            final_equation = sp.Eq(I_n, Ir - I if k2 == 0 else I - Ir)

        else:
            y_kn1 = sp.Indexed(sp.symbols("y"), k1)
            y_kn2 = sp.Indexed(sp.symbols("y"), k2)

            Ir = salR * (sp.Derivative(y_kn1, time) - sp.Derivative(y_kn2, time))

            final_equation = sp.Eq(I_n, Ir - I)

        return final_equation

    def get_data(self, kind, t, y):
        if type in ['P', 'V', 'Edis']:
            return np.column_stack((t, np.zeros_like(t)))
        elif type == 'I':
            ydata = self.A * np.sin(self.w * t + self.d) + self.B
            return np.column_stack((t, ydata))
