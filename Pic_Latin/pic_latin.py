import re


def translate(text):
    lst = text.split()
    lst_resp = []
    resp = ''
    for txt in lst:
        VOGAL_SOUNDS = re.compile('a|e|i|o|u|yt|xr')
        if re.match(VOGAL_SOUNDS, txt):
            lst_resp.append(txt + 'ay ')
            continue
        try:
            vogal_index = re.search(VOGAL_SOUNDS, txt).start()
        except AttributeError:
            vogal_index = 1
        if txt[vogal_index - 1:vogal_index+1] == 'qu':
            lst_resp.append(txt[vogal_index+1:] + txt[:vogal_index+1]+'ay ')
            continue
        lst_resp.append(txt[vogal_index:] + txt[:vogal_index] + 'ay ')
    return resp.join(lst_resp).strip()


x = translate("quick fast run")
print(x)
