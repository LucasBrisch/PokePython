import escolha
import PokeBox
import SafariSimples as Safari
import utils
import batalhasv3 as b
import pokecenter as pokecenter
import PokeShop as PokeShop
import bag

def start():
    escolha.escolha_inicial()
    menu()
    
    
def menu():
    print()
    utils.delay_print('''Bem-vindo ao menu principal! O que você gostaria de fazer?
[1] Acessar sua party
[2] Acessar sua PokéBox
[3] Acessar o Safari
[4] Batalhar
[5] PokeCenter
[6] PokeShop
[7] Sair do jogo\n''')
    
    for item in bag.player_bag:
        print(f"{item.nome} - {item.qtd}")
    
    escolha = input()
    if escolha == "1":
        PokeBox.player_party()
    elif escolha == "2":
        PokeBox.pc()
    elif escolha == "3":
        Safari.safari()
    elif escolha == "4":
        b.comeco_batalha()
    elif escolha == "5":
        pokecenter.pokecenter()
    elif escolha == "6":
        PokeShop.PokeShop()
    elif escolha == "7":
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