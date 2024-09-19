from Candidato2 import *

a = Candidato("Joao", "9")
b = Candidato("Maria", "10")
#c = Candidato() #erro

print(a.nome, a.pontuacao)
print(b.nome, b.pontuacao)
#print(c.nome, c.pontuacao)
print()

lista_candidatos = []
lista_candidatos.append(a)
lista_candidatos.append(b)
#lista_candidatos.append(c)

print("Lista de Candidatos...")
for cand in lista_candidatos:
	print(">>>",cand.nome,cand.pontuacao)
