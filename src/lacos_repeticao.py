#Ou laços de repetição(loop)

print("-----------------DO WHILE 1--------------------------------")
numero = 1
while(numero <= 10):
    print(numero)
    numero += 1
    
print("Laço encerrado...")
    
print("---------------------DO WHILE 2----------------------------")

nome = None
while True:
    print("Digite seu nome, ou x para parar:")
    nome = input()
    if nome == 'x' or nome == 'X':
        break
    print(f"Seja bem vindo, {nome}!")
    
print("Ate logo.")

print("----------------------FOR---------------------------")

lista = [2,6,9,4,0,12,3,7]
palavra = 'Boson'

for item in lista:
    print(item, end="\t")

print()

for letra in palavra:
    print(letra, end="\t")


print("\n---------------------RANGE 1----------------------------")

for numero in range(1, 11):
    print(numero, end='\t')
    

print("\n---------------------RANGE 2----------------------------")

for numero in range(10):
    print(numero, end='\t')

print("\n----------------------range 3 ---------------------------------")

nome = input("Digite o seu nome: ")
for x in range(10):
    print(f"{x + 1} - {nome}")

print("\n---range (valor inicial, valor final, incremento)----------------------")

for x in range(2, 20,2):
    print(x)


print("\n---range (valor inicial, valor final, incremento)- reverso---------------------")

for x in range(20, 2,-2):
    print(x)

print("\n-------------------------LISTAS----------------------------")

pedras = ('rubi','esmeralda', 'quartzo', 'safira', 'diamante', 'turmalina')

for pedra in pedras:
    if pedra == 'quartzo':
        continue
    print(pedra)

print("\n--------------------------------------------------------------------------")

