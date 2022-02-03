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

        def add_JJ(name, A, B, al, data_index):
            new_obj = JJ(loc=None, A=A, B=B, al=al)
            new_obj.name = f'{self.name}_{name}'
            new_obj.data_index = data_index
            new_names_obj.append(new_obj)

        def add_ib(name, val, data_index):
            new_obj = Ib(loc=None, val=val)
            new_obj.name = f'{self.name}_{name}'
            new_obj.data_index = data_index
            new_names_obj.append(new_obj)

        def add_L(name, val, data_index):
            new_obj = L(loc=None, val=val)
            new_obj.name = f'{self.name}_{name}'
            new_obj.data_index = data_index
            new_names_obj.append(new_obj)

        add_ib(name='Ib1', val=0.176, data_index=[sk[8]])
        add_ib(name='Ib2', val=0.176, data_index=[sk[1]])
        add_ib(name='Ib3', val=0.132, data_index=[sk[13]])
        add_ib(name='Ib4', val=0.132, data_index=[sk[11]])

        add_JJ(name='J1', A=0.25, B=0, al=1, data_index=[sk[7], 0])
        add_JJ(name='J2', A=0.176, B=0, al=1, data_index=[sk[6], 0])
        add_JJ(name='J3', A=0.176, B=0, al=1, data_index=[sk[0], sk[7]])
        add_JJ(name='J4', A=0.176, B=0, al=1, data_index=[sk[5], sk[6]])
        add_JJ(name='J5', A=0.25, B=0, al=1, data_index=[sk[8], 0])
        add_JJ(name='J6', A=0.176, B=0, al=1, data_index=[sk[4], 0])
        add_JJ(name='J7', A=0.176, B=0, al=1, data_index=[sk[2], sk[8]])
        add_JJ(name='J8', A=0.176, B=0, al=1, data_index=[sk[13], sk[4]])
        add_JJ(name='J9', A=0.176, B=0, al=1, data_index=[sk[11], 0])
        add_JJ(name='J10', A=0.176, B=0, al=1, data_index=[sk[11], sk[12]])
        add_JJ(name='J11', A=0.176, B=0, al=1, data_index=[sk[9], 0])
        add_JJ(name='J12', A=0.176, B=0, al=1, data_index=[sk[9], sk[10]])

        add_L(name='L1', val=15.1, data_index=[sk[7], sk[6]])
        add_L(name='L2', val=15.1, data_index=[sk[0], sk[2]])
        add_L(name='L3', val=3.78, data_index=[sk[6], sk[11]])
        add_L(name='L4', val=3.78, data_index=[sk[4], sk[9]])
        add_L(name='L5', val=5.68, data_index=[sk[12], sk[3]])
        add_L(name='L6', val=5.68, data_index=[sk[10], sk[3]])
        add_L(name='L7', val=5.68, data_index=[sk[1], sk[5]])
        add_L(name='L8', val=5.68, data_index=[sk[1], sk[13]])


        return new_names_obj