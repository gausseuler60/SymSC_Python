from Objects.ElementBase import *
from Objects.JJ import JJ
from Objects.Ib import Ib
from Objects.L import L
from Objects.R import R


class MDriver(ElementBase):
    def __init__(self, loc):
        super().__init__()

        self.loc = loc
        self.N = 8

        self.name = 'MDriver'
        self.description = 'Microstrip Driver'

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

        def add_R(name, r, loc):
            new_obj = R(loc=loc, r=r)
            new_obj.name = f'{self.name}_{name}'
            new_names_obj.append(new_obj)

        add_ib(name='Ib', val=2.77, loc=[sk[4]])

        add_JJ(name='Jin', c=1, r=1,A=2.01, B=0, loc=[sk[2], 0])
        add_JJ(name='Jout', c=1, r=1,A=2.01, B=0, loc=[sk[6], 0])

        add_L(name='Lin', val=0.75, loc=[sk[0], sk[7]])
        add_L(name='L1', val=0.05, loc=[sk[7], sk[2]])
        add_L(name='L2', val=0.6, loc=[sk[7], sk[3]])
        add_L(name='L3', val=0.05, loc=[sk[4], sk[3]])
        add_L(name='L4', val=0.62, loc=[sk[3], sk[5]])
        add_L(name='L5', val=0.05, loc=[sk[5], sk[6]])
        add_L(name='Lout', val=0.6, loc=[sk[5], sk[1]])

        add_R(name='R', r=1.5, loc=[sk[1], 0])

        return new_names_obj
