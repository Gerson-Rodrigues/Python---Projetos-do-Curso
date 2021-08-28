# Faça um programa que leia o comprimento do cateto oposto e do
# cateto adjacente de um triangulo retangulo, calcule e mostre o
# comprimento da hipotenusa.

from math import sqrt, hypot

ca = float(input('Escreva o valor do Cateto Adjacente: '))
co = float(input('Agora o valor do Cateto Oposto: '))
#h = sqrt((ca**2) + (co**2))
h = hypot(ca, co)
print('A Hipotenusa terá um comprimento de {:.2f}'.format(h))
