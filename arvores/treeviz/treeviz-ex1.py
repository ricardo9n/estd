from treeviz import draw, parse_tree

tree = ['A', ['B', ['F', [], []], ['G', [], []]], ['H', [], ['C', ['D', [], []], ['E', [], []]]]]

print(draw(tree))
print(draw(tree, mode="side"))
print(draw(tree, mode="folder", show_empty=True))

parsed = parse_tree("A(B(F,G),H(,C(D,E)))")
print(draw(parsed, mode="vertical"))