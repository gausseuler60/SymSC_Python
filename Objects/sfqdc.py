from Objects.ComplexObjectBase import ComplexObjectBase

class sfqdc(ComplexObjectBase):
    def __init__(self, loc):
        super().__init__(loc=loc)
        self.N = 8

        self.name = 'sfqdc'
        self.description = 'SFQ to DC converter'

    def create_elements(self, sk):
        self.add_JJ(name='J1', c=1, r=1, A=1.6, B=0, loc=[sk[6], 0])
        self.add_JJ(name='J2', c=1, r=1, A=0.8, B=0, loc=[sk[3], sk[6]])
        self.add_JJ(name='J3', c=1, r=1, A=1.2, B=0, loc=[sk[5], 0])
        self.add_JJ(name='J4', c=1, r=1, A=0.4, B=0, loc=[sk[4], sk[5]])
        self.add_JJ(name='J5', c=1, r=1, A=1.4, B=0, loc=[sk[2], 0])
        self.add_JJ(name='J6', c=1, r=1, A=1.4, B=0, loc=[sk[7], sk[2]])

        self.add_L(name='L1', val=2, loc=[sk[0], sk[3]])
        self.add_L(name='L2', val=2, loc=[sk[1], sk[4]])
        
        self.add_L(name='L3', val=4.6, loc=[sk[6], sk[7]])
        self.add_L(name='L4', val=4.6, loc=[sk[5], sk[7]])
        
        self.add_ib(name='Ib1', val=0.8, loc=[sk[6]])
        self.add_ib(name='Ib2', val=0.64, loc=[sk[2]])

        self.add_R(name='R1', r = 0.5, loc=[sk[7], 0])
