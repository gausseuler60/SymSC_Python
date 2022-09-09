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

        add_ib(name='Ib1', val=1.54, loc=[sk[4]])
        add_ib(name='Ib2', val=1.4, loc=[sk[9]])

        add_JJ(name='Jin', c=1, r=1,A=0.96, B=0, loc=[sk[2], 0])
        add_JJ(name='J1', c=1, r=1,A=1.12, B=0, loc=[sk[6], 0])
        add_JJ(name='Jout', c=1, r=1,A=2.01, B=0, loc=[sk[8], 0])

        add_L(name='Lin', val=0.95, loc=[sk[0], sk[10]])
        add_L(name='L1', val=0.05, loc=[sk[10], sk[2]])
        add_L(name='L2', val=1.76, loc=[sk[10], sk[3]])
        add_L(name='L3', val=0.05, loc=[sk[3], sk[4]])
        add_L(name='L4', val=1.03, loc=[sk[3], sk[5]])
        add_L(name='L5', val=0.05, loc=[sk[5], sk[6]])
        add_L(name='L6', val=1.81, loc=[sk[5], sk[7]])
        add_L(name='L7', val=0.05, loc=[sk[7], sk[8]])
        add_L(name='L8', val=0.05, loc=[sk[7], sk[9]])
        add_L(name='Lout', val=0.75, loc=[sk[7], sk[1]])

        return new_names_obj
