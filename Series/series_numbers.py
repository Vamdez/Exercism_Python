def slices(series, length):
    validation(series, length)
    resp = []
    i = 0
    while True:
        resp.append(series[i:length+i])
        i += 1
        if len(resp[-1]) != length or length == 0:
            resp.pop()
            break
    return resp


def validation(series, length):
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if not series:
        raise ValueError("series cannot be empty")
    if len(series) < length:
        raise ValueError("slice length cannot be greater than series length")
