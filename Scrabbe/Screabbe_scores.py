SCORES = {
    1: 'AEIOULNRST',
    2: 'DG',
    3: 'BCMP',
    4: 'FHVWY',
    5: 'K',
    8: 'JX',
    10: 'QZ',
}


def score(word):
    count = 0
    for char in word.upper():
        for k, v in SCORES.items():
            if char in v:
                count += k
    return count
