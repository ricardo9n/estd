class DequeVazio(Exception):
    pass


class DequeArray:
    '''
    Essa implementação de Deque segue FilaArray. 
    Mas ela tem alguns PROBLEMAS.
    Use deque_test.py para encontrar os problemas 
    e consertar.
    '''

    CAPACIDADE = 5
    
    def __init__(self):
        self._dados = [None] * self.CAPACIDADE
        self._tamanho = 0
        self._inicio = 0
        self._final = 0
  

    def is_empty(self):
        return self._tamanho == 0


    def size(self):
        return self._tamanho


    def _altera_tamanho(self, novo_tamanho):   
        dados_antigos = self._dados               
        self._dados = [None] * novo_tamanho       
        posicao = self._inicio

        for k in range(self._tamanho):            
            self._dados[k] = dados_antigos[posicao] 
            posicao = (posicao + 1) % len(dados_antigos) 

        self._inicio = 0                          

    def add_first(self, e):
        if self.is_empty():
            self._dados[self._inicio] = e
        else:
            self._inicio = (self._inicio - 1) % len(self._dados)
            self._dados[self._inicio] = e

        self._tamanho+=1


    def add_last(self, e):
        if self.is_empty():
            self._dados[self._final] = e
        else:
            self._final = (self._inicio + self._tamanho) % len(self._dados)
            self._dados[self._final] = e

        self._tamanho+=1


    def remove_first(self):
        if self.is_empty():
            raise DequeVazio("O deque está vazio.")

        removido = self._dados[self._inicio]
        self._dados[self._inicio] = None 
        self._inicio = (self._inicio + 1) % len(self._dados)
        self._tamanho-=1
        return removido 


    def remove_last(self):
        if self.is_empty():
            raise DequeVazio("O deque está vazio.")

        removido = self._dados[self._final]
        self._dados[self._final] = None 
        self._tamanho-=1
        self._final = (self._inicio + self._tamanho - 1) % len(self._dados)
        return removido


    def deque_sum(self):
        soma = 0
        posicao = self._inicio

        for k in range(self._tamanho):
            soma+=self._dados[posicao]
            posicao = (posicao + 1) % len(self._dados)

        return soma


    def eh_palindromo(self, p):
    
        posicao = self._inicio

        for k in range(self._tamanho):
            if p[k] != self._dados[posicao]:
                return False

            posicao = (posicao + 1) % len(self._dados)

        return True
    

    def first(self):
        return self._dados[self._inicio] 


    def last(self):
        return self._dados[self._final]