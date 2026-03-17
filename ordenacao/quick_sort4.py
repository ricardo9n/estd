from typing import List

def quicksort_outplace(lista: List[int], nivel: int = 0) -> List[int]:
    indent = "   " * nivel
    print(f"{indent}Quicksort: {lista}")

    # Condição de parada
    if len(lista) <= 1:
        print(f"{indent}Base: {lista} (já ordenada)")
        return lista

    # Escolha do pivô
    pivot = lista[0]
    print(f"{indent}Pivô escolhido: {pivot}")

    # Particionamento em novas listas (out-place)
    menores = [x for x in lista[1:] if x < pivot]
    maiores = [x for x in lista[1:] if x > pivot]

    print(f"{indent}menores: {menores}")
    print(f"{indent}maiores: {maiores}")

    # Recursão
    menores_ordenados = quicksort_outplace(menores, nivel + 1)
    maiores_ordenados = quicksort_outplace(maiores, nivel + 1)

    # Merge: concatenação simples
    ordenada = menores_ordenados + [pivot] + maiores_ordenados

    print(f"{indent}Concat: {menores_ordenados} + [{pivot}] + {maiores_ordenados}")
    print(f"{indent}Resultado parcial: {ordenada}\n")

    return ordenada


# Execução de demonstração
if __name__ == "__main__":
    lista = [46, 7, 81, 23, 14, 59, 33, 72, 17]
    print("\n========== QuickSort Out-Place ==========\n")
    print("Lista original:", lista, "\n")

    resultado = quicksort_outplace(lista)

    print("Resultado final:", resultado)
