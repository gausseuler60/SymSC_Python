from Objects.ElementBase import *
from Objects.JJ import JJ
from Objects.Ib import Ib


class DFF(ElementBase):
    def __init__(self, loc):
        super().__init__()

        self.check_loc(loc, 3)

        self.loc = loc
        self.N = 4

        self.name = 'DFF'
        self.description = 'D trigger with Read-Out line'

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

        add_JJ(name='Jin1', A=1, B=0, al=5, data_index=[sk[0], 0])
        add_JJ(name='Jm', A=0, B=0.5, al=1, data_index=[sk[3], 0])
        add_JJ(name='Jv', A=0, B=0.1, al=5, data_index=[sk[0], sk[3]])
        add_JJ(name='Jr', A=1, B=0, al=1, data_index=[sk[1], sk[2]])
        add_JJ(name='J1', A=0.5, B=0, al=3.5, data_index=[sk[3], sk[2]])
        add_JJ(name='Jout', A=2, B=0, al=2, data_index=[sk[2], 0])

        add_ib(name='ibJin', val=0.75, data_index=[sk[0]])
        add_ib(name='ibJout', val=1.5, data_index=[sk[2]])

        return new_names_obj
