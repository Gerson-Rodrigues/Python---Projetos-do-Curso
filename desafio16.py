# Crie um programa que leia um numero real qualquer pelo teclado
# e mostre na tela a sua porção inteira
# ex: digite um numero: 6.127
# O numero 6.127 tem a parte inteira 6
from math import trunc
num = float(input('Digite um numero aleatorio com ponto flotuante: '))
val_inteiro = trunc(num)
print('Seu numero {:.2f} foi arredondado para {}'.format(num, val_inteiro))
