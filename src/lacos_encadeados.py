'''
for cont_ex in range(1,6):
    print(f"\nRodada: {cont_ex}")
    for cont_in in range(5, 0, -1):
        print(f"\n\tValor: {cont_in}")
        
print("fim dos laços")
'''

import random
for A in range(1,6):
    print(f"\nConjunto {A}")
    for B in range(6):
        num = random.randint(1,100)
        print(f" Valor: {num}")
