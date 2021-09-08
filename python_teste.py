notas = []
cont = 0
while cont > 4:
    notas = float(input('Digite uma nota do aluno: '))
    cont += 1
    total = 0
    for nota in notas:
        total += nota
    media = total / len(notas)
    if media >= 7.0:
        print("aprovado com média:", media)
    else:
        print("reprovado com média:", media)

