import utils
import escolha as e
import CompiladorJogo as cj
import Pokemons as p

global pokemon_party, pokemon_box
pokemon_party = [ (p.Charizard)]
pokemon_box = [p.Entei]   
    
def pc():
    utils.delay_print("Bem vindo ao pc, o que você deseja fazer?\n")
    utils.delay_print("[1] - Adicionar um pokemon a sua party\n[2] - Adicionar um pokémon a sua box\n[3] - Ver a sua party\n[4] - Ver a sua box\n[5] - Voltar ao menu\n")
    escolha = int(input())
    if escolha == 1:
        if len(pokemon_party) == 6:
            utils.delay_print("Sua party está cheia, você precisa guardar um pokémon na sua box para adicionar outro.\n")
            pc()
        elif len(pokemon_box) == 0:
            utils.delay_print("Sua box está vazia, você precisa adicionar um pokémon a sua box para adicionar a sua party.\n")
            pc()
        else:
            adicionar_pokemon_party()
    elif escolha == 2:
        if len(pokemon_party) == 1:
            utils.delay_print("Sua party só tem um pokémon, você não pode guardar ele na box.\n")
            pc()
        else:
            guardar_pokemon()
    elif escolha == 3:
        ver_party()
    elif escolha == 4:
        ver_box()
    elif escolha == 5:
        cj.menu()
    else:
        utils.delay_print("Escolha inválida, tente novamente.\n")
        pc()

def guardar_pokemon():
    utils.delay_print("Qual Pokémon você deseja guardar na sua PokéBox?\n")
    for i in range(len(pokemon_party)):
        utils.delay_print(f"{i+1} - {pokemon_party[i].nome}")
    print()
    escolha = int(input())
    pokemon_box.append(pokemon_party[escolha-1])
    pokemon_party.pop(escolha-1)
    utils.delay_print("Pokémon guardado com sucesso!\n")
    pc()

def adicionar_pokemon_party():
    utils.delay_print("Qual Pokémon você deseja adicionar a sua party?\n")
    for i in range(len(pokemon_box)):
        utils.delay_print(f"{i+1} - {pokemon_box[i].nome}")
    print()
    escolha = int(input())
    pokemon_party.append(pokemon_box[escolha-1])
    pokemon_box.pop(escolha-1)
    utils.delay_print("Pokémon adicionado com sucesso!\n")
    pc()

def ver_party():
    utils.delay_print("Aqui está a sua party: \n")
    for i in range(len(pokemon_party)):
        utils.delay_print(f"{i+1} - {pokemon_party[i].nome}\n")
    pc()

def ver_box():
    utils.delay_print("Aqui está a sua PokéBox: \n")
    for i in range(len(pokemon_box)):
        utils.delay_print(f"{i+1} - {pokemon_box[i].nome}\n")
    pc()