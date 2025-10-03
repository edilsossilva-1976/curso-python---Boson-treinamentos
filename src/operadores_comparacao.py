a = 5
b = 5
print(f"a == b: {a == b}")
print(f"a != b: {a != b}")
print(f"a * 2 >= b: {a * 2 >= b}")
print(f"a != b: {a != b}")

x = y = z = False
n1 = n2 = 0
print("Digite um numero:")
n1 = int(input())
n2 = int(input("Digite outro numero: "))

x = n1 == n2
print('Sao iguais? ', x, '\n')

z = n1 > n2
print(f'{n1} é maior que {n2}? {z} ')

y = n1 != n2
print(f'{n1} é diferente de {n2}? {str(y)} ')