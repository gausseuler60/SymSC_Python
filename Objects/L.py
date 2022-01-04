import numpy as np

from Objects.ElementBase import *


class L(ElementBase):
    def __init__(self, loc, val=3):
        super().__init__()

        self.check_loc(loc, 2)

        # numeric parameters
        self.val = val

        self.loc = loc
        self.order = 0
        self.description = "Inductor"
        self.name = "L"

        self.complex = False

    def get_equation(self):
        k1, k2 = self.data_index

        y_k1 = sp.Indexed(sp.symbols("y"), k1)
        y_k2 = sp.Indexed(sp.symbols("y"), k2)

        if k1 == 0:
            S = -y_k2 / self.symbol_attribute('val')
        elif k2 == 0:
            S = y_k1 / self.symbol_attribute('val')
        else:
            S = (y_k1 - y_k2) / self.symbol_attribute('val')

        symbol_current = self.var_current()
        final_equation = sp.Eq(symbol_current, S)
        return final_equation

    def get_data(self, kind, t, y):
        if kind == 'I':
            p = super().get_data('P', t, y)
            return np.column_stack((p[:, 0], p[:, 1] / self.val))
        else:
            return super().get_data(kind, t, y)
