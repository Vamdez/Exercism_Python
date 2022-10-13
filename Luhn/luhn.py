class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(' ', '')

    def valid(self):
        if len(self.card_num) <= 1 or not (self.card_num.isnumeric()):
            return False
        new_num = dobrar(self.card_num)
        return somar(new_num) % 10 == 0


def dobrar(num):
    lista = ''
    itens = 0
    for index in range(-1, (-len(num))-1, -1):
        if index % -2 == 0:
            itens = (int(num[index])) * 2
            if itens > 9:
                itens -= 9
            lista += str(itens)
        else:
            lista += str(num[index])
    return lista


def somar(num):
    soma = 0
    for i in num:
        i = int(i)
        soma += i
    return soma