class ElementBase:
    def __init__(self):
        self.data_index = None
        self.current_index = None
        self.var_index = None

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
            return sol[current_index, :]
        else:
            raise ValueError(f'Data kind {kind} is not supported')
