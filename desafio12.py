#faça um algoritmo que leia o preço de um produto e mostre o novo
# preço, com 5% de desconto
p = float(input('Diga-me qual o preço atual deste produto: R$'))
pn = p*5/100
pf = p-pn
print('O preço deste item com desconto de 5%, fica R${:.2f} \no desc. foi de R${:.2f}'.format(pf, pn))
