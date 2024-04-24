import random
import utils
import Pokemons as p
import bag as b

pokemon_party = ["Bulbasaur", "Charmander", "Squirtle"]

def adversario():
    adversario = random.choice(["Bulbasaur", "Charmander", "Squirtle"])
    if adversario == "Bulbasaur":
        return p.Bulbasaur
    elif adversario == "Charmander":
        return p.Charmander
    elif adversario == "Squirtle":
        return p.Squirtle

def pokemon_escolhido ():
    utils.delay_print("Escolha um pokemon para batalhar: ")
    for i in range(len(pokemon_party)):
       utils.delay_print(f"{i+1}- {pokemon_party[i]} ")
    escolha = int(input(" \n"))
    if escolha == 1:
        return p.Bulbasaur
    elif escolha == 2:
        return p.Charmander
    elif escolha == 3:
        return p.Squirtle

def esquivar():
    random_number = random.randint(1, 100)
    if random_number <= 30:
        return True
    else:
        return False
    
def comeco_batalha ():
    pokemon_adversario = adversario()
    
    utils.delay_print (f"Seu adversário é um {pokemon_adversario.nome}!\n")
    pokemon_ativo = pokemon_escolhido()
    utils.delay_print (f"Você escolheu {pokemon_ativo.nome}!\n")
    batalha (pokemon_ativo, pokemon_adversario)

def batalha (pokemon_ativo, pokemon_adversario):
    
    while pokemon_ativo.hp and pokemon_adversario.hp > 0:
        utils.delay_print(f"{pokemon_ativo.nome} - HP: {pokemon_ativo.hp} ")
        utils.delay_print(f"{pokemon_adversario.nome} - HP: {pokemon_adversario.hp}")
        utils.delay_print("\nVocê deseja realizar um ataque e continuar a batalha? S/N: ")
        escolha = input().capitalize()
        if escolha == "S":
            ataque(pokemon_ativo, pokemon_adversario)
        else:
            utils.delay_print("Você desistiu da batalha!")
            break
    if pokemon_ativo.hp <= 0:
        utils.delay_print("Você foi derrotado!")
    elif pokemon_adversario.hp <= 0:
        utils.delay_print("Você venceu a batalha!")
        item = random.choice (["Potion", "Super Potion", "Hyper Potion", "Revive"])
        utils.delay_print (f"O adversário derrubou um(a) {item}")
        b.receber_item ()
def ataque (pokemon_ativo, pokemon_adversario):
    utils.delay_print("Escolha um ataque: ")
    for i in range(len(pokemon_ativo.movimentos)):
        utils.delay_print(f"{i+1} - {pokemon_ativo.movimentos[i].nome}")
    escolha = int(input("\n"))
    dano = pokemon_ativo.movimentos[escolha-1].dano
    tipo = pokemon_ativo.movimentos[escolha-1].tipo
    if tipo == pokemon_adversario.tipo:
        dano = dano * 0.75
    pokemon_adversario.hp -= dano
    utils.delay_print(f"{pokemon_adversario.nome} sofreu {dano} de dano!")
    if pokemon_adversario.hp <= 0:
        utils.delay_print(f"{pokemon_adversario.nome} foi derrotado!")
        batalha(pokemon_ativo, pokemon_adversario)
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
        batalha(pokemon_ativo, pokemon_adversario)
    else:
        batalha(pokemon_ativo, pokemon_adversario)
    
        
def mochila ():
    utils.delay_print("O que você deseja usar?\n")
    for i in range(len(utils.mochila)):
        utils.delay_print(f"{i+1} - {utils.mochila[i]}")
    escolha = int(input())
    if escolha in [1, 2, 3]:
        utils.delay_print(f"Você usou {utils.mochila[escolha-1]}!")
        pocao = utils.mochila[escolha-1]
        utils.mochila.remove(pocao)
        cura(pocao)
    elif escolha == 4:
        revive()
        

def revive ():
    utils.delay_print("Escolha um pokemon para reviver: ")
    for i in range(len(pokemon_party)):
       utils.delay_print(f"{i+1} - {pokemon_party[i]}")
    escolha = int(input())
    
    
comeco_batalha()