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

        if k1 < 0 or k2 < 0:
            self.error("is connected to a node with a negative index")

        if k1 == 0 and k2 == 0:
            self.warning("is grounded at both outputs")

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
            Is = self.symbol_attribute('A') * sp.sin(y_k) + self.symbol_attribute('B') * sp.sin(2 * y_k)
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
            Is = self.symbol_attribute('A') * sp.sin(diff_y) + self.symbol_attribute('B') * sp.sin(2 * diff_y)

        symbol_current = self.var_current()
        final_equation = sp.Eq(symbol_current, Ic + Ir + Is)

        return final_equation
