def tally(rows):
    dicionar = dict()
    table = list()
    for i in range(len(rows)):
        rows[i] = rows[i].split(';')
# Create a dict with the name of each team
    for itens in rows:
        if itens[0] not in dicionar:
            dicionar[itens[0]] = None
        if itens[1] not in dicionar:
            dicionar[itens[1]] = None
# Find the numbers of wins, draws and loss of each team
    for k in dicionar.keys():
        wins = draws = loss = 0
        for itens in rows:
            if k in itens[0]:
                draws, wins, loss = stats(itens, draws, wins, loss)
            if k in itens[1]:
                draws, loss, wins = stats(itens, draws, loss, wins)
        dicionar[k] = (wins + draws + loss), wins, draws, loss, (wins * 3 + draws)
# sorted alphabetically and by points
    for values in (sorted(sorted(dicionar.items()), key=lambda x: x[1][4], reverse=True)):
        table.append(f'{values[0]:<31}|{values[1][0]:>3} |{values[1][1]:>3}'
                     f' |{values[1][2]:>3} |{values[1][3]:>3} |{values[1][4]:>3}')
    header = f'{"Team":<31}|{"MP":>3} |{"W":>3} |{"D":>3} |{"L":>3} |{"P":>3}'
    table.insert(0, header)
    return table


def stats(itens, draws, wins, loss):
    if itens[2] == 'draw':
        draws += 1
    elif itens[2] == 'win':
        wins += 1
    elif itens[2] == 'loss':
        loss += 1
    return draws, wins, loss
