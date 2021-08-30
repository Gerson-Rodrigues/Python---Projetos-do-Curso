# Faça um programa que leia um ano qualquer e mostre se ele é Bissexto.#

#minha resolução do desafio
'''
ano = int(input('Digite um ano qualquer para recordar se ele é Bissexto ou não: '))
"""while ano < 1900 or ano > 2021:
    print('Ano Inválido: Na próxima tente outro ano acima de 1900 e abaixo de 2021!')
    ano = int(input('Digite outro ano....'))"""
if ano % 4 == 0:
    print('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {} NÃO é Bissexto'.format(ano))
'''

# Resolução do Professor Guanabara
from datetime import date
ano = int(input('Que ano quer analizar? Coloque 0 para analizar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÂO é BISSEXTO'.format(ano))

