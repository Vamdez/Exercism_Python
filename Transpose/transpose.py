def linesize(lines):
    resp = []
    for linhas in lines:
        resp.append(len(linhas))
    return max(resp)    

def transpose(lines):
    if not lines:
        return ""
    lines = lines.split("\n")
    maior = linesize(lines)
    valorLinha = ""
    count = 0
    if type(lines) != list:
        lines = [lines]
    while True:
        for linha in lines:
            if len(linha) <= count:
                valorLinha += '&'
                continue
            valorLinha += linha[count]
        count += 1
        valorLinha = valorLinha.rstrip("&")
        if count == maior:
            break
        valorLinha += "\n"
    valorLinha = valorLinha.replace("&", " ")
    return valorLinha

lines = ["The longest line.", "A long line.", "A longer line.", "A line."]
expected = [
    "TAAA",
    "h   ",
    "elll",
    " ooi",
    "lnnn",
    "ogge",
    "n e.",
    "glr",
    "ei ",
    "snl",
    "tei",
    " .n",
    "l e",
    "i .",
    "n",
    "e",
    ".",
]
print("||".join(expected))
print('----------')
print(transpose("\n".join(lines)))
print(transpose("\n".join(lines))== "\n".join(expected))