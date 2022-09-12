from Objects.ComplexObjectBase import ComplexObjectBase


class SFQ_DC(ComplexObjectBase):
    def __init__(self, loc):
        super().__init__(loc=loc)
        self.N = 13

        self.name = 'SFQ_DC'
        self.description = 'SFQ to DC converter'

    def create_elements(self, sk):
        self.add_JJ(name='J1', A=1.18, B=0, r=1, c=1, loc=[sk[5], sk[8]])
        self.add_JJ(name='J2', A=1.37, B=0, r=1, c=1, loc=[sk[6], sk[7]])
        self.add_JJ(name='J3', A=1.37, B=0, r=1, c=1, loc=[sk[8], 0])
        self.add_JJ(name='J4', A=1.96, B=0, r=1, c=1, loc=[sk[10], sk[11]])
        self.add_JJ(name='J5', A=1.96, B=0, r=1, c=1, loc=[sk[7], 0])
        self.add_JJ(name='J6', A=1.96, B=0, r=1, c=1, loc=[sk[11], sk[12]])

        self.add_L(name='L1', val=1.27, loc=[sk[0], sk[2]])
        self.add_L(name='L2', val=1.36, loc=[sk[2], sk[4]])
        self.add_L(name='L3', val=0.48, loc=[sk[4], sk[5]])
        self.add_L(name='L4', val=0.26, loc=[sk[4], sk[6]])
        self.add_L(name='L5', val=0.49, loc=[sk[8], sk[9]])
        self.add_L(name='L6', val=0.1, loc=[sk[9], sk[7]])
        self.add_L(name='L7', val=0.1, loc=[sk[9], sk[10]])
        self.add_L(name='L8', val=0.43, loc=[sk[12], 0])

        self.add_R(name='R1', r=1, loc=[sk[2], sk[3]])
        self.add_R(name='R2', r=1, loc=[sk[3], sk[8]])
        self.add_R(name='R3', r=1, loc=[sk[3], sk[11]])
        self.add_R(name='R4', r=1, loc=[sk[9], 0])
        self.add_R(name='R5', r=1, loc=[sk[11], sk[1]])
