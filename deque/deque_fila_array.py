from fila_array import *

class DequeArray(FilaArray):

    def add_first(self, e):
        """Adiciona um elemento no início do deque."""
        if self._tamanho == len(self._dados):
            self._altera_tamanho(2 * len(self._dados))  # Dobra o tamanho da lista se necessário
        self._inicio = (self._inicio - 1) % len(self._dados)  # Move o início para trás
        self._dados[self._inicio] = e
        self._tamanho += 1

    def add_last(self, e):
        """Adiciona um elemento no final do deque."""
        self.enqueue(e)  # Usa o método `enqueue` já definido para inserir no final

    def delete_first(self):
        """Remove e retorna o primeiro elemento do deque."""
        return self.dequeue()  # Usa o método `dequeue` já definido para remover do início

    def delete_last(self):
        """Remove e retorna o último elemento do deque."""
        if self.is_empty():
            raise FilaVazia('O Deque está vazio')
        # Calcula a posição do último elemento
        ultimo = (self._inicio + self._tamanho - 1) % len(self._dados)
        result = self._dados[ultimo]
        self._dados[ultimo] = None
        self._tamanho -= 1
        return result

    def last(self):
        """Retorna o último elemento do deque sem removê-lo."""
        if self.is_empty():
            raise FilaVazia('O Deque está vazio')
        ultimo = (self._inicio + self._tamanho - 1) % len(self._dados)
        return self._dados[ultimo]

if __name__ == "__main__":
    # Teste básico para verificar a implementação
    deque = DequeArray()
    deque.add_first(10)
    deque.add_last(20)
    deque.add_first(5)
    deque.add_last(30)
    deque.add_first(5)
    deque.add_last(30)
    deque.add_first(5)
    deque.add_last(30)

    print(deque)  # Esperado: [5, 10, 20, 30] tamanho: 4 capacidade 5

    print(deque.delete_first())  # Esperado: 5
    print(deque.delete_last())   # Esperado: 30
    print(deque)  # Esperado: [10, 20] tamanho: 2 capacidade 5
