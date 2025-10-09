# COMPREENSÃO DE LISTAS:

numeros = [1,4,7,9,10,12,21]
quadrados = list(map(lambda num: num**2, numeros))
print(f"Minha lista numeros: {numeros}")
print(f"Quadrado dos numeros: {quadrados}")

# List Comprehension
numeros = [1,4,7,9,10,12,21]
quadradosX = [num**2 for num in numeros] 
print(f"Quadrado dos numeros: {quadradosX}")


#Criar lista de numeros pares de 0 a 10
pares = [num for num in range(11) if num % 2 == 0]
print(f"Lista de pares: {pares}")

#Exemplos com textos (contar os numeros de vogais em um texto)
frase = "A lógica é apenas um princípio da sabedoria, e não o seu fim."
vogais = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]
lista_vogais = [v for v in frase if v in vogais]
print(f"A frase possui {len(lista_vogais)} vogais")


#Distributiva entre valores de duas listas
distributiva = [k * m for k in [2, 3, 5] for m in [10, 20, 30]]
print(f"Distributiva: {distributiva}")


