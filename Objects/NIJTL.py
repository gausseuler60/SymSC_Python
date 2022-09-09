from Objects.ElementBase import *
from Objects.JJ import JJ
from Objects.Ib import Ib


class NIJTL(ElementBase):
    def __init__(self, loc, N, ib_val=0.75, jj_c = 1, jj_r = 1, jj_a=1, jj_b=0, jj_c_c = 1, jj_c_r = 1, jj_c_a=0.7, jj_c_b=0):
        super().__init__()

        # numeric parameters
        self.N = N
        self.ib_val = ib_val
        self.jj_a = jj_a
        self.jj_b = jj_b
        self.jj_c = jj_c
        self.jj_r = jj_r

        self.jj_c_a = jj_c_a
        self.jj_c_b = jj_c_b
        self.jj_c_c = jj_c_c
        self.jj_c_r = jj_c_r

        self.loc = loc
        self.name = 'NIJTL'
        self.description = 'Josephson transmission line without L'

        self.complex = True

    def unzip(self):
        new_names_obj = []

        sk = self.data_index
        sk = [sk[0]] + sk[2:] + [sk[1]]

        # generate objects
        for i in range(self.N):
            # Josephson junction
            name = f'{self.name}_JJ_{i + 1}'
            jj_now = JJ(loc=[sk[i], 0], c=self.jj_c, r=self.jj_r, A=self.jj_a, B=self.jj_b)
            jj_now.name = name
            new_names_obj.append(jj_now)

            # Current bias
            name = f'{self.name}_Ib_{i + 1}'
            ib_now = Ib(loc=[sk[i]], val=self.ib_val)
            ib_now.name = name
            new_names_obj.append(ib_now)
            # Inductor
            if i == self.N - 1:  # inductors are only between JJ's
                continue
            name = f'{self.name}_JJc_{i + 1}'
            jjc_now = JJ(loc=[sk[i], 0], c=self.jj_c_c, r=self.jj_c_r, A=self.jj_c_a, B=self.jj_c_b)
            jjc_now.name = name
            new_names_obj.append(jjc_now)

        return new_names_obj
