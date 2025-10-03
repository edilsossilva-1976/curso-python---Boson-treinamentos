#SINTAXE:
#print(obetos, argumentos)

mensagem = "função print()"
print(mensagem)
print('Aula de python')#texto direto

nome = 'Edilson Silva'
idade = 48
canal = 'Boson treinamentos'
print(canal, "-", nome)

nome2 = input("Digite o seu nome: ")
msg = "Olá " + nome2 + ", Bem vindo ao curso de Python"
print(msg)

print()
print("Imprime a mensagem e muda de linha")
print("Imprime a mensagem e permanece na linha", end="")
print(" \'Continuo na mesma linha\'")
print()
print("O nome dele é {0} e ele tem {1} anos".format(nome, idade))
print(f"O nome dele é {nome} e ele tem {idade} anos")#mais facil e eficiente

print()
num1 = 10
num2 = 5
soma = f"A soma de {num1} + {num2} = {num1 + num2}"
subtracao = f"A subtração de {num1} - {num2} = {num1 - num2}"
multiplicacao = f"A multiplicacao de {num1} x {num2} = {num1 * num2}"
divisao = f"A divisão de {num1} / {num2} = {float(num1 + num2):.2f}"
resto = f"O resto da divisão de {num1} mod {num2} = {(num1 % num2)}"
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Resto da divisao (%): {resto}\n")