#Sao blocos de codigos que executam uma determinada tarefa.
#Vantagens: modularização, reuso do codigo, legibilidade

'''def function([argumentos]):
    <instruções>'''
    
def mensagem():
    print("Boson, treinamento em tecnologia.")
    print("Curso completo em Python.")
    
print()
mensagem()


#Função com argumentos:
def soma(a, b):
    print(f"{a} + {b} = {a+b}")

soma(5,2)

def mult(x, y):
    return x*y

'''a = 5
b = 8
c = mult(a,b)
print(f"{a} x {b} = {c}")

def div(k,j):
    if j != 0:
        return k / j
    else:
        return "Impossivel dividir por 0."

if __name__ == '__main__':
    a = int(input("Digite um numero: "))
    b = int(input("Digite outro numero: "))
    
    r = div(a,b)
    print(f"{a} / {b} = {r}")'''
    
    
'''print()
print("Calcular valores de quadrado")
def quadrado(val):
    quadrados = []
    for x in val:
        quadrados.append(x ** 2)
    return quadrados
        
if __name__ == '__main__':
    valores= [2,5,7,9,12]
    resultados = quadrado(valores)
    
    for g in resultados:
        print(g)
'''

print()
print("Executar contagem")
def contar(numero = 11, caractere = '+'):
    for i in range(1, numero):
        print(caractere)
    
if __name__ == '__main__':
    contar(numero = 7, caractere='<>')


x = 5
y = 6
z = 3

def soma_multi(a, b, c = 0):
    if c == 0:
        return a * b
    else:
        return a + b + c


if __name__ == '__main__':
    res = soma_multi(x,y, z)
    print(f"Soma_multi: {res}")


