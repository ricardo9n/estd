def bubbleSort(uma_lista):
    for varredura in range(len(uma_lista)-1,0,-1):
        for i in range(varredura):
            if uma_lista[i]>uma_lista[i+1]:
                temp = uma_lista[i]
                uma_lista[i] = uma_lista[i+1]
                uma_lista[i+1] = temp

def troca1(uma_lista,a,b):
	uma_lista[a],uma_lista[b] = uma_lista[b],uma_lista[a]

def bubbleSort1(uma_lista):
    for varredura in range(len(uma_lista)-1,0,-1):
        for i in range(varredura):
            if uma_lista[i]>uma_lista[i+1]:
                troca1(uma_lista,i,i+1)

if __name__ == "__main__":
	uma_lista = [54,26,93,17,77,31,44,55,20]
	bubbleSort(uma_lista)
	print(uma_lista)