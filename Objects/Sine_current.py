from Objects.CurrentSourceBase import CurrentSourceBase
from Functions import sin_I


class Sine_current(CurrentSourceBase):
    """
    Sinusoidal current from t0 to t0+length
    """
    def __init__(self, loc, t0=10, length=100, w=1, A=0.5):
        """
        A class constructor

        :param loc: nodes in a circuit to what the element is connected (zero is a ground)
        :param t0: current start time
        :param length: current length
        :param w: pulse frequency (omega)
        :param A: pulse amplitude (in normalized current units)
        """
        super().__init__(loc=loc)

        self.t0 = t0
        self.length = length
        self.A = A
        self.w = w

        self.name = "Sine_current"

    def get_current_from_time(self, t):
        val = sin_I(t, self.t0, self.length, self.w, self.A)
        return val


