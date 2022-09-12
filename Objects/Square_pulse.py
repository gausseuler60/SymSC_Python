import numpy as np
from Objects.CurrentSourceBase import CurrentSourceBase
from Functions import pulse_I


class Square_pulse(CurrentSourceBase):
    def __init__(self, loc, t0=10, length=100, A=0.5):
        super().__init__(loc=loc)

        self.t0 = t0
        self.length = length
        self.A = A

        self.name = "Square_pulse"

    def get_current_from_time(self, t):
        val = pulse_I(t, self.t0, self.length, self.A)
        return val
