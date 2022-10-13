from utils import Robot
from time import time
import re
inicio = time()
robo = Robot()
for i in range(100):
    print(robo.name)
    robo.reset()
fim = time()
print(fim - inicio)


