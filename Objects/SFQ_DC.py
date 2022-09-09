from Objects.ElementBase import *
from Objects.JJ import JJ
from Objects.L import L
from Objects.R import R

class SFQ_DC(ElementBase):
    def __init__(self, loc):
        super().__init__()

        self.loc = loc
        self.N = 13

        self.name = 'SFQ_DC'
        self.description = 'SFQ to DC converter'

        self.complex = True

    def unzip(self):
        sk = self.data_index
        new_names_obj = []

        def add_JJ(name, A, B, al, loc):
            new_obj = JJ(loc=loc, A=A, B=B, al=al)
            new_obj.name = f'{self.name}_{name}'
            new_names_obj.append(new_obj)

        def add_L(name, val, loc):
            new_obj = L(loc=loc, val=val)
            new_obj.name = f'{self.name}_{name}'
            new_names_obj.append(new_obj)

        def add_R(name, alR, loc):
            new_obj = R(loc=loc, alR=alR)
            new_obj.name = f'{self.name}_{name}'
            new_names_obj.append(new_obj)

        add_JJ(name='J1', A=1.18, B=0, al=1, loc=[sk[5], sk[8]])
        add_JJ(name='J2', A=1.37, B=0, al=1, loc=[sk[6], sk[7]])
        add_JJ(name='J3', A=1.37, B=0, al=1, loc=[sk[8], 0])
        add_JJ(name='J4', A=1.96, B=0, al=1, loc=[sk[10], sk[11]])
        add_JJ(name='J5', A=1.96, B=0, al=1, loc=[sk[7], 0])
        add_JJ(name='J6', A=1.96, B=0, al=1, loc=[sk[11], sk[12]])

        add_L(name='L1', val=1.27, loc=[sk[0], sk[2]])
        add_L(name='L2', val=1.36, loc=[sk[2], sk[4]])
        add_L(name='L3', val=0.48, loc=[sk[4], sk[5]])
        add_L(name='L4', val=0.26, loc=[sk[4], sk[6]])
        add_L(name='L5', val=0.49, loc=[sk[8], sk[9]])
        add_L(name='L6', val=0.1, loc=[sk[9], sk[7]])
        add_L(name='L7', val=0.1, loc=[sk[9], sk[10]])
        add_L(name='L8', val=0.43, loc=[sk[12], 0])

        add_R(name='R1', alR = 1, loc=[sk[2], sk[3]])
        add_R(name='R2', alR = 1, loc=[sk[3], sk[8]])
        add_R(name='R3', alR = 1, loc=[sk[3], sk[11]])
        add_R(name='R4', alR = 1, loc=[sk[9], 0])
        add_R(name='R5', alR = 1, loc=[sk[11], sk[1]])


        return new_names_obj