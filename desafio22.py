# Crie um programa que leia o nome completo de uma pessoa e mostre:
#  O nome com todas as letras maiúsculas.
#  O nome com todas minúsculas.
#  Quantas letras ao todos (sem considerar espaços)
#  Quantas letras tem o primeiro nome.

#minha resolução do problema
"""nome = str(input('Escreva um nome completo:'))
print(nome.upper())
print(nome.lower())
#print(nome.title())
nome1 = nome.split()
n = len(nome1)
if (n==2):
    print('Aotodo tem {} letras o nome '.format(len(nome)-1))
elif(n==3):
    print('Aotodo tem {} letras o nome '.format(len(nome)-2))
elif(n==4):
    print('Aotodo tem {} letras o nome '.format(len(nome)-3))
elif(n==5):
    print('Aotodo tem {} letras o nome '.format(len(nome)-4))
else:
    print('Aotodo tem {} letras o nome '.format(len(nome)))
print('O primeiro nome tem {} letras.'.format(len(nome1[0])))
"""
# resolução do Professor
nome = str(input('Digite seu nome completo: '))
nome1 = nome.split()
print("Analisando seu nome...")
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras.'.format(nome.find('   ')))
print('O primeiro nome tem {} letras.'.format(len(nome1[0])))



