#lista_candidato1.py
TAMANHO_MAX = 4

def adiciona(valor, lista):
	for i in range(TAMANHO_MAX) :
		if lista[i] == None:
			lista[i] = valor
			break

def adiciona_na_posicao(posicao,valor, lista):
	novo_valor = valor
	for i in range(posicao, TAMANHO_MAX) :
		temp = lista[i]
		lista[i] = novo_valor
		novo_valor = temp

def pega(posicao,lista):
	return lista[posicao]

def contem(candidato,lista):
	for i in range(TAMANHO_MAX) :
		if candidato == lista[i]: return i
	return None

def tamanho(lista):
	for i in range(TAMANHO_MAX) :
		if lista[i] == None: return i
	return TAMANHO_MAX

def imprime(lista):
	result = "["
	i = 0
	while i < tamanho(lista): # and lista[i] != None:
		result += (lista[i].nome)
		i += 1
		if i < tamanho(lista) and lista[i] != None: result += ", "
	result += "]"
	print(result)