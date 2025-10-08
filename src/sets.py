#Sets são coleções não ordenadas de valore unicos
planeta_anao = {'Plutao', 'Ceres', 'Eris', 'Haumea', 'Makemake'}
print(f"Planetas anoes: {planeta_anao}")

print()
print(f"Nº de itens do set: {len(planeta_anao)}")
print()
print("Verificar existencia de itens do set:")
print(f"Ceres é parte do planeta anao: {"Ceres" in planeta_anao}")
print(f"Lua é parte do planeta anao: {"Lua" in planeta_anao}")
print(f"Lua não é parte do planeta anao: {"Lua" not in planeta_anao}")

print()
print("Iteração com sets em caixa alta")
for astro in planeta_anao:
    print(f"Astro: {astro.upper()}")
    
print()
print("Criar lista com SET")
astros = {'Lua', 'Venus', 'Sirius', 'Marte', 'Lua'}
print(f"astros: {astros}")
astro_set = set(astros)
print(f"Astros: {astro_set}")

print()
print("Comparações de conjunto")
astros1 = {'Lua', 'Venus', 'Sirius', 'Marte', 'Lua', 'Io'}
astros2 = {'Lua', 'Venus', 'Sirius', 'Marte', 'Lua', 'Cometa de Halley'}
print(f"Astros1 == Astros2: {astros1 == astros2}")
print(f"Astros1 != Astros2: {astros1 != astros2}")
print(f"União de conjuntos: {astros1 | astros2}")
print(f"União de conjuntos: {astros1.union(astros2)}")
print(f"Interseccao de conjuntos: {astros1 & astros2}")
print(f"Interseccao de conjuntos: {astros1.intersection(astros2)}")
print(f"Diferença simetrica: {astros1 & astros2}")
print(f"Diferença simetrica: {astros1.symmetric_difference(astros2)}")

print()
print("Adicionar elementos ao conjunto")
print(f"Add Urano ao astros1: {astros1.add("Urano")}")
print(f"Add Sol ao astros1: {astros1.add("Sol")}")
print(f"Astros1: {astros1}")

print()
print("remover elementos do conjunto")
print(f"Remove Io do astros1: {astros1.remove("Io")}")
#print(f"Tentando remover Io do astros1: {astros1.remove("Io")}")#Erro de chave
print(f"Usando discard Io do astros1: {astros1.discard("Sol")}")#Sem erro anterior
print(f"Astros1: {astros1}")

print()
print(f"Ordenando a lista: {sorted(astros1)}")

print()
print(f"Remoção aleatorio: {astros1.pop()}")
print(f"Astros1: {astros1}")

print()
print(f"Removendo todo o conjunto: {astros1.clear()}")
print(f"Astros1: {astros1}")