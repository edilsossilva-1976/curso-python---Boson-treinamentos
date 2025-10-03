#Desvios condicionais
#Simples, composto e encadeado

n1 = n2 = 0
media = 0.0
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

#calcular a media aritmetica
media = (n1 + n2) / 2.0

if (media >= 7):
    print("Aluno aprovado!\n Parabéns.")
elif (media >= 5):
    print("Aluno de recuperação!\n Boa sorte.")
else:
    print("Aluno reprovado.\nVai estudar miserável!")

    
print("Sua média é {}".format(media))
print(f"Sua média é {media}")
