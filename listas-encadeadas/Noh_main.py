from Noh import *

noh1 = Noh(93)
print(noh1.getData())

noh2 = Noh(9)
print(noh2.getData())

print(noh1)
print(noh2)

noh1.setNext(noh2)

noh3 = Noh(33)
noh2.setNext(noh3)

print(noh1)
