# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!


def soma(a, b): return print(a+b)
def subtracao(a,b): return print(a-b)
def multiplicacao(a,b): return print(a*b)
def divisao(a,b): return print(a/b)



def menu():
    while True:
        print("\n******************* Calculadora em Python *******************")
        print("Selecione o número da operação desejada: ")
        print("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão")
        opcao = int(input("Digite sua opção (1/2/3/4) ")) 
        a = int(input("Digite o primeiro valor: "))
        b = int(input("Digite o segundo valor: "))
        if opcao == 1: soma(a, b)
        elif opcao == 2: subtracao(a, b)
        elif opcao == 3: multiplicacao(a, b)
        elif opcao == 4: divisao(a, b)
        else:
            print("Escolha uma operação valida")
        resp = str(input("Deseja sair?: (sim) ou (nao) "))
        if resp.upper() == "SIM": break
        else:
            continue

menu()        



                   