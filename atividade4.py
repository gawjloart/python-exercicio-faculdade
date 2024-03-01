# crie um programa que realiza a contade de 1 até 100, usando apenas numeros impares, ao final, deve exibir em tela quantos foram encontrados e exibir sua soma

contador = 0
soma = 0

for i in range(1, 101, 2):
    contador += 1
    soma += i

print("Impares encontrados: ", contador)
print("Soma  dos impares: ", soma)