def busca_binaria(uma_lista, item_pesquisado):
    inicio = 0
    fim   = len(uma_lista)-1
    encontrou = False

    while inicio<=fim and not encontrou:
        meio   = (inicio + fim)//2
        print(uma_lista[meio],'[',meio,']',end=" - ")
        if uma_lista[meio] == item_pesquisado:
            encontrou = True
        else:
            if item_pesquisado < uma_lista[meio]:
                fim = meio-1
            else:
                inicio = meio+1
    return encontrou

if __name__ == '__main__':
    '''
    lista_teste = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
    print('Procurando 3 na lista',lista_teste)
    print('resultado',busca_binaria(lista_teste, 3))
    print('Procurando 13 na lista',lista_teste)
    print('resultado',busca_binaria(lista_teste, 13))
    print('Procurando 0 na lista',lista_teste)
    print('resultado',busca_binaria(lista_teste, 0))
    print('Procurando 32 na lista',lista_teste)
    print('resultado',busca_binaria(lista_teste, 32))
    print('Procurando 43 na lista',lista_teste)
    print('resultado',busca_binaria(lista_teste, 43))
    '''
    '''
    Q-3
    '''
    lista_teste = [3, 5, 6, 8, 11, 12, 14, 15, 17, 18]
    print('Procurando 8 na lista',lista_teste)
    print('resultado',busca_binaria(lista_teste, 8))
    print();