def busca_binaria(uma_lista, item_procurado):
    if len(uma_lista) ==  0:
        return False
    else:
        meio = len(uma_lista)//2
        print(uma_lista[meio],'[',meio,']',end=" - ")
        if uma_lista[meio]==item_procurado:
            return True
        else:
            if item_procurado<uma_lista[meio]:
                return busca_binaria(uma_lista[:meio],item_procurado)
            else:
                return busca_binaria(uma_lista[meio+1:],item_procurado)

if __name__ == '__main__':
    '''
    lista_teste = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
    print('Procurando 3 na lista',lista_teste)
    print('resultado',busca_binaria(lista_teste, 3))
    print('Procurando 13 na lista',lista_teste)
    print('resultado',busca_binaria(lista_teste, 13))
    '''
    '''
    Q-3
    '''
    lista_teste = [3, 5, 6, 8, 11, 12, 14, 15, 17, 18]
    print('Procurando 8 na lista',lista_teste)
    print('resultado',busca_binaria(lista_teste, 16))
    print();