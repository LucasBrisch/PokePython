import time
import sys
import random
import SafariSimples as safari
import PokeBox as box
import copy
import PokeBox as pb
import Pokemons as p

player_name = ''
dinheiro = 9999

def delay_print(s):
    # print one character at a time
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)
        
def delay_print_s(s):
    # print one character at a time
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.9)
        


def arremesso():
    global pokemon
    print()
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
                delay_print(f"{safari.pokemon.nome} foi adicionado à sua PokéBox!\n")
                if safari.pokemon in p.pokemons_basicos:
                    p.pokemons_basicos.remove(safari.pokemon)
                elif safari.pokemon in p.pokemons_lendarios:
                    p.pokemons_lendarios.remove(safari.pokemon)
                xp()
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

def xp():
    for pokemon in pb.pokemon_party:
        if pokemon.hp > 0:
            pokemon.xp += random.randint(10, 30)
            delay_print(f"{pokemon.nome} ganhou {pokemon.xp} de XP!\n")
            if pokemon.xp >= pokemon.xp_max:
                pokemon.nivel += 1
                pokemon.xp = 0
                pokemon.xp_max = int(pokemon.xp_max * 1.1)
                delay_print(f"{pokemon.nome} subiu de nível! Agora está no nível {pokemon.nivel}!\n")
                if pokemon.evolucao and pokemon.nivel >= pokemon.nivel_evolucao:
                    delay_print(f"Parabéns! Seu {pokemon.nome} evoluiu para {pokemon.evolucao.nome}!\n")
                    pb.pokemon_party.append(criar_copia(pokemon.evolucao))
                    pb.pokemon_party.remove(pokemon)

                

            else:
                continue
        else:
            continue
    