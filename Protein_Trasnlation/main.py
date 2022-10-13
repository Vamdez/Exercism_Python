
from test import proteins
from time import time

inicio = time()
txt = "UGGUGUUAU" * 1000000 + "UAA"
x = proteins(txt)
print(x)
fim = time()
print(fim - inicio)
