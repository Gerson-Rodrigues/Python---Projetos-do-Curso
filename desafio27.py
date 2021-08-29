# Faça um programa que leia o nome completo de uma pessoa, mostrando
# em seguida o primeiro e o último nome saparadamente.
#
# EX:. Ana Maria de Souza
# primeiro = Ana
# último = Souza#

# Minha resolução do desafio
"""nome = str(input('Escreva seu nome completo: ')).strip()
nome = nome.title()
nom = nome.split()
tot = len(nom)
pri_nom = nom[0]
ult_nom = nom[tot-1]
print('O nome completo corrigido é {}, \n'
      'Primero nome: {} \n '
      'Último nome: {}'.format(nome, pri_nom, ult_nom))
"""

# Resolução do Professor Guanabara
n = str(input('Digite seu nome Completo: ')).strip()
nome = n.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
