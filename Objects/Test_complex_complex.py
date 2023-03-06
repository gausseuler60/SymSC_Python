from Objects.ComplexObjectBase import ComplexObjectBase
from Objects.JTL import JTL


class Test_complex_complex(ComplexObjectBase):
    def __init__(self, loc):
        super().__init__(loc=loc)
        self.check_loc(loc, 2)

        self.N = 3

        self.name = 'Test'
        self.description = 'Test'

    def create_elements(self, sk):
        jtl1 = JTL(loc=[sk[0], sk[2]], N=3)
        jtl2 = JTL(loc=[sk[2], sk[1]], N=2)

        self.add_complex_object(jtl1)
        self.add_complex_object(jtl2)
