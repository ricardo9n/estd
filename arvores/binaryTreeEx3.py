class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def __repr__(self):
        l = self.leftChild
        r = self.rightChild
        return(f'[ [{self.key}], [{l}], [{r}] ]')

    def postorder(self):
        if self != None:
            e=self.getLeftChild()
            e=e.postorder() if e else " "
            d=self.getRightChild()
            d=d.postorder() if d else " "

            return '({} {} {})'.format((e), (d), self.getRootVal())


    def preorder(self):
        if self != None:
            e=self.getLeftChild()
            e=e.preorder() if e else " "
            d=self.getRightChild()
            d=d.preorder() if d else " "

            return '({} {} {})'.format(self.getRootVal(), (e), (d))

    def inorder(self):
        if self != None:
            e=self.getLeftChild()
            e=e.inorder() if e else " "
            d=self.getRightChild()
            d=d.inorder() if d else " "

            return '({} {} {})'.format((e), self.getRootVal(), (d))

def exemplo01():
    print('exemplo01()')
    r = BinaryTree('a')
    print(r.getRootVal())
    print(r.getLeftChild())
    r.insertLeft('b')
    print(r.getLeftChild())
    print(r.getLeftChild().getRootVal())
    r.insertRight('c')
    print(r.getRightChild())
    print(r.getRightChild().getRootVal())
    r.getRightChild().setRootVal('hello')
    print(r.getRightChild().getRootVal())
    print()
    print(r)
    print(r.preorder())
    print(r.inorder())
    print(r.postorder())
    print('============')

def exemplo02():
    print('exemplo01()')
    r = BinaryTree('Book')
    r.insertLeft('C1')
    r.insertRight('C2')

    c1 = r.getLeftChild()
    c2 = r.getRightChild()

    c1.insertLeft("C11")
    c1.insertRight("C12")
    
    c12 = c1.getRightChild()
    c12.insertLeft("c121")
    c12.insertRight("c122")

    c2.insertLeft("C21")
    c2.insertRight("C22")

    c22 = c2.getRightChild()
    c22.insertLeft("c221")
    c22.insertRight("c222")

    print()
    #print(r)
    #print(r.preorder())
    #print(r.inorder())
    print(r.postorder())
    print('============')

if __name__ == '__main__':
    exemplo01()
    exemplo02()