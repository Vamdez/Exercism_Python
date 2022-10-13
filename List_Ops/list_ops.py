

def append(list1, list2):
    return list1 + list2


def concat(lists):
    new_list = []
    for itens in lists:
        for i in itens:
            new_list.append(i)
    return new_list


def filter(function, lsts):
    new_list = []
    for itens in lsts:
        if function(itens):
            new_list.append(itens)
    return new_list


def length(list):
    count = 0
    for i in list:
        count += 1
    return count


def map(function, list):
    return [function(iten) for iten in list]


def foldl(function, list, initial):
    for itens in list:
        initial = function(itens, initial)
    return initial

def foldr(function, list, initial):
    for itens in list[::-1]:
        initial = function(itens, initial)
    return initial


def reverse(list):
    return list[::-1]



lst= [1,2,3]
lst2 = ['a', 'b', 'c']
lists = [1, 2, 3, 4, 5, 6, 7]
x = foldl(lambda acc, el: el + acc, [1, 2, 3, 4], 5)
print(x)