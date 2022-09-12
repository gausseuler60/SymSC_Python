from Objects.ComplexObjectBase import ComplexObjectBase


class dcsfq(ComplexObjectBase):
    def __init__(self, loc):
        super().__init__(loc=loc)
        self.N = 3

        self.name = 'dcsfq'
        self.description = 'DC to SFQ converter'

    def create_elements(self, sk):
        self.add_ib(name='Ib1', val=0.75, loc=[sk[2]])

        self.add_JJ(name='J1', c=1, r=1, A=1, B=0, loc=[sk[2], 0])
        self.add_JJ(name='J2', c=1, r=1, A=1, B=0, loc=[sk[0], sk[2]])

        self.add_L(name='L1', val=1, loc=[sk[0], 0])
        self.add_L(name='L2', val=1, loc=[sk[2], sk[1]])

