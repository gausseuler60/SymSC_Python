from Objects.ElementBase import *
from Objects.JJ import JJ
from Objects.Ib import Ib
from Objects.L import L


class Neuron(ElementBase):
    def __init__(self, loc):
        super().__init__()

        #self.check_loc(loc, 3)

        self.loc = loc
        self.N = 4

        self.name = 'Neuron'
        self.description = 'Crotty Neuron 2010'

        self.complex = True

    def unzip(self):
        sk = self.loc
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

        add_JJ(name='JJ_c', c=1, r=1, A=1, B=0, loc=[sk[3], sk[2]])
        add_JJ(name='JJ_p', c=1, r=1, A=1, B=0, loc=[sk[1], 0])
        
        add_L(name='L_c', val=0.0001, loc=[sk[0], sk[3]])
        add_L(name='L_s', val=4.948, loc=[sk[0], 0])
        add_L(name='L_p', val=4.948, loc=[sk[2], sk[1]])

        add_ib(name='I_NB', val=1, loc=[sk[2]])

        return new_names_obj
