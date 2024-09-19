# Baseado em código do livro:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# License <http://www.gnu.org/licenses/>.

class PilhaVazia(Exception):
  pass

class PilhaArray:
  def __init__(self):
    self._pilha = []

  def __len__(self):
    return len(self._pilha)

  def size(self):
    return self.__len__()

  def is_empty(self):
    return len(self._pilha) == 0

  def push(self, e):
    self._pilha.append(e)

  def top(self):
    if self.is_empty():
      raise PilhaVazia('A pilha está vazia')
    return self._pilha[-1]

  def pop(self):
    if self.is_empty():
      raise PilhaVazia('A pilha está vazia')
    return self._pilha.pop()

if __name__ == '__main__': #código de teste
  p = PilhaArray()     # conteúdo [ ]
  try:
    print(p.top())       # erro!
  except :
    print('opz! tentei ver o topo de uma pilha vazia')
  p.push(5)            # conteúdo [5]
  p.push(3)            # conteúdo [5, 3]
  print(len(p))        # conteúdo [5, 3];    retorna 2
  print(p.pop())       # conteúdo [5];       retorna 3
  print(p.is_empty())  # conteúdo [5];       retorna False
  print(p.pop())       # conteúdo [ ];       retorna 5
  print(p.is_empty())  # conteúdo [ ];       retorna True
  p.push(7)            # conteúdo [7]
  p.push(9)            # conteúdo [7, 9]
  try:
    print(p.top())       # conteúdo [7, 9];    retorna 9
  except:
    print('pilha vazia')
  p.push(4)            # conteúdo [7, 9, 4]
  print(p.size())      # conteúdo [7, 9, 4]; retorna 3
  print(p.pop())       # conteúdo [7, 9];    retorna 4
  p.push(6)            # conteúdo [7, 9, 6]
  p.push(8)            # conteúdo [7, 9, 6, 8]
  print(p.pop())       # conteúdo [7, 9, 6]; retorna 8
