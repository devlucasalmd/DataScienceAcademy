# Manipulando Matrizes

import numpy as n

Criando uma matriz
arr9 = n.array( [ [1,2,3] , [4,5,6] ] ) 
type(arr9)
print(arr9)
print(arr9.shape)

Criando uma matriz 2x3 apenas com números "1"
arr10 = n.ones((2,3))
print(arr10)

Lista de listas
lista = [[13,81,22], [0, 34, 59], [21, 48, 94]]

A função matrix cria uma matriz a partir de uma lista de listas
arr11 = n.matrix(lista)
print(arr11)

*Formato da matriz*
n.shape(arr11)
arr11.size
print(arr11)
*Indexação da matriz*
arr11[2,1]
arr11[0:2,2]
arr11[1,]
*Alterando um elemento da matriz*
arr11[1,0] = 100

x = dsa.array([1, 2])  # NumPy decide o tipo dos dado
y = dsa.array([1.0, 2.0])  # NumPy decide o tipo dos dado
z = dsa.array([1, 2], dtype = dsa.float64)  # Forçamos um tipo de dado em particular
print(x.dtype, y.dtype, z.dtype)

arr12 = dsa.array([[24, 76, 92, 14], [47, 35, 89, 2]], dtype = float)
print(arr12)

**Manipulando Objetos de 3 e 4 Dimensões com NumPy**
Cria um array numpy de 3 dimensões
arr_3d = dsa.array([
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ],
    [
        [13, 14, 15, 16],
        [17, 18, 19, 20],
        [21, 22, 23, 24]
    ]
])
print(arr_3d)
arr_3d.ndim
arr_3d.shape

### Manipulando Arquivos com NumPy

import os
filename = os.path.join('dataset.csv')

!head dataset.csv
Carregando um dataset para dentro de um array
arr13 = dsa.loadtxt(filename, delimiter = ',', usecols = (0,1,2,3), skiprows = 1)

print(arr13)

Carregando apenas duas variáveis (colunas) do arquivo
var1, var2 = dsa.loadtxt(filename, delimiter = ',', usecols = (0,1), skiprows = 1, unpack = True)

Gerando um plot a partir de um arquivo usando o NumPy
import matplotlib.pyplot as plt
plt.show(plt.plot(var1, var2, 'o', markersize = 6, color = 'red'))