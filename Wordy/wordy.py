import re

def answer(question):
    lst = []
    words = ['What', 'is', 'by', '?']
    operatos = ["plus", "multiplied", "minus", "divided"]
    for wo in words:
        question = question.replace(wo, '')
    lst = question.split()
    print(lst)
    count = 0
    for i in lst:
        if re.search('-?\d', i):
            count += 1
        elif i in operatos:
            count -= 1
        else:
            raise ValueError("unknown operation")
        if count < 0 or count > 1:
            raise ValueError("syntax error")
    while True:
        if len(lst) % 2 == 0:
            raise ValueError("syntax error")
        if len(lst) == 1:
            return int(lst[0])
        lst = calculate_in_lst(lst, operatos.index(lst[1]))


def calculate_in_lst(lst, operador):
    resp = int()
    try:
        if operador == 0:
            resp = int(lst[0]) + int(lst[2])
        if operador == 1:
            resp = int(lst[0]) * int(lst[2])
        if operador == 2:
            resp = int(lst[0]) - int(lst[2])
        if operador == 3:
            resp = int(lst[0]) / int(lst[2])
    except:
        raise ValueError("syntax error")
    lst = remove_itens(lst, resp)
    return lst


def remove_itens(lst, resp):
    lst.pop(0)
    lst.pop(0)
    lst.pop(0)
    lst.insert(0, resp)
    return lst


resp = answer("What is -2 plus 2?")
print(resp)
