def convert(number):
    resul = str()
    if number % 3 == 0:
        resul = 'Pling'
    if number % 5 == 0:
        resul += 'Plang'
    if number % 7 == 0:
        resul += 'Plong'
    if resul == '':
        return str(number)
    return resul