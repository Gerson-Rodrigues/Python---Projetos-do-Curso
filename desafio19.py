# Um professor quer sortear um dos seus quatro alunos para
# apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e
# escrevendo nome do escolhido
"""import random
print('Escolhendo um aluno... ')
n = random.randint(1, 4)
if (n == 1):
    print('O aluno escolhido foi o Ciro')
elif (n == 2):
    print('O aluno escolhido foi o Belmiro')
elif (n == 3):
    print('O aluno escolhido foi a Julia')
else:
    print('O aluno escolhido foi a Mônica')"""
# Acima foi minha resolução

# Abaixo a resolução do professor Guanabara
import random
print('Escolha um aluno destes citados!')
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
