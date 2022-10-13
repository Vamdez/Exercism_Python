import itertools
def transpose(lines):
    resp = temp = ''
    count = 0
    leng = len(sorted(lines, key=lambda x: len(x))[-1])
    nw_lines = []
    for itens in lines:
        while len(itens) != leng:
            itens += ' '
        nw_lines.append(itens)
    print(nw_lines)
    while True:
        for itens in nw_lines:
            temp += itens[count]
        resp += f'{temp}\n'
        count += 1
        temp = ''
        if count > len(lines[0]):
            break
    return resp


X = transpose(["AB", "DEF"])
print(X)
