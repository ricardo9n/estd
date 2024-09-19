from pilha_array import *

p = PilhaArray()

x = 'estrutura'

for i in x:
	p.push(i)

while(not p.is_empty()):
	print(p.pop(),end="")