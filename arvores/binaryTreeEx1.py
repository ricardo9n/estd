def BinaryTree(r):
    return [r, [], []]

def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [], []])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

def exemplo01a():
	r = BinaryTree(3)
	insertLeft(r,4)
	insertLeft(r,5)
	insertRight(r,6)
	insertRight(r,7)
	l = getLeftChild(r)
	print(l)
	setRootVal(l,9)
	print(r)
	insertLeft(l,11)
	print(r)
	print(getRightChild(getRightChild(r)))
def exemplo01b():
	from pprint import pprint
	r = BinaryTree(3)
	pprint(r)
	insertLeft(r,4)
	pprint(r)
	insertLeft(r,5)
	pprint(r)
	insertRight(r,6)
	pprint(r)
	insertRight(r,7)
	pprint(r)
	l = getLeftChild(r)
	pprint(l)

	setRootVal(l,9)
	pprint(r)
	insertLeft(l,11)
	pprint(r)
	pprint(getRightChild(getRightChild(r)))


def exemplo02():
	b1 = BinaryTree(3)
	e1 = BinaryTree(5)
	insertLeft(b1,8)
	insertRight(b1,7)

	print(b1)
	print(e1)

def exercicio01():
	x = BinaryTree('a')
	insertLeft(x,'b')
	insertRight(x,'c')
	insertRight(getRightChild(x),'d')
	insertLeft(getRightChild(getRightChild(x)),'e')
	print(x)

if __name__ == '__main__':
	exemplo01a()
	#exemplo02()
	#exercicio01()
	pass