def is_heap_min(lista, i=0):
    result = True

    if i == 0 :
        dir = 2*i + 1
        esq = 2*i + 2
        result = result and is_heap_min(lista, dir)
        result = result and is_heap_min(lista, esq)
    else:
        dir = 2*i
        esq = 2*i+1
        if dir < len(lista): 
            temp = lista[i] < lista[dir]
            #print(f'min: {temp} = {lista[i]} < {lista[dir]}') #debug
            result = result and temp  and is_heap_min(lista, dir)
            #if not temp: print(f'[{i}]={lista[i]} e [{dir}]={lista[dir]}') #debug
        if esq < len(lista): 
            temp = lista[i] < lista[esq]
            #print(f'min: {temp} = {lista[i]} < {lista[esq]}') #debug
            result = result and temp  and is_heap_min(lista, esq)
            #if not temp: print(f'[{i}]={lista[i]} e [{esq}]={lista[esq]}') #debug

    return result

def is_heap_max(lista, i=0):   
    result = True

    if i == 0 :
        dir = 2*i + 1
        esq = 2*i + 2
        result = result and is_heap_max(lista, dir)
        result = result and is_heap_max(lista, esq)
    else:
        dir = 2*i
        esq = 2*i+1
        if dir < len(lista): 
            temp = lista[i] > lista[dir]
            #print(f'max: {temp} = {lista[i]} > {lista[dir]}') #debug
            result = result and temp  and is_heap_max(lista, dir)
            #if not temp: print(f'[{i}]={lista[i]} e [{dir}]={lista[dir]}') #debug
        if esq < len(lista): 
            temp = lista[i] > lista[esq]
            #print(f'max: {temp} = {lista[i]} > {lista[esq]}') #debug
            result = result and temp  and is_heap_max(lista, esq)
            #if not temp: print(f'[{i}]={lista[i]} e [{esq}]={lista[esq]}') #debug
    
    return result


def is_heap(lista):	
    if is_heap_min(lista): return True
    if is_heap_max(lista): return True
    return False


def teste():
	l1 = [0, 161, 41, 101, 141, 71, 91, 31, 21, 81, 17, 16, ]
	print(l1, is_heap(l1))
	l2 = [0, 2, 3, 6, 5, 9, 9, 11, 12, 10, 13]
	print(l2, is_heap(l2))
	l3 = [0, 161, 141, 101, 81, 71, 91, 31, 21, 41, 17, 16, 15, 11, 12, 13, 14]
	print(l3, is_heap(l3))

if __name__ == "__main__":
	teste()


'''

[0, 161, 41, 101, 141, 71, 91, 31, 21, 81, 17, 16, ]
[0,   1,  2,   3,   4,  5,  6,  7,  8,  9, 10, 11, ]
      7
    3
      8
  1
      9
    4
      10
0
      11
    5
      12
  2
      13
    6
      14
'''