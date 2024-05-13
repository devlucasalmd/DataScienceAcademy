## Capítulo 4 - Estruturas de Dados (Dicionários)
### Trabalhando com Dicionários

Isso é uma lista
estudantes_lst = ["Pedro", 24, "Ana", 22, "Ronaldo", 26, "Janaina", 25] 

Isso é um dicionário
estudantes_dict = {"Pedro":24, "Ana":22, "Ronaldo":26, "Janaina":25}

print(estudantes_dict["Pedro"])
estudantes_dict["Marcelo"] = 23
print(estudantes_dict)

estudantes_dict.clear()
del estudantes_dict

estudantes = {"Pedro":24, "Ana":22, "Ronaldo":26, "Janaina":25}

print(len(estudantes))
estudantes.keys()
estudantes.values()
estudantes.items()

estudantes2 = {"Camila":27, "Adriana":28, "Roberta":26}
estudantes.update(estudantes2)
print(estudantes)

dic1 = {}
dic1["chave_um"] = 2
print(dic1)
dic1[10] = 5
dic1[9.13] = "Python"
dic1["teste"] = 5
print(dic1)


dict1 = {}
dict1["teste"] = 10
dict1["key"] = "teste"
Atenção, pois chave e valor podem ser iguais, mas representam coisas diferentes.
print(dict1)

dict2 = {}
dict2["key1"] = "Data Science"
dict2["key2"] = 10
dict2["key3"] = 100
print(dict2)

a = dict2["key1"]
b = dict2["key2"]
c = dict2["key3"]
print(a, b, c)

Dicionário de listas
dict3 = {'chave1':1230, 'chave2':[22,453,73.4], 'chave3':['picanha', 'fraldinha', 'alcatra']}
print(dict3)

dict3['chave2']
Acessando um item da lista, dentro do dicionário
dict3['chave3'][0].upper()

Operações com itens da lista, dentro do dicionário
var1 = dict3['chave2'][0] - 2
print(var1)

### Criando Dicionários Aninhados
dict_aninhado = {'key1' {'key2_aninhada' {'key3_aninhada':'Dict aninhado em Python'}}}
print(dict_aninhado)
print(dict_aninhado['key1']['key2_aninhada']['key3_aninhada'])