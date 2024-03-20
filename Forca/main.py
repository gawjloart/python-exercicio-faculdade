# jogo da forca -ok
# intaface com "_" para indicar as letras. - ok
# tentativas mostrando em letras / "tentativas restantes:..." -ok 
# checkar numeros... -ok
# errou = encerrar - ok
# acertou = ganhou / manter chances - ok
# importar bibliot random pra gerar palavras aleatorais em formas aleatorias.. - ok


import random


#randomizar a palavra - tornando ela aleatoria
def escolher_palavra():
    palavras = ['goiabada', 'professor', 'analise e desenvolvimento de sistema']
    return random.choice(palavras)

#criar a interface da forca, armazenar as tentativas, while true;
def jogar_forca():
    palavra = escolher_palavra()
    letras_certas = ['_'] * len(palavra)
    letras_erradas = []
    tentativas = 6
    
    while True:
        palavra_atual = ' '.join(letras_certas)
        print(f'Palavra: {palavra_atual}')
        print(f'Voce ainda tem: [{tentativas}], tentativas :)')
        print(f'Voce ja disse: {", ".join(letras_erradas)}')
        
        if '_' not in letras_certas:
            print('Parabéns! Você ganhou parceiro!')
            break
        
        if tentativas == 0:
            print(f'Você perdeu meu camarada :/! A palavra era {palavra}.')
            break
        
        letra = input('Digite uma letra: ').lower()
        
        if len(letra) != 1 or not letra.isalpha():
            print('Por favor, digite apenas uma letra válida.')
            continue
        
        if letra in letras_certas or letra in letras_erradas:
            print('Você já tentou essa letra ai em.. Tente outra.')
            continue
        
        if letra in palavra:
            for i, l in enumerate(palavra):
                if l == letra:
                    letras_certas[i] = letra
        else:
            letras_erradas.append(letra)
            tentativas -= 1

jogar_forca()
