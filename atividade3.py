# crie um programa que exibe em tela a tabuada de determinado numero fornecido pelo usuario


num = int(input("Fale um numero para saber a tabuada: "))

print("Tabuada do", num)
for i in range(1, 11):
    print(num, "x", i, "=", num * i)