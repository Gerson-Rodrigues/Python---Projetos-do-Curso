# Faça um programa que leia um ângulo qualquer e mostre na tela
# o valor do seno, cosseno e tangente desse ângulo
from  math import radians, sin, cos, tan
ang = float(input('Digite um angulo para calculo: '))
s = sin(radians(ang))
print('O ângulo de {} tem o Seno de {:.2f}'.format(ang, s))
c = cos(radians(ang))
print('O ângulo de {} tem o Cosseno de {:.2f}'.format(ang, c))
t = tan(radians(ang))
print('O ângulo de {} tem um tangente de {:.2f}'.format(ang, t))
