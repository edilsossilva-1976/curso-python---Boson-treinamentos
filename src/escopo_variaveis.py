#Indica a visibilidade e acessibilidade de uma variavel dentro de um codigo

# Escopo Global e local

print()
var_global = "Curso completo de Python"

def escreve_texto():
    global var_global
    var_global = "Banco de dados com SQL"
    var_local = "Edilson Alves"
    print(f"Variavel Global: {var_global}")
    print(f"Variavel Local: {var_local}")
    
    
if __name__ == '__main__':
    print(f"Executar a função escreve_texto()")
    escreve_texto()

    print("\nTentar acessar as variaveis completamente.")
    print(f"Variavel Global: {var_global}")
    #print(f"Variavel Global: {var_local}") 
    # Linha nao executada, Variavel local não definida
    
    
