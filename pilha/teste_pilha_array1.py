p = PilhaArray() # conteúdo [ ]
p.push(5)# conteúdo [5]
p.push(3)# conteúdo [5, 3]
print(len(p))# conteúdo [5, 3];retorna 2
print(p.pop()) # conteúdo [5]; retorna 3
print(p.is_empty())# conteúdo [5]; retorna False
print(p.pop()) # conteúdo [ ]; retorna 5
print(p.is_empty())# conteúdo [ ]; retorna True
p.push(7)# conteúdo [7]
p.push(9)# conteúdo [7, 9]
print(p.top()) # conteúdo [7, 9];retorna 9
p.push(4)# conteúdo [7, 9, 4]
print(p.size())# conteúdo [7, 9, 4]; retorna 3
print(p.pop()) # conteúdo [7, 9];retorna 4
p.push(6)# conteúdo [7, 9, 6]
p.push(8)# conteúdo [7, 9, 6, 8]
print(p.pop()) # conteúdo [7, 9, 6]; retorna 8