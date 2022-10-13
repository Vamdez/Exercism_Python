def saddle_points(matrix):
    resp = []
    for linha, listas in enumerate(matrix):
        if len(listas) != len(matrix[0]):
            raise ValueError("irregular matrix")
        dict = {"row": None, "column": None}
        for ind, val in enumerate(listas):
            if val == max(listas):
                maior = val, ind, linha
                if is_saddle(maior, matrix):
                    dict["row"] = maior[2] + 1
                    dict["column"] = maior[1] + 1
                    resp.append(dict.copy())
    return resp


def is_saddle(maior, matrix):
    coluna = []
    for i in range(len(matrix)):
        coluna.append(matrix[i][maior[1]])
    return min(coluna) >= maior[0]
