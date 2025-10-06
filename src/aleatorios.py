import random

'''
print("Gerar cinco numeros aleatorios entre 1 e 50: \n")
for i in range(5):
    n = random.randint(1,50)
    print(f"Numero gerado: {n}")
'''

#Gerar numero aleatorio arrendondado e com casas decimais
'''valor = random.random()
print(f"Numero gerado: {round(valor * 10, 2)}")'''

'''valor = random.uniform(1, 100)
print(f"Numero: {round(valor, 4)}")'''

L = [2,4,6,9,10,11,1,3,5,7,33]
'''n = random.choice(L)
print(f"Numero escolhido: {n}")'''

#Sortear n numeros de uma lista
'''n = random.sample(L, 3)
print(f"Numero escolhido: {n}")'''

#embaralhar elementos de uma lista
print(f"Exibir a lista original: {L}")
print(f"Embaralhar a lista e exibi-la:")
n = random.shuffle(L)
print(f"Lista embaralhada: {L}")

