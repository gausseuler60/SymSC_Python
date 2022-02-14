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

        def add_JJ(name, A, B, al, data_index):
            new_obj = JJ(loc=None, A=A, B=B, al=al)
            new_obj.name = f'{self.name}_{name}'
            new_obj.data_index = data_index
            new_names_obj.append(new_obj)

        def add_L(name, val, data_index):
            new_obj = L(loc=None, val=val)
            new_obj.name = f'{self.name}_{name}'
            new_obj.data_index = data_index
            new_names_obj.append(new_obj)

        def add_R(name, alR, data_index):
            new_obj = R(loc=None, alR = alR)
            new_obj.name = f'{self.name}_{name}'
            new_obj.data_index = data_index
            new_names_obj.append(new_obj)


        add_JJ(name='J_IA', A=0.12, B=0, al=1, data_index=[sk[0], sk[3]])
        add_JJ(name='J_IB', A=0.12, B=0, al=1, data_index=[sk[1], sk[4]])
        add_JJ(name='J_UA', A=0.1, B=0, al=1, data_index=[sk[3], sk[2]])
        add_JJ(name='J_UB', A=0.1, B=0, al=1, data_index=[sk[4], sk[2]])
        add_JJ(name='J_LA', A=0.13, B=0, al=1, data_index=[sk[3], 0])
        add_JJ(name='J_LB', A=0.13, B=0, al=1, data_index=[sk[4], 0])
        add_JJ(name='J_LIM', A=0.18, B=0, al=1, data_index=[sk[2], sk[7]])
        add_JJ(name='J_P', A=0.07, B=0, al=1, data_index=[sk[5], 0])
        add_JJ(name='J_PS', A=0.05, B=0, al=1, data_index=[sk[6], 0])

        add_L(name='L_Bias', val=0.35, data_index=[sk[7], 0])
        add_L(name='L_Poff', val=0.016, data_index=[sk[2], sk[5]])

        add_R(name='R_S', alR = 10, data_index=[sk[5], sk[6]])

        return new_names_obj