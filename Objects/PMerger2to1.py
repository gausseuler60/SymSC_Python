from Objects.ElementBase import *
from Objects.JJ import JJ
from Objects.Ib import Ib


class PMerger2to1(ElementBase):
    def __init__(self, loc):
        super().__init__()

        self.check_loc(loc, 3)

        self.loc = loc
        self.N = 3

        self.name = 'PMerger2to1'
        self.description = 'Merger 2 pulses to 1 pulse'

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

        add_JJ(name='J1', A=1, B=0, al=1, data_index=[sk[0], 0])
        add_JJ(name='J2', A=1, B=0, al=1, data_index=[sk[1], 0])
        add_JJ(name='J3', A=0.7, B=0, al=1, data_index=[sk[0], sk[2]])
        add_JJ(name='J4', A=0.7, B=0, al=1, data_index=[sk[1], sk[2]])
        add_JJ(name='J5', A=1, B=0, al=1, data_index=[sk[2], 0])

        add_ib(name='ib0', val=1.7, data_index=[sk[2]])
        add_ib(name='ib1', val=0.5, data_index=[sk[0]])
        add_ib(name='ib2', val=0.5, data_index=[sk[1]])

        return new_names_obj
