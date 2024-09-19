# Baseado em código do livro:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# License <http://www.gnu.org/licenses/>.

from sys import *
from pilha_array import *

def inverte_arquivo(nome_arquivo):
  p = PilhaArray()
  arquivo = open(nome_arquivo)     #abre o arquivo
                                   
  for linha in arquivo:            #lê cada linha do arquivo 
    p.push(linha.rstrip('\n'))     # insere a linha na pilha 
  arquivo.close()                  # fecha o arqui
                                   
  output = open(nome_arquivo, 'w') # reabre o arquivo e sobrescreve
  while not p.is_empty():
    output.write(p.pop() + '\n')   # re-insert newline characters
  output.close()

def inverte_texto(texto):
  pilha = PilhaArray()
  for letra in texto:
    pilha.push(letra)
  palavra = ""
  while not pilha.is_empty():
    palavra += pilha.pop()
  return palavra

if __name__ == "__main__":
  try:
    if len(argv) > 1:
      print('vou inverter o arquivo...\n')
      inverte_arquivo(argv[1])
      print(argv[1],"invertido...")
      exit()
    else:
      print('vou inverter uma palavra...\n')
      palavra = input('digite uma palavra: ')
      print("a palavra invertida eh",inverte_texto(palavra))
  except Exception as e:
    print('erro: nao pude processar os dados')
