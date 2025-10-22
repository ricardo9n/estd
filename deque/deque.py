class DequeVazio(Exception):
    pass

class DequeArray:
    
    CAPACIDADE_PADRAO = 5  # Tamanho padrão do array

    def __init__(self):
        self._dados = [None] * DequeArray.CAPACIDADE_PADRAO
        self._tamanho = 0
        self._inicio = 0

    def __len__(self):
        return self._tamanho

    def is_empty(self):
        return self._tamanho == 0

    def add_first(self, e):
        if self._tamanho == len(self._dados):
            self._altera_tamanho(2 * len(self._dados))  # Dobra o tamanho se necessário
        self._inicio = (self._inicio - 1) % len(self._dados)  # Move o início para trás
        self._dados[self._inicio] = e
        self._tamanho += 1

    def add_last(self, e):
        if self._tamanho == len(self._dados):
            self._altera_tamanho(2 * len(self._dados))  # Dobra o tamanho se necessário
        disponivel = (self._inicio + self._tamanho) % len(self._dados)  # Calcula posição final
        self._dados[disponivel] = e
        self._tamanho += 1

    def delete_first(self):
        if self.is_empty():
            raise FilaVazia('O Deque está vazio')
        result = self._dados[self._inicio]
        self._dados[self._inicio] = None
        self._inicio = (self._inicio + 1) % len(self._dados)  # Move o início para frente
        self._tamanho -= 1
        return result

    def delete_last(self):
        if self.is_empty():
            raise DequeVazio('O Deque está vazio')
        ultimo = (self._inicio + self._tamanho - 1) % len(self._dados)  # Calcula a posição do último elemento
        result = self._dados[ultimo]
        self._dados[ultimo] = None
        self._tamanho -= 1
        return result

    def first(self):
        if self.is_empty():
            raise DequeVazio('O Deque está vazio')
        return self._dados[self._inicio]

    def last(self):
        if self.is_empty():
            raise DequeVazio('O Deque está vazio')
        ultimo = (self._inicio + self._tamanho - 1) % len(self._dados)
        return self._dados[ultimo]

    def _altera_tamanho(self, novo_tamanho):
        dados_antigos = self._dados  # Armazena o array atual
        self._dados = [None] * novo_tamanho  # Cria um novo array com o tamanho solicitado
        posicao = self._inicio
        for k in range(self._tamanho):  # Realoca os elementos existentes
            self._dados[k] = dados_antigos[posicao]
            posicao = (1 + posicao) % len(dados_antigos)  # Modulo para circularidade
        self._inicio = 0  # O início é realinhado para 0

    def show(self):
        print(self)

    def __str__(self):
        posicao = self._inicio
        result = "["
        for k in range(self._tamanho):
            result += str(self._dados[posicao]) + ", "
            posicao = (1 + posicao) % len(self._dados)
        result += f'] tamanho: {len(self)} capacidade {len(self._dados)}\n'
        return result

if __name__ == "__main__":
    deque = DequeArray()
    try:
        deque.first()
        print('deque: ',deque)
    except:
        print('deque: ',deque)
        pass
    deque.add_first(10)   # Adiciona 10 no início
    deque.add_last(20)    # Adiciona 20 no final
    deque.add_first(5)    # Adiciona 5 no início
    print(deque)          # Esperado: [5, 10, 20, 30] tamanho: 4 capacidade 5

    deque.add_last(30)    # Adiciona 30 no final
    deque.add_first(10)   # Adiciona 10 no início
    deque.add_last(20)    # Adiciona 20 no final
    deque.add_first(5)    # Adiciona 5 no início
    deque.add_last(30)    # Adiciona 30 no final

    print(deque)          # Esperado: [5, 10, 20, 30] tamanho: 4 capacidade 5

    print(deque.delete_first())  # Esperado: 5
    print(deque.delete_last())   # Esperado: 30
    print(deque)                 # Esperado: [10, 20] tamanho: 2 capacidade 5
