from deque import *

def executar_teste(nome, teste):
    print(f"\nIniciando: {nome}")

    falhas = 0

    try:
        teste()
    except AssertionError as erro:
        print(f"  FALHA: {erro}")
        falhas += 1

    if falhas == 0:
        print(f"Finalizado: {nome} - OK")
    else:
        print(f"Finalizado: {nome} - {falhas} falha(s)")

    return falhas


def teste_add_first():
    d = DequeArray()

    d.add_first(10)
    d.add_first(20)

    assert d.size() == 2, "add_first: tamanho incorreto"
    assert d.first() == 20, "add_first: first() incorreto"
    assert d.last() == 10, "add_first: last() incorreto"


def teste_add_last():
    d = DequeArray()

    d.add_last(10)
    d.add_last(20)

    assert d.size() == 2, "add_last: tamanho incorreto"
    assert d.first() == 10, "add_last: first() incorreto"
    assert d.last() == 20, "add_last: last() incorreto"


def teste_remove_first():
    d = DequeArray()

    d.add_last(10)
    d.add_last(20)

    removido = d.remove_first()

    assert removido == 10, "remove_first: elemento removido incorreto"
    assert d.size() == 1, "remove_first: tamanho incorreto"
    assert d.first() == 20, "remove_first: first() incorreto"
    assert d.last() == 20, "remove_first: last() incorreto"


def teste_remove_last():
    d = DequeArray()

    d.add_last(10)
    d.add_last(20)

    removido = d.remove_last()

    assert removido == 20, "remove_last: elemento removido incorreto"
    assert d.size() == 1, "remove_last: tamanho incorreto"
    assert d.first() == 10, "remove_last: first() incorreto"
    assert d.last() == 10, "remove_last: last() incorreto"


def teste_reutilizacao_depois_de_esvaziar():
    d = DequeArray()

    d.add_last(10)
    d.remove_last()

    d.add_first(20)

    assert d.size() == 1, "reutilização: tamanho incorreto"
    assert d.first() == 20, "reutilização: first() incorreto"
    assert d.last() == 20, "reutilização: last() incorreto depois de esvaziar o deque"


def teste_remove_first_ate_esvaziar():
    d = DequeArray()

    d.add_last(10)
    d.add_last(20)

    d.remove_first()
    d.remove_first()

    assert d.is_empty(), "remove_first: deque deveria estar vazio"

    d.add_last(30)

    assert d.first() == 30, "remove_first: first() incorreto após esvaziar e reutilizar"
    assert d.last() == 30, "remove_first: last() incorreto após esvaziar e reutilizar"


def teste_remove_last_ate_esvaziar():
    d = DequeArray()

    d.add_last(10)
    d.add_last(20)

    d.remove_last()
    d.remove_last()

    assert d.is_empty(), "remove_last: deque deveria estar vazio"

    d.add_first(30)

    assert d.first() == 30, "remove_last: first() incorreto após esvaziar e reutilizar"
    assert d.last() == 30, "remove_last: last() incorreto após esvaziar e reutilizar"


def teste_deque_circular():
    d = DequeArray()

    d.add_last(10)
    d.add_last(20)
    d.add_last(30)

    d.remove_first()
    d.remove_first()

    d.add_last(40)
    d.add_last(50)

    assert d.size() == 3, "circularidade: tamanho incorreto"
    assert d.first() == 30, "circularidade: first() incorreto"
    assert d.last() == 50, "circularidade: last() incorreto"


def teste_deque_sum():
    d = DequeArray()

    d.add_last(10)
    d.add_last(20)
    d.add_first(5)

    assert d.deque_sum() == 35, "deque_sum: soma incorreta"


def teste_deque_vazio():
    d = DequeArray()

    try:
        d.remove_first()
        assert False, "remove_first deveria lançar DequeVazio"
    except DequeVazio:
        pass

    try:
        d.remove_last()
        assert False, "remove_last deveria lançar DequeVazio"
    except DequeVazio:
        pass


def teste_excesso_de_capacidade():
    d = DequeArray()

    for i in range(d.CAPACIDADE):
        d.add_last(i)

    d.add_last(99)

    assert d.size() <= d.CAPACIDADE, "capacidade: deque ultrapassou a capacidade máxima"


def main():
    testes = [
        ("add_first", teste_add_first),
        ("add_last", teste_add_last),
        ("remove_first", teste_remove_first),
        ("remove_last", teste_remove_last),
        ("reutilização depois de esvaziar", teste_reutilizacao_depois_de_esvaziar),
        ("remove_first até esvaziar", teste_remove_first_ate_esvaziar),
        ("remove_last até esvaziar", teste_remove_last_ate_esvaziar),
        ("deque circular", teste_deque_circular),
        ("deque_sum", teste_deque_sum),
        ("deque vazio", teste_deque_vazio),
        ("excesso de capacidade", teste_excesso_de_capacidade),
    ]

    print("=== Testes do DequeArray ===")

    total_falhas = 0

    for nome, teste in testes:
        total_falhas += executar_teste(nome, teste)

    print("\n=== Resultado ===")
    print(f"Testes executados: {len(testes)}")
    print(f"Total de falhas: {total_falhas}")

    if total_falhas == 0:
        print("Todos os testes passaram.")
    else:
        print("Existem falhas na implementação.")


if __name__ == "__main__":
    main()