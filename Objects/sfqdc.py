from Objects.ElementBase import *
from Objects.JJ import JJ
from Objects.L import L
from Objects.R import R
from Objects.Ib import Ib

class sfqdc(ElementBase):
    def __init__(self, loc):
        super().__init__()

        self.loc = loc
        self.N = 8

        self.name = 'sfqdc'
        self.description = 'SFQ to DC converter'

        self.complex = True

    def unzip(self):
        sk = self.data_index
        new_names_obj = []

        def add_JJ(name, c, r, A, B, loc):
            new_obj = JJ(loc=loc, c=c, r=r, A=A, B=B)
            new_obj.name = f'{self.name}_{name}'
            new_names_obj.append(new_obj)

        def add_L(name, val, loc):
            new_obj = L(loc=loc, val=val)
            new_obj.name = f'{self.name}_{name}'
            new_names_obj.append(new_obj)

        def add_ib(name, val, loc):
            new_obj = Ib(loc=loc, val=val)
            new_obj.name = f'{self.name}_{name}'
            new_names_obj.append(new_obj)

        def add_R(name, r, loc):
            new_obj = R(loc=loc, r=r)
            new_obj.name = f'{self.name}_{name}'
            new_names_obj.append(new_obj)

        add_JJ(name='J1', c=1, r=1, A=1.6, B=0, loc=[sk[6], 0])
        add_JJ(name='J2', c=1, r=1, A=0.8, B=0, loc=[sk[3], sk[6]])
        add_JJ(name='J3', c=1, r=1, A=1.2, B=0, loc=[sk[5], 0])
        add_JJ(name='J4', c=1, r=1, A=0.4, B=0, loc=[sk[4], sk[5]])
        add_JJ(name='J5', c=1, r=1, A=1.4, B=0, loc=[sk[2], 0])
        add_JJ(name='J6', c=1, r=1, A=1.4, B=0, loc=[sk[7], sk[2]])

        add_L(name='L1', val=2, loc=[sk[0], sk[3]])
        add_L(name='L2', val=2, loc=[sk[1], sk[4]])
        
        add_L(name='L3', val=4.6, loc=[sk[6], sk[7]])
        add_L(name='L4', val=4.6, loc=[sk[5], sk[7]])
        
        add_ib(name='Ib1', val=0.8, loc=[sk[6]])
        add_ib(name='Ib2', val=0.64, loc=[sk[2]])

        add_R(name='R1', r = 0.5, loc=[sk[7], 0])


        return new_names_obj