#data1_test.py
from data1 import * #include
data1 = Data() #dia/mes/ano
data2 = Data() #dia/mes/ano

data1.ano = 2018
data1.mes = 4
data1.dia = 18

print("%d/%d/%d" %(data1.dia, data1.mes, data1.ano))
print(f"{data2.dia}/{data2.mes}/{data2.ano}")
