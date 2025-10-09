# TÓPICOS ADICIONAIS SOBRE FUNÇÕES:
#Funções lambdas (funções anonimas) - São funçoes que não tem nome e podem ser usadas no mesmo momento (sem definição previa).
#Sintaxe: 
#lambda argumentos: expressao

quadrado = lambda x: x ** 2
for i in range(1,11):
    print(quadrado(i), end=" ")

#Verificar numero par
print()
par = lambda x: x %2 == 0
print(f"O nº 8 é par: {par(8)}")
print(f"O nº 8 é par: {par(9)}")


#Converter Firenheit para Celsius
print()
f_c = lambda f: (f - 32) * 5/9
print(f"212 ºF convertido para Celsius: {f_c(212)}ºC")
print(f"32 ºF convertido para Celsius: {f_c(32)}ºC")


# Função "map()" - Função interna do python que permite aplicar outra função a cada elemento de um objeto iteravel.
#Retorna um objeto to tipo map contendo os resultados;
#Sintaxe:
# map(função, iteravel)

# Calculo de de multiplicação de itens de uma lista por 2.
num = [1,2,3,4,5,6,7,8]

multi = lambda x: x*2
dobro = list(map(lambda x: x*2, num))

print(f"Lista = [1, 2, 3, 4, 5, 6, 7, 8] * 2\n \t{dobro}")

print()
palavras = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação']
maiusculas = list(map(str.upper, palavras))
print(f"Maiusculas: {maiusculas}")


# Função filter()
#Sintaxe:
# filter(função, sequencia)
print()
def numeros_pares(n):
    return n % 2 == 0

numeros = [1,2,3,4,5,6,7,8,9,10,11,12]
pares = list(filter(numeros_pares, numeros))
print(f"Numeros pares: {pares}")

#Exemplo utilizando lambda:
print()
def numeros_pares(n):
    return n % 2 == 0

numeros = [1,2,3,4,5,6,7,8,9,10,11,12]
pares = list(filter(numeros_pares, numeros))
impares = list(filter(lambda x:x%2 != 0, numeros))
print(f"Numeros pares  : {pares}")
print(f"Numeros impares: {impares}")


#Função reduce() - Realiza operações cumulativas em sequencias de elementos.  
# Sintaxe:
# reduce(funcao, sequencia, valor_inicial)

from functools import reduce

def mult(x,y):
    return x * y

numeros = [1,2,3,4,8,6]

total = reduce(mult, numeros)
print(f"6! = {total}")

#Soma cumulativa dos quadrados de valores usando expressão lambda
print()
numeros = [1,2,3,4,]
total = reduce(lambda x, y: x**2 + y**2, numeros)
print(f"TOTAL: {total}")

