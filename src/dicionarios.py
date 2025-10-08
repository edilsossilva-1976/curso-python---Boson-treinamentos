#armazenam dados em pares {chave (key), valor (value)}

elemento = {
    "z": 3,
    "nome":"litio",
    "grupo":"Metais alcalinos",
    "densidade": 0.543
}

print("ACESSAR ITENS DO DICIONARIO (chave)")
print(f"Elemento: {elemento["nome"]}")
print(f"Densidade: {elemento["densidade"]}")
print(f"Grupo: {elemento["grupo"]}")

print()
print("Nº de elementos de um dicionario")
print(f"O dicionario possui: {len(elemento)} elementos")

print()
print("Atualizar valores de um dicionario")
elemento["grupo"] = "Alcalinos"
print(f"Elemento: {elemento}")

print()
print("Adicionar entrada de um dicionario")
elemento["periodo"] = 1
print(f"Elemento: {elemento}")

'''print()
print("Exclusao de itens de um dicionario")
del elemento["periodo"]
print(f"Elemento: {elemento}")

print()
print("Exclusao de todos os itens de um dicionario")
elemento.clear()
print(f"Elemento: {elemento}")'''

print()
print("Retornar os itens de um dicionario")
print(f"Elemento: {elemento.items()}")

print()
print(f"Elemento: {elemento.keys()}")
print("Retornar as chaves de itens por linha")
for i in elemento.keys():
    print(i)
    
print()
print(f"Elemento: {elemento.values()}")
print("Retornar as valores de itens por linha")
for i in elemento.values():
    print(i)

print()
print("Retornando o dicionario em forma de relatorio")
for i, j in elemento.items():
    print(f"{i} : {j}")