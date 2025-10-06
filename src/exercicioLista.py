bebidas = []
for i in range(5):
    print("Digite uma bebida favorita: ", end="")
    bebida = input()
    bebidas.append(bebida)
    
print(f"Bebidas escolhidas: {bebidas.sort()}")

for bebida in bebidas:
    print(f"Bebida: {bebida}")

print("Saúde!")