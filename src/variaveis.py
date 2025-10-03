nome_usuario = 'Edilson'

print(nome_usuario) #imprime valor da variavel
print("Nome do usuário:", nome_usuario) #imprime com texto
print(f"Nome do usuário: {nome_usuario}")#imprime com texto formatado


media = 0
n1 = n2 = n3 = n4 = 0.0
nome, idade = 'Edilson', 48
estado = True

print(f"Nome: {nome}, Idade:{idade}")

#Função type()
print(type(media))
print(f"Tipo de dados media: {type(media)}")

print(type(n2))
print(f"Tipo de dados n's: {type(n1)}")

print(type(media))
print(f"Tipo de dados media: {type(media)}")

print(type(nome))
print(f"Tipo de dados nome: {type(nome)}")

print(type(idade))
print(f"Tipo de dados idade: {type(idade)}")

print(type(estado))
print(f"Tipo de dados estado: {type(estado)}")

print(type(1+2j))
print(f"Tipo de dados complexos: {type(1+2j)}")


#função isinstance()

print(isinstance(media, (int,float)))
