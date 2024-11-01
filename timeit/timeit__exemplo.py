import timeit
import random

minimo = 0
maximo = 1000000

qtd_de_vezes_repete_teste = 50

lista = list(range(maximo))

def valor_aleatorio_a_procurar():
  return random.randint(minimo,maximo*1.25)

def funcao_a_ser_testada1(lista, valor): #pesquisa sequencial
  for i in lista:
    if i == valor: return True
  return False

def funcao_a_ser_testada2(lista, valor): #pesquisa binária
  if len(lista) == 0: return False

  meio = len(lista)//2
  valor_meio = lista[meio]

  if valor_meio == valor: return True
  elif valor > valor_meio: return funcao_a_ser_testada2(lista[meio+1:], valor)
  else: return funcao_a_ser_testada2(lista[:meio], valor)

def funcao_a_ser_testada3(lista, valor, inicio, fim): #pesquisa binária
  # print(len(lista), valor, inicio, fim)
  meio = (inicio + fim)//2
  if inicio > fim or meio >= len(lista): return False

  valor_meio = lista[meio]

  if valor_meio == valor: return True
  elif valor > valor_meio: return funcao_a_ser_testada3(lista, valor, meio+1, fim)
  else: return funcao_a_ser_testada3(lista, valor, inicio, meio-1)

def funcao_realiza_teste1():
  valor = valor_aleatorio_a_procurar() 
  resultado = funcao_a_ser_testada1(lista, valor)
  # print(f'procurando o valor {valor} na lista de tamanho {len(lista)} -> resultado: {resultado} ')

def funcao_realiza_teste2():
  valor = valor_aleatorio_a_procurar() 
  resultado = funcao_a_ser_testada2(lista, valor)
  # print(f'procurando o valor {valor} na lista de tamanho {len(lista)} -> resultado: {resultado} ')

tempo = timeit.timeit( stmt=funcao_realiza_teste1, number=qtd_de_vezes_repete_teste)
print(f'teste repetido {qtd_de_vezes_repete_teste} vezes')
print(f'tempo de duração do teste: {tempo}')

tempo = timeit.timeit( stmt=funcao_realiza_teste2, number=qtd_de_vezes_repete_teste)
print(f'teste repetido {qtd_de_vezes_repete_teste} vezes')
print(f'tempo de duração do teste: {tempo}')

#lista = list(range(maximo))

def funcao_realiza_teste3():
  valor = valor_aleatorio_a_procurar()
  resultado = funcao_a_ser_testada3(lista, valor, 0, len(lista))
  # print(f'procurando o valor {valor} na lista de tamanho {len(lista)} -> resultado: {resultado} ')


tempo = timeit.timeit(stmt=funcao_realiza_teste3, number=qtd_de_vezes_repete_teste)
print(f'teste repetido {qtd_de_vezes_repete_teste} vezes')
print(f'tempo de duração do teste: {tempo}')
