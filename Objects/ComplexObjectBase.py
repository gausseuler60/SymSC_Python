from Objects.ElementBase import *
from Objects.JJ import JJ
from Objects.Ib import Ib
from Objects.L import L
from Objects.R import R
from Objects.C import C
from Objects.Pulses import Pulses


class ComplexObjectBase(ElementBase):
    def __init__(self, loc):
        super().__init__()

        self.loc = loc
        # must be set in a child class constructor
        self.N = None
        self.name = None

        self.complex = True
        self._new_names_obj = []

    def add_JJ(self, name, c, r, A, B, loc):
        new_obj = JJ(loc=loc, c=c, r=r, A=A, B=B)
        new_obj.name = f'{self.name}_{name}'
        self._new_names_obj.append(new_obj)

    def add_ib(self, name, val, loc):
        new_obj = Ib(loc=loc, val=val)
        new_obj.name = f'{self.name}_{name}'
        self._new_names_obj.append(new_obj)

    def add_L(self, name, val, loc):
        new_obj = L(loc=loc, val=val)
        new_obj.name = f'{self.name}_{name}'
        self._new_names_obj.append(new_obj)

    def add_R(self, name, r, loc):
        new_obj = R(loc=loc, r=r)
        new_obj.name = f'{self.name}_{name}'
        self._new_names_obj.append(new_obj)

    def add_C(self, name, c, loc):
        new_obj = C(loc=loc, c=c)
        new_obj.name = f'{self.name}_{name}'
        self._new_names_obj.append(new_obj)

    def add_Pulses(self, name, loc, connect, type_p, t0, A, D, T, w):
        new_obj = Pulses(loc=loc, connect=connect, type_p=type_p, t0=t0, A=A, D=D, T=T, w=w)
        new_obj.name = f'{self.name}_{name}'
        self._new_names_obj.append(new_obj)

    def create_elements(self, sk):
        raise NotImplementedError

    def unzip(self):
        sk = self.data_index
        self.create_elements(sk)

        return self._new_names_obj
