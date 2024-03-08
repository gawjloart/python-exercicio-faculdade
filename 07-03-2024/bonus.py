def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

resultado = soma(5, 5, 5, 5, 5)
print(resultado)  
