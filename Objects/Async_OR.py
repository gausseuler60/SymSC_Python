from Objects.ComplexObjectBase import ComplexObjectBase


class Async_OR(ComplexObjectBase):
    """
    RSFQ logic asynchronous OR gate

    Inputs:
    1 - first input signal
    2 - second input signal
    3 - output
    """
    def __init__(self, loc):
        super().__init__(loc=loc)
        self.check_loc(loc, 3)
        self.N = 8

        self.name = 'Async_OR'
        self.description = 'Asynchronous OR gate'

    def create_elements(self, sk):
        self.add_JJ(name='J_IA', c=0.5, r=1, A=0.96, B=0, loc=[sk[0], sk[3]])
        self.add_JJ(name='J_IB', c=0.5, r=1, A=0.96, B=0, loc=[sk[1], sk[4]])
        self.add_JJ(name='J_UA', c=0.5, r=1, A=0.8, B=0, loc=[sk[3], sk[2]])
        self.add_JJ(name='J_UB', c=0.5, r=1, A=0.8, B=0, loc=[sk[4], sk[2]])
        self.add_JJ(name='J_LA', c=0.5, r=1, A=1.04, B=0, loc=[sk[3], 0])
        self.add_JJ(name='J_LB', c=0.5, r=1, A=1.04, B=0, loc=[sk[4], 0])
        self.add_JJ(name='J_LIM', c=0.5, r=1, A=1.44, B=0, loc=[sk[2], sk[7]])
        self.add_JJ(name='J_P', c=0.5, r=1, A=0.56, B=0, loc=[sk[5], 0])
        self.add_JJ(name='J_PS', c=0.5, r=1, A=0.4, B=0, loc=[sk[6], 0])

        self.add_L(name='L_Bias', val=132, loc=[sk[7], 0])
        self.add_L(name='L_Poff', val=6, loc=[sk[2], sk[5]])

        self.add_R(name='R_S', r=0.4, loc=[sk[5], sk[6]])
