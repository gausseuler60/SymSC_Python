from Objects.ComplexObjectBase import ComplexObjectBase


class C_element(ComplexObjectBase):
    def __init__(self, loc):
        super().__init__(loc=loc)
        self.N = 7

        self.name = 'C_element'
        self.description = 'Coincidence Junction'

    def create_elements(self, sk):
        self.add_ib(name='Ib1', val=0.2, loc=[sk[0]])
        self.add_ib(name='Ib2', val=0.2, loc=[sk[1]])

        self.add_JJ(name='J1', c=1, r=1, A=1, B=0, loc=[sk[0], 0])
        self.add_JJ(name='J2', c=1, r=1,A=1, B=0, loc=[sk[1], 0])
        self.add_JJ(name='J3', c=1, r=1,A=2, B=0, loc=[sk[3], 0])

        self.add_L(name='L1', val=2, loc=[sk[0], sk[3]])
        self.add_L(name='L2', val=2, loc=[sk[1], sk[3]])
        self.add_L(name='L3', val=0.5, loc=[sk[3], sk[2]])
