from Objects.ElementBase import *
from Objects.JJ import JJ
from Objects.Ib import Ib
from Objects.L import L


class PMerger2to1(ElementBase):
    def __init__(self, loc):
        super().__init__()

        self.loc = loc
        self.N = 6

        self.name = 'SPL1to4'
        self.description = 'Split 1 to 4'

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

        add_L(name='Lin', val=1.5, loc=[sk[0], sk[5]])

        add_JJ(name='Jm', A=1, B=0, al=1, loc=[sk[5], 0])
        add_JJ(name='Jo1', A=0.5, B=0, al=1, loc=[sk[5], sk[1]])
        add_JJ(name='Jo2', A=0.5, B=0, al=1, loc=[sk[5], sk[2]])
        add_JJ(name='Jo3', A=0.5, B=0, al=1, loc=[sk[5], sk[3]])
        add_JJ(name='Jo4', A=0.5, B=0, al=1, loc=[sk[5], sk[4]])

        add_ib(name='ibJm', val=0.75, loc=[sk[5]])

        return new_names_obj
