import random
from os import system, name

# 1- Definir a lista de palavras possíveis
# 2- Escolher uma palavra aleatória da lista
# 3- Criar uma lista vazia para armazenar as letras adivinhadas
# 4- Definir o número máximo de tentativas permitidas
# 5- Enquanto o número de tentativas não atingir o limite máximo:
# a. Mostrar a palavra como uma série de underscores, com as letras adivinhadas preenchidas nos espaços corretos
# b. Pedir ao jogador que adivinhe uma letra
# c. Verificar se a letra adivinhada está na palavra
# d. Se a letra adivinhada está na palavra, adicionar a letra à lista de letras adivinhadas e atualizar a exibição da palavra
# e. Se a letra adivinhada não está na palavra, reduzir o número de tentativas restantes e exibir a mensagem "Letra incorreta. Tentativas restantes: [número de tentativas restantes]"
# f. Verificar se todas as letras da palavra foram adivinhadas
# g. Se todas as letras foram adivinhadas, exibir a mensagem "Você venceu!"
# h. Se o número de tentativas restantes chegar a zero, exibir a mensagem "Você perdeu. A palavra era [palavra escolhida]" e encerrar o jogo.


def limpa_tela():
    if name == 'nt':
        system ('cls')
    else:
        system('clear')


# Função
def game():

    limpa_tela()
    print("\nBem-vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")

    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']
    
    palavra = random.choice(palavras)

    letras_descobertas = ['_' for letra in palavra]

    chances = 6
    letras_erradas = []

    while chances > 0:

        # Print
        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))

        # Tentativa
        tentativa = input("\nDigite uma letra: ").lower()

        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra era:", palavra)
            break

    if "_" in letras_descobertas:
        print("\nVocê perdeu, a palavra era:", palavra)




if __name__ == "__main__":
    game()
    print("\nParabéns. Você está aprendendo programação em Python com a DSA. :)\n")



