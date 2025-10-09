from math import sqrt

#Exceção criada pelo usuario (personalizado)
class NumeroNegativoError(Exception):
    def __init__(self):
        pass # Esta linha diz: "Ignore e passe adiante..."

if __name__ == '__main__':
    try:
        num = int(input("Digite um numero positivo: "))
        if num < 0:
            raise NumeroNegativoError
        
    except NumeroNegativoError:
        print("Foi fornecido um numero negativo!.")
    else:
        print(f"A raiz quadrada de {num} é {sqrt(num)}")
    finally:
        print("Fim do cálculo.")
        
