def equilateral(sides):
    return is_triangle(sides) and sides[0] == sides[1] == sides[2]


def isosceles(sides):
    return is_triangle(sides) and not scalene(sides) and not equilateral(sides)


def scalene(sides):
    return is_triangle(sides) and sides[0] != sides[1] != sides[2] != sides[0]


def is_triangle(sides):
    existe = sides[0] + sides[1] > sides[2] and sides[0] + sides[2] > sides[1] and sides[1] + sides[2] > sides[0]
    return existe
