# Crie um programa que leia um número inteiro e mostre na tela se ele é
# PAR ou ÍMPAR.#

#minha resolução do desafio
n = int(input('Digite um número qualquer: '))
if n % 2 == 0:
    print('O número {} é Par'.format(n))
else:
    print('O número {} é Ímpar'.format(n))


# resolução do Professor Guanabara
"""
número = int(input('Me diga um número qualquer: '))
resultado = número % 2
if resultado == 0:
    print('O número {} é PAR'.format(número))
else:
    print('O número {} é ÍMPAR'.format(número))

"""