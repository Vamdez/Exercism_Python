import re


def flatten_re(iterable):
    x = re.findall(r'-?\d+', str(iterable))
    return [int(i) for i in x]


def flatten(iterable):
    resp = []
    for item in iterable:
        if isinstance(item, (list, tuple)):
            resp.extend(flatten(item))
        elif item is not None:
            resp.append(item)
    return resp


x = flatten([12,[[[[3,None,8]]]],-14])
print(x)