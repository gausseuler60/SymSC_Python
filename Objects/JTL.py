from Objects.ComplexObjectBase import ComplexObjectBase


class JTL(ComplexObjectBase):
    def __init__(self, loc, N, ib_val=0.75, l_val=3, jj_c=1, jj_r=1,jj_a=1, jj_b=0):
        super().__init__(loc=loc)

        self.N = N
        self.ib_val = ib_val
        self.l_val = l_val
        self.jj_c = jj_c
        self.jj_r = jj_r
        self.jj_a = jj_a
        self.jj_b = jj_b

        self.name = 'JTL'
        self.description = 'Josephson transmission line'

    def create_elements(self, sk):
        sk = [sk[0]] + sk[2:] + [sk[1]]

        # generate objects
        for i in range(self.N):
            # Josephson junction
            name = f'JJ{i + 1}'
            self.add_JJ(name=name, loc=[sk[i], 0], c=self.jj_c, r=self.jj_r, A=self.jj_a, B=self.jj_b)

            # Current bias
            name = f'Ib{i + 1}'
            self.add_ib(name=name, val=self.ib_val, loc=[sk[i]])

            # Inductor
            if i == self.N - 1:  # inductors are only between JJ's
                continue
            name = f'L{i + 1}'
            self.add_L(name=name, val=self.l_val, loc=[sk[i], sk[i+1]])
