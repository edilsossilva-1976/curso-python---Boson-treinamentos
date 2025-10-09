# Exceção é um objeto que representa um erro que ocorreu durante a execução do programa.
# blocos try ...except para tratar possiveis erros que podem ocorrer.

'''
* Exception - Classe base para todas as exceções
* ArithmeticError - Classe base para todos os erros que ocorrem em calculos numericos
* OverflowError - Um calculo excedeu o limite maximo de um tipo numerico
* ZeroDivisionError - Lançada quando uma divisão ou módulo por zero é executada em tipos numericos
* ImportError - Lançada quando uma declaraçao import falha
* NameError - Um identificador (nome) não foi encontrado no namespace local ou global
* IOError - Ocorre quando uma operação de E/S, como ler ou escrever em um arquivo, falha.
* IndentationError - A identação não foi aplicada corretamente
* RecursionError - O interpretador detectou que a profundidade maxima de recursao foi excedida
* TypeError - Lançada quando uma função ou operação é inválida para o tipo de dados especificado
'''

'''
    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite outro numero: '))

    try:
        r = round(n1 / n2, 2) #Arredonda a divisão e configura 2 casas decimais
    except ZeroDivisionError:
        print("Não é possível dividir por 0!")
    else:
        print(f"Resultado: {r}")
'''


print()
def div(k, j):
    return round(k / j, 2)

if __name__ == '__main__':
    while True:
        try:
           n1 = float(input('Digite um numero: '))
           n2 = float(input('Digite outro numero: ')) 
           break
        except ValueError:
            print("Ocorreu um erro ao ler o valor. Tente novamente.")
    
    try:
        r = div(n1, n2)
    except ZeroDivisionError:
        print("Não é possível dividir por 0!")
    except:
        print("Ocorreu um erro desconhecido!")
    else:
        print(f"Resultado: {r}")
    finally:
        print("\nFim do calculo.")