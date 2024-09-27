from fila_array import *

fila1 = FilaArray()
fila1.first()
fila1.enqueue("ricardo")
fila1.enqueue("maria")
fila1.enqueue("joão")
print(fila1)
print(fila1.first())
fila1.dequeue()
print(fila1)
