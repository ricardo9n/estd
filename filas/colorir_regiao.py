def print_regiao(regiao):
	for i in regiao:
		for j in i:
			print(j,end=" ")
		print()
	print()

def colorir_regiao(regiao1,ponto,nova_cor):
	#seu codigo aqui
	return [ [i for i in j] for j in regiao1]

#Teste 1
regiao1  = [[1,0,0,2,2], [0,2,2,1,2],[2,1,1,1,2], [2,1,2,1,2],[2,2,1,2,2] ]
ponto1   = [2,2]
nova_cor1= 2
resultado_esperado1 = [[1,0,0,2,2], [0,2,2,2,2],[2,2,2,2,2], [2,2,2,2,2],[2,2,1,2,2] ]
resultado1 = colorir_regiao(regiao1,ponto1,nova_cor1)

print(resultado1 == resultado_esperado1) #deve ser True

print_regiao(regiao1)
print_regiao(resultado_esperado1)

#Teste 2
regiao2   = [[1,1,1,2,2,1], [1,2,2,1,2,1],[1,1,1,1,2,1], [1,1,2,1,1,1],[1,2,1,2,2,1] ]
ponto2    = [0,0]
nova_cor2 = 0
resultado_esperado2 = [[0,0,0,2,2,0], [0,2,2,0,2,0],[0,0,0,0,2,0], [0,0,2,0,0,0],[0,2,0,2,2,0] ]
resultado2 = colorir_regiao(regiao2,ponto2,nova_cor2)

print(resultado2 == resultado_esperado2) #deve ser True

print_regiao(regiao2)
print_regiao(resultado_esperado2)