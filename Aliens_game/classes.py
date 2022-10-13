"""Solution to Ellen's Alien Game exercise."""


def new_aliens_collection(lista):
    return [Alien(items[0], items[1]) for items in lista]


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Amount of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    health = 3
    total_aliens_created = 0

    def __init__(self, x_coordinate=0, y_coordinate=0):
        if type(x_coordinate) is tuple:
            self.x_coordinate = x_coordinate[0]
            self.y_coordinate = x_coordinate[1]
        else:
            self.x_coordinate = x_coordinate
            self.y_coordinate = y_coordinate
        Alien.total_aliens_created += 1

    def hit(self):
        self.health -= 1

    def is_alive(self):
        if self.health <= 0:
            return False

        return True

    def teleport(self, new_x, new_y):
        self.x_coordinate = new_x
        self.y_coordinate = new_y

    def collision_detection(self, other_object):
        pass


def teste(numeros):
    return [numeros[c] for c in range(2, -1, -1)]

