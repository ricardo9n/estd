from Noh import *

class ListaOrdenada:
	def __init__(self):
	    self.head = None

	def is_empty(self):
	    return self.head == None

	def add(self,item):
	    atual = self.head
	    anterior = None
	    parar = False
	    while atual != None and not parar:
	        if atual.getData() > item:
	            parar = True
	        else:
	            anterior = atual
	            atual = atual.getNext()

	    temp = Noh(item)
	    if anterior == None:
	        temp.setNext(self.head)
	        self.head = temp
	    else:
	        temp.setNext(atual)
	        anterior.setNext(temp)

	def size(self):
	    atual    = self.head
	    contador = 0
	    while atual != None:
	        contador = contador + 1
	        atual = atual.getNext()
	    return contador

	def search(self,item):
	    atual     = self.head #atual == temp
	    encontrou = False
	    parar     = False
	    while atual != None and not encontrou and not parar:
	        if atual.getData() == item:
	            encontrou = True
	        else:
	            if atual.getData() > item:
	                parar = True
	            else:
	                atual = atual.getNext()

	    return encontrou

	def remove(self,item):
	    atual = self.head
	    anterior = None
	    encontrou = False
	    while  not encontrou: #percorre a lista
	        if atual.getData() == item:
	            encontrou = True
	        else:
	            anterior = atual
	            atual = atual.getNext()

	    if anterior == None:
	        self.head = atual.getNext()
	    else:
	        anterior.setNext(atual.getNext())

if __name__ == "__main__":
	l1 = ListaOrdenada()
	l1.add(1)
	l1.add(2)
	l1.add(3)
	l1.remove(1)
	l1.remove(5)
	print(l1.size())