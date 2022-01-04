from Objects.ElementBase import *
from Objects.JJ import JJ
from Objects.Ib import Ib


class TFF(ElementBase):
    def __init__(self, loc):
        super().__init__()

        self.check_loc(loc, 4)

        self.loc = loc
        self.N = 5

        self.name = 'TFF'
        self.description = 'T trigger with Read-Out line'

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

        add_JJ(name='Jcin', A=0.1, B=0, al=1, data_index=[sk[0], sk[2]])
        add_JJ(name='Jm', A=0, B=0.7, al=1, data_index=[sk[4], 0])
        add_JJ(name='Jv', A=0, B=0.1, al=1, data_index=[sk[0], sk[4]])
        add_JJ(name='Jrs', A=0.1, B=0, al=1, data_index=[sk[1], sk[3]])
        add_JJ(name='Jlc', A=0.4, B=0, al=1, data_index=[sk[2], sk[4]])
        add_JJ(name='Jls', A=0.5, B=0, al=1, data_index=[sk[4], sk[3]])
        add_JJ(name='Joutc', A=1, B=0, al=1, data_index=[sk[2], 0])
        add_JJ(name='Jouts', A=1.5, B=0, al=1, data_index=[sk[3], 0])

        add_ib(name='ibJm', val=0.65, data_index=[sk[4]])
        add_ib(name='ibJoutc', val=0.6, data_index=[sk[2]])
        add_ib(name='ibJouts', val=1.1, data_index=[sk[3]])

        return new_names_obj

