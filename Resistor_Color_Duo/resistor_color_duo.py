lista_colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

def value(colors):
    resp = ''
    return int(resp.join([str(lista_colors.index(c)) for c in colors[:2]]))
