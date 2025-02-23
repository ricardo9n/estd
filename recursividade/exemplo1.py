def contagem_regressiva(n):
    if n == 0:
        print("Fogo!")
    else:
        print("%d..."%n)
        contagem_regressiva(n-1)

#contagem_regressiva(10)

def soma_ateh(n):
	if n == 0:
		return 0
	else:
		return n + soma_ateh(n-1)

print(soma_ateh(5))