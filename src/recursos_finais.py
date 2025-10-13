# trocar valores entre variaveis (algoritmo)
var1 = 12
var2 = 31

'''
aux = var1
var1 = var2
var2 = aux
'''

# Em python, faça assim:

var1, var2 = var2, var1
print (f"Var1: {var1}, Var2: {var2}")

# Operador condicional Ternario
menor = var1 if var1 < var2 else var2
maior = var1 if var1 > var2 else var2

print(f"Menor: {menor}")
print(f"Maior: {maior}")

print(f"Maior valor: {(var1, var2)[var1 < var2]}")
print(f"Menor valor: {(var1, var2)[var1 > var2]}")


# Generators:
'''
É um tipo especial de objeto parecido com as Compreensoes de lista
Na sua sintaxe usa-se () ao inves de []. Nao retorna uma lista, mas
um objeto iteravel do tipo Generator.
'''
# Exemplo: Calcular o quadrado da lista abaixo:
print()
valores = [1, 3, 5, 7, 9, 11 ,13]
quadrados = (item**2 for item in valores)

for valor in quadrados:
    print(f"{valor}", end=", ")


# Função Enumerate()
''' 
Itera sobre elementos de uma sequencia qualquer (lista ou tupla) e retorna os
elementos e seus numeros de indices simultaneamente em formato de tuplas(indice, itens)
'''
#Exemplo:
print("\n")
bebidas = ['Cafe', 'Cha', 'Suco', 'Agua', 'Refrigerante']
for indice, item in enumerate(bebidas):
    print(f"{indice + 1}: {item}")

print()
temperaturas = [-1, 10, 5, -3, 8, 4, -2, -5, -7]
total = 0
for i, t in enumerate(temperaturas):
    if t < 0:
        total += 1
        print(f"A temperatura em indice:{i} é negativa com {t}ºC")

print(f"Total de temperaturas abaixo de 0: {total}")


# Gereanciamento de contexto com a palavra chave with

print()
try:
    a = open('/home/edilsonsilva/devel/curso-python---Boson-treinamentos/src/frutas.dat', 'r', encoding='utf-8')
    print(a.read())
except IOError:
    print("Não foi possivel abrir o arquivo")
else:
    a.close()


print("----------------------------------------------------")
print()

with open('/home/edilsonsilva/devel/curso-python---Boson-treinamentos/src/frutas.dat', 'r', encoding='utf-8') as listaDeFrutas:
    for linha in listaDeFrutas:
        print(linha, end="")





