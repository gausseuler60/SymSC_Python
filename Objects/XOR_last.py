from Objects.ComplexObjectBase import ComplexObjectBase


class XOR_last(ComplexObjectBase):
    def __init__(self, loc, connect='Current', type_p='Gauss', t0=50, A=1, D=15, T=500, w=1):
        super().__init__(loc=loc)
        self.N = 9

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
        self.add_ib(name='Ib1', val=0.5, loc=[sk[6]])
        self.add_ib(name='Ib2', val=0.5, loc=[sk[7]])

        self.add_JJ(name='J1', c=1, r=1, A=1.37, B=0, loc=[sk[4], 0])
        self.add_JJ(name='J2', c=1, r=1, A=1.37, B=0, loc=[sk[5], 0])
        self.add_JJ(name='J3', c=1, r=1, A=1.37, B=0, loc=[sk[4], sk[6]])
        self.add_JJ(name='J4', c=1, r=1, A=1.37, B=0, loc=[sk[5], sk[7]])
        self.add_JJ(name='J5', c=1, r=1, A=1.77, B=0, loc=[sk[8], sk[3]])
        self.add_JJ(name='J6', c=1, r=1, A=1.54, B=0, loc=[sk[2], sk[3]])
        self.add_JJ(name='J7', c=1, r=1, A=1.5, B=0, loc=[sk[3], 0])

        self.add_L(name='L1', val=2, loc=[sk[6], sk[8]])
        self.add_L(name='L2', val=2, loc=[sk[7], sk[8]])
        self.add_L(name='L3', val=0.19, loc=[sk[0], sk[4]])
        self.add_L(name='L4', val=0.19, loc=[sk[1], sk[5]])


        
