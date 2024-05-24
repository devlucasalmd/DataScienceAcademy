# Introdução à Programação Orientada a Objetos

Classes
Em Programação Orientada a Objetos (POO), uma classe é uma estrutura que descreve um objeto, especificando os atributos e comportamentos que o objeto deve ter. Uma classe é uma espécie de modelo que define as características e ações que um objeto deve possuir.

As classes são usadas para criar objetos, que são instâncias da classe. Cada objeto criado a partir da mesma classe terá os mesmos atributos e comportamentos.

Para criar uma classe em Python, utiliza-se a palavra reservada class.

O nome da classe segue a mesma convenção de nomes para criação de funções e variáveis em Python, mas normalmente se usa a primeira letra maiúscula em cada palavra no nome da classe.

**Criando uma classe chamada Livro**
class Livro():
    
    # __init__ CONSTRUTOR - vai inicializar cada objeto criado a partir desta classe
    # (self) é uma referência a cada atributo da própria classe (e não de uma classe mãe, por exemplo)
    def __init__(self):
        
        # Atributos são propriedades 
        self.titulo = 'Sapiens - Uma Breve História da Humanidade'
        self.isbn = 9988888
        print("Construtor chamado para criar um objeto desta classe.")
        
    # Métodos são funções que executam ações nos objetos da classe
    def imprime(self):
        print("Foi criado o livro %s com ISBN %d" %(self.titulo, self.isbn))

Criando a classe Livro com parâmetros no método construtor
class Livro():
    
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
        print("Construtor chamado para criar um objeto desta classe.")
        
    def imprime(self, titulo, isbn):
        print("Este é o livro %s e ISBN %d" %(titulo, isbn))

Criando o objeto Livro2 que é uma instância da classe Livro
Livro2 = Livro("O Poder do Hábito", 77886611)


## Objetos
**Em Python, Tudo é Objeto!**

print(type([]))
print(type(10))
print(type([]))
print(type(()))
print(type({}))
print(type('a'))

**Usando atributos**
hasattr(Func1, "nome") - has attributes(obj, name)
setattr(Func1, "salario", 4500) - set attribute
hasattr(Func1, "salario")
getattr(Func1, "salario") - get attribute
delattr(Func1, "salario") - del attribute


## Métodos

os métodos de classes são funções definidas dentro de uma classe, que realizam operações específicas em objetos criados a partir dessa classe. Os métodos de classes são usados para implementar o comportamento dos objetos que pertencem a essa classe.

métodos de classes sempre incluem o parâmetro self como o primeiro argumento, que é usado para se referir ao objeto atual da classe.

O método **init** é um método especial que é chamado quando um objeto é criado a partir da classe. Este método é usado para inicializar os atributos do objeto.

Criando uma classe chamada Circulo
class Circulo():
    
    # O valor de pi é constante
    pi = 3.14

    # Quando um objeto desta classe for criado, este método será executado e o valor default do raio será 5.
    def __init__(self, raio = 5):
        self.raio = raio 

    # Esse método calcula a área. 
    def area(self):
        return (self.raio * self.raio) * Circulo.pi

    # Método para gerar um novo raio
    def setRaio(self, novo_raio):
        self.raio = novo_raio

    # Método para obter o raio do círculo
    def getRaio(self):
        return self.raio


circ = Circulo()
circ.getRaio()
circ1 = Circulo(7)
circ1.getRaio()
print ('O raio é:', circ.getRaio())
print('Área igual a:', circ.area())
circ.setRaio(3)
print ('Novo raio igual a:', circ.getRaio())