from Objects.ElementBase import *
from Objects.JJ import JJ
from Objects.Ib import Ib
from Objects.L import L


class dcsfq(ElementBase):
    def __init__(self, loc):
        super().__init__()

        self.loc = loc
        self.N = 4

        self.name = 'dcsfq'
        self.description = 'DC to SFQ converter'

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

        add_ib(name='Ib1', val=0.75, loc=[sk[2]])

        add_JJ(name='J1', c=1, r=1, A=1, B=0, loc=[sk[2], 0])
        add_JJ(name='J2', c=1, r=1, A=1, B=0, loc=[sk[0], sk[2]])

        add_L(name='L1', val=1, loc=[sk[0], 0])
        add_L(name='L2', val=1, loc=[sk[2], sk[1]])


        return new_names_obj
