import time
import sys


global pokemon_party, pokemon_box
pokemon_party = ["Squirtle", "Charmander", "Bulbasaur", "Pikachu", "pidgeot", "Lapras"]
pokemon_box = ['Arcanine', 'Gyarados', 'Alakazam', 'Machamp', 'Gengar', 'Lapras', 'Snorlax',]
player_name = "Lucas"
#valor aplicado somente para testes, o objetivo é puxar eles dos outros arquivos

def delay_print(s):
    # print one character at a time
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
        
def adicionar_starter():
    global pokemon_1, pokemon_party
    pokemon_party.append(pokemon_1)
    
def player_party():
    global player_name, pokemon_party
    print()
    delay_print(f'''Olá, {player_name}! Essa é a sua equipe de Pokémons atual:''')
    for i in pokemon_party:
        delay_print(f"\n{i}")
    delay_print('''\nGostaria de acessar a sua box?
[1] sim
[2] não''')
    escolha = input()
    if escolha == "1":
        box()
        
    elif escolha == "2":
        print()
        #
    else:
        delay_print("Escolha inválida, tente novamente.")
        player_party()        
        
if __name__ == "__main__":
    player_party()
    
def box():
    global player_name, pokemon_party, pokemon_box
    delay_print(f'''Olá, {player_name}! Essa é a sua PokéBox atual:''')
    for pokemon in pokemon_box:
        delay_print(f"\n{pokemon}")
    delay_print('''\n\nO que você deseja fazer agora?
[1] Adicionar um Pokémon da sua party à sua PokéBox
[2] Adicionar um Pokémon da sua box a sua equipe de Pokémons
[3] Sair''')
    escolha = input()
    if escolha == "1":
        delay_print("Qual Pokémon você deseja adicionar à sua PokéBox? ")
        delay_print(pokemon_party)
        escolha = input()
        while escolha not in pokemon_party:
            delay_print("Por favor, escolha um Pokémon válido!")
            escolha = input()
        pokemon_box.append(escolha)
        pokemon_party.remove(escolha)
        delay_print(f"{escolha} foi removido de sua party e adicionado à sua PokéBox!")
        box()
    elif escolha == "2":
        delay_print("Qual Pokémon você deseja adicionar à sua party? ")
        delay_print(pokemon_box)
        escolha = input()
        while escolha not in pokemon_box:
            delay_print("Por favor, escolha um Pokémon válido!")
            escolha = input()
        if len(pokemon_party) == 6:
            delay_print("Sua party está cheia! Por favor, remova um Pokémon antes de adicionar outro.")
            box()
        elif len(pokemon_party) < 6:
            pokemon_party.append(escolha)
            pokemon_box.remove(escolha)
            delay_print(f"{escolha} foi removido de sua PokéBox e adicionado à sua party!")
            box()
    else:
        delay_print("Escolha inválida, tente novamente.")
        box()