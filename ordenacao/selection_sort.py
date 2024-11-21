def selectionSort1(uma_lista):
   for posicao_verificada in range(len(uma_lista)-1,0,-1):
       posicao_maior = 0
       for posicao in range(1,posicao_verificada+1):
           if uma_lista[posicao]>uma_lista[posicao_maior]:
               posicao_maior = posicao

       temp = uma_lista[posicao_verificada]
       uma_lista[posicao_verificada] = uma_lista[posicao_maior]
       uma_lista[posicao_maior] = temp


def selectionSort2(uma_lista): #menor
   for posicao_verificada in range(len(uma_lista)):
       posicao_menor = posicao_verificada
       for posicao in range(posicao_verificada,len(uma_lista)):
           if uma_lista[posicao]<uma_lista[posicao_menor]:
               posicao_menor = posicao
       if posicao_verificada != posicao_menor:
       	temp = uma_lista[posicao_verificada]
       	uma_lista[posicao_verificada] = uma_lista[posicao_menor]
       	uma_lista[posicao_menor] = temp

if __name__ == "__main__":
    uma_lista = [54,26,93,17,77,31,44,55,20]
    selectionSort2(uma_lista)
    print(uma_lista)
    uma_lista = [1,2,3,4,5,6]
    selectionSort2(uma_lista)
    print(uma_lista)
    uma_lista = [7,6,5,4,2,1]
    selectionSort2(uma_lista)
    print(uma_lista)
