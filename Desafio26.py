# Faça um programa que leia uma frase pelo teclado e mostre
# Quantas vezes aparece a letra "A".
# Em que posição ela aparecea primeira vez.
# Em que posição ela apace a última vez. #

# Minha resolução
"""frase = str(input('Escreva uma frase bem legal: ')).strip()
frase = frase.upper()
conta = frase.count('A')
esq = frase.find('A')
dir = frase.rfind('A')
print('Na frase tem {} A´s a primeira aparece na posição {} e a última '
      'na position {}'.format(conta, esq, dir))
"""

# Resolução do Professor Guanabara
frase = str(input('Digite uma frase: ')).upper().strip()
print('A frase A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primera letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))
