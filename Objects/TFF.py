from Objects.ComplexObjectBase import ComplexObjectBase

class TFF(ComplexObjectBase):
    def __init__(self, loc):
        super().__init__(loc=loc)
        self.N = 7

        self.name = 'TFF'
        self.description = 'T trigger with Read-Out line'

    def create_elements(self, sk):
        add_JJ(name='J2', c=1,r=1,A=1, B=0, loc=[sk[3], sk[4]])
        add_JJ(name='J4', c=1,r=1,A=1, B=0, loc=[sk[3], sk[6]])
        add_JJ(name='J1', c=1,r=1,A=1.5, B=0, loc=[sk[4], 0])
        add_JJ(name='J3', c=1,r=1, A=1.5, B=0, loc=[sk[6], 0])
        
        add_L(name='L0',val=1,loc=[sk[0],sk[3]])
        add_L(name='L1',val=1,loc=[sk[4],sk[5]])
        add_L(name='L2',val=1,loc=[sk[5],sk[6]])
        
        add_L(name='L3',val=1,loc=[sk[4],sk[1]])
        add_L(name='L4',val=1,loc=[sk[6],sk[2]])

        add_ib(name='Ib1', val=0.75, loc=[sk[4]])
        
        add_R(name='R1', r=1, loc=[sk[5],0])
