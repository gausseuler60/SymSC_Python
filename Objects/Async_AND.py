from Objects.ElementBase import *
from Objects.JJ import JJ
from Objects.Ib import Ib
from Objects.L import L
from Objects.R import R


class Async_AND(ElementBase):
    def __init__(self, loc):
        super().__init__()

        self.loc = loc
        self.N =7

        self.name = 'Async_AND'
        self.description = 'Asynchronous AND gate'

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

        def add_R(name, alR, data_index):
            new_obj = R(loc=None, alR = alR)
            new_obj.name = f'{self.name}_{name}'
            new_obj.data_index = data_index
            new_names_obj.append(new_obj)

        add_ib(name='Ib1', val=0.7, data_index=[sk[2]])

        add_JJ(name='J1', A=0.84, B=0, al=1, data_index=[sk[3], sk[2]])
        add_JJ(name='J2', A=0.84, B=0, al=1, data_index=[sk[5], sk[2]])
        add_JJ(name='J3', A=1.68, B=0, al=1, data_index=[sk[2], 0])
        add_JJ(name='JD1', A=0.6, B=0, al=1, data_index=[sk[4], sk[2]])
        add_JJ(name='JD2', A=0.6, B=0, al=1, data_index=[sk[6], sk[2]])

        add_L(name='L1', val=0.12, data_index=[sk[0], sk[3]])
        add_L(name='L2', val=0.12, data_index=[sk[1], sk[5]])

        add_R(name='RD1', alR = 6.7, data_index=[sk[3], sk[4]])
        add_R(name='RD2', alR = 6.7, data_index=[sk[5], sk[6]])

        return new_names_obj