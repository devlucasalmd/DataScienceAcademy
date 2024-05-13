## Capítulo 4 - Estruturas de Dados (Listas)

### Trabalhando com Listas
lista_1 = ["arroz, frango, tomate, leite"]
type(lista_1)
print(lista_1)

lista_2 = [23, 100, "Cientista de Dados"]
item1 = lista_2[0]
item2 = lista_2[1]
item3 = lista_2[2]
print(item1, item2, item3)

**Atualizando Um Item da Lista**
lista_1[2]
lista_1[2] = "chocolate"

**Deletando Um Item da Lista**
del lista_1[3]

### Listas de Listas (Listas Aninhadas)

**Listas de listas são matrizes em Python.**

listas = [ [1,2,3], [10,15,14], [10.1,8.7,2.3] ]

print(listas)

a = listas[0]
print(a)

b = a[0]
print(b)

list1 = listas[1]
print(list1)
valor_1_0 = list1[0]
valor_1_2 = list1[2]

**Operações com Listas**
listas = [[1,2,3], [10,15,14], [10.1,8.7,2.3]]
a = listas[0][0]
b = listas[1][2]
c = listas[0][2] + 10

**Concatenando Listas**
lista_s1 = [34, 32, 56]
lista_s2 = [21, 90, 51]
lista_total = lista_s1 + lista_s2

**Operador in**
lista_teste_op = [100, 2, -5, 3.4]
print(10 in lista_teste_op)
print(100 in lista_teste_op)

**Funções Built-in**
lista_numeros = [10, 20, 50, -3.4]
len(lista_numeros)
max(lista_numeros)
min(lista_numeros)

lista_formacoes_dsa = ["Analista de Dados", "Cientista de Dados", "Engenheiro de Dados"]
lista_formacoes_dsa.append("Engenheiro de IA")
lista_formacoes_dsa.append("Engenheiro de IA")
lista_formacoes_dsa.count("Engenheiro de IA")

Criando uma lista vazia
a = []
print(a)
type(a)
a.append(10)
a.append(50)
print(a)

Copiando os itens de uma lista para outra
old_list = [1,2,5,10]
new_list = []
for item in old_list:
    new_list.append(item)

print(new_list)

cidades = ['Recife', 'Manaus', 'Salvador']
cidades.extend(['Fortaleza', 'Palmas'])
print (cidades)
cidades.index('Salvador')
cidades.insert(2, 110)
cidades.remove(110)
cidades.reverse()

x = [3, 4, 2, 1]
x.sort()
