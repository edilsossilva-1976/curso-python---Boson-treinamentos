
#Funções builtin (internas)
valores = [2,5,8,-1,0,11,7,-6]
print(f"Lista valores: {valores}\n")
print(f"Maior valor da lista: {max(valores)}")
print(f"Menor valor da lista: {min(valores)}")
a =-5
b = 4
print()
print(f"A = -5 e B = 4")
print(F"Valor absoluto de A: {abs(a)}")
print()
print(f"Potenciação - A elevado a B: {pow(a,b)}")


c = 2.789011
#Arredondamento (round)
print()
print("ARREDONDAMENTO: (round)\n")
print("Arredondar 2.789011 com 3 casas decimais:\n")
print(f"{round(c,3)}")

print()
import math 

x = 8 
y = 100
raiz_quadrada = math.sqrt(x)
print(f"Raiz Quadrada (para cima): {math.ceil(raiz_quadrada)}")
print(f"Raiz Quadrada (para baixo): {math.floor(raiz_quadrada)}")
print()
print("Logaritmo: (base 10)")
print(f"10logy = {math.log10(y)}")

print()
print("PI: (3.14...)")
print(f"PI = {math.pi}")

print()
print("FATORIAL:")
print(f"x! = {math.factorial(x)}")

print()
print("Numero Infinito:")
print(f"x:inf = {x / math.inf}")