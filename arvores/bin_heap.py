class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percUp(self,i):
        while i // 2 > 0:
          if self.heapList[i] < self.heapList[i // 2]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2

    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        self.print_tree2() #para debug
        while (i > 0):
            print(i,self.heapList)
            #print("\n"+"="*5+">",i,"\n") #para debug

            self.percDown(i)
            i = i - 1
            #self.print_tree2() #para debuhg
            input("press <enter> to continue...") #para debuhg

    def __str__(self):
        return str(self.heapList)

    def print(self):
        print(self)

    def print_tree(self):
        for i in range(self.currentSize):
            print(" "*((i+1)//2) ,self.heapList[i])
    
    def print_tree2(self, nivel=1):
        import math
        if (nivel <= self.currentSize):
            v = int(math.log2(nivel))
            self.print_tree2(2*nivel+1)
            print(f"--"*(v) + str(self.heapList[nivel]))
            self.print_tree2(2*nivel)
            

def exemplo01():
    bh = BinHeap()
    bh.insert(8)
    bh.insert(7)
    bh.insert(3)
    bh.insert(11)
    bh.insert(10)
    bh.insert(2)
    bh.insert(1)
    bh.insert(11)
    bh.insert(5)
    bh.insert(4)

    '''
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())
    '''

    print(bh)

def exemplo02():
    bh = BinHeap()
    bh.insert(5)
    bh.insert(12)
    bh.insert(11)
    bh.insert(14)
    bh.insert(18)
    bh.insert(19)
    bh.insert(21)
    bh.insert(33)
    bh.insert(17)
    bh.insert(27)

    '''
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())
    '''

    print(bh)
    bh.insert(7)  

def exemplo03():
    bh = BinHeap()
    bh.insert(5)
    bh.insert(12)
    bh.insert(11)
    bh.insert(14)
    bh.insert(18)
    bh.insert(19)
    bh.insert(21)
    bh.insert(33)
    bh.insert(17)
    bh.insert(27)

    print(bh)
    bh.print_tree2()

    print("\nremovendo:",bh.delMin(),"\n")
    bh.print_tree2()

def exemplo04(): #buildheap
    bh = BinHeap()
    lista = [13,12,11,10,9,9,6,5,2,3]
    bh.buildHeap(lista)
    print(bh)
    bh.print_tree2()

if __name__ == "__main__":
    exemplo04()