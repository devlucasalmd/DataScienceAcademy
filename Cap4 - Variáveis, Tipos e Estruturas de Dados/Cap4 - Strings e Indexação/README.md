## Capítulo 4 - Strings e Indexação

### Criando uma String

'Oi'
'Criando uma string em Python'
"Podemos usar aspas duplas ou simples para strings em Python"
"Testando strings em 'Python'"

**Imprimindo uma String**
print ('Testando Strings em Python')
print ('Testando \n Strings \n em \n Python')

**Indexando Strings**

s = 'Data Science Academy'
> Indexação em Python começar por zero.
Primeiro elemento da string
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

print(s[:3])
print(s[:4])
print(s[-1])
print(s[:-1])
print(s[::1])
print(s[::2])
print(s[::-1])

**Propriedades de Strings**
Alterando um caracter (não é possível alterar um elemento da string)
s[0] = 'x'
Concatenando strings
s = s + ' é a melhor maneira de estar preparado para o mercado de trabalho em Ciência de Dados!'

Podemos usar o símbolo de multiplicação para criar repetição!
letra = 'w'
print(letra*3)

**Funções Built-in de Strings**
s.upper()
s.lower()
s.split()
s.split('y')

**Funções String**
s = 'seja bem vindo ao universo da Linguagem Python!'
s.capitalize()
s.count('a')
s.isalnum()
s.islower()
s.isspace()
s.endswith('o')

**Comparando Strings**
print("Python" == "R")
print("Python" == "Python")