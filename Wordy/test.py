import re
OPS = {
    "plus": "__add__", "minus": "__sub__",
    "multiplied by": "__mul__", "divided by": "__truediv__"
}
def answer(question):
    question = question.removeprefix("What is").removesuffix("?").strip()
    # question = question.strip("What is").strip("?").strip()
    if not question: raise ValueError("syntax error")
    # if only a digit, return it
    if re.search(re.compile("^-?\d$"), question): return int(question)
    # translate supported operations. raise error if none found.
    foundOp = False
    for name, op in OPS.items():
        if name in question:
            question = question.replace(name, op)
            foundOp = True
    if not foundOp: raise ValueError("unknown operation")
    # process one or more operations
    ret = question.split()
    while len(ret) > 1:
        try:
            x, op, y, *tail = ret
            if op not in OPS.values(): raise ValueError("syntax error")
            # put result as first element and append what remains
            ret = [int(x).__getattribute__(op)(int(y)), *tail]
        except: raise ValueError("syntax error")
    return ret[0]


resp = answer("What is 2 plus 2?")
print(resp)