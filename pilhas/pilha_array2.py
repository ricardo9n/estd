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

  def __xgetitem__(self,pos): #errado!
    return self._pilha[pos]

  def __iter__(self): #
    self._copia = self._pilha[:]
    while(len(self._copia) > 0):
      yield self._copia.pop()

  def __iter2__(self): #errado
    if(len(self._copia) > 0):
      yield self._copia.pop()

  def __xiter0__(self): #funciona com next
    self._copia = self._pilha[:]
    return (self)

  def __xnext__(self):
    if(len(self._copia) > 0):
      return self._copia.pop()
    raise StopIteration



if __name__ == '__main__':
  p = PilhaArray()     # conteúdo [ ]
  p.push(5)            # conteúdo [5]
  p.push(3)            # conteúdo [5, 3]
  p.push(7)            # conteúdo [7]
  p.push(9)            # conteúdo [7, 9]
  for i in p:
    print(i)

  i = iter(p)
  print(next(i))
  print(next(i))
  print(next(i))
  print(next(i))
  
  i = iter(p)
  for j in i:
    print(j)
  