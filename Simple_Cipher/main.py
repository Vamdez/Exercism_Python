from cipher import Cipher

cipher = Cipher()
plaintext = "aaaaaaaaaa"
print(cipher.encode(plaintext))

def reverse(text):
    return text[::-1]


texto = "carro"

x = reverse(texto)
print(x)