def is_isogram(string):
    string = string.replace('-', '').lower()
    resp = string.replace(' ', '')
    for i in resp:
        count = resp.count(i)
        if count > 1:
            return False
    return True
