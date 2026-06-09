# treeviz

Modulo simples para desenhar arvores binarias em texto (ASCII/Unicode), focado em uso didatico.

## API publica

- `draw(tree, mode="vertical", show_empty=False) -> str`
- `parse_tree(text) -> tuple | None`

## O mais importante

- `draw()` sempre retorna `str` (nao faz `print()` internamente).
- Arvore vazia (`[]` ou `None`) retorna exatamente:

```text
<empty tree>
```

- Entradas aceitas:
  - lista aninhada: `[valor, esquerda, direita]`
  - objeto estilo BinaryTree (duck typing):
    - `getRootVal()`
    - `getLeftChild()`
    - `getRightChild()`
  - texto no formato: `node(left,right)`

- Modelo interno usado pelo modulo:

```python
(value, left, right)
```

com `None` para subarvore vazia.

## Modos de visualizacao

### 1) vertical (padrao)

```python
print(draw(tree))
print(draw(tree, mode="vertical"))
```

Exemplo:

```text
  _A
 /  \
 B  H_
/ \   \
F G   C
     / \
     D E
```

### 2) side

```python
print(draw(tree, mode="side"))
```

Exemplo:

```text
│       ┌── 4
└── *
    │   ┌── 2
    └── +
        └── 7
```

### 3) folder

```python
print(draw(tree, mode="folder"))
```

Exemplo:

```text
A
├── B
│   ├── F
│   └── G
└── H
    └── C
        ├── D
        └── E
```

## Mostrar filhos ausentes

Use `show_empty=True` para exibir `∅` em vazios estruturais:

```python
print(draw(tree, mode="folder", show_empty=True))
```

Exemplo:

```text
A
├── B
│   ├── F
│   └── G
└── H
    ├── ∅
    └── C
```

## parse_tree(text)

Converte texto para arvore interna:

```python
t = parse_tree("A(B(F,G),H(,C(D,E)))")
print(draw(t, mode="vertical"))
```

Tambem funciona com operadores e numeros:

```python
t = parse_tree("*(+(7,2),4)")
print(draw(t, mode="side"))
```

## Exemplo rapido completo

```python
from treeviz import draw, parse_tree

tree = ['A', ['B', ['F', [], []], ['G', [], []]], ['H', [], ['C', ['D', [], []], ['E', [], []]]]]

print(draw(tree))
print(draw(tree, mode="side"))
print(draw(tree, mode="folder", show_empty=True))

parsed = parse_tree("A(B(F,G),H(,C(D,E)))")
print(draw(parsed, mode="vertical"))
```

## Observacao

Ha um bloco de demonstracao em `if __name__ == "__main__":` dentro de `treeviz.py`.
Execute para ver varios exemplos:

```bash
python treeviz.py
```
