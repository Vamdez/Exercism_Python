import re
from itertools import groupby


def decode(string):
    divi = re.findall(r'\d+|[a-zA-z\s]', string)
    count = 0
    resp = ''
    for iten in divi:
        if iten.isnumeric():
            count = int(iten)
        else:
            if count != 0:
                resp += iten*count
                count = 0
            else:
                resp += iten
    return resp


def encode(string):
    if not string:
        return ''
    resp = ''
    temp = string[0]
    count = 0
    for key, iten in enumerate(string):
        if iten != temp:
            if count == 1:
                resp += string[key - 1]
            else:
                resp += f'{count}{string[key - 1]}'
            count = 0
            temp = iten
        count += 1
    resp += string[-1] if count == 1 else f'{count}{string[-1]}'
    return resp


def encode2(s):
    code = ''
    for k, g in groupby(s):
        section = sum(2 for _ in g)
        if section > 1:
            code += str(section) + k
        else:
            code += k
    return code



txt = 'OOOLLLAAAA'
x = encode2(txt)
print(x)
