#lista_candidato2_test.py
from lista_candidato2 import *
from Candidato1 import *

def teste_inserir_no_final_da_lista():
	lista_cand = [None, None, None, None]
	lista_cand2 = [None, None, None, None,None]
	imprime(lista_cand)

	cand1 = Candidato()
	cand2 = Candidato()
	cand1.nome = "Joao"
	cand2.nome = "Maria"
	adiciona(cand1, lista_cand)
	adiciona(cand2, lista_cand)
	imprime(lista_cand)

	cand3 = Candidato()
	cand3.nome = "Jose"
	#adiciona(cand3, lista_cand)
	#adiciona(cand3, lista_cand)
	imprime(lista_cand)

	adiciona(cand3, lista_cand2)
	print('lista2: ')
	imprime(lista_cand2)

	#Deve imprimir "[Joao, Maria, Jose, Jose]"

def teste_inserir_posicao_da_lista():
	lista_cand = [None, None, None, None]
	imprime(lista_cand)

	cand1 = Candidato() 
	cand2 = Candidato()
	cand1.nome = "Joao"
	cand2.nome = "Maria"
	adiciona(cand1, lista_cand) #nao funciona!!!
	adiciona(cand2, lista_cand)
	imprime(lista_cand)

	cand3 = Candidato()
	cand3.nome = "Jose"
	adiciona_na_posicao(0, cand3, lista_cand)
	imprime(lista_cand)

	#Deve imprimir "[Jose, Joao, Maria]"

teste_inserir_no_final_da_lista() #1
teste_inserir_posicao_da_lista()   #2