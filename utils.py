import time
import sys
import random
import Safari as safari
import PokeBox as box
import copy

player_name = ''
mochila = ["Potion", "Super Potion", "Hyper Potion", "Revive"]

def delay_print(s):
    # print one character at a time
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.0)
        
def delay_print_s(s):
    # print one character at a time
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.9)
        


def arremesso():
    global pokemon
    escolha = input()
        
    while escolha not in ["1", "2"]:
            print()
            delay_print("Por favor, escolha uma opção válida!\n")
            delay_print("Você quer capturar o Pokémon? \n[1] sim\n[2] não\n")    
            escolha = input()
            
    if escolha == "1":
            delay_print("Pokébola vai!\n")
            time.sleep(1)
            delay_print_s("...")
            time.sleep(1)
            random_number = random.randint(1, 100)
            if random_number <= 60:        
                delay_print(f"Parabéns! Você capturou um {safari.pokemon.nome}!\n")
                box.pokemon_box.append(copy.deepcopy(safari.pokemon))
                delay_print(f"{safari.pokemon} foi adicionado à sua PokéBox!\n")
                safari.safari()
            else:
                delay_print(f"Essa não! O {safari.pokemon.nome} escapou!\n")
                delay_print("Volte aqui depois de um tempo para tentar encontra-lo novamente!\n")
                safari.safari()
    if escolha == "2":
        delay_print(f"Você fugiu de {safari.pokemon.nome}!\n")
        safari.safari()

def criar_copia(pokemon):
    return copy.deepcopy(pokemon)