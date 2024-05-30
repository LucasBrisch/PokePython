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
        utils.delay_print ('''Você gostaria de ir para uma caverna ou para uma floresta?
[1] Caverna
[2] Floresta
[3] Sair\n''')
        escolha = input()
        
        while escolha not in ["1", "2", '3']:
            print()
            utils.delay_print("Por favor, escolha uma opção válida!\n")
            utils.delay_print("Você quer capturar o Pokémon? \n[1] sim\n[2] não\n")
            escolha = input()
        
        if escolha == "1":
            utils.delay_print("indo para a caverna...")
            time.sleep(1)
            caverna()
        if escolha == "2":
            utils.delay_print("indo para a floresta...")
            utils.time.sleep(1)
            floresta()
        elif escolha == "3":
            utils.delay_print("Saindo do Safari...")
            cj.menu()
    elif escolha in ["n", "não", "nao", "2"]:
        utils.delay_print("Tudo bem, até a próxima!\n")
        cj.menu()
    else:
        utils.delay_print("\nEscolha inválida, tente novamente.")
        safari()
        
def caverna():
    global pokemon, local
    local = 'caverna'
    pokemons_caverna = [p.Zubat, p.Geodude, p.Onix, p.Machop, p.Cubone]
    lendarios_caverna = [p.Mewtwo, p.Mew, p.Articuno, p.Zapdos, p.Moltres, p.Groundon]
    spawn_lendario = random.randint(1, 100)
    if spawn_lendario <= 5:
        utils.delay_print("\nVocê entrou na caverna\n")
        time.sleep(1)
        utils.delay_print("Espera, aquilo é um pokémon lendário?\n")
        time.sleep(1)
        pokemon = random.choice(lendarios_caverna)
        utils.delay_print(f"\nUm {pokemon.nome} apareceu!\n")
        utils.delay_print('''Você quer capturar o Pokémon?
[1] sim
[2] não
''')
        utils.arremesso()
                       
    elif spawn_lendario > 5:                
        utils.delay_print("\nVocê entrou na caverna\n")
        time.sleep(1)
        utils.delay_print("procurando um Pokémon...")
        time.sleep(1)
        pokemon = random.choice(pokemons_caverna)
        utils.delay_print(f"\nUm {pokemon.nome} apareceu!\n")
        utils.delay_print('''Você quer capturar o Pokémon?
[1] sim
[2] não
''')
        utils.arremesso()
    
def floresta():
    global pokemon, local
    local = 'floresta'
    pokemons_floresta = [p.Pidgey, p.Rattata, p.Oddish, p.Bellsprout, p.Caterpie]
    lendarios_floresta = [p.Celebi, p.Raikou, p.Entei, p.Suicune, p.Lugia, p.Kyogre]
    spawn_lendario = random.randint(1, 100)
    if spawn_lendario <= 5:
        utils.delay_print("\nVocê entrou na floresta\n")
        time.sleep(1)
        utils.delay_print("Espera, aquilo é um pokémon lendário?\n")
        time.sleep(1)
        pokemon = random.choice(lendarios_floresta)
        utils.delay_print(f"\nUm {pokemon.nome} apareceu!\n")
        utils.delay_print('''Você quer capturar o Pokémon?
[1] sim
[2] não
''')
        utils.arremesso()
                       
    elif spawn_lendario > 5:                
        utils.delay_print("\nVocê entrou na floresta\n")
        time.sleep(1)
        utils.delay_print("procurando um Pokémon...")
        time.sleep(1)
        pokemon = random.choice(pokemons_floresta)
        utils.delay_print(f"\nUm {pokemon.nome} apareceu!\n")
        utils.delay_print('''Você quer capturar o Pokémon?
[1] sim
[2] não
''')  
        utils.arremesso()


if __name__ == "__main__":
    safari()      