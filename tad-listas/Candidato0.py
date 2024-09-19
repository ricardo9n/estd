#candidato0.py
class Candidato:
    nome = ""
    pontuacao = -1


a = Candidato(); b = Candidato(); c = Candidato()
a.nome = "Joao"; a.pontuacao = "9"
b.nome = "Maria"; b.pontuacao = "10"
print(a.nome, a.pontuacao); print(b.nome, b.pontuacao)
lista_candidatos = []
lista_candidatos.append(a)
lista_candidatos.append(b)
lista_candidatos.append(c)
print("Lista de Candidatos...")
for cand in lista_candidatos:
    print(">>>",cand.nome,cand.pontuacao)

#e = Candidato('Ricardo',100)