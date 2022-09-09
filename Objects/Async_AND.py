from Objects.ElementBase import *
from Objects.JJ import JJ
from Objects.Ib import Ib
from Objects.L import L
from Objects.R import R


class Async_AND(ElementBase):
    def __init__(self, loc):
        super().__init__()

        self.loc = loc
        self.N = 7

        self.name = 'Async_AND'
        self.description = 'Asynchronous AND gate'

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
            new_obj = R(loc=loc, r = r)
            new_obj.name = f'{self.name}_{name}'
            new_names_obj.append(new_obj)

        add_ib(name='Ib1', val=0.56, loc=[sk[2]])

        add_JJ(name='J1', c=1, r=1e-3, A=0.672, B=0, loc=[sk[3], sk[2]])
        add_JJ(name='J2', c=1, r=1e-3, A=0.672, B=0, loc=[sk[5], sk[2]])
        add_JJ(name='J3', c=1, r=1e-3, A=1.344, B=0, loc=[sk[2], 0])
        add_JJ(name='JD1', c=1, r=1e-3, A=0.48, B=0, loc=[sk[4], sk[2]])
        add_JJ(name='JD2', c=1, r=1e-3, A=0.48, B=0, loc=[sk[6], sk[2]])

        add_L(name='L1', val=4.545, loc=[sk[0], sk[3]])
        add_L(name='L2', val=4.545, loc=[sk[1], sk[5]])

        add_R(name='RD1', r = 0.279, loc=[sk[3], sk[4]])
        add_R(name='RD2', r = 0.279, loc=[sk[5], sk[6]])

        return new_names_obj
