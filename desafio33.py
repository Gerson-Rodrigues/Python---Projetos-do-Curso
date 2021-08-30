# Faça um programa que leia 3 números e mostre qual é o maior
# e qual é o menor.#

#minha resolução do desafio
'''
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if n1 > n2 and n1 > n3:
    print('o maior numero é {}'.format(n1))
if n1 < n2 >n3:
    print('o maior numero é {}'.format(n2))
if n1 < n3 > n2:
    print('o maior numero é {}'.format(n3))
if n1 < n2 and n1 < n3:
    print('o menor numero é {}'.format(n1))
if n1 > n2 < n3:
    print('o menor numero é {}'.format(n2))
if n1 > n3 < n2:
    print('o menor numero é {}'.format(n3))
'''

# Resolução do Professor Guanabara
a = int(input('Primeiro valor: '))
b = int(input('segundo valor: '))
c = int(input('Terceiro valor: '))
# Verificando que é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitando foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))

