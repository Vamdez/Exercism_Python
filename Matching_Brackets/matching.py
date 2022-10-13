dicionario = {
    '[': ']',
    '{': '}',
    '(': ')'
              }


def is_paired(input_string):
    count = 0
    lista = ['.']
    for symbols in input_string:
        if symbols in dicionario.keys():
            lista.append(dicionario[symbols])
            count += 1
        if symbols in dicionario.values():
            if symbols != lista[-1]:
                return False
            lista.pop()
            count -= 1
        if count < 0:
            return False
    if count == 0:
        return True
    return False
