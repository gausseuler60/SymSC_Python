import numpy as np
import warnings


class ElementBase:
    def __init__(self):
        self.data_index = None
        self.current_index = []
        self.var_index = None
        self.name = None
        self.complex = False

        self.contains_current = False
        self.contains_variable = False
        self.double_voltage = False
        self.double_current = False

    def check_loc(self, loc, len_required):
        if np.all(np.array(loc) == 0):
            warnings.warn(f'{self.name} is grounded at each output')

        if len(loc) != len_required:
            raise ValueError(f'Number of connections for {self.name} is {len_required},'
                             f' but actually {len(loc)} was specified')

    def get_data(self, kind, t, sol):
        if kind == 'V':  # return V+ - V-
            voltage_index = self.data_index
            if voltage_index[0] == 0:  # V+ is missing
                return -sol[voltage_index[1] - 1, :]
            elif voltage_index[1] == 0:  # V- is missing
                return sol[voltage_index[0] - 1, :]
            else:  # everything is present
                return sol[voltage_index[0] - 1, :] - sol[voltage_index[1] - 1, :]
        elif kind == 'I':
            current_index = self.current_index
            return sol[current_index[0], :]
        else:
            raise ValueError(f'Data kind {kind} is not supported')
