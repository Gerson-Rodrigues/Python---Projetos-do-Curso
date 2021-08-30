# Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para salários inferiores ou iguais, o aumento é de 15%.#

#minha resolução do desafio
sal = float(input('Digite seu salário: '))
if sal > 1250.0:
    print('Seu salário foi reajustado com 10% e ficou R${:.2f}'.format(sal+(sal*0.10)))
else:
    print('Seu salário foi reajustado com 15% e ficou R${:.2f}'.format(sal+(sal*0.15)))

# Resolução Professor Guanabara
'''
salário = float(input('Qual o salário do funcionário? R$'))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário, novo))

'''