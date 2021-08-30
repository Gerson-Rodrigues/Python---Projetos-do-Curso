# Escreva um programa que faça o computador "pensar" em um número
# inteiro dentre 0 e 5 e peça para o usuário tentar descobrir qual foi o
# número escolhido pelo computador.
# O porgrama deverá escrever na tela se o usuário venceu ou perdeu.#

#minha resolução do desafio
import random

print('Estou pensando em um número de 0 a 5, tente advinhar!!')
comp = random.randint(0, 5)
chute = int(input('Digite aqui seu chute, lembre-se apenas de 0 a 5:'))
if comp == chute:
    print('Acertou, em pensei nesse número!!!')
    print('Boa Jogada!!!!!')
else:
    print('ERROOOOUUU, eu pensei em {}'.format(comp))
    print('Mais sorte na próxima vez...')


# Resolução do Professor Guanabara

"""
from random import randint
from time import sleep 
computador = randint(0, 5) # Faz o computador "PENSAR" 
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...)
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('PROCESANDO... ')    
sleep(3)
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('GANHEI!! Eu pensei no número {} e não no {}!'.format(computador, jogador))
    """