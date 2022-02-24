import sys
from ggame import *

def mostralinha():
    print(f'\033[1;37m{"-=-"}\033[m' * 30)

def main():
    mostralinha()
    print(f'\033[7;0;47m{"JOGO DA ADIVINHAÇÃO 2":^80}\033[m')
    mostralinha()
    print(f'\033[1;35m{"PENSE EM UM NÚMERO ENTRE 0 E 100 PARA QUE EU POSSA ADIVINHAR-LO.":^80}\033[m')
    mostralinha()
    tentativas = []
    inicio = 0
    fim = 100
    pensou = str(input('Pensou em um número? então digite OK para começar!')).strip()
    mostralinha()
    while pensou in 'OKok':
        palpite = (inicio + fim) // 2
        print(f'\033[4;34mVocê pensou no número {palpite}!\033[m')
        mostralinha()
        aproximação = int(
            input('Acertei? \n [0] Sim \n [1] Não, tente um número maior.  \n [2] Não, tente um número menor. '))
        mostralinha()
        if aproximação == 1:
            inicio = palpite + 1
            tentativas.append(palpite)
        if aproximação == 2:
            fim = palpite - 1
            tentativas.append(palpite)
        if aproximação == 0:
            tentativas.append(palpite)
            pygame.mixer.music.load('win.mp3')
            pygame.mixer.music.play()
            while (pygame.mixer.music.get_busy()): pass
            print()
            print(f'Precisei de {len(tentativas)} tentativa(s) para adivinhar!')
            print()
            mostralinha()
            break
    pass

if __name__ == '__main__':
    main()
    sys.exit(0)

