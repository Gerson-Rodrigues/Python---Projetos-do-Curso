# Faça um algoritmo que leia o salário de um funcionário e
# mostre seu novo salário, com 15% de aumento.
sal_func = float(input('Informe seu sálario para corrigi-lo: '))
nov_sal = sal_func +  (sal_func *15/100)

print('Seu novo sálario com acréscimo de 15% fica em R${:.2f}'.format(nov_sal))
