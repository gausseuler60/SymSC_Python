from Objects.ElementBase import *
from Objects.JJ import JJ
from Objects.Ib import Ib
from Objects.L import L


class Splitter(ElementBase):
    def __init__(self, loc):
        super().__init__()

        self.loc = loc
        self.N = 4

        self.name = 'Splitter'
        self.description = 'Splitter'

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
            new_obj.loc = loc
            new_names_obj.append(new_obj)

        def add_L(name, val, loc):
            new_obj = L(loc=loc, val=val)
            new_obj.name = f'{self.name}_{name}'
            new_obj.loc = loc
            new_names_obj.append(new_obj)

        add_ib(name='ibJin', val=0.75, loc=[sk[3]])
        add_ib(name='ibJout1', val=0.75, loc=[sk[1]])
        add_ib(name='ibJout2', val=0.75, loc=[sk[2]])

        add_JJ(name='Jin', c=1, r=1, A=1.4, B=0, loc=[sk[3], 0])
        add_JJ(name='Jout1', c=1, r=1, A=1, B=0, loc=[sk[1], 0])
        add_JJ(name='Jout2', c=1, r=1, A=1, B=0, loc=[sk[2], 0])

        add_L(name='Lin', val=1, loc=[sk[0],sk[3]])
        add_L(name='Lout1', val=3.7, loc=[sk[3], sk[1]])
        add_L(name='Lout2', val=3.7, loc=[sk[3], sk[2]])

        return new_names_obj
