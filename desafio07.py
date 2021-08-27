# Desenvolva um programa que leia as duas notas de um aluno,
# calcule e mostre a sua média.
not1 = float(input('Digite a nota 1: '))
not2 = float(input('Digite a nota 2: '))
média = (not1 + not2)/2
print('A média do aluno entre {} e {} será de {:.1f}'.format(not1, not2, média))
