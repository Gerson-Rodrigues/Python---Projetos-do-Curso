# Crie um programa que leia o nome de uma pessoa e diga se ela tem
# "Silva" no nome#

# Minha resolução
"""nome = str(input('Digite seu nome Completo: '))
nome = nome.title()
teste = 'Silva' in nome
if (teste == True):
    print('Achei o nome Silva')
else:
    print('Não achei o nome Silva')"""

# Resolução do professor Guanabara
nome = str(input('Qual seu nome completo? ')).strip()
nome = nome.title()
print('Seu nome tem Silva? {}'.format('Silva' in nome))
