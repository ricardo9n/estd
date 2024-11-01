def busca_sequencial(uma_lista, item_pesquisado):
    pos = 0
    encontrou = False
    tamanho_lista = len(uma_lista)
    
    while pos < tamanho_lista and not encontrou:
        if uma_lista[pos] == item_pesquisado:
            encontrou = True
        else:
            pos = pos+1

    return encontrou

if __name__ == '__main__':
	lista_teste = [1, 2, 32, 8, 17, 19, 42, 13, 0]
	print('Procurando 3 na lista',lista_teste)
	print('resultado:', busca_sequencial(lista_teste, 3),'\n')
	print('Procurando 13 na lista',lista_teste)
	print('resultado:', busca_sequencial(lista_teste, 13))