from Objects.ComplexObjectBase import ComplexObjectBase


class XOR(ComplexObjectBase):
    def __init__(self, loc, connect='Current', type_p='Gauss', t0=50, A=1, D=15, T=500, w=1):
        super().__init__(loc=loc)
        self.check_loc(loc, 3)
        self.N = 10

        self.connect = connect
        self.type_p = type_p
        self.t0 = t0
        self.A = A
        self.D = D
        self.T = T
        self.w = w

        self.name = 'XOR'
        self.description = 'Exclusive OR'

    def create_elements(self, sk):
        self.add_ib(name='Ib1', val=0.0112, loc=[sk[4]])
        self.add_ib(name='Ib2', val=0.0056, loc=[sk[6]])

        self.add_JJ(name='J1', c=1, r=1, A=0.0112, B=0, loc=[sk[3], 0])
        self.add_JJ(name='J2', c=1, r=1, A=0.0112, B=0, loc=[sk[5], 0])
        self.add_JJ(name='J3', c=1, r=1, A=0.008, B=0, loc=[sk[3], sk[4]])
        self.add_JJ(name='J4', c=1, r=1, A=0.008, B=0, loc=[sk[5], sk[6]])
        self.add_JJ(name='J5', c=1, r=1, A=0.008, B=0, loc=[sk[7], sk[8]])
        self.add_JJ(name='J6', c=1, r=1, A=0.008, B=0, loc=[sk[9], sk[8]])
        self.add_JJ(name='J7', c=1, r=1, A=0.016, B=0, loc=[sk[8], 0])

        self.add_L(name='L1', val=0.76, loc=[sk[4], sk[7]])
        self.add_L(name='L2', val=0.76, loc=[sk[6], sk[7]])
        self.add_L(name='L3', val=0.19, loc=[sk[0], sk[3]])
        self.add_L(name='L4', val=0.19, loc=[sk[1], sk[5]])
        self.add_L(name='L5', val=0.19, loc=[sk[8], sk[2]])

        self.add_Pulses(name='T', loc=[sk[9]], connect=self.connect, type_p=self.type_p, t0=self.t0, A=self.A, D=self.D,
                        T=self.T, w=self.w)
