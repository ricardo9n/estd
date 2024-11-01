class Noh:
    def __init__(self,valor_inicial):
        self._dados = valor_inicial
        self._proximo = None  
    
    def getData(self):
        return self._dados

    def getNext(self):
        return self._proximo

    def setData(self, novo_valor):
        self._dados =  novo_valor

    def setNext(self, novo_proximo):
        self._proximo = novo_proximo
        
    def __str__(self):
        return "Noh["+str(self.getData())+"] => " + str(self.getNext())

def fazNada():
    n1.setData(22)

    print(n1.getData())
    print(n1.getNext())
    
    n2 = Noh(23)
    n1.setNext(n2)

    n3 = Noh(24)
    n2.setNext(n3)

    n4 = Noh(25)
    n3.setNext(n4)

    print(n1)

if __name__ == "__main__": 
    n1 = Noh(33)
    print(n1)

    n1.setData(22)

    print(n1.getData())
    print(n1.getNext())
    print(n1)

    n2 = Noh(23)
    n1.setNext(n2)
    print(n1)

    n3 = Noh(24)
    n2.setNext(n3)

    n4 = Noh(25)
    n3.setNext(n4)

    print( str(n1) )

print('estou no arquivo Noh')