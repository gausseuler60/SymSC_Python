from Objects.CurrentSourceBase import CurrentSourceBase


class Ib(CurrentSourceBase):
    def __init__(self, loc, val):
        super().__init__(loc=loc)

        self.val = val
        self.name = 'Ib'

    def get_current_from_time(self, t):
        return self.val
