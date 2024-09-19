#lista_candidato2.py

TAMANHO_MAX = 4

tamanho_lista = 0

def adiciona(valor,lista):
	global tamanho_lista
	if tamanho_lista < TAMANHO_MAX:
		lista[tamanho_lista] = valor
		tamanho_lista += 1

def adiciona_na_posicao(posicao,valor, lista):
	novo_valor = valor
	for i in range(posicao, TAMANHO_MAX) :
		temp = lista[i]
		lista[i] = novo_valor
		novo_valor = temp

def pega(posicao,lista):
	pass

def contem(candidato,lista):
	pass

def tamanho(lista):
	return tamanho_lista

def imprime(lista):
	result = "["
	i = 0
	while i < tamanho(lista) and lista[i] != None:
		result += (lista[i].nome)
		i += 1
		if i < tamanho(lista) and lista[i] != None: result += ", "
	result += "]"
	print(result)