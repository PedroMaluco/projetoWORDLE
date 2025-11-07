import random

#print(VERDE + "A" + RESET, AMARELO + "B" + RESET, CINZA + "C" + RESET)

VERDE = '\033[92m'
AMARELO = '\033[93m'
CINZA = '\033[90m'
RESET = '\033[0m'

repositorioPalavras = ["verde", "lapis", "plano", "bravo"]
palavras = ["canto"]
palavra_secreta = random.choice(palavras).upper
fragmentadoSorteado = []

#A palavra sorteada é fragmentada em uma lista para avaliação
for letras in range (len(palavra_secreta)):
    fragmentadoSorteado.append(palavra_secreta[letras])

#Usuário faz sua tentativa
tentativa = input("Faça sua tentativa: ").upper
fragmentadoTentativa = []

#A palavra testada é fragmentada em uma lista para avaliação
for letras in range (len(tentativa)):
    fragmentadoTentativa.append(tentativa[letras])

#Variáveis para contar tentativas e armazenar palavras testadas    
contadorTentativas = 0
palavrasTentadas = []

while contadorTentativas <= 2:
    palavrasTentadas.append(tentativa)

    for j in range(5):
        if fragmentadoTentativa[j] in fragmentadoSorteado:
            if fragmentadoTentativa[j] == fragmentadoSorteado[j]:
                print(VERDE + fragmentadoTentativa[j]+RESET, end="")
            else:
                print(AMARELO + fragmentadoTentativa[j]+RESET, end="")
        else:
            print(CINZA + fragmentadoTentativa[j]+RESET, end="") 
    if tentativa == palavra_secreta:
        break
    print()
    print('=======================================')
    print(f'Palavras tentadas: {palavrasTentadas}')
    tentativa = input("Faça sua tentativa: ")
    fragmentadoTentativa = []
    for letras in range (len(tentativa)):
        fragmentadoTentativa.append(tentativa[letras])
    contadorTentativas+=1




print()
print('=======================================')
if contadorTentativas <=6:
    print(f'Você venceu! A palavra secreta é {palavra_secreta}')
else:
    print(f'Você perdeu! A palavra secreata é {palavra_secreta}')
         