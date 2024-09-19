#import Candidato1 as C
from Candidato1 import *

a = Candidato()
a.nome = "Joao"
a.pontuacao = "9"

b = Candidato()
b.nome = "Maria"
b.pontuacao = "10"

c = Candidato()

print(a.nome, a.pontuacao)
print(b.nome, b.pontuacao)
print()


lista_candidatos = []
lista_candidatos.append(a)
lista_candidatos.append(b)
lista_candidatos.append(c)

print("Lista de Candidatos...")
for cand in lista_candidatos:
	print(">>>",cand)
