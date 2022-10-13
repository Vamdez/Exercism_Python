def score(x, y):
    formula = (x**2) + (y**2)
    print(formula)
    if formula <= 1**2:
        return 10
    if formula <= 5**2:
        return 5
    if formula <= 10**2:
        return 1
    return 0


z = score(10, 0)
print(z)


