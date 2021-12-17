from Objects.ElementBase import *


class Ib(ElementBase):
    def __init__(self, loc, val=0.75):
        super().__init__()

        # numeric parameters
        self.val = val

        self.loc = loc
        self.order = 0
        self.description = "Bias current"
        self.name = "Ib"

        self.complex = False

    def get_equation(self):
        S = - self.symbol_attribute('val')
        symbol_current = self.var_current()
        final_equation = sp.Eq(symbol_current, S)
        return final_equation
