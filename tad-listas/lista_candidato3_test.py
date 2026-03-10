#lista_candidato3_test.py
from lista_candidato3 import *
from Candidato1 import *

def teste_inserir_no_final_da_lista():
	cand1 = Candidato()
	cand2 = Candidato()

	cand1.nome = "Joao"
	cand2.nome = "Maria"

	lista1 = Lista_candidato()
	lista2 = Lista_candidato()
	lista1.adiciona(cand1)
	lista1.adiciona(cand2)

	print(lista1)
	print(len(lista1))

	l2 = Lista_candidato()
	len(l2)
	l2.adiciona(cand1)
	l2.adiciona(cand2)
	l2.adiciona(cand2)

	print(l2)

	print(len(l2))

	#Deve imprimir "[Joao, Maria]"

if __name__ == '__main__':
	teste_inserir_no_final_da_lista()