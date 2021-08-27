# Crie um programa  que leia quanto dinheiro uma pessoa tem na
#  carteira e mostre quantos Dólares ela pode comprar.
#  Considere
#  US$1,00 = R$3,27
din = float(input('Quantos Reais, tens na carteira? R$'))
dolar = din/3.27
print('Com R${:.2f} você consegue comprar ${:.2f}, nos locais de cambio.'.format(din, dolar))
