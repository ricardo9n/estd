def busca_sequencial_ordenada(uma_lista, item_pesquisado):
    pos = 0
    encontrou = False
    parar = False

    tamanho_lista = len(uma_lista)
    
    while pos < tamanho_lista and not encontrou and not parar:
        if uma_lista[pos] == item_pesquisado:
            encontrou = True
        else:
            if uma_lista[pos] > item_pesquisado:
                parar = True
            else:
	            pos = pos+1

    return encontrou

if __name__ == '__main__':
	lista_teste = [0, 1, 2, 8, 13, 17, 19, 32, 42]
	print('Procurando 3 na lista',lista_teste)
	print('resultado:', busca_sequencial_ordenada(lista_teste, 3),'\n')
	print('Procurando 13 na lista',lista_teste)
	print('resultado:', busca_sequencial_ordenada(lista_teste, 13))