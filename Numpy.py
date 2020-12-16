import numpy as np
#Criando uma array ou vetor
x=np.array([1,2,3,4])
y = np.array([1,2,3,4])
print(x+y)
#Criando um vetor sem valor definido
z=np.ones((5))
print(z)
#Criando um vetor geometricamente ou em range
r=np.arange(5) 
r = np.arange(0,11,2)
print(r)
#Limitando a exibição
print(x[0:3])
print(x[1:])
#Criando Matrizes
x = np.array([[1,2,3,4,5],[1,2,3,4,5]])
z = np.array([[1,2,3,4,5]]*10)
print(z[5][3])
'''
Sempre tem que ser uma matriz quadrática
'''
x=np.zeros((5,5))
x = np.eye((4))
x
#As quatro operações
x = np.array([[2,2,2,2,2)]]*5)
z = np.array([[2,4,6,8,10]]*5)
x+z
x-z
z-x
x*z
x/z
z/x
'''Pode se criar uma variavel para armazenar esses valores
'''
