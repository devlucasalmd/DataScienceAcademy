## Capítulo 5 - Exercícios Loops e Condiconais
 
### Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"
dia = str(input("Qual o dia da semana?"))
if dia == "Sabado" or "Domingo": print("Hoje é dia de descanso") 
else: print("Você precisa trabalhar!")

### Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista
lista_frutas = ['Uva', 'Melancia', 'Manga', 'Laranja', 'Morango']
nova_lista = [x for x in lista_frutas if 'Morango' in x]
print(nova_lista)

### Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma lista
numeros = (3, 5, 22, 9)
lista_dobro = [x*2 for x in numeros]
print(lista_dobro)

### Exercício 4 - Crie uma sequência de números pares entre 100 e 150 e imprima na tela
for x in range(100, 151, 2):
    print(x)

### Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. Enquanto temperatura for maior que 35, imprima as temperaturas na tel
temperatura = 40
while temperatura > 35:
    print(temperatura)
    temperatura -= 1 

### Exercício 6 - Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, imprima os valores na tela, mas quando for encontrado o valor 23, interrompa a execução do programa
contador = 0
while contador < 100:
    if contador == 23:
        break
    print(contador)
    contador += 1

### Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20, adicione à lista, apenas os valores pares e imprima a lista
lista_num = []
num = 4

while num <= 20:
    if num % 2 == 0:
        lista_num.append(num)
    num += 1

print(lista_num)

# numeros = list()
# i = 4
# while (i <= 20):
#     numeros.append(i)
#     i = i+2
# print(numeros)

### Exercício 8 - Transforme o resultado desta função range em uma lista: range(5, 45, 2)
lista_num = []
nums = range(5, 45, 2)
for x in nums:
    lista_num.append(x)

print(lista_num)

### Exercício 9 - Faça a correção dos erros no código abaixo e execute o programa. Dica: são 3 erros.
temperatura = float(input('Qual a temperatura? '))
if temperatura > 30:
    print('Vista roupas leves.')
else:
    print('Busque seus casacos.')

# Erro 1 - : no if
# Erro 2 - print desalinhado
# Erro 3 - : no else


### Exercício 10 - Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. Use um placeholder na sua instrução de impressão
frase = "A gratidão é a virtude das almas nobres. O quão feliz é uma pessoa depende da profundidade de sua gratidão." 
print(frase.count('r'))
