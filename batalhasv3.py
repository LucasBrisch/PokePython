#fazer sistema bag
#fazer verificar se o pokemon esta vivo e se tem algum vivo na party
#fazer sistema de troca de pokemon
#fazer sistema pro adversario trocar pokemon nocauteado, e o mesmo pro player

import random
import utils as utils
import Pokemons as p
import PokeBox as pb
import CompiladorJogo as cj
import requests
party_adversario = []


def ataque_efetivo(tipo_atacante, tipo_defensor):
    if tipo_atacante == "Fire" and tipo_defensor in ["Grass", "Bug", "Ice"]:
        return True
    elif tipo_atacante == "Water" and tipo_defensor in ["Fire", "Ground", "Rock"]:
        return True
    elif tipo_atacante == "Electric" and tipo_defensor in ["Water", "Flying"]:
        return True
    elif tipo_atacante == "Grass" and tipo_defensor in ["Water", "Ground", "Rock"]:
        return True
    elif tipo_atacante == "Ice" and tipo_defensor in ["Grass", "Ground", "Flying", "Dragon"]:
        return True
    elif tipo_atacante == "Fighting" and tipo_defensor in ["Normal", "Ice", "Rock", "Dark", "Steel"]:
        return True
    elif tipo_atacante == "Poison" and tipo_defensor in ["Grass", "Fairy"]:
        return True
    elif tipo_atacante == "Ground" and tipo_defensor in ["Fire", "Electric", "Poison", "Rock", "Steel"]:
        return True
    elif tipo_atacante == "Flying" and tipo_defensor in ["Grass", "Fighting", "Bug"]:
        return True
    elif tipo_atacante == "Psychic" and tipo_defensor in ["Fighting", "Poison"]:
        return True
    elif tipo_atacante == "Bug" and tipo_defensor in ["Grass", "Psychic", "Dark"]:
        return True
    elif tipo_atacante == "Rock" and tipo_defensor in ["Fire", "Ice", "Flying", "Bug"]:
        return True
    elif tipo_atacante == "Ghost" and tipo_defensor in ["Psychic", "Ghost"]:
        return True
    elif tipo_atacante == "Dragon" and tipo_defensor in ["Dragon"]:
        return True
    elif tipo_atacante == "Dark" and tipo_defensor in ["Psychic", "Ghost"]:
        return True
    elif tipo_atacante == "Steel" and tipo_defensor in ["Ice", "Rock", "Fairy"]:
        return True
    elif tipo_atacante == "Fairy" and tipo_defensor in ["Fighting", "Dragon", "Dark"]:
        return True
    else:
        return False
        

def esta_vivo(pokemon):
    if pokemon.hp > 0:
        return True
    else:
        return False
    
    

def adversario():
    global party_adversario
    for i in range(6):
        party_adversario.append(utils.criar_copia(random.choice(p.Pokemons_no_jogo)))
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
            bag()
        if escolha == 4:
            fuga = random.randint(1, 100)
            if fuga <= 50:
                print("Você conseguiu fugir!")
                cj.menu()
            else:
                print("Você não conseguiu fugir!")
                menu_batalha()
        else:
            menu_batalha(pokemon_ativo, pokemon_adversario)
            
def ataque (pokemon_ativo, pokemon_adversario):
    utils.delay_print("Escolha um ataque: ")
    for i in range(len(pokemon_ativo.movimentos)):
        utils.delay_print(f"{i+1} - {pokemon_ativo.movimentos[i].nome} ")
    escolha = int(input("\n"))
    dano = pokemon_ativo.movimentos[escolha-1].dano
    tipo = pokemon_ativo.movimentos[escolha-1].tipo
    if tipo == pokemon_adversario.tipo:
        print ("Ataque não muito efetivo!")
        dano = dano * 0.75
    else:
        if ataque_efetivo(tipo, pokemon_adversario.tipo):
            dano = dano * 1.5
            print("Ataque super efetivo!")
    pokemon_adversario.hp -= dano
    utils.delay_print(f"{pokemon_adversario.nome} sofreu {dano} de dano!")
    #aqui vai verificar se o adversario morreu, se ele estiver vivo, ele ataca, se não, ele troca de pokemon (função q eu ainda tenho q fazer)
    

def ataque_adversario (pokemon_ativo, pokemon_adversario):
    utils.delay_print("\nO adversário está atacando!")
    pokemon_adversario_movimento = random.choice(pokemon_adversario.movimentos)
    dano = pokemon_adversario_movimento.dano
    tipo = pokemon_adversario_movimento.tipo
    utils.delay_print('\n' + pokemon_adversario_movimento.nome + ' foi usado!')
    if tipo == pokemon_adversario.tipo:
        print("Ataque não muito efetivo!")
        dano = dano * 0.75
    else:
        if ataque_efetivo(tipo, pokemon_adversario.tipo):
            print("Ataque super efetivo!")
            dano = dano * 1.5
    pokemon_ativo.hp -= dano
    utils.delay_print(f"\n{pokemon_ativo.nome} sofreu {dano} de dano!\n")
    
comeco_batalha()