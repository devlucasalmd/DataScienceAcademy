## Capítulo 6 - Pacotes e Módulos

Pacotes e Módulos
Em Python, um módulo é um arquivo (script) que contém código Python e pode ser importado em outros arquivos Python. Ele é usado para compartilhar funções, classes e variáveis entre arquivos.

Já um pacote é uma coleção de módulos organizados em uma estrutura de diretórios. Ele permite a divisão de um aplicativo em múltiplos módulos, o que facilita a manutenção e o desenvolvimento.

Visite o PyPi, repositório de pacotes da Linguagem Python: https://pypi.org/

Importando um pacote Python
import numpy

Verificando todos os métodos e atributos disponíveis no pacote
dir(numpy)

Usando um dos métodos do pacote Numpy
numpy.sqrt(25)

Importando apenas um dos métodos do pacote Numpy
from numpy import sqrt

Usando o método
sqrt(9)

Help do método sqrt do pacote Numpy
help(sqrt)

import random
random.choice(['Abacate', 'Banana', 'Laranja'])
random.sample(range(100), 10)

import statistics
dados = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
statistics.mean(dados)
statistics.median(dados)

import os
os.getcwd()
print(dir(os))

Importando o módulo request do pacote urllib, usado para trazer url's para dentro do nosso ambiente Python
import urllib.request
http://python.org

Variável resposta armazena o objeto de conexão à url passada como parâmetro
resposta = urllib.request.urlopen('http://python.org')

Objeto resposta
print(resposta)
Chamando o método read() do objeto resposta e armazenando o código html na variável html
html = resposta.read()
print(html)