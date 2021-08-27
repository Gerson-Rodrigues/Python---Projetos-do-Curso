# Escreva um programa que pergunte a quantidae de KM percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi
# alugado. Calcule o preço a pagar, sabendo que o carro
# custa R$60 por dia e R$0,15 por Km rodado.
dias = int(input('Digite o total de dias com o carro: '))
km = float(input('total de Km percorridos: '))
#preço_dias = dias * 60
#preço_km = km *0.15
tot = (dias*60) + (km*0.15)
print('O Total à pagar pelo aluguel do carro é R${:.2f}'.format(tot))
