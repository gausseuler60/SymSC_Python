from Objects.ElementBase import *
from Objects.C import C
from Objects.R import R
from Objects.L import L


class Synaps(ElementBase):
    def __init__(self, loc):
        super().__init__()

        #self.check_loc(loc, 3)

        self.loc = loc
        self.N = 3

        self.name = 'Synaps'
        self.description = 'Crotty Synaps 2010'

        self.complex = True

    def unzip(self):
        sk = self.loc
        new_names_obj = []

        def add_C(name, c, loc):
            new_obj = C(loc=loc, c=c)
            new_obj.name = f'{self.name}_{name}'
            new_names_obj.append(new_obj)

        def add_R(name, r,loc):
            new_obj = R(loc=loc, r=r)
            new_obj.name = f'{self.name}_{name}'
            new_names_obj.append(new_obj)
            
        def add_L(name, val, loc):
            new_obj = L(loc=loc, val=val)
            new_obj.name = f'{self.name}_{name}'
            new_names_obj.append(new_obj)

        add_L(name='L_syn', val=1, loc=[sk[0], sk[2]])
        add_R(name='R_syn', r=0.01, loc=[sk[2], sk[1]])
        
        add_C(name='C_syn', c=1, loc=[sk[1], 0])

        
        return new_names_obj
