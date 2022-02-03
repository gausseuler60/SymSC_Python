from Objects.ElementBase import *
from Objects.JJ import JJ
from Objects.Ib import Ib
from Objects.L import L


class MReceiver(ElementBase):
    def __init__(self, loc):
        super().__init__()

        self.loc = loc
        self.N = 11

        self.name = 'MReceiver'
        self.description = 'Microstrip Receiver'

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

        add_ib(name='Ib1', val=1.54, data_index=[sk[4]])
        add_ib(name='Ib2', val=1.4, data_index=[sk[9]])

        add_JJ(name='Jin', A=0.96, B=0, al=1, data_index=[sk[0], 0])
        add_JJ(name='J1', A=1.12, B=0, al=1, data_index=[sk[6], 0])
        add_JJ(name='Jout', A=2.01, B=0, al=1, data_index=[sk[8], 0])

        add_L(name='Lin', val=0.95, data_index=[sk[2], sk[1]])
        add_L(name='L1', val=0.05, data_index=[sk[1], sk[0]])
        add_L(name='L2', val=1.76, data_index=[sk[1], sk[3]])
        add_L(name='L3', val=0.05, data_index=[sk[3], sk[4]])
        add_L(name='L4', val=1.03, data_index=[sk[3], sk[5]])
        add_L(name='L5', val=0.05, data_index=[sk[5], sk[6]])
        add_L(name='L6', val=1.81, data_index=[sk[5], sk[7]])
        add_L(name='L7', val=0.05, data_index=[sk[7], sk[8]])
        add_L(name='L8', val=0.05, data_index=[sk[7], sk[9]])
        add_L(name='Lout', val=0.75, data_index=[sk[7], sk[10]])

        return new_names_obj