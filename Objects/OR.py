from Objects.ElementBase import *
from Objects.JJ import JJ
from Objects.Ib import Ib
from Objects.L import L


class OR(ElementBase):
    def __init__(self, loc):
        super().__init__()

        self.loc = loc
        self.N = 14

        self.name = 'OR'
        self.description = 'gate OR'

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
            new_obj.loc = loc
            new_names_obj.append(new_obj)

        def add_L(name, val, loc):
            new_obj = L(loc=loc, val=val)
            new_obj.name = f'{self.name}_{name}'
            new_obj.loc = loc
            new_names_obj.append(new_obj)

        add_ib(name='Ib1', val=1.408, loc=[sk[8]])
        add_ib(name='Ib2', val=1.408, loc=[sk[1]])
        add_ib(name='Ib3', val=1.056, loc=[sk[13]])
        add_ib(name='Ib4', val=1.056, loc=[sk[11]])

        add_JJ(name='J1', c=1, r=1,A=2, B=0, loc=[sk[7], 0])
        add_JJ(name='J2', c=1, r=1,A=1.408, B=0, loc=[sk[6], 0])
        add_JJ(name='J3', c=1, r=1,A=1.408, B=0, loc=[sk[0], sk[7]])
        add_JJ(name='J4', c=1, r=1,A=1.408, B=0, loc=[sk[5], sk[6]])
        add_JJ(name='J5', c=1, r=1,A=2, B=0, loc=[sk[8], 0])
        add_JJ(name='J6', c=1, r=1,A=1.408, B=0, loc=[sk[4], 0])
        add_JJ(name='J7', c=1, r=1,A=1.408, B=0, loc=[sk[2], sk[8]])
        add_JJ(name='J8', c=1, r=1,A=1.408, B=0, loc=[sk[13], sk[4]])
        add_JJ(name='J9', c=1, r=1,A=1.408, B=0, loc=[sk[11], 0])
        add_JJ(name='J10', c=1, r=1,A=1.408, B=0, loc=[sk[11], sk[12]])
        add_JJ(name='J11', c=1, r=1,A=1.408, B=0, loc=[sk[9], 0])
        add_JJ(name='J12', c=1, r=1,A=1.408, B=0, loc=[sk[9], sk[10]])

        add_L(name='L1', val=5.72, loc=[sk[7], sk[6]])
        add_L(name='L2', val=5.72, loc=[sk[0], sk[2]])
        add_L(name='L3', val=1.43, loc=[sk[6], sk[11]])
        add_L(name='L4', val=1.43, loc=[sk[4], sk[9]])
        add_L(name='L5', val=2.15, loc=[sk[12], sk[3]])
        add_L(name='L6', val=2.15, loc=[sk[10], sk[3]])
        add_L(name='L7', val=2.15, loc=[sk[1], sk[5]])
        add_L(name='L8', val=2.15, loc=[sk[1], sk[13]])


        return new_names_obj