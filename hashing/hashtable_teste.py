from hashtable import *

H=HashTable()
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
print(H._slots)
#[77, 44, 55, 20, 26, 93, 17, None, None, 31, 54]
print(H._valores)
#['bird', 'goat', 'pig', 'chicken', 'dog', 'lion','tiger', None, None, 'cow', 'cat']
print(H[17]) #'tiger'
H[20]='duck'
H[66]='fly'
print(H[20]) #'duck'
print(H._valores) #['bird', 'goat', 'pig', 'duck', 'dog', 'lion', 'tiger', 'fly', None, 'cow', 'cat']
print(H[99])#None