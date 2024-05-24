import random
def inicio():
    print("Bem vindo ao jogo da forca: ")
    print("Adivinhe a palavra abaixo: ")


def jogo():
    inicio()
    lista_words = ["joelho", "abacate", "natureza", "palavra", "noventa"]
    
    word = random.choice(lista_words)
    
    tentativas = len(word) + 2

    word_descobertas = ['_' for letter in word]

    word_error = []

    while tentativas > 0: 
        print(" ".join(word_descobertas))
        print("\nChances restante:", tentativas)
        print("\nLetras erradas:", " ".join(word_error))
        letra = input("\nDigite uma letra: ").lower()
        if letra in word:
            i = 0
            for letter in word:
                if letra == letter:
                    word_descobertas[i] = letra
                i+=1
        else:
            tentativas-=1
            word_error.append(letra)

        if "_" not in word_descobertas:
            print("Você venceu!!!")
            break

    if "_" in word_descobertas:
            print("Você Perdeu, Tente novamente!")


if __name__ == "__main__":    
    jogo()
    