class Candidato:
	def __init__(self):
		self.nome = ""
		self.pontuacao = -1
	def __str__(self):
		return self.nome+" "+str(self.pontuacao)
if __name__ == '__main__':
	a = Candidato()
	a.nome = 'Ricardo'
	b = Candidato();  b.nome="Joao"
	print(a); print(b)