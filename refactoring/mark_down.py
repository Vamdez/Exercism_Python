import re


def parse(markdown):
    res = ''
    in_list = False
    in_list_append = False
    for i in markdown.split('\n'):
        lista = re.findall('^#{1,6} ', i)
        if lista:
            c = len(lista[0]) - 1
            i = f'<h{c}>' + i[c + 1:] + f'</h{c}>'
        is_a_list = re.match(r'\* (.*)', i)
        if is_a_list:
            curr = is_a_list.group(1)
            if not in_list:
                in_list = True
                curr = is_a_bold(curr)
                curr = is_a_italic(curr)
                i = '<ul><li>' + curr + '</li>'
            else:
                curr = is_a_bold(curr)
                curr = is_a_italic(curr)
                i = '<li>' + curr + '</li>'
        else:
            if in_list:
                in_list_append = True
                in_list = False
        is_a_list = re.match('<h|<ul|<p|<li', i)
        if not is_a_list:
            i = '<p>' + i + '</p>'
        i = is_a_bold(i)
        i = is_a_italic(i)
        if in_list_append:
            i = '</ul>' + i
            in_list_append = False
        res += i
    if in_list:
        res += '</ul>'
    return res


def is_a_bold(curr):
    m1 = re.match('(.*)__(.*)__(.*)', curr)
    if m1:
        curr = m1.group(1) + '<strong>' + \
               m1.group(2) + '</strong>' + m1.group(3)
    return curr


def is_a_italic(curr):
    m1 = re.match('(.*)_(.*)_(.*)', curr)
    if m1:
        curr = m1.group(1) + '<em>' + m1.group(2) + \
               '</em>' + m1.group(3)
    return curr


