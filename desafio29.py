# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele
# foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.#

#minha resolução do desafio
velo = float(input('Digite a velocidade de um veículo no qual costuma dirigir: '))
if velo <= 80.0 and velo > 74.0:
    print('Uma boa velocidade para viagens, segurança sempre!')
elif velo < 75:
    print('Velocidade abaixo do habitual da pista, suba sua velocidade ou poderá \n'
          'receber uma multa por congestionar a via!!')
else:
    multa = (velo - 80)*7+50
    if velo >80.0 and velo < 100.0:
        ponto = 5
    elif velo >99.0 and velo < 150.0:
        ponto = 12; multa = multa + 250
    elif velo >149.0:
        ponto = 30; multa = multa + 1000
    print('Você passou o limite de velocidade, você receberá uma multa.\n'
              'o valor da multa aplicada será relativo a sua velocidade, ficando R${:.2f} \n'
              'e {} pontos na carteira'.format(multa, ponto))
    if ponto == 30:
        print('Por exceder demais a velocidade, terá a carteira suspensa.')

print('Sempre Dirija com Cuidado, e não Beba se for dirijir...')

# Resolução do Professor Guanabara
"""
velocidade = float(input('Qual é a valocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format{multa))
print('Tenha um bom dia! Dirija com Segurança!')

"""