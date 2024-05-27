# Operações Matemáticas com Arrays NumPy

arr15 = dsa.arange(1, 10)

**Soma dos elementos do array**
dsa.sum(arr15)

**Retorna o produto dos elementos**
dsa.prod(arr15)

**Soma acumulada dos elementos**
dsa.cumsum(arr15)

**Cria 2 arrays**
arr16 = dsa.array([3, 2, 1])
arr17 = dsa.array([1, 2, 3])

**Soma dos arrays**
arr18 = dsa.add(arr16, arr17) 

print(arr18)

**Cria duas matrizes**
arr19 = dsa.array([[1, 2], [3, 4]])
arr20 = dsa.array([[5, 6], [0, 7]])

arr19.shape
arr20.shape

**Multiplicar as duas matrizes**

Para multiplicar duas matrizes NumPy, podemos usar a função dot() ou o operador @. 

o número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz.

arr21 = dsa.dot(arr19, arr20)
arr21 = arr19 @ arr20
arr21 = dsa.tensordot(arr19, arr20, axes = ((1),(0)))print(arr21)  


