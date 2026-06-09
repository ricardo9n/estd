from pathlib import Path
import sys

_HERE = Path(__file__).resolve().parent
_PARENT = _HERE.parent

# Permite executar este arquivo tanto na pasta "arvores" quanto na "treeviz".
if str(_PARENT) not in sys.path:
    sys.path.insert(0, str(_PARENT))

from binaryTreeEx1 import *
from treeviz.treeviz import draw

def build_example1():
    x = BinaryTree('A')
    insertLeft(x, 'B')
    insertRight(x, 'C')
    insertLeft(getLeftChild(x), 'D')
    insertRight(getLeftChild(x), 'E')
    insertLeft(getRightChild(x), 'F')
    insertRight(getRightChild(x), 'G')
    insertLeft(x, 'H')
    return x

def build_example2():
    x = BinaryTree('A')
    insertLeft(x, 'B')
    insertRight(x, 'C')
    insertLeft(getRightChild(x), 'D')
    insertRight(getRightChild(x), 'E')
    insertLeft(getLeftChild(x), 'F')
    insertRight(getLeftChild(x), 'G')
    insertRight(x, 'H')
    return x


def build_example3():
    x = BinaryTree('A')
    insertLeft(x, 'B')
    insertRight(x, 'C')
    insertLeft(getLeftChild(x), 'D')
    insertRight(getLeftChild(x), 'E')
    insertLeft(getRightChild(x), 'F')
    insertRight(getLeftChild(getLeftChild(x)), 'G')

    insertLeft(x, 'H')
    return x

if __name__ == "__main__":
    tree1 = build_example1()
    tree2 = build_example2()
    tree3 = build_example3()

    print("=== arvore 1 ===")
    # print(draw(tree1))

    print("=== arvore 2 ===")
    print(draw(tree2))

    print("=== arvore 3 ===")
    # print(draw(tree3))
