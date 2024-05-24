## Expressões Regulares

Expressões regulares são padrões usados para combinar ou encontrar ocorrências de sequências de caracteres em uma string. Em Python, expressões regulares são geralmente usadas para manipular strings e realizar tarefas como validação de entrada de dados, extração de informações de strings e substituição de texto.

import re
texto = "Meu e-mail é exemplo@gmail.com e você pode me contatar em outro_email@yahoo.com."

Expressão regular para contar quantas vezes o caracter arroba aparece no texto
resultado = len(re.findall("@", texto))

print("O caractere '@' apareceu", resultado, "vezes no texto.")

Expressão regular para extrair a palavra que aparece após a palavra "você" em um texto
resultado = re.findall(r'você (\w+)', texto)

print("A palavra após 'você' é:", resultado[0])

Expressão regular para extrair endereços de e-mail de uma string
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', texto)

print(emails)


text = "O aluno estava incrivelmente perdido, mas encontrou a DSA e rapidamente começou a aprender."

Extraindo os advérbios da frase
for m in re.finditer(r"\w+mente\b", text):
    print('%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))