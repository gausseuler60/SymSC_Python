import numpy as np
from Objects.ElementBase import ElementBase
from Functions import pulse_I


class Square_pulse(ElementBase):
    def __init__(self, loc, t0=10, length=100, A=0.5):
        super().__init__()
        if len(loc) == 1:
            loc = [loc[0], 0]

        self.t0 = t0
        self.length = length
        self.A = A
        self.loc = loc

        self.name = "Square_pulse"
        self.complex = False

        self.contains_current = False
        self.contains_variable = False

    def get_matrix_stamp(self, h):
        return np.zeros((2, 2)) if 0 in self.loc else np.zeros((1, 1))

    def get_right_side(self, sol, i, h):
        t = i * h

        val = pulse_I(t, self.t0, self.length, self.A)

        if self.loc[0] == 0:  # no V+
            return np.array([-val])
        elif self.loc[1] == 0:  # no V-
            return np.array([val])
        else:
            return np.array([-val, val])

    def get_data(self, kind, t, sol):
        if kind == 'I':
            t = np.array(t)
            return np.array([pulse_I(i, self.t0, self.length, self.A) for i in t])
        else:
            raise ValueError('Only I(t) data are avaliable for current sources')
