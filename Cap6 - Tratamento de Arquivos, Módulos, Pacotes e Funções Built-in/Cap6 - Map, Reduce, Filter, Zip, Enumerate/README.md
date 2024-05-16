## Função Map

Função Map

A função map() em Python é uma função que aplica uma determinada função a cada elemento de uma estrutura de dados iterável (como uma lista, tupla ou outro objeto iterável). A função map() retorna um objeto que pode ser convertido em outra estrutura de dados, como uma lista, se necessário.

Função Python que retorna um número ao quadrado
def potencia(x):
    return x ** 2

numeros = [1, 2, 3, 4, 5]

numeros_ao_quadrado = list(map(potencia, numeros))

print(numeros_ao_quadrado)

Criando duas funções

Função 1 - Recebe uma temperatura como parâmetro e retorna a temperatura em Fahrenheit
def fahrenheit(T):
    return ((float(9)/5)*T + 32)

Função 2 - Recebe uma temperatura como parâmetro e retorna a temperatura em Celsius
def celsius(T):
    return (float(5)/9)*(T-32)

Criando uma lista
temperaturas = [0, 22.5, 40, 100]

Aplicando a função a cada elemento da lista de temperaturas. 
map(fahrenheit, temperaturas)

Função map() retornando a lista de temperaturas convertidas em Fahrenheit
list(map(fahrenheit, temperaturas))

Usando um loop for para imprimir o resultado da função map()
for temp in map(fahrenheit, temperaturas):
    print(temp)

list(map(celsius, temperaturas))

Usando expressão lambda
map(lambda x: (5.0/9)*(x - 32), temperaturas)

list(map(lambda x: (5.0/9)*(x - 32), temperaturas))

Somando os elementos de 2 listas
a = [1,2,3,4]
b = [5,6,7,8]

list(map(lambda x,y:x+y, a, b))


## Função Reduce

A função reduce() em Python é uma função da biblioteca functools que aplica uma determinada função binária a pares consecutivos de elementos em uma estrutura de dados iterável (como uma lista, tupla ou outro objeto iterável), reduzindo-a a um único valor.

Importando a função reduce do módulo functools
from functools import reduce

from IPython.display import Image
Image('arquivos/reduce.png')

Criando uma lista
lista = [47, 11 , 42, 13]

Funçao
def soma(a,b):
    x = a + b
    return x

Usando reduce com uma função e uma lista. A função vai retornar o valor máximo
reduce(soma, lista)

Usando a função reduce() com lambda
reduce(lambda x,y: x+y, lst)

Podemos atribuir a expressão lambda a uma variável
max_find2 = lambda a,b: a if (a > b) else b

Reduzindo a lista até o valor máximo, através da função criada com a expressão lambda
reduce(max_find2, lst)

## Função Filter

A função filter() em Python é uma função que filtra elementos de uma estrutura de dados iterável (como uma lista, tupla ou outro objeto iterável) com base em uma determinada condição. A função filter() retorna um objeto filtro, que pode ser convertido em outra estrutura de dados, como uma lista, se necessário.

Criando uma função
def verificaPar(num):
    if num % 2 == 0:
        return True
    else:
        return False

Chamando a função e passando um número como parâmetro. Retornará Falso de for ímpar e True se for par.
verificaPar(35)

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

A função filter() retorna um iterator
filter(verificaPar, lista)

list(filter(verificaPar, lista))

list(filter(lambda x: x%2==0, lista))

list(filter(lambda num: num > 8, lista))


## Zip

A função zip() em Python é uma função que agrupa elementos de múltiplas estruturas de dados iteráveis (como listas, tuplas ou outros objetos iteráveis) juntos em pares. A função zip() retorna um objeto zip, que pode ser convertido em outra estrutura de dados, como uma lista ou dicionário, se necessário.

Criando duas listas
x = [1,2,3]
y = [4,5,6]

Perceba que zip retorna tuplas. Neste caso, uma lista de tuplas
list(zip(x,y))

Atenção quando as sequências tiverem número diferente de elementos
list(zip('ABCD', 'xy'))

Criando 2 dicionários
d1 = {'a':1,'b':2}
d2 = {'c':4,'d':5}

Zip vai unir as chaves
list(zip(d1,d2))

Zip pode unir os valores (itens)
list(zip(d1, d2.values()))

Criando uma função para trocar valores entre 2 dicionários
def trocaValores(d1, d2):
    
    dicTemp = {}
    
    for d1key, d2val in zip(d1, d2.values()):
        dicTemp[d1key] = d2val
    
    return dicTemp

trocaValores(d1, d2)

## Enumerate

A função enumerate() em Python é uma função que permite iterar sobre uma estrutura de dados (como uma lista, tupla ou outro objeto iterável). A função enumerate() retorna um objeto enumerado, que pode ser usado em loops para percorrer a estrutura de dados e acessar o contador e o valor de cada elemento.

Criando uma lista
seq = ['a','b','c']

list(enumerate(seq))

Imprimindo os valores de uma lista com a função enumerate() e seus respectivos índices
for indice, valor in enumerate(seq):
    print (indice, valor)

for indice, valor in enumerate(seq):
    if indice >= 2:
        break
    else:
        print (valor)

lista = ['Marketing', 'Tecnologia', 'Business']

for i, item in enumerate(lista):
    print(i, item)

for i, item in enumerate(range(10)):
    print(i, item)

for i, item in enumerate('Data Science Academy'):
    print(i, item)        