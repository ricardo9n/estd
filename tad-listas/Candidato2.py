class Candidato:
	#nome = ""
	#pontuacao = -1

	def __init__(self, nome_, pontuacao_):
		self.nome = nome_
		self.pontuacao = pontuacao_

	def eh_vencedor(self):
		if self.pontuacao > 50:
			return True
		else:
			return False

a = Candidato('Ricardo',100)
b = Candidato('Ricardo',40)

print(a.nome)
print(a.pontuacao)
print(a.eh_vencedor())
print(b.eh_vencedor())