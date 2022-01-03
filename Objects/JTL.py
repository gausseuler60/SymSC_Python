from Objects.ElementBase import *
from Objects.JJ import JJ
from Objects.L import L
from Objects.Ib import Ib


class JTL(ElementBase):
    def __init__(self, loc, N, ib_val=0.75, l_val=3, jj_a=1, jj_b=0, jj_al=1):
        super().__init__()

        # numeric parameters
        self.N = N
        self.ib_val = ib_val
        self.l_val = l_val
        self.jj_a = jj_a
        self.jj_b = jj_b
        self.jj_al = jj_al

        self.loc = loc
        self.name = 'JTL'
        self.description = 'Josephson transmission line'

        self.complex = True

    # original name: ObjUnZip
    # instantiates all child objects
    # and returns a list of child objects
    # when this method is calles, data_index for input, output and internal connections is already built
    def unzip(self):
        new_names_obj = []

        sk = self.data_index
        print('sk', sk)
        sk = [sk[0]] + sk[2:] + [sk[1]]

        # generate objects
        for i in range(self.N):
            # Josephson junction
            name = f'{self.name}_JJ_{i + 1}'
            jj_now = JJ(loc=None, A=self.jj_a, B=self.jj_b, al=self.jj_al)  # loc is not needeed, it is used to make DataIndex, but we make it here manually
            jj_now.data_index = [sk[i], 0]
            jj_now.name = name
            new_names_obj.append(jj_now)

            # Current bias
            name = f'{self.name}_Ib_{i + 1}'
            ib_now = Ib(loc=None, val=self.ib_val)
            ib_now.data_index = [sk[i]]
            ib_now.name = name
            new_names_obj.append(ib_now)
            # Inductor
            if i == self.N - 1:  # inductors are only between JJ's
                continue
            name = f'{self.name}_L_{i + 1}'
            l_now = L(loc=None, val=self.l_val)
            l_now.data_index = [sk[i], sk[i+1]]
            l_now.name = name
            new_names_obj.append(l_now)

        return new_names_obj
