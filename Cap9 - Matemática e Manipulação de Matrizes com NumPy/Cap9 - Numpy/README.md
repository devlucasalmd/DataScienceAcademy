# Numpy

Um array NumPy é uma estrutura de dados multidimensional usada em computação científica e análise de dados. O NumPy fornece um objeto de matriz N-dimensional (ou ndarray), que é uma grade homogênea de elementos, geralmente números, que podem ser indexados por um conjunto de inteiros.

Os arrays NumPy são mais eficientes do que as listas Python para armazenar e manipular grandes quantidades de dados, pois são implementados em Linguagem C e fornecem várias otimizações de desempenho. 

import numpy as n

n.__version__

**Criando Arrays NumPy**
arr1 = n.array([10, 21, 32, 43, 48, 15, 76, 57, 89])
print(arr1)

Um objeto do tipo ndarray é um recipiente multidimensional de itens do mesmo tipo e tamanho
type(arr1)

**Indexação em Arrays NumPy**
Imprimindo um elemento específico no array
arr1[4] 

Indexação
arr1[1:4] 
arr1[1:4+1] 

Cria uma lista de índices
indices = [1, 2, 5, 6]

Imprimindo os elementos dos índices
arr1[indices] 

Cria uma máscara booleana para os elementos pares
mask = (arr1 % 2 == 0)
print(mask)

print(arr1[mask])

Alterando um elemento do array
arr1[0] = 100
print(arr1)

Não é possível incluir elemento de outro tipo
try:
    arr1[0] = 'Novo elemento'
except:
    print("Operação não permitida!")


### Funções NumPy
A função array() cria um array NumPy
arr2 = n.array([1, 2, 3, 4, 5])
print(arr2)
type(arr2)

Usando métodos do array NumPy
arr2.cumsum()
arr2.cumprod()

arr3 = n.arange(0, 50, 5)
print(arr3)
type(arr3)

Formato do array
n.shape(arr3)

print(arr3.dtype)

Cria um array preenchido com zeros
arr4 = n.zeros(10)
print(arr4)

Retorna 1 nas posições em diagonal e 0 no restante
arr5 = n.eye(3)
print(arr5)

Os valores passados como parâmetro, formam uma diagonal
arr6 = n.diag(n.array([1, 2, 3, 4]))

Array de valores booleanos
arr7 = dsa.array([True, False, False, True])

Array de strings
arr8 = dsa.array(['Linguagem Python', 'Linguagem R', 'Linguagem Julia'])