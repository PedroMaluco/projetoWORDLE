import random

VERDE = '\033[92m'
AMARELO = '\033[93m'
CINZA = '\033[90m'
RESET = '\033[0m'


def palpitar():
    tentativa = input("Faça sua tentativa: ")
    while len(tentativa) != 5:
        print('O palpite deve ser uma palavra de 5 letras!')
        tentativa = input("Refaça seu palpite: ")
    fragmentadoTentativa = []
    for letras in range (5):
        fragmentadoTentativa.append(tentativa[letras]) 
    return tentativa.lower(), fragmentadoTentativa

def relatorio(contadorTentativas, palavrasTentadas, tentativa):
        palavrasTentadas.append(tentativa)
        print()
        print('=======================================')
        print(f'Palavras tentadas: {palavrasTentadas}')
        print(f'Tentativas restantes: {contadorTentativas}')
        return palavrasTentadas

def verificarPalpite(fragmentadoTentativa, tentativa, fragmentadoSorteado, palavrasTentadas):
    if tentativa in palavrasTentadas:
        while tentativa in palavrasTentadas:
            print(f'A palavra {tentativa} já foi testada!')
            tentativa, fragmentadoTentativa = palpitar()

    vitoria = False
    resultado = ["cinza"] * 5
    restantes = fragmentadoSorteado.copy()

    for i in range(5):
        if fragmentadoTentativa[i] == fragmentadoSorteado[i]:
            resultado[i] = "verde"
            restantes[i] = None

    for j in range(5):
        if resultado[j] == "cinza":
            letra = fragmentadoTentativa[j]
            if letra in restantes:
                resultado[j] = "amarelo"
                restantes[restantes.index(letra)] = None
            
    for i in range(5):
        letra = fragmentadoTentativa[i]
        if resultado[i] == "verde":
            print(VERDE + letra.upper() + RESET, end="")
        elif resultado[i] == "amarelo":
            print(AMARELO + letra.upper() + RESET, end="")
        else:
            print(CINZA + letra.upper() + RESET, end="")
    print()

    if fragmentadoTentativa == fragmentadoSorteado:
        vitoria = True
    return vitoria, tentativa, fragmentadoTentativa

def main():
    palavras = ["canto"]
    palavra_secreta = random.choice(palavras)

    #A palavra sorteada é fragmentada em uma lista para avaliação
    fragmentadoSorteado = []
    for letras in range (0,5):
        fragmentadoSorteado.append(palavra_secreta[letras])

    #O jogador faz seu palpite, que é fragmentado em uma lista para avaliação
    tentativa, fragmentadoTentativa = palpitar()

    #Variáveis para contar tentativas e armazenar palavras testadas    
    contadorTentativas = 6
    palavrasTentadas = []

    while contadorTentativas > 0:
        chance, tentativa, fragmentadoTentativa = verificarPalpite(fragmentadoTentativa, tentativa, fragmentadoSorteado, palavrasTentadas)
        if chance == True:
            break

        contadorTentativas -= 1
        relatorio(contadorTentativas, palavrasTentadas, tentativa)
        tentativa, fragmentadoTentativa = palpitar()
            
    print()
    print('=======================================')
    if contadorTentativas >=0:
        print(f'Você venceu! A palavra secreta é {palavra_secreta.upper()}')
    else:
        print(f'Você perdeu! A palavra secreta é {palavra_secreta.upper()}')



main()
