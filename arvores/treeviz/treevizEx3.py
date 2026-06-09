from binaryTreeEx2 import BinaryTree
from treeviz.treeviz import draw


def build_example_tree() -> BinaryTree:
    """Monta uma arvore usando a API orientada a objeto do BinaryTreeEx2."""
    root = BinaryTree("A")

    root.insertLeft("B")
    root.insertRight("H")

    left = root.getLeftChild()
    left.insertLeft("F")
    left.insertRight("G")

    right = root.getRightChild()
    right.insertRight("C")

    c_node = right.getRightChild()
    c_node.insertLeft("D")
    c_node.insertRight("E")

    return root


if __name__ == "__main__":
    tree = build_example_tree()

    print("=== vertical (padrao) ===")
    print(draw(tree))

    print("\n=== side ===")
    print(draw(tree, mode="side"))

    print("\n=== folder ===")
    print(draw(tree, mode="folder", show_empty=True))
