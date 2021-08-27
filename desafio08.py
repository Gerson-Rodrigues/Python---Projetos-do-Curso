# Escreva um programa que leia um valor em metros e o exiba
# convertido em centimetros e milietros.
metros = float(input('Digite um valor em metros para calculo: '))
centi = metros * 100
mili = metros * 1000
print('você colocou {} metros, em centimetros tem {:.0f} e em milimetros fica {:.0f}'.format(metros, centi, mili))
