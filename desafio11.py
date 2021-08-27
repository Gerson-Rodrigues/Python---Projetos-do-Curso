# Faça um programa que leia a largura e a altura de uma parede em
# metros, calcule a sua área e a quantidade de tinta nececssária para
# pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
print('Vamos calcular pra você, quanto de tinta vai precisar para pintar!')
alt = float(input('Quanto tem a altura da parede? '))
larg = float(input('E qual a largura? '))
metq = alt * larg
tottinta = metq / 2
print('Sua parede é de {} X {} e sua área é de {:.2f}m²'.format(alt, larg, metq))
print('O total é de {:.3f} litros de tinta para pintar a parede.'.format(tottinta))
