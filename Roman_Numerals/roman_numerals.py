def roman(number):
    val = [[10, 'I', 'V', 'X'],
           [100, 'X', 'L', 'C'],
           [1000, 'C', 'D', 'M']]
    resp = ''
    while number != 0:
        for num, i, v, x in val:
            lst = [i, i*2, i*3, i+v, v, v+i, v+i*2, v+i*3, i+x]
            if number < num or number >= 1000:
                unidade = int(str(number)[0])
                if number > 1000:
                    resp += 'M' * unidade
                else:
                    if unidade != 0:
                        resp += lst[unidade - 1]
                try:
                    number = int(str(number)[1:])
                except ValueError:
                    number = 0
                break
    return resp


rom = roman(2447)
print(rom)
