def factors(value):
    div = 2
    resp = []
    while value > 1:
        if value % div == 0:
            value /= div
            resp.append(div)
        else:
            div += 1
    return resp
