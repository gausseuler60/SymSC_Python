from Objects.ElementBase import *
from Objects.JJ import JJ
from Objects.Ib import Ib
from Objects.L import L


class C_element(ElementBase):
    def __init__(self, loc):
        super().__init__()

        self.loc = loc
        self.N = 7

        self.name = 'C_element'
        self.description = 'Coincidence Junction'

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

        add_ib(name='Ib1', val=1.4, data_index=[sk[5]])
        add_ib(name='Ib2', val=0.7, data_index=[sk[6]])

        add_JJ(name='J1', A=1.4, B=0, al=1, data_index=[sk[3], 0])
        add_JJ(name='J2', A=1.4, B=0, al=1, data_index=[sk[4], 0])
        add_JJ(name='J3', A=1, B=0, al=1, data_index=[sk[3], sk[5]])
        add_JJ(name='J4', A=1, B=0, al=1, data_index=[sk[4], sk[5]])
        add_JJ(name='J5', A=1, B=0, al=1, data_index=[sk[6], 0])

        add_L(name='L1', val=2, data_index=[sk[0], sk[3]])
        add_L(name='L2', val=2, data_index=[sk[1], sk[4]])
        add_L(name='L3', val=0.5, data_index=[sk[5], sk[6]])
        add_L(name='L4', val=2, data_index=[sk[6], sk[2]])


        return new_names_obj