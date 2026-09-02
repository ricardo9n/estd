#lista_candidato3_test.py
from lista_candidato3 import *
from Candidato1 import *

cand1 = Candidato()
cand2 = Candidato()

cand1.nome = "Joao"
cand2.nome = "Maria"

lista1 = Lista_candidato()
lista1.adiciona(cand1)
lista1.adiciona(cand2)
print(lista1)
print(cand1)