import random

VERDE = '\033[92m'
AMARELO = '\033[93m'
CINZA = '\033[90m'
RESET = '\033[0m'

def menu():
    print('1 - Jogar')
    print('2 - Sair')
    opt = int(input('Faça sua escolha: '))
    if opt != 1 and opt != 2:
        while opt != 1 and opt != 2:
            print('Escolha inválida!')
            opt = int(input('Faça sua escolha: '))
    return opt

def palpitar():
    tentativa = input("Faça sua tentativa: ").lower()
    while len(tentativa) != 5:
        print('O palpite deve ser uma palavra de 5 letras!')
        tentativa = input("Refaça seu palpite: ").lower()
    fragmentadoTentativa = []
    for letras in range (5):
        fragmentadoTentativa.append(tentativa[letras]) 
    return tentativa, fragmentadoTentativa

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
    palavras = [
"canto", "abaco", "livro", "casal", "pazeo", "mudar", "cinto", "pular", "pluma",
"velho", "campo", "caber", "rolar", "cesta", "teste", "cifra", "gente", "firme",
"torre", "folha", "dupla", "nobre", "parta", "sorte", "ponto", "lento", "falar",
"verde", "ferro", "corpo", "cairo", "dedos", "trato", "danos", "lindo", "custo",
"metro", "linha", "corte", "limpo", "carta", "botar", "bando", "bolsa", "sinal",
"festa", "canso", "caber", "mapas", "audio", "amigo", "trama", "cavar", "gesto",
"moeda", "pisar", "breve", "troca", "senso", "curva", "terra", "couro", "morto",
"forno", "porta", "barco", "trato", "manga", "tocar", "cavar", "nuvem", "bicho",
"luzes", "lemos", "surto", "vazio", "dente", "ganho", "pavio", "sabor", "duelo",
"faixa", "moita", "claro", "cubra", "furto", "noite", "vista", "haste", "cinto",
"latas", "gordo", "cervo", "caber", "tropa", "antes", "lutar", "furar", "cetro", 
"casco", "perna", "versa", "pular", "tonto", "bolha", "focar", "fenda", "lidar",
"final", "retro", "magia", "cetro", "bazar", "cubra", "servo", "gueto", "navio",
"treno", "leste", "aroma", "lousa", "perto", "cacho", "vinho", "punho", "treta",
"gabar", "fugir", "samba", "plano", "grade", "ninho", "multa", "louca", "vapor",
"rumor", "pecar", "tarde", "farol", "pique", "mocho", "repor", "binho", "caldo",
"frota", "trapo", "meter", "tocar", "rolha", "banca", "prato", "moeda", "socar",
"andar", "tinta", "fazia", "matar", "logar", "verbo", "dizer", "morro", "letra",
"odiar", "pedra", "lento", "socar", "folga", "marca", "arcos", "fugiu", "surdo",
"lombo", "penso", "reino", "curar", "jogar", "largo", "tiver", "regar", "solto",
"bater", "sonho", "peste", "pardo", "borda", "cimal", "matar", "legal", "bravo",
"tosco", "fugaz", "perua", "manso", "verao", "farpa", "grifo", "crime", "bicha"
]
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
    print('Deseja jogar novamente? (S/N)')
    resp = input('Faça sua escolha: ').upper()
    if resp != 'S' and resp != 'N':
        while resp != 'S' and resp != 'N':
            print('Resposta inválida!')
            resp = input('Faça sua escolha: ').upper()
    return resp

opt = menu()
if opt == 1:
    resp = main()
    while resp == 'S':
        resp = main()       
    print('Até a próxima!')
else:
    print('Saindo do programa...')
