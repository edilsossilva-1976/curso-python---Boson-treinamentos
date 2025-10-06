# import generico, importa todo modulo math
import math 
print(math.sqrt(81))


# importar somente a funcionalidade sqrt
from math import sqrt, sin
print(sqrt(81))


# importar universal (mesmo efeito do generico)
from math import * 
print(sqrt(81))

# importar modulos usando alias
import math as m
print(m.sqrt(81))

import saida_de_dados as sd

if __name__ == '__main__':
    sd.divisao

