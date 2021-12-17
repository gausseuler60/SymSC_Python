import sympy as sp
import warnings


class ElementBase:
    def __init__(self):
        self.name = ""
        self.data_index = [None, None]

    # object initialization after acquisition of data_index
    # may be overridden in a child class
    def init_object(self):
        pass

    def error(self, error_msg):
        raise ValueError(f'{self.name} {error_msg}')

    def warning(self, warning_msg):
        warnings.warn(f'{self.name} {warning_msg}')

    def symbol_attribute(self, sym):
        return sp.symbols(f"{self.name}.{sym}")

    def var_current(self):
        I_ = sp.symbols("I")
        return sp.Indexed(I_, sp.symbols(self.name))

    # get equation for this element current
    # must be overridden in a child class
    def get_equation(self):
        pass
