import random
from string import ascii_uppercase

lista = []


def get_name() -> str:
    while True:
        name = f'{random.choice(ascii_uppercase)}{random.choice(ascii_uppercase)}{random.randint(0, 999):0>3}'
        if name in lista:
            continue
        lista.append(name)
        break
    return name


class Robot:
    def __init__(self):
        self.name = get_name()

    def reset(self):
        self.__init__()
