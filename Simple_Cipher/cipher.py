from string import ascii_lowercase
import re
import random


class Cipher:
    def __init__(self, key=None):
        if key is None:
            self.key = key_is_None()
        else:
            self.key = key
        self.code = translate(self.key)

    def encode(self, text):
        return self.encode_decode(text, 0)

    def decode(self, text):
        return self.encode_decode(text, 1)

    def encode_decode(self, text, key):
        new_text = ''
        count = 0
        for letters in text:
            if key == 1:
                pos = (re.search(letters, ascii_lowercase).start() - int(self.code[count % len(self.code)])) % 26
            elif key == 0:
                pos = (re.search(letters, ascii_lowercase).start() + int(self.code[count % len(self.code)])) % 26
            count += 1
            new_text += ascii_lowercase[pos]
        return new_text


def translate(key):
    new_key = list()
    for letters in key:
        new_key.append(re.search(letters, ascii_lowercase).start())
    return new_key


def key_is_None():
    Nkey = ''
    for i in range(10):
        Nkey += random.choice(ascii_lowercase)
    return Nkey

