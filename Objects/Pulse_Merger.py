from Objects.ElementBase import *
from Objects.JJ import JJ
from Objects.Ib import Ib
from Objects.L import L


class Pulse_Merger(ElementBase):
    def __init__(self, loc):
        super().__init__()

        self.loc = loc
        self.N = 14

        self.name = 'Pulse_Merger'
        self.description = 'Merger 2 pulses to 1 pulse'

        self.complex = True

    def unzip(self):
        sk = self.data_index
        new_names_obj = []

        def add_JJ(name, c, r, A, B, loc):
            new_obj = JJ(loc=loc, A=A, B=B, r=al, c=1)
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

        add_JJ(name='J3', c=1,r=1, A=2.01, B=0, loc=[sk[3], sk[4]])
        add_JJ(name='J2', c=1, r=1, A=1.79, B=0, loc=[sk[5], sk[9]])
        add_JJ(name='J4', c=1, r=1, A=2.01, B=0, loc=[sk[6], sk[7]])
        add_JJ(name='J1', c=1, r=1, A=1.79, B=0, loc=[sk[8], sk[9]])
        add_JJ(name='J5', c=1, r=1, A=2.01, B=0, loc=[sk[12], sk[13]])

        add_ib(name='Ib1', val=4.1, loc=[sk[11]])

        add_L(name='L1', val=0.75, loc=[sk[0], sk[4]])
        add_L(name='L2', val=0.75, loc=[sk[1], sk[7]])
        add_L(name='Lp3', val=0.01, loc=[sk[3], 0])
        add_L(name='Lp2', val=0.25, loc=[sk[4], sk[5]])
        add_L(name='Lp4', val=0.01, loc=[sk[6], 0])
        add_L(name='Lp1', val=0.25, loc=[sk[7], sk[8]])
        add_L(name='L5', val=0.08, loc=[sk[9], sk[10]])
        add_L(name='L11', val=0.05, loc=[sk[11], sk[10]])
        add_L(name='L4', val=1, loc=[sk[10], sk[12]])
        add_L(name='Lp5', val=0.01, loc=[sk[13], 0])
        add_L(name='L3', val=0.75, loc=[sk[12], sk[2]])

        return new_names_obj
