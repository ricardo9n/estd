#lista_candidato1.py
CAPACIDADE_LISTA = 4

def adiciona(valor, lista):
	for i in range(CAPACIDADE_LISTA) :
		if lista[i] == None:
			lista[i] = valor
			break

def adiciona_na_posicao(posicao,valor, lista):
	novo_valor = valor
	for i in range(posicao, CAPACIDADE_LISTA) :
		temp = lista[i]
		lista[i] = novo_valor
		novo_valor = temp

def pega(posicao,lista):
	return lista[posicao]

def contem(candidato,lista):
	for i in range(CAPACIDADE_LISTA) :
		if candidato == lista[i]: return i
	return None

def tamanho(lista):
	for i in range(CAPACIDADE_LISTA) :
		if lista[i] == None: return i
	return CAPACIDADE_LISTA

def imprime(lista):
	result = "["
	i = 0
	while i < tamanho(lista): # and lista[i] != None:
		result += (lista[i].nome)
		i += 1
		if i < tamanho(lista) and lista[i] != None: result += ", "
	result += "]"
	print(result)