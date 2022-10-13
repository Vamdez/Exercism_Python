import re
def abbreviate(words):
    lista = ''
    p = re.compile("[a-z']+", re.I)
    return lista.join(char[0].upper() for char in re.findall(p, words))
