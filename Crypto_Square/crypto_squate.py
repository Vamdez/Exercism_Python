def cipher_text(plain_text):
    row = columns = count = 0
    resp = []
    table = []
    plain_text = ''.join(c for c in plain_text.lower() if c.isalnum())
    while row * columns < len(plain_text):
        columns += 1
        if row * columns < len(plain_text):
            row += 1
            continue
        break
    temp = ''
    for itens in plain_text:
        temp += itens
        if len(temp) == columns:
            table.append(temp)
            temp = ''
    if temp:
        while len(temp) != columns:
            temp += ' '
        table.append(temp)
        temp = ''
    while count < columns:
        for row in table:
            temp += row[count]
        resp.append(temp)
        temp = ''
        count += 1
    return ' '.join(resp)


le = cipher_text('OLA MUNDO')
print(le)