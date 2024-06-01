import utils
import batalhasv3 as b
import CompiladorJogo as cj
import Pokemons as p
import random
import copy
import time
import sys
import PokeBox as pb

player_bag = [p.Hyper_Potion]

def delay_print(s):
    # print one character at a time
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)

def recompensa():
    itens = [p.Potion, p.Super_Potion, p.Hyper_Potion, p.Revive]
    reward = random.choice(itens)
    if reward in player_bag:
        reward.qtd += 1
        delay_print (f"Você recebeu mais um(a) {reward.nome}!\n")
        print(f"{reward.qtd} {reward.nome}(s) na sua mochila\n")
    else:
        player_bag.append(reward)
        reward.qtd += 1
        delay_print (f"Você recebeu um(a) {reward.nome}!\n")    
        delay_print(f"{reward.qtd} {reward.nome}(s) na sua mochila\n")
        
def bag(pokemon_ativo, pokemon_adversario):
    print("Selecione um item da sua mochila: (para voltar digite 0)")
    for i, item in enumerate(player_bag):
        delay_print(f"{i+1}. {item.nome} x ({item.qtd})")
    
    choice = int(input("\n"))
    if choice == 0:
        b.menu_batalha(pokemon_ativo, pokemon_adversario)
    
    else:
        choice = int(choice) - 1
        item = player_bag[choice]
        usar_item(item, pokemon_ativo, pokemon_adversario)
    

def usar_item(item, pokemon_ativo, pokemon_adversario):
    if item.cura > 0:
        for i in range(len(pb.pokemon_party)):
            delay_print(f"{i+1}- {pb.pokemon_party[i].nome} ")
        delay_print("\nQual pokemon deseja curar? (para voltar digite 0)\n")
        escolha = int(input())
        if escolha == 0:
            bag()
        else:
            pokemon = pb.pokemon_party[escolha-1]
            if pokemon.hp == pokemon.hp_max:
                delay_print(f"{pokemon.nome} já está com a vida cheia!\n")
                usar_item(item)
            elif pokemon.hp <= 0:
                delay_print(f"{pokemon.nome} está desmaiado!\n")
                usar_item(item)
            else:
                pokemon.hp += item.cura
                if pokemon.hp > pokemon.hp_max:
                    diferenca = abs(item.cura - pokemon.hp)
                    pokemon.hp = pokemon.hp_max
                    delay_print(f"{pokemon.nome} foi curado em {diferenca} pontos de vida!\n")
                else:
                    delay_print(f"{pokemon.nome} foi curado em {item.cura} pontos de vida!\n")
                item.qtd -= 1
                if item.qtd == 0:
                    player_bag.remove(item)
                    b.menu_batalha(pokemon_ativo, pokemon_adversario)
            
    elif item.nome == "Revive":
        revive()
        item.qtd -= 1
        if item.qtd == 0:
            player_bag.remove(item)
            b.menu_batalha(pokemon_ativo, pokemon_adversario)
        
def revive():
    for i in range(len(pb.pokemon_party)):
        delay_print(f"{i+1}- {pb.pokemon_party[i].nome} ")
    delay_print("\nQual pokemon deseja reviver? (para voltar digite 0)\n")
    escolha = int(input())
    if escolha == 0:
        bag()
    else:
        pokemon = pb.pokemon_party[escolha-1]
        if pokemon.hp > 0:
            delay_print(f"{pokemon.nome} já está vivo!\n")
            revive()
        else:
            pokemon.hp = pokemon.hp_max/2
            delay_print(f"{pokemon.nome} foi revivido!\n")

        

if __name__ == "__main__":
    
    bag()
    
    

