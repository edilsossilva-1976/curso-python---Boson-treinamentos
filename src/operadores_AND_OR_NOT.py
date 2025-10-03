#Tabela verdade:AND
#+-------------+-------------+-----------+
#| Condição A  | Condição B  | Resultado |
#+-------------+-------------+-----------+
#|    False    |    False    |    False  |
#+-------------+-------------+-----------+
#|    True     |    False    |    False  |
#+-------------+-------------+-----------+
#|    False    |    True     |    False  |
#+-------------+-------------+-----------+
#|    True     |    True     |    True   |
#+-------------+-------------+-----------+

#Tabela verdade:OR
#+-------------+-------------+-----------+
#| Condição A  | Condição B  | Resultado |
#+-------------+-------------+-----------+
#|    False    |    False    |    False  |
#+-------------+-------------+-----------+
#|    True     |    False    |    True   |
#+-------------+-------------+-----------+
#|    False    |    True     |    True   |
#+-------------+-------------+-----------+
#|    True     |    True     |    True   |
#+-------------+-------------+-----------+

#Tabela verdade:NOT
#+----------+---------+
#| Entrada  | Saída   |
#+----------+---------+
#|  False   |  True   |
#+----------+---------+
#|   True   |  False  |
#+----------+---------+

idade = 25
altura = 1.75

resultado = (idade >= 18) and (altura >= 1.70)
msg = "Pode participar do evento? " + str(resultado)
print(msg)

#Programa de disparo de alarme:
print()
porta ='a'
janela = 'f'
alarme = (porta =='a') or (janela == 'a')
msg = "Alarme disparado? " + str(alarme)
print(msg)

print()
tem_dinheiro = False
tem_dinheiro = not tem_dinheiro

msg = 'Tem dinheiro? ' + str(tem_dinheiro)
print(msg)

