def quickSort(uma_lista):
   quickSortHelper(uma_lista,0,len(uma_lista)-1,0)

def quickSortHelper(uma_lista,primeiro,ultimo,tabs):
   if primeiro<ultimo:
       tabs += 1
       splitpoint = partitionp(uma_lista,primeiro,ultimo,tabs)
       print(f'{"\t"*tabs}split: {uma_lista[splitpoint]} <- {splitpoint}')
       quickSortHelper(uma_lista,primeiro,splitpoint-1,tabs)
       quickSortHelper(uma_lista,splitpoint+1,ultimo,tabs)


def partitionp(uma_lista,primeiro,ultimo, tabs=1):
   pivot = uma_lista[primeiro]

   print("="*60)
   print(f'{"\t"*tabs}nivel: {tabs}')
   print(f'{"\t"*tabs}antes: {uma_lista[primeiro:ultimo+1]}')

   leftmark = primeiro+1
   rightmark = ultimo

   terminou = False
   while not terminou:

       while leftmark <= rightmark and uma_lista[leftmark] <= pivot:
           leftmark = leftmark + 1

       while uma_lista[rightmark] >= pivot and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           terminou = True
       else:
           temp = uma_lista[leftmark]
           uma_lista[leftmark] = uma_lista[rightmark]
           uma_lista[rightmark] = temp

   temp = uma_lista[primeiro]
   uma_lista[primeiro] = uma_lista[rightmark]
   uma_lista[rightmark] = temp

   print(f'{"\t"*tabs}left: {uma_lista[primeiro:rightmark]}')
   print(f'{"\t"*tabs}pivot: ({pivot}) ({leftmark}<>{rightmark}) -> ({uma_lista[leftmark]}<>{uma_lista[rightmark]})')
   print(f'{"\t"*tabs}right: {uma_lista[rightmark+1:ultimo+1]}')
   print(f'{"\t"*tabs}depois: {uma_lista[primeiro:ultimo+1]}')
   return rightmark

def partitionu(uma_lista,primeiro,ultimo, tabs=1):
   pivot = uma_lista[ultimo]

   # print("="*60)
   print(f'{"\t"*tabs}nivel: {tabs}')
   print(f'{"\t"*tabs}antes: {uma_lista[primeiro:ultimo+1]}')

   leftmark = primeiro
   rightmark = ultimo-1

   terminou = False
   while not terminou:

       while leftmark <= rightmark and uma_lista[leftmark] <= pivot:
           leftmark = leftmark + 1

       while uma_lista[rightmark] >= pivot and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           terminou = True
       else:
           temp = uma_lista[leftmark]
           uma_lista[leftmark] = uma_lista[rightmark]
           uma_lista[rightmark] = temp

   temp = uma_lista[ultimo]
   uma_lista[ultimo] = uma_lista[leftmark]
   uma_lista[leftmark] = temp

   print(f'{"\t"*tabs}left: {uma_lista[primeiro:leftmark]}')
   print(f'{"\t"*tabs}pivot: ({pivot}) ({leftmark}<>{rightmark}) -> ({uma_lista[leftmark]}<>{uma_lista[rightmark]})')
   print(f'{"\t"*tabs}right: {uma_lista[leftmark+1:ultimo+1]}')
   print(f'{"\t"*tabs}depois: {uma_lista[primeiro:ultimo+1]}')

   return leftmark

if __name__ == "__main__":
    def ordena(lista):
        quickSort(lista)

    import sys
    uma_lista = [46, 7, 81, 23, 14, 59, 33, 72, 18]
    if len(sys.argv) > 1:
        uma_lista = list(map(int, sys.argv[1:]))
    ordena(uma_lista)
