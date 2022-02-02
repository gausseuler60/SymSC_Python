from Objects.ElementBase import *
from Objects.JJ import JJ
from Objects.Ib import Ib
from Objects.L import L

class Splitter(ElementBase):
    def __init__(self,loc):
        super().__init__()

        #self.check_loc() - always return True

        self.loc = loc
        self.N = 4


        self.name = 'Splitter'
        #self.description =

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


        add_ib(name='ibJJin', val = 0.75, data_index=[sk[3]])
        add_ib(name='ibJJout1', val = 0.75, data_index=[sk[1]])
        add_ib(name='ibJJout2', val = 0.75, data_index=[sk[2]])

        add_JJ(name='Jin', A = 6, B = 0, al = 1, data_index=[sk[3], 0])
        add_JJ(name='Jout1', A=2, B=0, al=1, data_index=[sk[1], 0])
        add_JJ(name='Jout2', A=2, B=0, al=1, data_index=[sk[2], 0])

        add_L(name='Lin', val = 3, data_index=[sk[0],sk[3]])
        add_L(name='Lout1', val = 3, data_index=[sk[3], sk[1]])
        add_L(name='Lout2', val = 3, data_index=[sk[3], sk[2]])

        return new_names_obj