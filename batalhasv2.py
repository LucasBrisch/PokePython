import utils
import random
import bag as b
import CompiladorJogo as cj
import Pokemons as p
import PokeBox as pb
party_adversario = []

import copy


def adversario():
    global party_adversario
    party_adversario = copy.deepcopy(random.sample(p.Pokemons_no_jogo, 6))
    return random.choice(party_adversario)
    
    
def pokemon_escolhido():
    utils.delay_print("Escolha um pokemon para batalhar: ")
    for i in range(len(pb.pokemon_party)):
       utils.delay_print(f"{i+1}- {pb.pokemon_party[i].nome} ")  # Acessa o nome do Pokemon
    escolha = int(input(" \n"))
    pokemon_ativo = pb.pokemon_party[escolha-1]
    return pokemon_ativo
    

def comeco_batalha ():
    pokemon_adversario = adversario()
    
    utils.delay_print (f"Seu adversário é um {pokemon_adversario.nome}!\n")
    pokemon_ativo = pokemon_escolhido()
    utils.delay_print (f"Você escolheu {pokemon_ativo.nome}!\n")
    menu_batalha (pokemon_ativo, pokemon_adversario)


def menu_batalha (pokemon_ativo, pokemon_adversario):
    utils.delay_print(f"Pokémon ativo: {pokemon_ativo.nome} - HP: {pokemon_ativo.hp}\nPokémon adversário: {pokemon_adversario.nome} - HP: {pokemon_adversario.hp}\n")
    utils.delay_print("O que você deseja fazer?\n")
    utils.delay_print("[1] - Atacar\n[2] - Trocar de pokemon\n[3] - Acessar sua bag \n[4] - Fugir\n")
    escolha = int(input())
    if escolha == 1:
        ataque(pokemon_ativo, pokemon_adversario)
    if escolha == 2:
        pokemon_ativo = trocar_pokemon()
    if escolha == 3:
        b.bag(pokemon_ativo, pokemon_adversario)
    if escolha == 4:
        fuga = random.choice([True, False])
        if fuga:
            print("Você conseguiu fugir!")
        else:
            print("Você não conseguiu fugir!")
            menu_batalha()
            
def ataque (pokemon_ativo, pokemon_adversario):
    utils.delay_print("Escolha um ataque: ")
    for i in range(len(pokemon_ativo.movimentos)):
        utils.delay_print(f"{i+1} - {pokemon_ativo.movimentos[i].nome} ")
    escolha = int(input("\n"))
    dano = pokemon_ativo.movimentos[escolha-1].dano
    tipo = pokemon_ativo.movimentos[escolha-1].tipo
    if tipo == pokemon_adversario.tipo:
        dano = dano * 0.75
    pokemon_adversario.hp -= dano
    utils.delay_print(f"{pokemon_adversario.nome} sofreu {dano} de dano!")
    if pokemon_adversario.hp <= 0:
        utils.delay_print(f"\n{pokemon_adversario.nome} foi derrotado!\n")
        random_item()
    else:
        ataque_adversario(pokemon_ativo, pokemon_adversario)

def ataque_adversario (pokemon_ativo, pokemon_adversario):
    utils.delay_print("\nO adversário está atacando!")
    pokemon_adversario_movimento = random.choice(pokemon_adversario.movimentos)
    dano = pokemon_adversario_movimento.dano
    tipo = pokemon_adversario_movimento.tipo
    utils.delay_print('\n' + pokemon_adversario_movimento.nome + ' foi usado!')
    if tipo == pokemon_ativo.tipo:
        dano = dano * 0.75
    pokemon_ativo.hp -= dano
    utils.delay_print(f"\n{pokemon_ativo.nome} sofreu {dano} de dano!\n")
    if pokemon_ativo.hp <= 0:
        utils.delay_print(f"{pokemon_ativo.nome} foi derrotado!")
        utils.delay_print("Você foi derrotado!\n Você voltou para casa...")
        cj.menu()
    else:
        menu_batalha(pokemon_ativo, pokemon_adversario)
        
def random_item():
    global item
    utils.delay_print("Você venceu a batalha!\n")
    b.obj = random.choice (["Potion", "Super Potion", "Hyper Potion", "Revive"])
    utils.delay_print (f"O adversário derrubou um(a) {b.obj}\n")
    print()
    b.receber_item ()

def trocar_pokemon():
    utils.delay_print("Escolha um pokemon para batalhar: (precione 0 para sair)\n")
    for i in range(len(pb.pokemon_party)):
       utils.delay_print(f"{i+1}- {pb.pokemon_party[i]} ")  # Acessa o nome do Pokemon
    escolha = int(input(" \n"))
    pkmn = pb.pokemon_party[escolha-1]
    if escolha == 0:
        menu_batalha()
    else:
        pokemon_ativo = p.escolhido(pkmn)
        return pokemon_ativo
    menu_batalha()
    
            
        
        

if __name__ == "__main__": 
    comeco_batalha()