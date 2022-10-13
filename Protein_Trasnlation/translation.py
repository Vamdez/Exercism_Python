import re
table = {
    "Methionine": ["AUG"],
    "Phenylalanine": ["UUU", "UUC"],
    "Leucine": ["UUA", "UUG"],
    "Serine": ["UCU", "UCC", "UCA", "UCG"],
    "Tyrosine": ["UAU", "UAC"],
    "Cysteine": ["UGU", "UGC"],
    "Tryptophan": ["UGG"],
    "STOP": ["UAA", "UAG", "UGA"]
}


def proteins(strand):
    division = re.findall(r'.{3}', strand)
    resp = list()
    for iten in division:
        if iten in table['STOP']:
            break
        for k, v in table.items():
            if iten in v:
                resp.append(k)
    return resp
