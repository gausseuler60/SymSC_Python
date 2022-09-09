from Objects.ElementBase import *
from Objects.JJ import JJ
from Objects.Ib import Ib
from Objects.L import L


class C_element(ElementBase):
    def __init__(self, loc):
        super().__init__()

        self.loc = loc
        self.N = 21

        self.name = 'C_element'
        self.description = 'Coincidence Junction'

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

        add_ib(name='Ib7', val=1.4, loc=[sk[0]])
        add_ib(name='Ib10', val=1.41, loc=[sk[5]])
        add_ib(name='Ib11', val=1.41, loc=[sk[8]])
        add_ib(name='Ib18', val=1.4, loc=[sk[1]])
        add_ib(name='Ib19', val=1.4, loc=[sk[2]])

        add_JJ(name='J12', c=1, r=1, A=1.51, B=0, loc=[sk[3], 0])
        add_JJ(name='J0', c=1, r=1,A=2.1, B=0, loc=[sk[4], 0])
        add_JJ(name='J1', c=1, r=1,A=2.84, B=0, loc=[sk[9], 0])
        add_JJ(name='J2', c=1, r=1, A=2.1, B=0, loc=[sk[7], 0])
        add_JJ(name='J16', c=1, r=1,A=1.51, B=0, loc=[sk[6], 0])
        add_JJ(name='J21', c=1, r=1,A=2.89, B=0, loc=[sk[2], 0])

        add_L(name='L7', val=0.81, loc=[sk[0], sk[3]])
        add_L(name='L10', val=1.25, loc=[sk[3], sk[4]])
        add_L(name='L3', val=0.54, loc=[sk[4], sk[5]])
        add_L(name='L5', val=1.25, loc=[sk[5], sk[9]])
        
        add_L(name='L8', val=0.81, loc=[sk[1], sk[6]])
        add_L(name='L13', val=1.25, loc=[sk[6], sk[7]])
        add_L(name='L4', val=0.54, loc=[sk[7], sk[8]])
        add_L(name='L6', val=1.25, loc=[sk[8], sk[9]])
        
        add_L(name='L9', val=1.14, loc=[sk[9], sk[2]])

        return new_names_obj
