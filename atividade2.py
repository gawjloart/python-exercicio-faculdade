# crie um programa que realiza a progressão aritmética de 20 elementos com o 20 primeiro termo e razao definidos pelo usuario em python

termo1 = float(input("Digite o primeiro numero de progressão: "))
razao = float(input("Digite a razao: "))

progressao = [termo1 + i * razao for i in range(20)]

print("Progressão aritimética é:", progressao)