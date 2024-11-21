def quickSort(uma_lista):
   quickSortHelper(uma_lista,0,len(uma_lista)-1)

def quickSortHelper(uma_lista,primeiro,ultimo):
   if primeiro<ultimo:

       splitpoint = partition(uma_lista,primeiro,ultimo)

       quickSortHelper(uma_lista,primeiro,splitpoint-1)
       quickSortHelper(uma_lista,splitpoint+1,ultimo)

def partition(uma_lista,primeiro,ultimo):
   pivot = uma_lista[primeiro]

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


   return rightmark

if __name__ == "__main__":
    uma_lista = [54,26,93,17,77,31,44,55,20]
    uma_lista = [14, 17, 13, 15, 19, 10, 3, 16, 9, 12] 
    quickSort(uma_lista)
    print(uma_lista)