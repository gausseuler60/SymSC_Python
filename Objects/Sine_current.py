from Objects.CurrentSourceBase import CurrentSourceBase
import numpy as np
from Functions import sin_I


class Sine_current(CurrentSourceBase):
    def __init__(self, loc, t0=10, length=100, w=1, A=0.5):
        super().__init__(loc=loc)

        self.t0 = t0
        self.length = length
        self.A = A
        self.w = w

        self.name = "Sine_current"

    def get_current_from_time(self, t):
        val = sin_I(t, self.t0, self.length, self.w, self.A)
        return val


