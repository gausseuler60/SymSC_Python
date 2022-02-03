from Objects.ElementBase import *
from Objects.JJ import JJ
from Objects.Ib import Ib
from Objects.L import L
from Objects.R import R

class MDriver(ElementBase):
    def __init__(self,loc):
        super().__init__()


        self.loc = loc
        self.N = 8


        self.name = 'MDriver'
        self.description = 'Microstrip Driver'

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
            new_obj = R(loc=None, alR=alR)
            new_obj.name = f'{self.name}_{name}'
            new_obj.data_index = data_index
            new_names_obj.append(new_obj)
            

        add_ib(name='Ib', val = 2.77, data_index=[sk[4]])

        add_JJ(name='Jin', A=2.01, B = 0, al = 1, data_index=[sk[0], 0])
        add_JJ(name='Jout', A=2.01, B=0, al=1, data_index=[sk[6], 0])

        add_L(name='Lin', val = 0.75, data_index=[sk[2], sk[1]])
        add_L(name='L1', val = 0.05, data_index=[sk[1],sk[0]])
        add_L(name='L2', val = 0.6, data_index=[sk[1], sk[3]])
        add_L(name='L3', val = 0.05, data_index=[sk[4], sk[3]])
        add_L(name='L4', val = 0.62, data_index=[sk[3], sk[5]])
        add_L(name='L5', val = 0.05, data_index=[sk[5], sk[6]])
        add_L(name='Lout', val = 0.6, data_index=[sk[5], sk[7]])

        add_R(name='R', alR=1.5, data_index=[sk[7], 0])

        return new_names_obj