# Escreva um programa que converta um temperatura digitada
# e conerta para ºF
celsius = float(input('Digite a temperatura em ºC para conversão: '))
fah = ((9*celsius)/5)+32
print('A temperatura em Fahrenheit é {:.1f}ºF'.format(fah))
