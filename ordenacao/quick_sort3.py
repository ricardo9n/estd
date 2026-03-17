from typing import List, Callable


# ================================
# QuickSort (interface principal)
# ================================
def quicksort(lista: List[int], partition: Callable = None) -> None:
    """Quicksort in-place com escolha configurável de pivô."""
    if partition is None:
        partition = partition_primeiro  # padrão didático
    quicksort_helper(lista, 0, len(lista) - 1, 0, partition)


def quicksort_helper(lista, primeiro, ultimo, nivel, partition):
    indent = "   " * nivel
    print(f'{indent}Quicksort({primeiro}, {ultimo}) -> {lista[primeiro:ultimo+1]}')

    if primeiro >= ultimo:
        print(f'{indent}Base: sublista com 0 ou 1 elemento, já ordenada.')
        return

    split = partition(lista, primeiro, ultimo, nivel)
    print(f'{indent}Pivô posicionado em {split}: {lista[split]}')
    print()

    quicksort_helper(lista, primeiro, split - 1, nivel + 1, partition)
    quicksort_helper(lista, split + 1, ultimo, nivel + 1, partition)


# =======================================
# Estratégia 1 — pivô no primeiro elemento
# =======================================
def partition_primeiro(lista, primeiro, ultimo, nivel):
    indent = "   " * nivel
    pivot = lista[primeiro]

    print(f'{indent}[Partition: pivô primeiro elemento]')
    print(f'{indent}Pivot = {pivot}')
    print(f'{indent}Antes: {lista[primeiro:ultimo+1]}')

    left = primeiro + 1
    right = ultimo

    while True:
        while left <= right and lista[left] <= pivot:
            left += 1
        while right >= left and lista[right] >= pivot:
            right -= 1
        if right < left:
            break
        lista[left], lista[right] = lista[right], lista[left]

    lista[primeiro], lista[right] = lista[right], lista[primeiro]

    print(f'{indent}Depois: {lista[primeiro:ultimo+1]}')
    print(f'{indent}Pivô colocado na posição {right}')
    return right


# =====================================
# Estratégia 2 — pivô no último elemento
# =====================================
def partition_ultimo(lista, primeiro, ultimo, nivel):
    indent = "   " * nivel
    pivot = lista[ultimo]

    print(f'{indent}[Partition: pivô último elemento]')
    print(f'{indent}Pivot = {pivot}')
    print(f'{indent}Antes: {lista[primeiro:ultimo+1]}')

    left = primeiro
    right = ultimo - 1

    while True:
        while left <= right and lista[left] <= pivot:
            left += 1
        while right >= left and lista[right] >= pivot:
            right -= 1
        if right < left:
            break
        lista[left], lista[right] = lista[right], lista[left]

    lista[left], lista[ultimo] = lista[ultimo], lista[left]

    print(f'{indent}Depois: {lista[primeiro:ultimo+1]}')
    print(f'{indent}Pivô colocado na posição {left}')
    return left


# ==================================================
# Estratégia 3 — mediana de três (primeiro, meio, último)
# ==================================================
def partition_mediana(lista, primeiro, ultimo, nivel):
    indent = "   " * nivel
    meio = (primeiro + ultimo) // 2

    # Pega os valores
    trio = [
        (lista[primeiro], primeiro),
        (lista[meio], meio),
        (lista[ultimo], ultimo),
    ]

    # Ordena pelo valor para pegar a mediana
    trio_sorted = sorted(trio, key=lambda x: x[0])
    _, idx_pivot = trio_sorted[1]  # índice da mediana

    # Coloca o pivô no início para usar partição do "primeiro"
    lista[primeiro], lista[idx_pivot] = lista[idx_pivot], lista[primeiro]
    pivot = lista[primeiro]

    print(f'{indent}[Partition: mediana de 3]')
    print(f'{indent}Indices considerados: {primeiro}, {meio}, {ultimo}')
    print(f'{indent}Pivot escolhido (mediana): {pivot}')
    print(f'{indent}Antes: {lista[primeiro:ultimo+1]}')

    return partition_primeiro(lista, primeiro, ultimo, nivel)


# =====================
# Execução de exemplo
# =====================
if __name__ == "__main__":
    lista = [46, 7, 81, 23, 14, 59, 33, 72, 17]
    
    print("\n====================")
    print(" QuickSort didático ")
    print("====================\n")

    print("Lista original:", lista, "\n")
    
    quicksort(lista, partition_primeiro)

    print("\nLista final ordenada:", lista)
