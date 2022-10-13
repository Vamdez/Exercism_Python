def sum_of_multiples(limit, multiples):
    resp = 0
    for i in range(limit):
        is_multiple = []
        for itens in multiples:
            if itens == 0:
                continue
            is_multiple.append(i % itens == 0)
        if any(is_multiple):
            resp += i
    return resp


x = sum_of_multiples(100, [2, 3, 5, 7, 11])
print(x)