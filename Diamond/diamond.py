from string import ascii_uppercase


def rows(letter):
    resp = []
    pos = ascii_uppercase.index(letter)
    count = 1
    for i in range(pos+1):
        if i == 0:
            resp.append(f'{" "*pos}A{" "*pos}')
        else:
            txt = f'{" "* (pos - i)+ascii_uppercase[i]}'
            resp.append(txt+' '*count+txt[::-1])
            count += 2
    for itn in range(len(resp)-2, -1, -1):
        resp.append(resp[itn])
    return resp

z = rows('G')
for i in z:
    print(i)