# Baseado em código do livro:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# License <http://www.gnu.org/licenses/>.

from pilha_array import *

def delimitadores_equivalentes(d_fecha, d_abre):
  abre  = '({['                # delimitadores - abertura
  fecha = ')}]'                # delimitadoers - fechamento
  return fecha.index(d_fecha) == abre.index(d_abre)

def is_matched(expr):
  abre  = '({['                # delimitadores - abertura
  fecha = ')}]'                # delimitadoers - fechamento
  pilha = PilhaArray()
  for d in expr:
    if d in abre:
      pilha.push(d)            # push o delimitador de abertura
    elif d in fecha:
      if pilha.is_empty():
        return False           # não bate
      if not delimitadores_equivalentes(d,pilha.pop()):
        return False           # não bate
  return pilha.is_empty()      # tem mais delimitadores na pilha?

if __name__ == '__main__':
  expr = input('digite uma expressão com () e/ou [] e/ou {}: ')
  if (is_matched(expr)):
    print('os delimitadores estão corretos na expressão ', expr)
  else:
    print('há problema nos delimitadores da expressão ',expr)
