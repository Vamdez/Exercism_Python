from string import ascii_lowercase, ascii_uppercase


def rotate(text, key):
    new_text = ''
    for letters in text:
        if letters in ascii_lowercase:
            new_text += ascii_lowercase[(ascii_lowercase.index(letters) + key) % 26]
        elif letters in ascii_uppercase:
            new_text += ascii_uppercase[(ascii_uppercase.index(letters) + key) % 26]
        else:
            new_text += letters
    return new_text


eresp = rotate('Abcde, 3fgh', 3)
print(eresp)