## Capítulo 4 - Exercícios

### Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n)


### Exercício 2 - Crie uma lista de 5 objetos e imprima na tela
obj = ['Faca', 'Garfo', 'Colher', 'Prato', 'Copo']
print(obj)

### Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
nome = "Michael"
sobrenome = "Jackson"
nomeInteiro = nome + " " + sobrenome
print(nomeInteiro)

### Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do objeto tupla para verificar quantas vezes o número 4 aparece na tupla

t1 = (1, 2, 2, 3, 4, 4, 4, 5)
t1.count(4)

### Exercício 5 - Crie um dicionário vazio e imprima na tela
di = {}
di = dict()
print(di)

### Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
frutas = {0: 'laranja', 1: 'morango', 2: 'banana'}
print(frutas)

### Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
frutas[3] = 'uva'

### Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos. Imprima o dicionário na tela.
num = {'pares': [2, 4, 6], 'impares': [1,3,5], 'numeros': [10,11,12,13]}
print(num)

### Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e o quarto elemento um valor do tipo float. Imprima a lista.

list1 = ['Papel', (2,3),{'homem': 'aranha', 'capitao': 'america'}, 3.14]
print(list1)
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])

### Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'

print(frase[1:19])
print(frase[0:18])