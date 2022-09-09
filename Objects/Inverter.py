from Objects.ElementBase import *
from Objects.JJ import JJ
from Objects.Ib import Ib
from Objects.L import L
from Objects.Pulses import Pulses
from Objects.R import R


class Inverter(ElementBase):
    def __init__(self, loc, connect='Current', type_p='Gauss', t0=50, A=1, D=15, T=500, w=1):
        super().__init__()

        self.loc = loc
        self.N = 27
        self.connect = connect
        self.type_p = type_p
        self.t0 = t0
        self.A = A
        self.D = D
        self.T = T
        self.w = w

        self.name = 'Inverter'
        self.description = 'RSFQ inverter'

        self.complex = True

    def unzip(self):
        sk = self.data_index
        new_names_obj = []

        def add_JJ(name, A, B, al, loc):
            new_obj = JJ(loc=loc, A=A, B=B, al=al)
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

        def add_R(name, alR, loc):
            new_obj = R(loc=loc, alR = alR)
            new_obj.name = f'{self.name}_{name}'
            new_names_obj.append(new_obj)


        add_ib(name='Io1', val=2.01, loc=[sk[6]])
        add_ib(name='Io2', val=1.92, loc=[sk[12]])
        add_ib(name='I1', val=1.24, loc=[sk[15]])
        add_ib(name='I2', val=1.48, loc=[sk[24]])

        add_JJ(name='J1', A=2.01, B=0, al=1, loc=[sk[3], sk[4]])
        add_JJ(name='J2', A=2.48, B=0, al=1, loc=[sk[7], sk[8]])
        add_JJ(name='J3', A=1.12, B=0, al=1, loc=[sk[7], sk[9]])
        add_JJ(name='J4', A=1.4, B=0, al=1, loc=[sk[10], sk[18]])
        add_JJ(name='J5', A=2.35, B=0, al=1, loc=[sk[13], sk[19]])
        add_JJ(name='J6', A=2.84, B=0, al=1, loc=[sk[16], sk[17]])
        add_JJ(name='J7', A=2.35, B=0, al=1, loc=[sk[21], sk[22]])
        add_JJ(name='J8', A=2.11, B=0, al=1, loc=[sk[25], sk[26]])

        add_L(name='L1', val=0.011, loc=[sk[4], 0])
        add_L(name='L2', val=0.75, loc=[sk[0], sk[3]])
        add_L(name='L3', val=0.392, loc=[sk[3], sk[5]])
        add_L(name='L4', val=0.133, loc=[sk[6], sk[5]])
        add_L(name='L5', val=0.371, loc=[sk[5], sk[7]])
        add_L(name='L6', val=0.033, loc=[sk[8], 0])
        add_L(name='L7', val=0.369, loc=[sk[9], sk[10]])
        add_L(name='L8', val=0.124, loc=[sk[10], sk[11]])
        add_L(name='L9', val=0.396, loc=[sk[18], sk[20]])
        add_L(name='L10', val=0.271, loc=[sk[12], sk[11]])
        add_L(name='L11', val=2.23, loc=[sk[13], sk[11]])
        add_L(name='L12', val=0.215, loc=[sk[19], sk[20]])
        add_L(name='L13', val=0.492, loc=[sk[14], sk[13]])
        add_L(name='L14', val=0.127, loc=[sk[15], sk[14]])
        add_L(name='L15', val=0.386, loc=[sk[16], sk[14]])
        add_L(name='L16', val=0.008, loc=[sk[17], 0])
        add_L(name='L17', val=0.3, loc=[sk[1], sk[16]])
        add_L(name='L18', val=0.332, loc=[sk[20], sk[21]])
        add_L(name='L19', val=0.055, loc=[sk[22], 0])
        add_L(name='L20', val=0.646, loc=[sk[21], sk[23]])
        add_L(name='L21', val=0.192, loc=[sk[24], sk[23]])
        add_L(name='L22', val=0.423, loc=[sk[23], sk[25]])
        add_L(name='L23', val=0.011, loc=[sk[26], 0])
        add_L(name='L24', val=0.9, loc=[sk[25], sk[2]])

        add_Pulses(name='D', loc=[sk[5]])

        add_R(name='R', alR = 5, loc=[sk[6], 0])


        return new_names_obj