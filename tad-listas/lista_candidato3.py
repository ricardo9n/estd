#lista_candidato3.py

from Candidato1 import *

class Lista_candidato:
	def __init__(self):
		self.TAMANHO_MAX = 5
		self.lista = [None, None, None, None, None]
		self.tamanho_lista = 0

	def adiciona(self, valor):
		if self.tamanho_lista < self.TAMANHO_MAX:
			self.lista[self.tamanho_lista] = valor
			self.tamanho_lista += 1

	def __len__(self):
		return self.tamanho_lista

	def adiciona_na_posicao(self, posicao,valor):
		pass

	def pega(self, posicao):
		pass

	def contem(self, candidato):
		pass

	def tamanho(self):
		return self.tamanho

	def __str__(self):
		result = "["
		i = 0
		for c in self.lista:
			if c == None: break
			result += str(c) + ", "
		result += "]"
		#print(result)
		return result
