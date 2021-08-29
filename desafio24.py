#Crie um programa que leia o nome de uma cidade e diga se ela começa
# ou não com o nome "Santo"

#minha resolução do problema
nome = str(input('Digite o nome de uma cidade: ')).strip()
teste = nome[:5].title() == 'Santo'
print(teste)
