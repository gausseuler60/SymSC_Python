from Objects.ElementBase import *
from Objects.JJ import JJ
from Objects.Ib import Ib
from Objects.L import L


class C_element(ElementBase):
    def __init__(self, loc):
        super().__init__()

        self.loc = loc
        self.N = 7

        self.name = 'C_element'
        self.description = 'Coincidence Junction'

        self.complex = True

    def unzip(self):
        sk = self.data_index
        new_names_obj = []

        def add_JJ(name, c, r, A, B, loc):
            new_obj = JJ(loc=loc, c=c, r=r, A=A, B=B)
            new_obj.name = f'{self.name}_{name}'
            new_names_obj.append(new_obj)

        def add_ib(name, val, loc):
            new_obj = Ib(loc=loc, val=val)
            new_obj.name = f'{self.name}_{name}'
            new_names_obj.append(new_obj)

        def add_L(name, val, loc):
            new_obj = L(loc=loc, val=val)
            new_obj.name = f'{self.name}_{name}'
            new_names_obj.append(new_obj)

        add_ib(name='Ib1', val=0.2, loc=[sk[0]])
        add_ib(name='Ib2', val=0.2, loc=[sk[1]])

        add_JJ(name='J1', c=1, r=1, A=1, B=0, loc=[sk[0], 0])
        add_JJ(name='J2', c=1, r=1,A=1, B=0, loc=[sk[1], 0])
        add_JJ(name='J3', c=1, r=1,A=2, B=0, loc=[sk[3], 0])

        add_L(name='L1', val=2, loc=[sk[0], sk[3]])
        add_L(name='L2', val=2, loc=[sk[1], sk[3]])
        add_L(name='L3', val=0.5, loc=[sk[3], sk[2]])

        return new_names_obj
