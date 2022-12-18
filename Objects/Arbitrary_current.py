from Objects.CurrentSourceBase import CurrentSourceBase
from Functions import sin_I
import numpy as np


class Arbitrary_current(CurrentSourceBase):
    """
    Arbitrary current I(t)
    """
    def __init__(self, loc, t, curr_t):
        """
        A class constructor

        :param loc: nodes in a circuit to what the element is connected (zero is a ground)
        :param t: simuation time array
        :param curr_t: I(t) array (must be the same length as t)
        """
        super().__init__(loc=loc)

        self.t = np.array(t)
        self.curr_t = np.array(curr_t)

        self.name = "Arbitrary_current"

    def get_current_from_time(self, t):
        idx = np.nonzero(t==self.t)[0][0]
        return self.curr_t[idx]
