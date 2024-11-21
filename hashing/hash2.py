def hash(uma_string, tamanho_tabela):
    sum = 0
    for pos in range(len(uma_string)):
        sum = sum + (pos+1)*ord(uma_string[pos])

    return sum % tamanho_tabela

if __name__ == '__main__':
	print(hash('cat',11))
	print(hash('tac',11))