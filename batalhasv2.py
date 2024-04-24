import utils
import random
import bag

def menu_batalha ():
    utils.delay_print("O que você deseja fazer?\n")
    utils.delay_print("[1] - Atacar\n[2] - Trocar de pokemon\n[3] - Acessar sua bag \n[4] - Fugir\n")
    escolha = int(input())
    if escolha == 1:
        ataque()
    if escolha == 2:
        trocar_pokemon()
    if escolha == 3:
        bag()
    if escolha == 4:
        fuga = random.choice([True, False])
        if fuga:
            print("Você conseguiu fugir!")
        else:
            print("Você não conseguiu fugir!")
            menu_batalha()
            
        
        

menu_batalha()