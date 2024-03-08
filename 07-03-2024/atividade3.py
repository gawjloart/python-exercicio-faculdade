# crie uma funcao com dois parametros relacionados ao nome e sobrenome de uma pessoa, a funcao deve retornar uma
#mensagem de boas vindas e esses dados devem ser digitados pelo usuario


def mensagem(nome, sobrenome):
    return f"Seja bem vindo, {nome} {sobrenome}"

nome = input("Qual seu primeiro nome?\n -> ")
sobrenome = input("Qual seu segundo nome?\n -> ")

print(mensagem(nome, sobrenome))