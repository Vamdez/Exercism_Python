def count_words(sentence):
    resp = dict()
    sentence = sentence.lower()
    for i in sentence:
        if i.isalnum() or i == " " or i == "'":
            continue
        sentence = sentence.replace(i, ' ').lower()
    sentence = sentence.split()
    for i in set(sentence):
        i = clear_sentence(i)
        resp[i] = ''
    for c in range(len(sentence)):
        sentence[c] = clear_sentence(sentence[c])
    for k in resp.keys():
        count = 0
        for itens in sentence:
            if itens == k:
                count += 1
            resp[k] = count
    return resp


def clear_sentence(item):
    if item[0] == "'":
        return item.replace("'", '')
    return item
