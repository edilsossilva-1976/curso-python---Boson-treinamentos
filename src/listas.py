# Lista: representa uma sequencia de valores
# Sintaxe: nome_lista = [valores]
'''notas = [5,7,8,6,9]
print(notas)
'''

n1 = [4,6,7,8,0,3]
n2 = [1,6,3,0,12,11]
valores = n1 + n2
print(f"Lista n1: {n1}")
print(f"Lista n2: {n2}")

print(f"Lista concatenada: {valores}") #concatena as duas listas anteriores
print(f"Tipo de valor: {type(valores)}") # retorna o tipo de dados
print(f"Posição 6: {valores[6]}") # = 1 retorna o valor do indice informado

#Os valores negativos invertem a busca dos itens
print(f"Valor do ultimo item: {valores[-1]}")  # = 11 retorna o valor do ultimo item da lista
print(f"Valor do segundo item: {valores[-2]}")  #= 12 retorna o valor do penultimo item da lista

#substituir o valor no indice informado
valores[0] = 9 
print(f"Valor atualizado no indice 0: {valores[0]}")

#Slicing
#Imprime os valores de a partir do indice 0, 2 valores posteriores (9,6);
print(f"Slicing[0:2]: {valores[0:2]}")

#Imprime os valores a partir do indice 0, e todos os itens posteriores
print(f"Slicing[0:]: {valores[0:]}")

#Imprime os valores do inicio da lista até a quantidade informada
print(f"Slicing[:4]: {valores[:4]}")

#Imprime o tamanho da lista (elementos)
print(f"Tamanho da lista: {len(valores)}")

#Imprime uma versao ordenada da lista
print(f"Lista ordenada: {sorted(valores)}")

#Imprime uma versao ordenada da lista em ordem inversa
print(f"Lista ordenada reversa: {sorted(valores, reverse=True)}")

#Imprime a soma de todos os valores da lista
print(f"Soma dos itens: {sum(valores)}")

#Imprime o valor minimo e maximo da lista
print(f"Item minimo: {min(valores)}")
print(f"Item maximo: {max(valores)}")

#Inserir novo elemento no final da lista:
valores.append(13)
print(f"Lista: {valores}")

#Tirar um elemento da lista:
valores.pop() #Sem especificar, será removido o ultimo elemento.
print(f"Lista: {valores}")

#Tirar um elemento da lista na posição especificada:
valores.pop(3) #Sem especificar, será removido o ultimo elemento.
print(f"Lista: {valores}")

#Inserir um elemento na posição especifica:
#Sintaxe: valores.insert(posicao, valor)
valores.insert(3, 21)
print(f"Lista: {valores}")

#Verificar se um valor existe na lista:
print(f"A lista contem o valor 12: {12 in valores}")#true
print(f"A lista contem o valor 17: {17 in valores}")#false

#Combinar listas com laço for:
print("\nCombinar listas com laço for:")

#planetas = [] #Lista vazia
#planetas = list() #Tambem cria uma Lista vazia

planetas = ['Mercurio', 'Vênus', 'Marte', 'Saturno', 'Urano', 'Netuno']

for planeta in planetas:
    print(planeta)





