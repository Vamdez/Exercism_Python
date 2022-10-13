from random import randint
from math import floor


class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = modifier(self.constitution) + 10

    def ability(self):
        num = []
        for i in range(4):
            num.append(randint(1, 6))
        num = sorted(num)
        num.pop(0)
        return sum(num)


def modifier(constitution):
    return floor((constitution - 10)/2)


boneco = Character()
print(boneco.strength)
print(boneco.dexterity)
print(boneco.constitution)
print(boneco.intelligence)
print(boneco.wisdom)
print(boneco.charisma)
print(boneco.hitpoints)



