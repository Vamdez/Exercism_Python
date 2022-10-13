#test
class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self.hour += self.minute // 60
        self.minute %= 60
        self.hour %= 24

    def __repr__(self):
        return f'Clock({self.hour}, {self.minute})'

    def __str__(self):
        return f'{self.hour:0>2}:{self.minute:0>2}'

    def __eq__(self, other):
        return self.minute == other.minute and self.hour == other.hour

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)
