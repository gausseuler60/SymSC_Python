from Objects.ElementBase import *
from Objects.JJ import JJ
from Objects.Ib import Ib
from Objects.L import L
from Objects.Pulses import Pulses


class XOR(ElementBase):
    def __init__(self, loc, connect='Current', type_p='Gauss', t0=50, A=1, D=15, T=500, w=1):
        super().__init__()

        self.loc = loc
        self.N = 10
        self.connect = connect
        self.type_p = type_p
        self.t0 = t0
        self.A = A
        self.D = D
        self.T = T
        self.w = w

        self.name = 'XOR'
        self.description = 'Exclusive OR'

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

        def add_Pulses(name, loc):
            new_obj = Pulses(loc=loc, connect=self.connect, type_p=self.type_p, t0=self.t0, A=self.A, D=self.D, T=self.T, w=self.w)
            new_obj.name = f'{self.name}_{name}'
            new_names_obj.append(new_obj)

        add_ib(name='Ib1', val=0.0112, loc=[sk[4]])
        add_ib(name='Ib2', val=0.0056, loc=[sk[6]])

        add_JJ(name='J1', c=1,r=1,A=0.0112, B=0, loc=[sk[3], 0])
        add_JJ(name='J2',c=1,r=1, A=0.0112, B=0, loc=[sk[5], 0])
        add_JJ(name='J3', c=1,r=1,A=0.008, B=0, loc=[sk[3], sk[4]])
        add_JJ(name='J4', c=1,r=1,A=0.008, B=0, loc=[sk[5], sk[6]])
        add_JJ(name='J5', c=1,r=1,A=0.008, B=0, loc=[sk[7], sk[8]])
        add_JJ(name='J6', c=1,r=1,A=0.008, B=0, loc=[sk[9], sk[8]])
        add_JJ(name='J7', c=1,r=1,A=0.016, B=0, loc=[sk[8], 0])

        add_L(name='L1', val=0.76, loc=[sk[4], sk[7]])
        add_L(name='L2', val=0.76, loc=[sk[6], sk[7]])
        add_L(name='L3', val=0.19, loc=[sk[0], sk[3]])
        add_L(name='L4', val=0.19, loc=[sk[1], sk[5]])
        add_L(name='L5', val=0.19, loc=[sk[8], sk[2]])

        add_Pulses(name='T', loc=[sk[9]])

        return new_names_obj
