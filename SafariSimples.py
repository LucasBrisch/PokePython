import utils as utils
import random
import time
import PokeBox as box
import CompiladorJogo as cj
import Pokemons as p

def safari():
    utils.delay_print ("\nBem-vindo ao Safari!\n")
    utils.delay_print('''\nVocê quer encontrar um Pokémon? 
[1] sim
[2] nao
''')
    escolha = input()
    if escolha in ["s", "sim", '1']:
        spawn_lendario = random.randint(1, 100)
    if spawn_lendario <= 5:
        utils.delay_print("\nVocê entrou no Safari\n")
        time.sleep(1)
        utils.delay_print("Espera, aquilo é um pokémon lendário?\n")
        time.sleep(1)
        pokemon = random.choice(p.pokemons_lendarios)
        utils.delay_print(f"\nUm {pokemon.nome} apareceu!\n")
        utils.delay_print('''Você quer capturar o Pokémon?
[1] sim
[2] não
''')
        utils.arremesso()
                       
    elif spawn_lendario > 5:                
        utils.delay_print("\nVocê entrou no safari\n")
        time.sleep(1)
        utils.delay_print("procurando um Pokémon...")
        time.sleep(1)
        pokemon = random.choice(p.pokemons_basicos)
        utils.delay_print(f"\nUm {pokemon.nome} apareceu!\n")
        utils.delay_print('''Você quer capturar o Pokémon?
[1] sim
[2] não
''')
        utils.arremesso()