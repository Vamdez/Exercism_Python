def transform(legacy_data):
    resp = dict()
    for k, v in legacy_data.items():
        for itens in v:
            resp[itens.lower()] = k
    return resp


x = transform({1: ["A", "E"], 2: ["D", "G"]})
print(x)