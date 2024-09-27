#fila_array_main.py
from fila_array import *
from random import randint
from time import sleep

f = FilaArray()
f2= FilaArray()
#print('dequeue: ',f.dequeue())

def pausa():
	sleep(1)

def ta_na_hora(i):
	return randint(1,i) == 1

for i in range(1,28,1):
	try:
		print('tempo: ', i)
		if ta_na_hora(2) :
			valor = randint(1,100)
			print('entrou na fila: ',valor)
			f.enqueue(valor)
		if ta_na_hora(5) :
			print('saiu da fila: ',f.dequeue())
		if ta_na_hora(7):
			print('first: ',f.first())
		f.show(); pausa()

	except FilaVazia as fv:
		print('opz, comando sobre a fila vazia\n')
		pausa()
if not f.is_empty():
	print('o restante fica para amanha...')
print('acabou o expediente!!')
