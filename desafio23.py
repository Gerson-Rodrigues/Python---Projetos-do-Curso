# Faça um programa que leia um numero de 0 a 9999 e mostre na
# tela cada um dos digitos separados.
# ex:. Digite um numero: 1834
# unidade: 4
# dezenas 3
# centena: 8
# milhar: 1

#minha resolução do problema
"""n = input('Escreva um numero de 0 à 9999')
t = len(n)
if(t==4):
    print('unidade: ', n[3])
    print('dezena: ', n[2])
    print('centena: ', n[1])
    print('milhar: ', n[0])
elif(t==3):
    print('unidade: ', n[2])
    print('dezena: ', n[1])
    print('centena: ', n[0])
elif(t==2):
    print('unidade: ', n[1])
    print('dezena: ', n[0])
elif(t==1):
    print('unidade: ', n[0])
else:
    print('Você não digitou nenhum numero ou passou o limite estipulado.')"""

# Resolução do Professor Guanabara
num = int(input('Informe um numero: '))
u = num // 1 % 10
d = num // 10 %10
c = num // 100 % 10
m = num //1000 % 10
print('Analizando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))




