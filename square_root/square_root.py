def square_root(number):
    temp = 1
    count = 0
    while number != 0:
        number -= temp
        temp += 2
        count +=1
        if number < 0:
            return "there is no root"
    return count

print(square_root(1025))