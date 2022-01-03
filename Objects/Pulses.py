from Objects.ElementBase import ElementBase
import sympy as sp


class Pulses(ElementBase):
    def __init__(self, loc, connect='Current', type_p='Gauss', t0=50, A=1, D=15, T=500, w=1):
        super().__init__()

        # numeric parameters
        if not connect in ['Current', 'Phase']:
            raise ValueError('Connect must be "Current" or "Phase"')
        self.connect = connect

        if not type_p in ['Gauss', 'Sin']:
            raise ValueError('type_p must be "Gauss" or "Sin"')
        self.type_p = type_p

        self.t0 = t0
        self.A = A
        self.D = D
        self.T = T
        self.w = w

        self.loc = loc
        self.name = "Pulses"
        self.order = 0
        self.description = "Pulse generator"

        self.complex = False

    def get_equation(self):
        sA = self.symbol_attribute('A')
        time = sp.symbols("t")
        I_n = self.var_current()

        if self.connect == 'Current' and self.type_p == 'Gauss':
            st0 = self.symbol_attribute('t0')
            sD = self.symbol_attribute('D')
            sT = self.symbol_attribute('T')

            gauss_I_func = sp.Function('gauss_I')
            gauss_I = gauss_I_func(time, st0, sA, sD, sT)

            final_equation = sp.Eq(I_n, -gauss_I)

        else:
            sw = self.symbol_attribute('w')
            final_equation = sp.Eq(I_n, -sA * sp.sin(sw * time))

        return final_equation
