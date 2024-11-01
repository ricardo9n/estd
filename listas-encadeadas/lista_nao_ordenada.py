from Noh import *

class ListaNaoOrdenada:
	def __init__(self):
		self.head = None

	def is_empty(self):
		return self.head == None

	def add(self, item):
		temp = Noh(item)
		temp.setNext(self.head)
		self.head = temp

	def size(self):
		atual    = self.head
		contador = 0
		while atual != None:
			#print(atual.getData())
			contador = contador + 1
			atual = atual.getNext()
		return contador

	def search(self,item):
		atual     = self.head #atual == temp
		encontrou = False
		while atual != None and not encontrou:
			if atual.getData() == item:
				encontrou = True
			else:
				atual = atual.getNext()

		return encontrou

	#incompleto!
	def remove(self,item):
		atual = self.head
		anterior = None
		encontrou = False
		while not encontrou: #percorre a lista
			if atual.getData() == item:
				encontrou = True
			else:
				anterior = atual
				atual = atual.getNext()

		if anterior == None:
			self.head = atual.getNext()
		else:
			anterior.setNext(atual.getNext())

	def __str__(self):
		atual    = self.head

		result = '['
		while atual != None:
			result += str(atual.getData())
			if  atual.getNext(): result += ","
			atual = atual.getNext()
		result += ']'

		return result


## ----------

	def show(self):
		info = self.head
		dados = []
		dados.append(info.__str__())
		print(dados)


l = ListaNaoOrdenada()
l.add(1)
l.add(2)
l.add(10)
l.add(20)
l.add(30)
l.size()
print(l)
l.remove(30)
l.show()