def _merge(uma_lista2,esquerda, direita):
    i=0
    j=0
    k=0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            uma_lista2[k]=esquerda[i]
            i=i+1
        else:
            uma_lista2[k]=direita[j]
            j=j+1
        k=k+1

    while i < len(esquerda):
        uma_lista2[k]=esquerda[i]
        i=i+1
        k=k+1

    while j < len(direita):
        uma_lista2[k]=direita[j]
        j=j+1
        k=k+1

def mergeSort(uma_lista1):
    print("Splitting ",uma_lista1)
    if len(uma_lista1)>1:
        meio = len(uma_lista1)//2
        esquerda = uma_lista1[:meio]
        direita = uma_lista1[meio:]

        mergeSort(esquerda)
        mergeSort(direita)
        _merge(uma_lista1,esquerda, direita)

    print("Merging ",uma_lista1)

if __name__ == "__main__":
    uma_lista = [54,26,93,17,77,31,44,55,20]
    mergeSort(uma_lista)
    print(uma_lista)