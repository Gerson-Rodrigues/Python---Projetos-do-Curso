# o mesmo professor do desafio anterior quer sortear a ordem
# de apresentação de trabalhos dos alunos. Faça um programa
# que leia o nome e mostre a ordem sorteada.
import random
print('Escolha os alunos que irão apresentar para por em uma ordem: ')
n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do terceiro aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem escolhida para apresentação foi \n{}'.format(lista))
