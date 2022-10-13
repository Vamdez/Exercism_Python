def find_anagrams(word, candidates):
    resp = []
    for opc in candidates:
        if sorted(opc.upper()) == sorted(word.upper()) and opc.upper() != word.upper():
            resp.append(opc)
    return resp
