from Objects.ElementBase import *
from Objects.JJ import JJ
from Objects.L import L
from Objects.Ib import Ib
from Objects.R import R

class TFF(ElementBase):
    def __init__(self, loc):
        super().__init__()

        self.loc = loc
        self.N = 7

        self.name = 'TFF'
        self.description = 'T trigger with Read-Out line'

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
            new_obj.loc = loc
            new_names_obj.append(new_obj)
            
        def add_R(name,r,loc):
            new_obj = R(loc=loc, r=r)
            new_obj.name = f'{self.name}_{name}'
            new_obj.loc = loc
            new_names_obj.append(new_obj)

        add_JJ(name='J2', c=1,r=1,A=1, B=0, loc=[sk[3], sk[4]])
        add_JJ(name='J4', c=1,r=1,A=1, B=0, loc=[sk[3], sk[6]])
        add_JJ(name='J1', c=1,r=1,A=1.5, B=0, loc=[sk[4], 0])
        add_JJ(name='J3', c=1,r=1, A=1.5, B=0, loc=[sk[6], 0])
        
        add_L(name='L0',val=1,loc=[sk[0],sk[3]])
        add_L(name='L1',val=1,loc=[sk[4],sk[5]])
        add_L(name='L2',val=1,loc=[sk[5],sk[6]])
        
        add_L(name='L3',val=1,loc=[sk[4],sk[1]])
        add_L(name='L4',val=1,loc=[sk[6],sk[2]])

        add_ib(name='Ib1', val=0.75, loc=[sk[4]])
        
        add_R(name='R1', r=1, loc=[sk[5],0])
        return new_names_obj
