import random

VERDE = '\033[92m'
AMARELO = '\033[93m'
CINZA = '\033[90m'
RESET = '\033[0m'

def menu():
    print('1 - Jogar')
    print('2 - Sair')
    opt = int(input("Informe sua opção: "))
    return opt

def palpitar():
    tentativa = input("Faça sua tentativa: ")
    while len(tentativa) != 5:
        print('O palpite deve ser uma palavra de 5 letras!')
        tentativa = input("Refaça seu palpite: ")
    return tentativa.lower()

def relatorio(contadorTentativas, palavrasTentadas):
        print()
        print('=======================================')
        print(f'Palavras tentadas: {palavrasTentadas}')
        print(f'Tentativas restantes: {contadorTentativas}')

def fragmentar(tentativa):
        fragmentadoTentativa = []
        for letras in range (5):
            fragmentadoTentativa.append(tentativa[letras])
        return fragmentadoTentativa

opt = menu()

if opt == 1:
    palavras = ["canto"]
    palavra_secreta = random.choice(palavras)
    fragmentadoSorteado = []

    #A palavra sorteada é fragmentada em uma lista para avaliação
    for letras in range (0,5):
        fragmentadoSorteado.append(palavra_secreta[letras])

    #O jogador faz seu palpite, que é fragmentado em uma lista para avaliação
    tentativa = palpitar()
    fragmentadoTentativa = fragmentar(tentativa)

    #Variáveis para contar tentativas e armazenar palavras testadas    
    contadorTentativas = 6
    palavrasTentadas = []

    while contadorTentativas > 0:
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
            break

        palavrasTentadas.append(tentativa)
        contadorTentativas -= 1
        relatorio(contadorTentativas, palavrasTentadas)
        tentativa = palpitar()
        fragmentadoTentativa = fragmentar(tentativa)
        
    print()
    print('=======================================')
    if contadorTentativas >0:
        print(f'Você venceu! A palavra secreta é {palavra_secreta.upper()}')
    else:
        print(f'Você perdeu! A palavra secreta é {palavra_secreta.upper()}')
else:
    print('Saindo do programa...')