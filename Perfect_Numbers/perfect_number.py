def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    tot = 0
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    for i in range(number - 1, 0, -1):
        if number % i == 0:
            tot += i
    if tot == number:
        return 'perfect'
    if tot > number:
        return 'abundant'
    return 'deficient'

