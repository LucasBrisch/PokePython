import escolha
import PokeBox
import Safari
import utils

def start():
    escolha.escolha_inicial()
    menu()
    
    
def menu():
    print()
    utils.delay_print('''Bem-vindo ao menu principal! O que você gostaria de fazer?
[1] Acessar sua party
[2] Acessar sua PokéBox
[3] Acessar o Safari
[4] Batalhar (em breve)
[5] Sair do jogo\n''')
    escolha = input()
    if escolha == "1":
        PokeBox.player_party()
    elif escolha == "2":
        PokeBox.box()
    elif escolha == "3":
        Safari.safari()
    elif escolha == "4":
        utils.delay_print("Essa funcionalidade ainda não foi implementada, volte mais tarde!\n")
        menu()
    elif escolha == "5":
        utils.delay_print("Tem certeza de que deseja sair do jogo? Seu progresso não será salvo!\n")
        utils.delay_print('''[1] sim
[2] não\n''')
        escolha = input()
        if escolha == "1":
            print()
            utils.delay_print("Tudo bem, até a próxima!")
            exit()
        elif escolha == "2":
            menu()
        else:
            print()
            utils.delay_print("Escolha inválida, tente novamente.")
            menu()
    else:
        print()
        utils.delay_print("Escolha inválida, tente novamente.")
        menu()

if __name__ == "__main__":
    start()