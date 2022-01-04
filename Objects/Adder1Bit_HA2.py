from Objects.ElementBase import *
from Objects.JJ import JJ
from Objects.Ib import Ib


class Adder1Bit_HA2(ElementBase):
    def __init__(self, loc):
        super().__init__()

        self.check_loc(loc, 5)

        self.loc = loc
        self.N = 6

        self.name = 'Adder1Bit_HA2'
        self.description = '1-bit adder version HA2'

        self.complex = True

    def unzip(self):
        sk = self.data_index
        new_names_obj = []

        def add_JJ(name, A, B, al, data_index):
            new_obj = JJ(loc=None, A=A, B=B, al=al)
            new_obj.name = f'{self.name}_{name}'
            new_obj.data_index = data_index
            new_names_obj.append(new_obj)

        def add_ib(name, val, data_index):
            new_obj = Ib(loc=None, val=val)
            new_obj.name = f'{self.name}_{name}'
            new_obj.data_index = data_index
            new_names_obj.append(new_obj)

        add_JJ(name='Jin1', A=1, B=0, al=1, data_index=[sk[0], 0])
        add_JJ(name='Jin2', A=1, B=0, al=1, data_index=[sk[1], 0])
        add_JJ(name='Jm', A=0, B=0.7, al=1, data_index=[sk[5], 0])
        add_JJ(name='Jv1', A=0, B=0.1, al=1, data_index=[sk[0], sk[5]])
        add_JJ(name='Jv2', A=0, B=0.1, al=1, data_index=[sk[1], sk[5]])
        add_JJ(name='Jrs', A=0.1, B=0, al=1, data_index=[sk[2], sk[4]])
        add_JJ(name='Jlc', A=0.4, B=0, al=1, data_index=[sk[3], sk[5]])
        add_JJ(name='Jls', A=0.5, B=0, al=1, data_index=[sk[4], sk[5]])
        add_JJ(name='Joutc', A=1, B=0, al=1, data_index=[sk[3], 0])
        add_JJ(name='Jouts', A=1.5, B=0, al=1, data_index=[sk[4], 0])
        add_JJ(name='Jrc1', A=0.1, B=0, al=1, data_index=[sk[0], sk[3]])
        add_JJ(name='Jrc2', A=0.1, B=0, al=1, data_index=[sk[1], sk[3]])

        add_ib('ibJin1', val=0.9, data_index=[sk[0]])
        add_ib('ibJin2', val=0.9, data_index=[sk[1]])
        add_ib('ibJm', val=0.65, data_index=[sk[5]])
        add_ib('ibJoutc', val=0.9, data_index=[sk[3]])
        add_ib('ibJouts', val=1.1, data_index=[sk[4]])

        return new_names_obj

    def get_phase(self, mas_phases, mode):
        X = np.zeros((mas_phases.shape[0], 3))
        F = np.zeros((mas_phases.shape[0], 10))

        X[:, 0] = mas_phases[:, self.data_index[0] - 1]  # data_index is 1-based, but arrays in Python are 0-based
        X[:, 1] = mas_phases[:, self.data_index[1] - 1]
        X[:, 2] = mas_phases[:, self.data_index[2] - 1]

        F[:, 0] = mas_phases[:, self.data_index[3] - 1]
        F[:, 1] = mas_phases[:, self.data_index[4] - 1]
        F[:, 2] = mas_phases[:, self.data_index[5] - 1]

        F[:, 3] = X[:, 0] - F[:, 2]
        F[:, 4] = X[:, 1] - F[:, 2]
        F[:, 5] = X[:, 0] - F[:, 0]
        F[:, 6] = X[:, 1] - F[:, 0]
        F[:, 7] = F[:, 0] - F[:, 2]
        F[:, 8] = F[:, 1] - F[:, 2]
        F[:, 9] = X[:, 2] - F[:, 1]

        if mode == 0:
            return F
        else:
            return np.hstack((X, F[:, :2]))





