def square_of_sum(number):
    tot = 0
    for num in range(number+1):
        tot += num
    return tot**2


def sum_of_squares(number):
    tot = 0
    for num in range(number+1):
        tot += (num**2)
    return tot


def difference_of_squares(number):
    return abs(square_of_sum(number) - sum_of_squares(number))
