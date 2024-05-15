## Capítulo 5 - Funções

print('Hello World')

Definindo uma função
def primeiraFunc():
    print('Hello World')

primeiraFunc()

def primeiraFunc():
    nome = 'Bob'
    print('Hello %s' %(nome))

primeiraFunc()


Definindo uma função com parâmetro
def segundaFunc(nome):
    print('Hello %s' %(nome))

segundaFunc('Aluno')
Erro -> segundaFunc()

Função para somar números
def addNum(firstnum, secondnum):
    print("Primeiro número: " + str(firstnum))
    print("Segundo número: " + str(secondnum))
    print("Soma: ", firstnum + secondnum)

addNum(4, 7)    
addNum(45, 3)


Funções com número variável de argumentos
def printVarInfo( arg1, *vartuple ):
    
    Imprimindo o valor do primeiro argumento
    print ("O parâmetro passado foi: ", arg1)
   
    Imprimindo o valor do segundo argumento 
    for item in vartuple:
        print ("O parâmetro passado foi: ", item)
    return;

Fazendo chamada à função usando apenas 1 argumento
printVarInfo(10)    
printVarInfo('Chocolate', 'Morango')


Escopo de Variável  - Local e Global
---------------

Variável Global
var_global = 10  *Esta é uma variável global*

Função
def multiplica_numeros(num1, num2):
    var_global = num1 * num2  *Esta é uma variável local*
    print(var_global)


Função
def multiplica_numeros(num1, num2):
    var_local = num1 * num2  *Esta é uma variável local*
    print(var_global)


print(var_local)
print(var_global)


**Funções Built-in**
abs(-56)
abs(23)
bool(0)
int(4.3)

Erro ao executar por causa da conversão
idade = input("Digite sua idade: ")
if idade > 13:
    print("Você pode acessar Redes Sociais sem supervisão!")  
else:
    print("Seus pais não deveriam você acessar Redes Sociais sem supervisão!")

Usando a função int para converter o valor digitado
idade = int(input("Digite sua idade: "))
if idade > 13:
    print("Você pode acessar Redes Sociais sem supervisão!")  
else:
    print("Seus pais não deveriam você acessar Redes Sociais sem supervisão!")  


**Criando Funções Usando Outras Funções**

caixa_baixa = "Este Texto Deveria Estar Todo Em LowerCase"

def lowercase(text):
    return text.lower()

lowercased_string = lowercase(caixa_baixa)

print(lowercased_string)

**Fazendo Split dos Dados**

Fazendo split dos dados
def split_string_palavras(text):
    return text.split(" ")

texto = "Esta função será bastante útil para separar grandes volumes de dados."

Isso divide a string em uma lista de palavras
print(split_string_palavras(texto))
Podemos atribuir o output de uma função para uma variável
token = split_string_palavras(texto)
print(token)

Fazendo split dos dados
def split_string_letras(text):
    texto = text.upper()
    for letra in texto:
        print(letra)

print(split_string_letras(texto))