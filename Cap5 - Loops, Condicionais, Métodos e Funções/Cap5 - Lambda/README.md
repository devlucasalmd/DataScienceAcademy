## Expressão Lambda

Definindo uma função - 3 linhas de código
def potencia(num):
    resultado = num ** 2
    return resultado

# Definindo uma função - 2 linhas de código
def potencia(num):
    return num ** 2

# Definindo uma função - 1 linha de código
def potencia(num): return num ** 2    

# Definindo uma expressão lambda (função anônima)
potencia = lambda num: num ** 2

- Normalmente não atribuimos lambda em uma variavel, mas sim no momento em que precisa executa-la. Ex: Elevar o número por 2 com alguma regra em uma linha do codigo.

operadores de comparação retornam boolean: true or false
Par = lambda x: x%2==0
Par(3)

first = lambda s: s[0]
first('Python')

reverso = lambda s: s[::-1]
reverso('Python')

addNum = lambda x,y : x+y
addNum(2,3)