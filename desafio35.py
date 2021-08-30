# Desenvolva um programa que leia o comprimento de 3 retas e diga
# ao usuário se elas podem ou não formar um triângulo.#

# minha resolução esta com falhas...
'''print('Vamos descobrir se podes formar um triâgulo')
lado1 = int(input('Digite o valor um: '))
lado2 = int(input('Digite o valor dois: '))
lado3 = int(input('Digite o valor três: '))
#print(lado1, lado2, lado3)
if lado2 < lado1 > lado3:
    lado2 + lado3 >= lado1
    print('Isso forma um Triângulo1')
elif lado1 < lado2 > lado3:
    lado1 + lado3 >= lado2
    print('Isso forma um Triângulo2')
elif lado1 < lado3 > lado2:
    lado1 + lado2 >= lado3
    print('Isso forma um Triângulo3')
else:
    print('Isso não forma nenhum tipo de Triângulo!!!')
'''

# Resolução do Professor Guanabara
print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÂO PODEM FORMAR um triângulo')

