"""Visualizador de arvores binarias para uso didatico.

API publica:
- draw(tree, mode="vertical", show_empty=False)
- parse_tree(text)

Modelo interno unificado:
(value, left, right)
onde left/right sao None quando a subarvore e vazia.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

_InternalTree = Optional[tuple[Any, "_InternalTree", "_InternalTree"]]
_EMPTY_MARK = "__TREEVIZ_EMPTY__"


@dataclass
class _TextParser:
    """Parser recursivo-descendente para arvores no formato textual."""

    text: str
    pos: int = 0

    def parse(self) -> _InternalTree:
        self._skip_ws()
        if self._eof():
            raise ValueError("texto de arvore vazio")

        node = self._parse_node()
        self._skip_ws()
        if not self._eof():
            rest = self.text[self.pos : self.pos + 20]
            raise ValueError(f"conteudo inesperado apos a arvore: {rest!r}")
        return node

    def _parse_node(self) -> _InternalTree:
        self._skip_ws()
        label = self._parse_label()

        self._skip_ws()
        if self._peek() != "(":
            return (label, None, None)

        self.pos += 1  # '('
        self._skip_ws()

        if self._peek() == ",":
            left = None
        else:
            left = self._parse_node()

        self._skip_ws()
        if self._peek() != ",":
            raise ValueError(f"esperado ',' na posicao {self.pos}")
        self.pos += 1

        self._skip_ws()
        if self._peek() == ")":
            right = None
        else:
            right = self._parse_node()

        self._skip_ws()
        if self._peek() != ")":
            raise ValueError(f"esperado ')' na posicao {self.pos}")
        self.pos += 1

        return (label, left, right)

    def _parse_label(self) -> str:
        self._skip_ws()
        start = self.pos
        while not self._eof():
            ch = self.text[self.pos]
            if ch in "()," or ch.isspace():
                break
            self.pos += 1

        if self.pos == start:
            raise ValueError(f"esperado rotulo de no na posicao {self.pos}")

        return self.text[start:self.pos]

    def _skip_ws(self) -> None:
        while not self._eof() and self.text[self.pos].isspace():
            self.pos += 1

    def _peek(self) -> str:
        if self._eof():
            return ""
        return self.text[self.pos]

    def _eof(self) -> bool:
        return self.pos >= len(self.text)


def parse_tree(text: str) -> _InternalTree:
    """Converte texto no formato node(left,right) para o modelo interno.

    Exemplos validos:
    - "A(B(F,G),H(,C(D,E)))"
    - "*(+(7,2),4)"
    """

    if not isinstance(text, str):
        raise TypeError("parse_tree() espera uma string")

    parser = _TextParser(text=text)
    return parser.parse()


def draw(tree: Any, mode: str = "vertical", show_empty: bool = False) -> str:
    """Renderiza uma arvore binaria em formato textual.

    Parametros:
    - tree: arvore em lista aninhada, objeto estilo BinaryTree, texto ou modelo interno.
    - mode: "vertical", "side" ou "folder".
    - show_empty: quando True, exibe subarvores ausentes como "∅" nos pontos estruturais.

    Retorna:
    - str com o desenho da arvore.
    """

    normalized = _normalize_tree(tree)
    if normalized is None:
        return "<empty tree>"

    if show_empty:
        normalized = _add_structural_empty_nodes(normalized)

    mode = mode.lower().strip()
    if mode == "vertical":
        return _build_ascii_vertical(normalized)
    if mode == "side":
        return _build_ascii_side(normalized)
    if mode == "folder":
        return _build_ascii_folder(normalized)

    raise ValueError("modo invalido. Use: 'vertical', 'side' ou 'folder'.")


def _normalize_tree(tree: Any) -> _InternalTree:
    """Normaliza diferentes formatos de entrada para (value, left, right)."""

    if tree is None:
        return None

    if isinstance(tree, list):
        return _convert_from_list(tree)

    if isinstance(tree, tuple) and len(tree) == 3:
        value, left, right = tree
        return (value, _normalize_tree(left), _normalize_tree(right))

    if isinstance(tree, str):
        stripped = tree.strip()
        if not stripped:
            raise ValueError("string vazia nao representa uma arvore valida")
        return _parse_tree(stripped)

    if _is_binarytree_like(tree):
        return _convert_from_binarytree(tree)

    raise TypeError(
        "formato de arvore nao suportado. Use lista aninhada, texto, "
        "objeto estilo BinaryTree, None, [] ou tupla interna."
    )


def _convert_from_list(tree: Any) -> _InternalTree:
    """Converte arvore no formato [node, left, right]."""

    if tree == []:
        return None

    if not isinstance(tree, list):
        raise TypeError("_convert_from_list espera uma lista")

    if len(tree) != 3:
        raise ValueError("lista de arvore deve ter exatamente 3 elementos: [node, left, right]")

    value, left, right = tree
    return (value, _convert_from_list(left), _convert_from_list(right))


def _is_binarytree_like(obj: Any) -> bool:
    """Verifica compatibilidade via duck typing com BinaryTree."""

    return (
        hasattr(obj, "getRootVal")
        and callable(getattr(obj, "getRootVal"))
        and hasattr(obj, "getLeftChild")
        and callable(getattr(obj, "getLeftChild"))
        and hasattr(obj, "getRightChild")
        and callable(getattr(obj, "getRightChild"))
    )


def _convert_from_binarytree(tree: Any) -> _InternalTree:
    """Converte objeto estilo BinaryTree para o modelo interno."""

    if tree is None:
        return None

    if not _is_binarytree_like(tree):
        raise TypeError("objeto nao e compativel com BinaryTree")

    root = tree.getRootVal()
    left_obj = tree.getLeftChild()
    right_obj = tree.getRightChild()

    left = _convert_binary_child(left_obj)
    right = _convert_binary_child(right_obj)

    # Tratar padrao comum de arvore vazia representada por raiz None sem filhos.
    if root is None and left is None and right is None:
        return None

    return (root, left, right)


def _convert_binary_child(child: Any) -> _InternalTree:
    if child is None:
        return None

    if child == []:
        return None

    if _is_binarytree_like(child):
        return _convert_from_binarytree(child)

    if isinstance(child, list):
        return _convert_from_list(child)

    if isinstance(child, tuple) and len(child) == 3:
        return _normalize_tree(child)

    raise TypeError("filho retornado por BinaryTree deve ser None, lista, tupla ou BinaryTree")


def _parse_tree(text: str) -> _InternalTree:
    return parse_tree(text)


def _make_empty_node() -> tuple[str, None, None]:
    return (_EMPTY_MARK, None, None)


def _is_empty_marker(node: _InternalTree) -> bool:
    return isinstance(node, tuple) and len(node) == 3 and node[0] == _EMPTY_MARK


def _add_structural_empty_nodes(node: _InternalTree) -> _InternalTree:
    """Insere nos vazios estruturais quando apenas um filho existe.

    Regras:
    - se um no tem somente um filho, o outro lado vira "∅";
    - folhas continuam sem filhos explicitos para evitar poluicao visual.
    """

    if node is None:
        return None

    value, left, right = node
    left_n = _add_structural_empty_nodes(left)
    right_n = _add_structural_empty_nodes(right)

    has_left = left_n is not None
    has_right = right_n is not None

    if has_left and not has_right:
        right_n = _make_empty_node()
    elif has_right and not has_left:
        left_n = _make_empty_node()

    return (value, left_n, right_n)


def _label(value: Any) -> str:
    if value == _EMPTY_MARK:
        return "∅"
    return str(value)


def _build_ascii_vertical(tree: _InternalTree) -> str:
    """Renderiza em modo vertical usando composicao recursiva de blocos."""

    lines, _, _, _ = _build_vertical_block(tree)
    return "\n".join(lines)


def _build_vertical_block(node: _InternalTree) -> tuple[list[str], int, int, int]:
    """Retorna (linhas, largura, altura, posicao_do_no_raiz)."""

    if node is None:
        return [""], 0, 1, 0

    value, left, right = node
    label = _label(value)
    label_w = len(label)

    if left is None and right is None:
        return [label], label_w, 1, label_w // 2

    if right is None:
        left_lines, left_w, left_h, left_root = _build_vertical_block(left)

        first = " " * (left_root + 1)
        first += "_" * (left_w - left_root - 1)
        first += label

        second = " " * left_root + "/"
        second += " " * (left_w - left_root - 1 + label_w)

        shifted = [line + " " * label_w for line in left_lines]
        lines = [first, second] + shifted
        return lines, left_w + label_w, left_h + 2, left_w + label_w // 2

    if left is None:
        right_lines, right_w, right_h, right_root = _build_vertical_block(right)

        first = label
        first += "_" * right_root
        first += " " * (right_w - right_root)

        second = " " * (label_w + right_root) + "\\"
        second += " " * (right_w - right_root - 1)

        shifted = [" " * label_w + line for line in right_lines]
        lines = [first, second] + shifted
        return lines, right_w + label_w, right_h + 2, label_w // 2

    left_lines, left_w, left_h, left_root = _build_vertical_block(left)
    right_lines, right_w, right_h, right_root = _build_vertical_block(right)

    first = " " * (left_root + 1)
    first += "_" * (left_w - left_root - 1)
    first += label
    first += "_" * right_root
    first += " " * (right_w - right_root)

    second = " " * left_root + "/"
    second += " " * (left_w - left_root - 1 + label_w + right_root)
    second += "\\"
    second += " " * (right_w - right_root - 1)

    if left_h < right_h:
        left_lines += [" " * left_w] * (right_h - left_h)
    elif right_h < left_h:
        right_lines += [" " * right_w] * (left_h - right_h)

    merged = [l + " " * label_w + r for l, r in zip(left_lines, right_lines)]
    lines = [first, second] + merged

    total_w = left_w + label_w + right_w
    root_pos = left_w + label_w // 2
    total_h = max(left_h, right_h) + 2
    return lines, total_w, total_h, root_pos


def _build_ascii_side(tree: _InternalTree) -> str:
    """Renderiza em modo lateral (raiz ao centro/esquerda, direita para cima)."""

    lines: list[str] = []
    _side_walk(tree, prefix="", is_left=True, lines=lines)
    return "\n".join(lines)


def _side_walk(node: _InternalTree, prefix: str, is_left: bool, lines: list[str]) -> None:
    if node is None:
        return

    value, left, right = node

    if right is not None:
        next_prefix = prefix + ("│   " if is_left else "    ")
        _side_walk(right, next_prefix, False, lines)

    branch = "└── " if is_left else "┌── "
    lines.append(prefix + branch + _label(value))

    if left is not None:
        next_prefix = prefix + ("    " if is_left else "│   ")
        _side_walk(left, next_prefix, True, lines)


def _build_ascii_folder(tree: _InternalTree) -> str:
    """Renderiza em modo hierarquico tipo pastas."""

    if tree is None:
        return "<empty tree>"

    value, left, right = tree
    lines = [_label(value)]

    children = _folder_children(left, right)
    for index, child in enumerate(children):
        last = index == len(children) - 1
        _folder_walk(child, prefix="", is_last=last, lines=lines)

    return "\n".join(lines)


def _folder_children(left: _InternalTree, right: _InternalTree) -> list[_InternalTree]:
    children: list[_InternalTree] = []
    if left is not None:
        children.append(left)
    if right is not None:
        children.append(right)
    return children


def _folder_walk(node: _InternalTree, prefix: str, is_last: bool, lines: list[str]) -> None:
    if node is None:
        return

    value, left, right = node
    connector = "└── " if is_last else "├── "
    lines.append(prefix + connector + _label(value))

    next_prefix = prefix + ("    " if is_last else "│   ")
    children = _folder_children(left, right)
    for index, child in enumerate(children):
        child_last = index == len(children) - 1
        _folder_walk(child, prefix=next_prefix, is_last=child_last, lines=lines)


if __name__ == "__main__":
    # Exemplo 1: lista aninhada.
    nested = [
        "A",
        ["B", ["F", [], []], ["G", [], []]],
        ["H", [], ["C", ["D", [], []], ["E", [], []]]],
    ]

    # Exemplo 2: objeto compativel com BinaryTree (duck typing).
    class DemoBinaryTree:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

        def getRootVal(self):
            return self.value

        def getLeftChild(self):
            return self.left

        def getRightChild(self):
            return self.right

    bt = DemoBinaryTree(
        "*",
        DemoBinaryTree("+", DemoBinaryTree("7"), DemoBinaryTree("2")),
        DemoBinaryTree("4"),
    )

    # Exemplo 3: texto parseado.
    parsed = parse_tree("A(B(F,G),H(,C(D,E)))")

    examples = [
        ("Lista aninhada", nested),
        ("BinaryTree", bt),
        ("parse_tree", parsed),
    ]

    for title, tree_obj in examples:
        print(f"\n=== {title} ===")
        print("\n-- draw(tree) [padrao: vertical] --")
        print(draw(tree_obj))
        print("\n-- draw(tree, mode='vertical') --")
        print(draw(tree_obj, mode="vertical"))
        print("\n-- draw(tree, mode='side') --")
        print(draw(tree_obj, mode="side"))
        print("\n-- draw(tree, mode='folder') --")
        print(draw(tree_obj, mode="folder"))

    print("\n-- show_empty=True (folder) --")
    print(draw(nested, mode="folder", show_empty=True))

