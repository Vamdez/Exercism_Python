def find(search_list, value):
    temp = search_list
    if not search_list:
        raise ValueError("value not in array")
    while True:
        mediana = int(len(temp)/2)
        if temp[mediana] > value:
            temp = temp[:mediana]
        elif temp[mediana] < value:
            temp = temp[mediana:]
        elif temp[mediana] == value:
            return search_list.index(temp[mediana])
        if mediana == 0:
            raise ValueError("value not in array")


x = find([12,34,56,78,96], 34)
print(x)