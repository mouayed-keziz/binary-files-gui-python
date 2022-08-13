from sys import getsizeof
from pickle import dumps
from os import system
system('cls')

i = 0
while True:
    print(i, ' : ',getsizeof(dumps(i)))
    if getsizeof(dumps(i)) > 38:
        break
    i += 1