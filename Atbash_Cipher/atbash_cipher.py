from string import ascii_lowercase
import re

def encode(plain_text):
    plain_text = re.sub('\W', '', plain_text)
    new_text = ''
    count = 0
    for letters in plain_text.replace(' ', '').lower():
        count += 1
        if letters.isalpha():
            num_lst = ascii_lowercase.index(letters)
            new_text += ascii_lowercase[-(num_lst+1)]
        else:
            new_text += letters
        if count == 5:
            new_text += ' '
            count = 0
    return new_text.strip()

def decode(ciphered_text):
    ciphered_text = re.sub('\W', '', ciphered_text)
    new_text = ''
    for letters in ciphered_text.replace(' ', '').lower():
        if letters.isalpha():
            num_lst = ascii_lowercase.index(letters)
            new_text += ascii_lowercase[abs(num_lst -25)]
        else:
            new_text += letters
    return new_text


resp = encode('abcdefghijklmnopqrstuvwxyz')
print(resp)
resp2 = decode('trybe')
print(resp2)