# Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) 
# e depois faça uma chamada à função para listar os números    

lista_pares = []
def pares():
    for x in range(1, 20):
        if x % 2 == 0:
            lista_pares.append(x) 
            print(x)
    listar(lista_pares)
    
def listar(lista_pares):
    print(lista_pares)

pares()

# Exercício 2 - Crie uam função que receba uma string como argumento e retorne a mesma string em letras maiúsculas.
# Faça uma chamada à função, passando como parâmetro uma string

def maiusculas(texto): return texto.upper()

print(maiusculas("ola mundo"))

# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e 
# imprima a lista
lista = [1, 2, 3, 4]

def outraLista(lista):
    lista.extend([2, 3])
    return print(lista)

outraLista(lista)

# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos. Faça duas chamadas 
# à função, com apenas 1 elemento e na segunda chamada com 4 elementos
def treinando(arg1, *vartuple):
    print(arg1)
    for x in vartuple:
            print ("O parâmetro passado foi: ", x)
    return

treinando('Primeiro', 2)
print("")
treinando('Segunda', [3, 4, 5, 6])

# Exercício 5 - Crie uma função anônima e atribua seu retorno a uma variável chamada soma. A expressão vai receber 2 
# números como parâmetro e retornar a soma deles
soma = lambda a, b: a+b
print(soma(2,2))

# Exercício 6 - Execute o código abaixo e certifique-se que compreende a diferença entre variável global e local
total = 0
def soma( arg1, arg2 ):
    total = arg1 + arg2; 
    print ("Dentro da função o total é: ", total)
    return total


soma( 10, 20 )
print ("Fora da função o total é: ", total)

# Exercício 7 - Abaixo você encontra uma lista com temperaturas em graus Celsius
# Crie uma função anônima que converta cada temperatura para Fahrenheit
# Dica: para conseguir realizar este exercício, você deve criar sua função lambda, dentro de uma função 
# (que será estudada no próximo capítulo). Isso permite aplicar sua função a cada elemento da lista
# Como descobrir a fórmula matemática que converte de Celsius para Fahrenheit? Pesquise!!!
Celsius = [39.2, 36.5, 37.3, 37.8]
help(map)
Fahrenheit = map(lambda x: float((9)/5)+32, Celsius)
print (list(Fahrenheit))

# Exercício 8 - Crie uma list comprehension que imprima o quadrado dos números de 1 a 10
lista = [x**2 for x in range(1,11)]
print(lista)

# Exercício 9 - Crie uma list comprehension que imprima as palavras com a letra a no nome
palavras = ["maça", "coiote", "banana", "terreno", "Python"]
lista = [x for x in palavras if 'a' in x]
print(lista)

# Exercício 10 - Crie uma list comprehension que imprima os números menores que 5 em um intervalo de 1 a 10
lista = [x for x in range(1,10) if x < 5]
print(lista)