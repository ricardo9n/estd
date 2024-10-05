# Teste para SetWithQueue

'''
Acrescente aqui o seu código para SetWithQueue ou realize a importação do módulo para que os testes possam ser realizados corretamente.

'''

def test_add_unique_elements():
    set_queue = SetWithQueue()
    set_queue.add(1)
    set_queue.add(2)
    set_queue.add(3)
    assert set_queue.list() == [1, 2, 3], "Erro: Esperado [1, 2, 3]"

def test_add_duplicate_elements():
    set_queue = SetWithQueue()
    set_queue.add(1)
    set_queue.add(2)
    set_queue.add(3)
    set_queue.add(2)  # Deve ser ignorado
    set_queue.add(2)  # Deve ser ignorado
    set_queue.add(2)  # Deve ser ignorado
    set_queue.add(3)  # Deve ser ignorado
    set_queue.add(2)  # Deve ser ignorado
    set_queue.add(2)  # Deve ser ignorado
    assert set_queue.list() == [1, 2, 3], "Erro: Esperado [1, 2, 3]"

def test_remove_existing_element():
    set_queue = SetWithQueue()
    set_queue.add(1)
    set_queue.add(2)
    set_queue.add(3)
    set_queue.remove(1)
    assert set_queue.list() == [2,3], "Erro: Esperado [2,3]"
    set_queue.remove(2)
    assert set_queue.list() == [3], "Erro: Esperado [3]"
    set_queue.remove(3)
    assert set_queue.list() == [], "Erro: Esperado []"

def test_remove_non_existing_element():
    set_queue = SetWithQueue()
    set_queue.add(1)
    try:
        set_queue.remove(2)  # Deve lançar exceção
        assert False, "Erro: Exceção não lançada para elemento não existente"
    except ValueError as e:
        assert str(e) == "Element not found", "Erro: Mensagem de erro inesperada"

def test_contains_existing_element():
    set_queue = SetWithQueue()
    set_queue.add(1)
    assert set_queue.contains(1) is True, "Erro: Esperado True"

def test_contains_non_existing_element():
    set_queue = SetWithQueue()
    assert set_queue.contains(2) is False, "Erro: Esperado False"

def test_size_of_set():
    set_queue = SetWithQueue()
    set_queue.add(1)
    set_queue.add(2)
    assert set_queue.size() == 2, "Erro: Esperado 2"
    set_queue.remove(1)
    assert set_queue.size() == 1, "Erro: Esperado 1"

def test_list_empty_set():
    empty_set = SetWithQueue()
    assert empty_set.list() == [], "Erro: Esperado []"

def test_list_after_operations():
    set_queue = SetWithQueue()
    set_queue.add(1)
    set_queue.add(2)
    set_queue.remove(1)
    assert set_queue.list() == [2], "Erro: Esperado [2]"

def test_add_multiple_unique_elements():
    set_queue = SetWithQueue()
    for i in range(10):
        set_queue.add(i)
    assert set_queue.size() == 10, "Erro: Esperado 10"
    assert set_queue.list() == list(range(10)), "Erro: Esperado [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"

def test_add_multiple_duplicate_elements():
    set_queue = SetWithQueue()
    for i in range(5):
        set_queue.add(1)  # Adicionando duplicados
    assert set_queue.size() == 1, "Erro: Esperado 1 após adição de duplicados"

def run_tests():
    test_add_unique_elements()
    test_add_duplicate_elements()
    test_remove_existing_element()
    test_remove_non_existing_element()
    test_contains_existing_element()
    test_contains_non_existing_element()
    test_size_of_set()
    test_list_empty_set()
    test_list_after_operations()
    test_add_multiple_unique_elements()
    test_add_multiple_duplicate_elements()
    print("Todos os testes passaram!")

if __name__ == "__main__":
    run_tests()