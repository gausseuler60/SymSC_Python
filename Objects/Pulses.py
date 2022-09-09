import numpy as np
from Objects.ElementBase import ElementBase
from Functions import gauss_I


class Pulses(ElementBase):
    def __init__(self, loc, connect='Current', type_p='Gauss', t0=50, A=1, D=15, T=500, w=1):
        super().__init__()
        if len(loc) == 1:
            loc = [loc[0], 0]

        # numeric parameters
        if connect not in ['Current', 'Phase']:
            raise ValueError('Connect must be "Current" or "Phase"')
        self.connect = connect

        if type_p not in ['Gauss', 'Sin']:
            raise ValueError('type_p must be "Gauss" or "Sin"')
        self.type_p = type_p

        self.t0 = t0
        self.A = A
        self.D = D
        self.T = T
        self.w = w

        self.loc = loc
        self.name = "Pulses"
        self.complex = False

        self.contains_current = False
        self.contains_variable = False

    def get_matrix_stamp(self, h):
        return np.zeros((2, 2)) if 0 in self.loc else np.zeros((1, 1))

    def get_right_side(self, sol, i, h):
        t = i * h

        sA = self.A
        if self.connect == 'Current' and self.type_p == 'Gauss':
            st0 = self.t0
            sD = self.D
            sT = self.T
            val = gauss_I(t, st0, sA, sD, sT)
        else:
            sw = self.w
            val = np.sin(sw * t)

        if self.loc[0] == 0:  # no V+
            return np.array([-val])
        elif self.loc[1] == 0:  # no V-
            return np.array([val])
        else:
            return np.array([-val, val])

    def get_data(self, kind, t, sol):
        if kind == 'I':
            t = np.array(t)
            if self.connect == 'Current' and self.type_p == 'Gauss':
                return np.array([gauss_I(i, self.t0, self.A, self.D, self.T) for i in t])
            else:
                return self.A * np.sin(t * self.w)
        else:
            raise ValueError('Only I(t) data are avaliable for current sources')
