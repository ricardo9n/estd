from fila_array import *

fila = FilaArray()
for i in range(6):
	fila.enqueue(10*i)
	fila.show()
print(fila)