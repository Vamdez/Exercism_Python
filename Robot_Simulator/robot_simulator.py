# Globals for the directions
# Change the values as you see fit
EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.direction = direction
        self.coordinates = (self.x_pos, self.y_pos)

    def move(self, movements):
        for letters in movements:
            if letters == 'R':
                self.direction -= 1
            if letters == 'L':
                self.direction += 1
            self.direction = self.direction % 4
            if letters == 'A':
                if self.direction == 0:
                    self.x_pos += 1
                if self.direction == 1:
                    self.y_pos += 1
                if self.direction == 2:
                    self.x_pos -= 1
                if self.direction == 3:
                    self.y_pos -= 1
        self.coordinates = (self.x_pos, self.y_pos)


robo = Robot(EAST, 1, 3)
x = robo.move('LLLLLL')
print(x)
