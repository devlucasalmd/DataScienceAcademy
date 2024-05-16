## Capítulo 6 - Tratamento de Erros e Exceções

Erros e Exceções

Sempre leia as mensagens de erro. Erros fazem parte do processo de aprendizagem e vão acompanhar você na sua jornada em programação, em qualquer linguagem.

### Try, Except, Finally

**Utilizando try e except**
try:
    8 + 's'
except TypeError:
    print("Operação não permitida")

**Utilizando try, except e else**
try:
    f = open('arquivos/testandoerros.txt','w')
    f.write('Gravando no arquivo')
except IOError:
    print ("Erro: arquivo não encontrado ou não pode ser salvo.")
else:
    print ("Conteúdo gravado com sucesso!")
    f.close()



try:
    f = open('arquivos/testandoerros','r')
except IOError:
    print ("Erro: arquivo não encontrado ou não pode ser lido.")
else:
    print ("Conteúdo gravado com sucesso!")
    f.close()


**Utilizando try, except, else e finally**
try:
    f = open('arquivos/testandoerros.txt','w')
    f.write('Gravando no arquivo')
except IOError:
    print ("Erro: arquivo não encontrado ou não pode ser salvo.")
else:
    print ("Conteúdo gravado com sucesso!")
    f.close()
finally:
    print ("Comandos no bloco finally são sempre executados!")    

> Cada possibilidade de erro deve ser tratada no seu programa.

def askint():
    try:
        val = int((input("Digite um número: ")))
    except:
        print ("Você não digitou um número!")
    finally:
        print ("Obrigado!")    

def askint():
        try:
            val = int(input("Digite um número: "))
        except:
            print ("Você não digitou um número!")
            val = int(input("Tente novamente. Digite um número: "))
        finally:
            print ("Obrigado!")
        print (val) 

def askint():
    while True:
        try:
            val = int(input("Digite um número: "))
        except:
            print ("Você não digitou um número!")
            continue
        else:
            print ("Obrigado por digitar um número!")
            break
        finally:
            print("Fim da execução!")
        print (val)                 