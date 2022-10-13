def square(number):
    grains = list()
    atual = 1
    count = 0
    while count != 64:
        grains.append(atual)
        atual *= 2
        count += 1
    if number <= 0 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return grains[number - 1]


def total():
    tot = 0
    for c in range(1, 65):
        tot += square(c)
    return tot
