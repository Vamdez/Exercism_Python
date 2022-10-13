def recite(start, take=1):
    resp = []
    for num in range(take):
        if start == 1 or start == 0:
            start, resp = exceptions(start, resp, verse=1)
        else:
            resp.append(f'{start} bottles of beer on the wall, {start} bottles of beer.')
            start -= 1
        if start == 1 or start == 0 or start == 99:
            if start == 99:
                break
            start, resp = exceptions(start, resp, verse=2)
        else:
            resp.append(f'Take one down and pass it around, {start} bottles of beer on the wall.')
        if num != take-1:
            resp.append('')
    return resp


def exceptions(start, lst, verse):
    if verse == 1:
        if start == 1:
            lst.append(f'{start} bottle of beer on the wall, {start} bottle of beer.')
            start -= 1
        elif start == 0:
            lst.append('No more bottles of beer on the wall, no more bottles of beer.')
            lst.append('Go to the store and buy some more, 99 bottles of beer on the wall.')
            start = 99
    else:
        if start == 1:
            lst.append('Take one down and pass it around, 1 bottle of beer on the wall.')
        elif start == 0:
            lst.append('Take it down and pass it around, no more bottles of beer on the wall.')
    return start, lst


x = recite(10, 11)
for i in x:
    print(i)
