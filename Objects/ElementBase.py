import numpy as np
import sympy as sp
import warnings


class ElementBase:
    def __init__(self):
        self.name = ""
        self.data_index = [0, 0]

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

    def check_contacts(self, k1, k2):
        if k1 < 0 or k2 < 0:
            self.error("is connected to a node with a negative index")

        if k1 == 0 and k2 == 0:
            self.warning("is grounded at both outputs")

    # get equation for this element current
    # must be overridden in a child class
    def get_equation(self):
        pass

    # get physical quantities from solution
    # may be overridden in a child class
    def get_data(self, kind, t, y):
        n = y.shape[1] // 2

        if kind == 'P':
            data1 = t
            if self.data_index[0] != 0 and self.data_index[1] != 0:
                data2 = y[:, self.data_index[0] - 1] - y[:, self.data_index[1] - 1]
            else:
                if self.data_index[0] == 0:
                    data2 = y[:, self.data_index[1] - 1]
                else:
                    data2 = y[:, self.data_index[0] - 1]

        elif kind == 'V':
            data1 = t
            if self.data_index[0] != 0 and self.data_index[1] != 0:
                data2 = y[:, n + self.data_index[0] - 1] - y[:, n + self.data_index[1] - 1]
            else:
                if self.data_index[0] == 0:
                    data2 = y[:, n + self.data_index[1] - 1]
                else:
                    data2 = y[:, n + self.data_index[0] - 1]

        else:
            raise ValueError('Invalid data kind')

        return np.column_stack((data1, data2))
