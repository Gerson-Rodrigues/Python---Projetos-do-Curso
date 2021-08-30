# Desenvolva um programa que pergunte a distância de uma viagem
# em Km.
# Calcule a preço da passagem, cobrando R$0,50 por Km para viagens
# de 200Km e R$0,45 para viagens mais longas.#

#minha resolução do desafio
print('Vai Viajar? Calcule quanto te Custará a Passagem.')
km = int(input('Digite quantos Km vai percorrer até o destino: '))
if km < 201:
    passag = km * 0.50 + 30
    print('Você pagará R${:.2f} pela Passagem até seu destino'.format(passag))
else:
    passag = km * 0.45 + 50
    print('Você pagará R${:.2f} pela Passagem até seu destino'.format(passag))


# resolução do Professor Guanabara
"""
distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar um viagem de {}Km.'.format(distância))
if distância <=200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))

"""