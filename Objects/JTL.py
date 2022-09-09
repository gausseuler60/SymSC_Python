from Objects.ElementBase import *
from Objects.JJ import JJ
from Objects.L import L
from Objects.Ib import Ib


class JTL(ElementBase):
    def __init__(self, loc, N, ib_val=0.75, l_val=3, jj_c=1, jj_r=1,jj_a=1, jj_b=0):
        super().__init__()

        # numeric parameters
        self.N = N
        self.ib_val = ib_val
        self.l_val = l_val
        self.jj_c = jj_c
        self.jj_r = jj_r
        self.jj_a = jj_a
        self.jj_b = jj_b
  

        self.loc = loc
        self.name = 'JTL'
        self.description = 'Josephson transmission line'

        self.complex = True

    # original name: ObjUnZip
    # instantiates all child objects
    # and returns a list of child objects
    # when this method is calles, loc for input, output and internal connections is already built
    def unzip(self):
        new_obj = []

        sk = self.data_index
        sk = [sk[0]] + sk[2:] + [sk[1]]

        # generate objects
        for i in range(self.N):
            # Josephson junction
            name = f'{self.name}_JJ{i + 1}'
            jj_now = JJ(loc=[sk[i], 0], c=self.jj_c, r=self.jj_r, A=self.jj_a, B=self.jj_b)
            jj_now.name = name
            new_obj.append(jj_now)

            # Current bias
            name = f'{self.name}_Ib{i + 1}'
            ib_now = Ib(loc=[sk[i]], val=self.ib_val)
            ib_now.name = name
            new_obj.append(ib_now)
            # Inductor
            if i == self.N - 1:  # inductors are only between JJ's
                continue
            name = f'{self.name}_L{i + 1}'
            l_now = L(loc=[sk[i], sk[i+1]], val=self.l_val)
            l_now.name = name
            new_obj.append(l_now)

        return new_obj
