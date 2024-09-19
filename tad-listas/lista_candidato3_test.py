#lista_candidato3_test.py
from lista_candidato3 import *
from Candidato1 import *

def teste_inserir_no_final_da_lista():
	cand1 = Candidato()
	cand2 = Candidato()

	cand1.nome = "Joao"
	cand2.nome = "Maria"

	l = Lista_candidato()
	lista2 = Lista_candidato()
	l.adiciona(cand1)
	l.adiciona(cand2)

	print(l)
	print(len(l))

	l2 = Lista_candidato()
	len(l2)
	l2.adiciona(cand1)
	l2.adiciona(cand2)
	l2.adiciona(cand2)

	print(l2)

	print(len(l2))

	#Deve imprimir "[Joao, Maria]"

teste_inserir_no_final_da_lista()