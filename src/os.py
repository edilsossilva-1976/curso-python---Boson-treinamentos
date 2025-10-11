# Gerenciamento de pastas e arquivos do sistema
# Os scripts serao digitados no terminal (Powershell - Ctrl+shift+")
# Dentro do terminal digitar py para acessar o terminal python

'''
>>> import os --> Tarefas relacionadas a arquivo, diretorios, pastas, etc...
>>> os.name
'nt' --> Retorna o nome do Sistema Operacional(windows)
'posix' --> Retorna o nome do Sistema Operacional(linux)
>>> os.getcwd() --> (currene work directory - diretorio de trabalho atual)
'C:\\Python-Projetos'
>>> os.curdir --> Atalho para o diretorio atual
'.'
>>> os.listdir() --> Retorna uma lista com todo o conteudo do diretorio atual.
'['.git', 'src']'
>>> os.listdir('C:\\') --> Retorna uma lista com todo o conteudo de outro
diretorio.
'['$Recycle.Bin', 'Arquivos de Programas', 'Arquivos de Programas RFB',
'Config.Msi', 'Documents and Settings', 'DumpStack.log.tmp', 'edilson',
'hiberfil.sys', 'inetpub', 'Instala Impressoras', 'MS Office Setup',
'MSOCache', 'pagefile.sys', 'PerfLogs', 'Program Files', 'Program Files (x86)',
'ProgramData', 'Recovery', 'SGP4', 'SIGGO', 'SIGRH', 'swapfile.sys',
'System Volume Information', 'Temp', 'Users', 'Windows']'
>>> os.chdir('C:\\') --> Muda de diretorio. Pode usar caminho absoluto ou 
caminho relativo
>>> os.getcwd() --> diretorio atual
'C:\\'
>>> os.mkdir("teste") --> criar uma pasta no diretorio atual
>>> os.listdir()
'['.git', 'Novo diretorio', 'src']'
>>> os.chdir("Novo diretorio") --> acessar novo diretorio
>>> os.getcwd() --> retorna o diretorio atual
'C:\\Users\\alves.ferreira\\Desktop\\projects\\vs-workspace\\curso-python---
Boson-treinamentos\\Novo diretorio'
>>> os.getcwd()
'C:\\Users\\alves.ferreira\\Desktop\\projects\\vs-workspace\\curso-python---
Boson-treinamentos\\Novo diretorio'
'C:\\Users\\alves.ferreira\\Desktop\\projects\\vs-workspace\\curso-python---
Boson-treinamentos\\Novo diretorio'
>>> pasta_nova = "Teste2"
>>> pasta_nova = "Teste2"
>>> pasta_pai = "C:\\"
>>> pasta_pai = "C:\\"
>>> caminho_completo = os.path.join(pasta_pai, pasta_nova)
>>> print(caminho_completo)
C:\Teste2
>>> caminho_completo
'C:\\Teste2'
C:\Teste2
>>> caminho_completo
'C:\\Teste2'
>>> os.mkdir(caminho_completo)
>>> caminho_completo
'C:\\Teste2'
>>> os.mkdir(caminho_completo)
'C:\\Teste2'
>>> os.mkdir(caminho_completo)
>>> os.mkdir(caminho_completo)
>>> os.listdir("C:\\")
['$Recycle.Bin', 'Arquivos de Programas', 'Arquivos de Programas RFB',
'Config.Msi','Documents and Settings', 'DumpStack.log.tmp', 'edilson',
'hiberfil.sys', 'inetpub', 'Instala Impressoras', 'MS Office Setup',
'MSOCache', 'pagefile.sys', 'PerfLogs', 'Program Files', 'Program Files (x86)',
'ProgramData', 'Recovery', 'SGP4', 'SIGGO', 'SIGRH', 'swapfile.sys',
'System Volume Information', 'Temp', 'Teste2', 'Users', 'Windows']
>>> os.rename('C:\\Teste2', 'C:\\Teste10') --> renomeia pasta
>>> os.rmdir('C:\\Teste10') --> remover diretorio(pasta vazia)
>>> os.path.basename(os.getcwd()) --> retorna o nome do arquivo ou pasta 
a partir do caminho completo
'Teste'
>>> os.path.dirname(os.getcwd()) --> retorna o nome da pasta 
que contem o arquivo atual
'C:\\'

>>> pasta_pai = os.getcwd()
>>> novas_pastas = "America\\Brasil\\IlhaBela"
>>> caminho = os.path.join(pasta_pai, novas_pastas)
>>> print(caminho)
C:\Teste\Ameria\Brasil\IlhaBela
>>> os.makedirs(caminho) --> criar diretorio de forma recursiva
>>> os.path.exists('C:\\Teste\\Ameria') -->Existe este caminho?
True
>>> os.path.exists('C:\\Teste\\Asia') -->Existe este caminho?
False
>>> os.path.isdir('C:\\Teste') -->É diretorio?
True
>>> os.path.isfile('C:\\Teste') -->É um arquivo?
False
>>> manipulador = open('arq.txt', 'x')
>>> manipulador.close()
>>> os.listdir()
['arq.txt']
>>> arquivo = os.path.basename('C:\\Teste\\arq.txt')
>>> print(arquivo)
arq.txt
>>> os.path.splitext(arquivo)
('arq', '.txt')
>>> os.remove("arq.txt")
>>> os.listdir()
[]>>> import pathlib
>>> caminho = pathlib.Path()
>>> caminho.cwd()
WindowsPath('C:/Users/alves.ferreira/Desktop/projects/vs-workspace/
curso-python---Boson-treinamentos/Novo diretorio')
>>> import shutil
>>> shutil.rmtree("C:\\Teste10") --> remove uma arvore de diretorios 
(diretorio não vazio)

'''

# Script para renomear varios arquivos de um diretorio com um nome padrao.
import os
os.chdir("C:\\Teste")
print(f"Diretorio atual: {os.getcwd()}")

padrao_nome = input("Qual o padrao de nomes de arquivos a usar (sem extensao)")

for contador, arq in enumerate(os.listdir()):
    if os.path.isfile(arq):
        nome_arq, exten_arq = os.path.splitext(arq)
        nome_arq = padrao_nome + '' + str(contador)

        nome_novo = f"{nome_arq}{exten_arq}"
        os.rename(arq, nome_novo)


print("\nArquivos renomeados")
