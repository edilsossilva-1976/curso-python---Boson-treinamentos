'''
Strings são cadeias de caracteres que permitem que se armazenem dados textuais
'''
nome = "Edilson"
letra = nome[2]
print()
print(f"letra na posição 2: {letra}")
print(f"Tamanho da String: {len(nome)}")
curso = "Curso de Pyton"
instrutor = nome
print()
print("CONCATENAÇÃO DE STRINGS")
print(curso + " com " + instrutor)

print("Separar uma lista de strings")
frase = "Vamos aprender Python hoje?"
palavras = frase.split()
print(palavras)
print()
print("Palavras isoladas:")
print(palavras[0])
print(palavras[1])
print(palavras[2])
print(palavras[3])
print()
print("Usando a função for:")
for palavra in palavras:
    print(palavra)
print()
print("Imprimir as letras da frase usando a função for com 1 letra por linha:")
for letra in frase:
    print(letra)
print()
print("Imprimir as letras da frase usando a função for com as letras tabuladas:")
for letra in frase:
    print(letra, end="\t")

print()
print("Fatiamento de palavras (slicing):")
print(f"frase[0:5] - {frase[0:5]}")
print(f"frase[6:15] - {frase[6:15]}")
print(f"frase[7:19] - {frase[7:19]}")
print(f"frase[-3:] - {frase[-3:]}")

'''
print()
print("Encontrar a posição de um caractere em uma string")
email = input("Digite o seu endereço de email: ")
arroba = email.find('@')
print(f"Posição do @: {arroba}")
print()
print("Separando usuario do dominio:")
usuario = email[0:arroba]
dominio = email[arroba+1:]
print(f"Usuario: {usuario}")
print(f"Dominio: {dominio}")
'''
print()
item = "hipoclorito"
pos = item.find("clor")
print(f"Posição de clor: {pos}")
pos = item.find("flu")
print(f"Posição de flu: {pos}")

print()
print("PROCURAR UM TERMO NA FRASE:")
produtos = "carbonato de sódio e óxido de zinco"
print(f"Existe sódio em produtos: {"sódio" in produtos}")
print(f"Existe magnésio em produtos: {"magnésio" in produtos}")
print(f"Nao existe magnésio em produtos: {"magnésio" not in produtos}")

print()
print("Mudando a caixa do texto")
objeto_celeste = "galaxia espiral M31"
frase = "NAO GRITE COMIGO!!"
print(f"Objeto celeste: {objeto_celeste}")
print(f"Caixa Alta: {objeto_celeste.upper()}")
print(f"Frase: {frase.lower()}")
print(f"Capitalizada: {objeto_celeste.capitalize()}")
print(f"1º letra cada palavra caixa alta: {objeto_celeste.title()}")

print()
print("Manipular itens da variaveis")
suplemento = "cloreto de magnésio"
n_suplemento = suplemento.replace("magnésio", "zinco")
print(suplemento + " por " + n_suplemento)

print()
print("ELIMINAR ESPAÇOS EM STRINGS")
frase = "     Ômega 3 é bom para a saude!      "
print(frase)
print(f"Eliminar espaços a direita: {frase.rstrip()}")
print(f"Eliminar espaços a esquerda: {frase.lstrip()}")
print(f"Eliminar espaços a esquerda e direita: {frase.strip()}")


print()
print("ALINHAMENTO EM STRINGS")
fruta = "Abacate"
print(fruta)
print(f"Alinhar justificado a direita: {fruta.rjust(20, "-")}")
print(f"Alinhar justificado a esquerda: {fruta.ljust(20, "-")}")
print(f"Centralizar string: {fruta.center(20, "-")}")

print()
print("PREFIXAÇÃO E SUFIXAÇÃO")
p = "Bóson Treinamentos"
print(f"O termo inicia com B?: {p.startswith("B")}")
print(f"O termo inicia com b?: {p.startswith("b")}")
print(f"O termo inicia com Bó?: {p.startswith("Bó")}")
print(f"O termo finaliza com s?: {p.endswith("s")}")
print(f"O termo finaliza com o?: {p.endswith("o")}")

print("DocStrings: texto explicativo")
texto = """
É uma  especie de documentação que podemos inserir dentro de um modulo,
função ou classe python, entre outros locais.
    Respeita deslocamento e é multilinhas.
"""
print(texto)