from pilha_array import PilhaArray
from binaryTreeEx3 import BinaryTree
from TreeTraversalEx1 import *

def buildParseTree(fpexp):
    
    fplist = fpexp.split()
    pStack = PilhaArray()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

def operar(operador, operando1, operando2):
  if operador == '+':
    return operando1 + operando2
  raise Exception("not implemented")

def postordereval(parseTree):
#def evaluate(parseTree):
    import operator
    
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(postordereval(leftC),postordereval(rightC))
    else:
        return parseTree.getRootVal()

def printexp(tree):
  sVal = ""
  if tree:
      sVal = '(' + printexp(tree.getLeftChild())
      sVal = sVal + str(tree.getRootVal())
      sVal = sVal + printexp(tree.getRightChild())+')'
  return sVal

if __name__ == "__main__":
  pt = buildParseTree("( ( 11 + 0 ) * ( 1 + ( 3 + 5 ) ) )");  print(pt)
  #pt = buildParseTree("( 3 * ( 2 + 1 ) ) ");  print(pt)
  
#   print("preorder: ",pt.preorder())
#   print("inorder: ",pt.inorder())
#   print("posorder: ",pt.postorder())

#   print(postordereval(pt))
  print(printexp(pt))