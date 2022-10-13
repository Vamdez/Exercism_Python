manual = {
    1: "eggs",
    2: "peanuts",
    4: "shellfish",
    8: "strawberries",
    16: "tomatoes",
    32: "chocolate",
    64: "pollen",
    128: "cats"
    }


class Allergies:

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        return item in self.lst

    @property
    def lst(self):
        lista = get_lista(self.score)
        return [manual[i] for i in lista]


def get_lista(score):
    maior = 0
    resp = []
    while score != 0:
        if 2 ** (maior + 1) <= score:
            maior += 1
        else:
            if maior < 8:
                resp.append(2 ** maior)
            score = score - (2 ** maior)
            maior = 0
    return resp

