# Trabalhando com Polimorfismo de Classes em Python

O polimorfismo permite que objetos de diferentes classes possam ser tratados de forma uniforme. Isso significa que um objeto pode ser tratado como se fosse um objeto de uma superclasse, mesmo que ele seja de uma subclasse.

Com o Polimorfismo, os mesmos atributos e métodos podem ser utilizados em objetos distintos, porém, com implementações lógicas diferentes.


Superclasse
class Veiculo:
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        pass

    def frear(self):
        pass

Subclasse
class Carro(Veiculo):
    
    def acelerar(self):
        print("O carro está acelerando.")

    def frear(self):
        print("O carro está freando.")


Subclasse
class Moto(Veiculo):
    
    def acelerar(self):
        print("A moto está acelerando.")

    def frear(self):
        print("A moto está freando.")


Subclasse
class Aviao(Veiculo):
    
    def acelerar(self):
        print("O avião está acelerando.")

    def frear(self):
        print("O avião está freando.")

    def decolar(self):
        print("O avião está decolando.")


lista_veiculos = [Carro("Porsche", "911 Turbo"), Moto("Honda", "CB 1000R Black Edition"), Aviao("Boeing", "757")]

for item in lista_veiculos:
    
    # O método acelerar tem comportamento diferente dependendo do tipo de objeto
    item.acelerar()
    
    # O método frear tem comportamento diferente dependendo do tipo de objeto
    item.frear()

    # Executamos o método decolar somente se o o objeto for instância da classe Aviao
    if isinstance(item, Aviao):
        item.decolar()

    print("---")