def insertionSort(uma_lista):
   for index in range(1,len(uma_lista)):

     valor_atual = uma_lista[index]
     posicao = index

     while posicao>0 and uma_lista[posicao-1]>valor_atual:
         uma_lista[posicao]=uma_lista[posicao-1]
         posicao = posicao-1

     uma_lista[posicao]=valor_atual

if __name__ == "__main__":
  uma_lista = [54,26,93,17,77,31,44,55,20]
  insertionSort(uma_lista)
  print(uma_lista)
