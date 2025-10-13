# Manipulação de arquivos de textos
'''
# MODOS DE ACESSO A ARQUIVOS COM open()
+--------+-----------------------------------------------+
|  Modo  |      SIGNIFICADO                              |
+--------+-----------------------------------------------+
|  r     |      Somente leitura                          |
+--------+-----------------------------------------------+
|  r+    | Leitura e escrita. O texto é inseerido no     |
|        |   inicio do arquivo                           |
+--------+-----------------------------------------------+
|   w    | Escrita, apagando (truncando) o conteudo      |
|        |   existente do arquivo                        |
+--------+-----------------------------------------------+
|        | Leitura e Escrita, o arquivo é criado, se não |
|    w+  |   existir; se existir, é truncado. O texto é  |
|        |   inserido no inicio do arquivo               |
+--------+-----------------------------------------------+
|        | Escrita, preservando o conteudo existente     |
|        |  (append). O arquivo é criado, se nao existir |
|    a   |   existir; O texto é  inserido no final do    |
|        |   arquivo                                     |
+--------+-----------------------------------------------+
|    b   |      Modo binario                             |
+--------+-----------------------------------------------+
|    +   |      Atualização leitura/Escrita              |
+--------+-----------------------------------------------+
|    X   | Abre o arquivo para criação exclusiva,        |
|        |   falhando se o arquivo já existir            |
+--------+-----------------------------------------------+

# Podemos combinar os modos, por exemplo:
# r+, w+, w+b. O modo padrao é r (leitura), caso não seja especificado.
'''

'''print("Método read():\n")
print(manipulador.read())'''

'''print("Método readLine():\n")
print(manipulador.readline())
print(manipulador.readline())'''

'''print("Método readLines():\n")
print(manipulador.readlines())'''

'''texto = input("Qual termo deseja procurar no arquivo? ")
try:
    manipulador = open('C:\\Users\\alves.ferreira\\Documents\\arquivo2.txt',
                       'r', encoding='utf-8')
    for linha in manipulador:
        linha = linha.rstrip()
        if texto in linha:
            print("A String foi encontrada.")
            print(linha)
        else:
            print("A String não foi encontrada.")
except IOError:
    print("Não foi possivel abrir o arquivo.")
else:
    manipulador.close()
finally:
    print("Fim dos trabalhos.")'''

# Escrever em arquivos de texto
'''texto = "\nPython é usado em Ciencia de Dados Extensivamente."
try:
    manipulador = open('C:\\Users\\alves.ferreira\\Documents\\arquivo2.txt',
                       'a', encoding='utf-8')
    manipulador.write("\nPython é muito empregado em IA.")
    manipulador.write("\nInteligencia Artificial veio pra ficar. 
    DE NOVOVOVOVOVOV")
    manipulador.write(texto)
except IOError:
    print("Não foi possivel abrir o arquivo.")
else:
    manipulador.close()
finally:
    print("Fim dos trabalhos.")'''

# Criar e gravar o arquivo:
frutas = ['Morango\n', 'Uva\n', 'Caju\n', 'Amora\n', 'Framboesa\n', 'Graviola']
try:
    # manipulador = open('C:\\Users\\alves.ferreira\\Documents\\frutas.dat', 'w', encoding='utf-8')
    manipulador = open('frutas.dat', 'w', encoding='utf-8')
    manipulador.writelines(frutas)
except IOError:
    print("Não foi possivel abrir o arquivo.")
else:
    manipulador.close()
finally:
    print("Fim dos trabalhos.")
    

# Ler o arquivo criado:
try:
    manipulador = open('frutas.dat', 'r', encoding='utf-8')
    print(manipulador.read())
except IOError:
    print("Não foi possivel abrir o arquivo.")
else:
    manipulador.close()
finally:
    print("Fim dos trabalhos.")