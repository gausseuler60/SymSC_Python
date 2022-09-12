from Objects.ComplexObjectBase import ComplexObjectBase


class Likh_Inverter(ComplexObjectBase):
    def __init__(self, loc):
        super().__init__(loc=loc)
        self.N = 9

        self.name = 'Likh_Inverter'
        self.description = 'RSFQ inverter Likharev version'

    def create_elements(self, sk):
        self.add_ib(name='Ib', val=0.5, loc=[sk[5]])

        self.add_JJ(name='J1', c=1, r=1, A=1, B=0, loc=[sk[4], sk[5]])
        self.add_JJ(name='J2', c=1, r=1, A=1, B=0, loc=[sk[7], sk[6]])
        self.add_JJ(name='J3', c=1, r=1, A=1, B=0, loc=[sk[2], 0])
        self.add_JJ(name='J4', c=1, r=1, A=1, B=0, loc=[sk[5], sk[6]])
        self.add_JJ(name='J5', c=1, r=1, A=1, B=0, loc=[sk[6], 0])
        
        self.add_L(name='L1', val=0.1, loc=[sk[0], sk[4]])
        self.add_L(name='L2', val=0.1, loc=[sk[2], sk[8]])
        self.add_L(name='L3', val=0.1, loc=[sk[8], sk[1]])
        self.add_L(name='L4', val=0.1, loc=[sk[1], sk[7]])
        self.add_L(name='L5', val=0.1, loc=[sk[2], sk[5]])
        self.add_L(name='L6', val=0.1, loc=[sk[6], sk[3]])

        self.add_R(name='R', r=0.2, loc=[sk[8], 0])
