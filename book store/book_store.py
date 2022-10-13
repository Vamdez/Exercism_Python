def total(basket):
    num_books = dict()
    for items in basket:
        if items not in num_books:
            num_books[items] = basket.count(items)
    count = len(basket)
    resp = divisivel = 0
    if len(num_books) == 5:
        if count % 4 == 0:
            divisivel = (8 * count) * 0.8
    while True:
        ordem = sorted(num_books.keys(), key=num_books.get, reverse=True)

        if len(num_books) == 5:
            if count == 8:
                resp += (8 * 4) * 0.8
                num_books = update_dict(num_books, ordem[:4])
                count -= 4
            else:
                resp += (8 * 5) * 0.75
                num_books = update_dict(num_books, ordem)
                count -= 5
        elif len(num_books) == 4:
            resp += (8 * 4) * 0.8
            num_books = update_dict(num_books, ordem[:4])
            count -= 4
        elif len(num_books) == 3:
            resp += (8 * 3) * 0.9
            num_books = update_dict(num_books, ordem)
            count -= 3
        elif len(num_books) == 2:
            resp += (8 * 2) * 0.95
            num_books = update_dict(num_books, ordem)
            count -= 2
        elif len(num_books) == 1:
            resp += 8
            num_books = update_dict(num_books, ordem)
            count -= 1
        if count == 0:
            break
    if divisivel != 0 and divisivel < resp:
        resp = divisivel
    return int(round(resp*100))


def update_dict(num_books, deleted_books):
    for values in deleted_books:
        num_books[values] -= 1
        if num_books[values] == 0:
            del num_books[values]
    return num_books
