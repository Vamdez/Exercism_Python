def steps(number):
    count = 0
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    while True:
        if number == 1:
            return count
        if number % 2 == 0:
            number /= 2
        elif number % 2 == 1:
            number = number*3 + 1
        count += 1
