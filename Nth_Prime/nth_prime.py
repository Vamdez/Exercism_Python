from time import time
inicio = time()


def prime(number):
    if number <= 0:
        raise ValueError('there is no zeroth prime')
    # variable rank start with 1 because 2 is the only even prime number
    if number == 1:
        return 2
    num = 1
    rank = 1
    while rank != number:
        num += 2
        count = 0
        for c in range(1, num+1):
            if count == 2:
                count = 3
                break
            if num % c == 0:
                count += 1
        if count == 2:
            rank += 1
    return num


def prime2(number):
    if number == 0:
        raise ValueError("there is no zeroth prime")
    idx = 1
    primes = [2]
    number_in_question = 2
    while idx < number:
        number_in_question += 1
        if all(number_in_question % p != 0 for p in primes):
            # found a new prime
            idx += 1
            primes.append(number_in_question)
            if idx == number:
                break
    return primes[-1]


x = prime2(1)
print(x)
print(time() - inicio)





