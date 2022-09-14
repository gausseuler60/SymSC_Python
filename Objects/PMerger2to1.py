from Objects.ComplexObjectBase import ComplexObjectBase


class PMerger2to1(ComplexObjectBase):
    def __init__(self, loc):
        super().__init__(loc=loc)
        self.check_loc(loc, 3)
        self.N = 3

        self.name = 'PMerger2to1'
        self.description = 'Merger 2 pulses to 1 pulse'

    def create_elements(self, sk):
        self.add_JJ(name='J1', A=1, B=0, r=1, c=1, loc=[sk[0], 0])
        self.add_JJ(name='J2', A=1, B=0, r=1, c=1, loc=[sk[1], 0])
        self.add_JJ(name='J3', A=0.7, B=0, r=1, c=1, loc=[sk[0], sk[2]])
        self.add_JJ(name='J4', A=0.7, B=0, r=1, c=1, loc=[sk[1], sk[2]])
        self.add_JJ(name='J5', A=1, B=0, r=1, c=1, loc=[sk[2], 0])

        self.add_ib(name='ib0', val=1.7, loc=[sk[2]])
        self.add_ib(name='ib1', val=0.5, loc=[sk[0]])
        self.add_ib(name='ib2', val=0.5, loc=[sk[1]])
