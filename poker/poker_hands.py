#Program to analyze different poker hands and return the best

values = {'1': '10', '0': '', 'J': '11', 'Q': '12', 'K': '13', 'A': '14'}
combinations = {}
ranking = ['straight_flush', 'four', 'full_house', 'flush', 'straight', 'three', 'two_pair', 'pair', 'high']


def best_hands(hands):
    lst_hands = []
    count = 0
    for hand in hands:
        alfa = ''
        num = []
        combinations.clear()
        combinations['index'] = count
        for letters in hand:
            if letters in values.keys():
                letters = values[letters]
            if letters.isalpha():
                alfa += letters
            if letters.isnumeric():
                num.append(int(letters))
        # Check Flush
        if alfa.count(alfa[0]) == 5:
            combinations['flush'] = [max(num)]
        # Check Straight
        is_straight(sorted(num))
        # Is Straight_Flush
        if 'flush' in combinations.keys() and 'straight' in combinations.keys():
            combinations['straight_flush'] = combinations['straight']
        # Set High Card
        combinations['high'] = sorted(num, reverse=True)
        # Check all combinations
        pair_three_four(sorted(num, reverse=True))
        lst_hands.append(combinations.copy())
        count += 1
    return hands_win(lst_hands, hands)


def is_straight(num):
    var = num[0]
    resp = [var, var + 1, var + 2, var + 3, var + 4]
    if resp == num or [1, 2, 3, 4, 5] == sorted(aces(num)):
        if 14 in num:
            combinations['straight'] = [5]
        else:
            combinations['straight'] = [max(num)]


def pair_three_four(num):
    quant = []
    matchs = []
    lst = []
    for itens in num:
        if itens not in lst:
            if num.count(itens) > 1:
                quant.append(num.count(itens))
                if num.count(itens) == 3:
                    matchs.insert(0, itens)
                else:
                    matchs.append(itens)
            lst.append(itens)
    if 4 in quant:
        combinations['four'] = matchs + clear_lst(lst, matchs)
    if len(quant) == 2 and 3 in quant:
        combinations['full_house'] = matchs + clear_lst(lst, matchs)
    elif len(quant) == 2:
        combinations['two_pair'] = matchs + clear_lst(lst, matchs)
    if len(quant) == 1 and 3 in quant:
        combinations['three'] = matchs + clear_lst(lst, matchs)
    elif len(quant) == 1 and 2 in quant:
        combinations['pair'] = matchs + clear_lst(lst, matchs)


def aces(num):
    new_num = []
    for i in num:
        if i == 14:
            i = 1
        new_num.append(i)
    return new_num


def hands_win(lst_combination, hands):
    resp_equal = []
    for iten in ranking:
        for cards in lst_combination:
            if iten in cards.keys():
                resp_equal.append(cards)
        if len(resp_equal) == 1:
            return [hands[util['index']] for util in resp_equal]
        if len(resp_equal) >= 1:
            count = 0
            while count < len(resp_equal[0][iten]):
                new_resp = []
                maior = 0
                for equals in resp_equal:
                    if equals[iten][count] > maior:
                        new_resp.clear()
                        new_resp.append(equals)
                        maior = equals[iten][count]
                    elif equals[iten][count] == maior:
                        new_resp.append(equals)
                if len(new_resp) == 1:
                    return [hands[util['index']]for util in new_resp]
                resp_equal = new_resp
                count += 1
            return [hands[util['index']] for util in resp_equal]


def clear_lst(lst, matchs):
    new_lst = []
    for itens in lst:
        if itens in matchs:
            continue
        new_lst.append(itens)
    return new_lst


x = best_hands([
                    "4D 5S 6S 8D 3C",
                    "2S 4C 7S 9H 10H",
                    "3S 4S 5D 6H JH",
                    "3H 4H 5C 6C JD",
                ])
print(x)
