from Objects.ElementBase import *
from Objects.JJ import JJ
from Objects.L import L
from Objects.R import R


class Async_OR(ElementBase):
    def __init__(self, loc):
        super().__init__()

        self.loc = loc
        self.N = 8

        self.name = 'Async_OR'
        self.description = 'Asynchronous OR gate'

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

        def add_R(name, r, loc):
            new_obj = R(loc=loc, r = r)
            new_obj.name = f'{self.name}_{name}'
            new_names_obj.append(new_obj)

        add_JJ(name='J_IA', c=0.5, r=1e-3, A=0.96, B=0, loc=[sk[0], sk[3]])
        add_JJ(name='J_IB', c=0.5, r=1e-3, A=0.96, B=0, loc=[sk[1], sk[4]])
        add_JJ(name='J_UA', c=0.5, r=1e-3, A=0.8, B=0, loc=[sk[3], sk[2]])
        add_JJ(name='J_UB', c=0.5, r=1e-3, A=0.8, B=0, loc=[sk[4], sk[2]])
        add_JJ(name='J_LA', c=0.5, r=1e-3, A=1.04, B=0, loc=[sk[3], 0])
        add_JJ(name='J_LB', c=0.5, r=1e-3, A=1.04, B=0, loc=[sk[4], 0])
        add_JJ(name='J_LIM', c=0.5, r=1e-3, A=1.44, B=0, loc=[sk[2], sk[7]])
        add_JJ(name='J_P', c=0.5, r=1e-3, A=0.56, B=0, loc=[sk[5], 0])
        add_JJ(name='J_PS', c=0.5, r=1e-3, A=0.4, B=0, loc=[sk[6], 0])

        add_L(name='L_Bias', val=132.57, loc=[sk[7], 0])
        add_L(name='L_Poff', val=6.06, loc=[sk[2], sk[5]])

        add_R(name='R_S', r=0.41667, loc=[sk[5], sk[6]])

        return new_names_obj
