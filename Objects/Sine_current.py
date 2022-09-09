from Objects.ElementBase import ElementBase
import numpy as np
from Functions import sin_I


class Sine_current(ElementBase):
    def __init__(self, loc, t0=10, length=100, w=1, A=0.5):
        super().__init__()
        if len(loc) == 1:
            loc = [loc[0], 0]

        self.t0 = t0
        self.length = length
        self.A = A
        self.w = w
        self.loc = loc

        self.name = "Sine_current"
        self.complex = False

        self.contains_current = False
        self.contains_variable = False

    def get_matrix_stamp(self, h):
        return np.zeros((2, 2)) if 0 in self.loc else np.zeros((1, 1))

    def get_right_side(self, sol, i, h):
        t = i * h

        val = sin_I(t, self.t0, self.length, self.w, self.A)

        if self.loc[0] == 0:  # no V+
            return np.array([-val])
        elif self.loc[1] == 0:  # no V-
            return np.array([val])
        else:
            return np.array([-val, val])

    def get_data(self, kind, t, sol):
        if kind == 'I':
            t = np.array(t)
            return np.array([sin_I(i, self.t0, self.length, self.w, self.A) for i in t])
        else:
            raise ValueError('Only I(t) data are avaliable for current sources')
