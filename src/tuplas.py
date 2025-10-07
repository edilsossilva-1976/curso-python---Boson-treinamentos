#Criação de uma tupla (lembrando que é imutavel)
tupla = (2,4,6,7,9)
print(f"Tupla: {tupla}")

#Não aceita modificar itens (imutavel)
#tupla[1]=5 //runtime error

halogenios = ('F', 'CL','BR', 'I', 'AT')
gases_nobres = ('HE', 'NE','AR', 'XE','KR','RN')
t1 = (5,2,6,8,4,4,5,6,4,0,12,22,3,4,5)

#Retornar tamanho da tupla:
print(f"Tamanho da tupla: {len(halogenios)}")

#Retornar um elemento em particular da tupla:
print(f"Elemento 3: {halogenios[3]}")

#Retornar ultimo item da tupla:
print(f"Ultimo Elemento: {halogenios[-1]}")

#Concatenar as tuplas:
elementos = halogenios + gases_nobres
print(f"Listas concatenadas: {elementos}")

#Contar elementos repetidos:
elementos = halogenios + gases_nobres
print(f"Quantos vezes repete o nº 5: {t1.count(5)}")
print(f"Quantos vezes repete o nº 3: {t1.count(3)}")

print("\nSlicing:")
print(f"halogenios[0:2]: {halogenios[0:2]}")
print(f"halogenios[:3]: {halogenios[:3]}")
print(f"halogenios[-2:]: {halogenios[-2:]}")


#Verificar a presença de um elemento na tupla:
print(f"Cloro (cl) está presente na lista: {'CL' in halogenios}")
print(f"Ferro (fe) está presente na lista: {'FE' in halogenios}")

#Soma de elementos de uma tupla:
print(f"Soma de elementos na lista: {sum(t1)}")
print(f"Valor minimo na lista: {min(t1)}")
print(f"Valor maximo na lista: {max(t1)}")

#Operações não disponiveis em tuplas: sort, append, reverse, pop...

#
for elemento in elementos:
    print(f"Elemento químico: {elemento}", end="\n")
    
grupo17 = list(halogenios)
grupo17[0] = 'H'
print(f"Grupo 17: {grupo17}")

#Criar uma tupla apartir de uma lista
grupo1 = ['LI', 'NA','K', 'RB', 'CS', 'FR']
alcalinos = tuple(grupo1)


print(f"Tupla criada: {alcalinos}")

