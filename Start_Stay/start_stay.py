name_number = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
               'nine', 'ten', 'eleven', ' twelve', 'thirteen', 'fourteen', 'fifteen',
               'sixteen', 'seventeen', 'eighteen', 'nineteen']

tens_numbers = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

size = [' ', ' thousand ', ' million ', ' billion ']


def say(number):
    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")
    number = division_number(str(number))
    number = clear_zeros(number)
    resp = ''
    while True:
        if number[0] != '-1':
            resp += writen_at_hundreds(number[0]) + size[len(number) - 1]
        number.pop(0)
        if not number:
            break
    return resp.strip()


def division_number(number):
    princ = []
    temp = ''
    for i in number[::-1]:
        temp += i
        if len(temp) == 3:
            princ.insert(0, temp[::-1])
            temp = ''
    if temp:
        princ.insert(0, temp[::-1])
    if not princ:
        princ.append(number)
    return princ


def clear_zeros(lst):
    new_lst = []
    if len(lst) == 1:
        return lst
    for itens in lst:
        while itens[0] == '0':
            itens = itens[1:]
            if len(itens) == 0:
                itens = '-1'
                break
        new_lst.append(itens)
    return new_lst


def writen_at_hundreds(number):
    word_name = ''
    if len(number) == 3:
        word_name = name_number[int(number[-3])] + ' hundred '
        number = number[1:]
        if number == '00':
            number = ''
    if len(number) == 2:
        if int(number[-2]) <= 1:
            word_name += name_number[int(number[-2:])]
        elif int(number[-1]) == 0:
            word_name += tens_numbers[int(number[-2]) - 2]
        else:
            word_name += tens_numbers[int(number[-2]) - 2] + '-' + name_number[int(number[-1])]
    if len(number) == 1:
        word_name += name_number[int(number)]
    return word_name


# Principal Code
resp2 = say('1000000')
print(resp2)
