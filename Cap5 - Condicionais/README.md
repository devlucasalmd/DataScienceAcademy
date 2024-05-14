## Capítulo 5 - Condicionais

### Condicional If

Condicional If (Se)
if 5 > 2:
    print("A sentença é verdadeira!")

Condicional If...Else
if 5 < 2:
    print("A sentença é verdadeira!")
else:
    print("A sentença é falsa!")

Condicional If...Else com variável
dia = "Terça"
if dia == "Segunda":
    print("Hoje fará sol!")
else:
    print("Hoje vai chover!")    

Podemos usar o operador elif para validar mais de uma condição
if dia == "Segunda":
    print("Hoje fará sol!")
elif dia == "Terça":
    print("Hoje vai chover!")
else:
    print("Sem previsão do tempo para o dia selecionado")   

**Operadores Relacionais**

Retorna um valor booleano.
6 > 3
4 < 8
4 >= 4
7 <= 9
5 == 5

Atenção com a sintaxe
--> Fique atento aos espaços entre a margem e cada um dos seus comandos. Falaremos mais sobre indentação ao longo do curso. A indentação faz parte da sintaxe da linguagem Python.

if 5 == 5:
    print("Testando Python!")

if True:
    print('Parece que Python funciona!')


if 4 > 3
    print("Tudo funciona!")


**Condicionais Aninhados**
idade = 18
if idade > 17:
    print("Você pode dirigir!")

Nome = "Bob"
if idade > 13:
    if Nome == "Bob":
        print("Ok Bob, você está autorizado a entrar!")
    else:
        print("Desculpe, mas você não pode entrar!")

idade = 13
Nome = "Bob"
if idade >= 13 and Nome == "Bob":
    print("Ok Bob, você está autorizado a entrar!")

**Operadores Lógicos**
Operador and - Retorna True se ambas as declarações forem verdadeiras.
Operador or - Retorna True se uma das declarações for verdadeira.
Operador not - Inverte o resultado, retorna False se o resultado for True.

**Operador and**
numero = 4

if (numero > 5) and (numero % 2 == 0):
    print("Isso está sendo impresso porque as duas condições são verdadeiras!")
else:
    print("Isso está sendo impresso porque uma das duas condições é falsa!")

**Operador or**
numero = 4

if (numero > 5) or (numero % 2 == 0):
    print("Isso está sendo impresso porque uma duas condições é verdadeira!")    


**Operador not**
numero = 4

if not(numero > 5) and (numero % 2 == 0):
    print("Isso está sendo impresso porque as duas condições são verdadeiras!")
else:
    print("Isso está sendo impresso porque uma das duas condições é falsa!")

**Operador and, or e not**
numero = 4

if (not(numero > 5) and (numero % 2 == 0)) or (numero == 4):
    print("Isso está sendo impresso porque as duas primeiras condições são verdadeiras ou a terceira é verdadeira!") 


**Usando mais de uma condição na cláusula if e introduzindo Placeholders**
disciplina = 'Data Science'
nota_final = 90
semestre = 2

if disciplina == 'Data Science' and nota_final >= 80 and semestre != 1:
    print('Você foi aprovado em %s com média final %r!' %(disciplina, nota_final))
else:
    print('Lamento, acho que você precisa estudar mais!')       