import time
import sys


pokedex = ['Charmander', 'chameleon', 'Charizard', 'Squirtle', 'Wartortle', 'Blastoise', 'Bulbasaur', 'Ivysaur', 'Venusaur']

def delay_print(s):
    # print one character at a time
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
        
def escolha_inicial():
    global player_name, starter_pokemon
    print()
    player_name = str(input('''Olá, meu nome é Professor Carvalho, bem-vindo ao mundo dos Pokémons! Este mundo é habitado 
    por criaturas chamadas Pokémons! Para algumas pessoas, os Pokémons são animais de estimação. Outros os usam para lutar. 
    Eu mesmo... Estudo Pokémons como profissão.\n\nAgora me diga, qual é o seu nome? ''')).strip().lower().title()
    starter_pokemon = str(input(f'''É um prazer! {player_name}, agora me diga, qual vai ser o seu pokemon inicial?
    \n Squirtle(água), Charmander(fogo), Bulbasaur(grama) ou Pikachu(elétrico)? ''')).strip().lower()
    while starter_pokemon not in ["squirtle","água","squirtle(água)","charmander","fogo","charmander(fogo)",
    "bulbasaur","grama","bulbasaur(grama)","pikachu","elétrico","pikachu(elétrico)"]:
        print()
        print("este não é um pokémon inicial válido, por favor, escolha um dos pokémons iniciais disponíveis!\n")
        starter_pokemon = input("Então, vai ser o Squirtle(água), Charmander(fogo), Bulbasaur(grama) ou Pikachu(eletrico)? ").strip().lower()
    if starter_pokemon in ["squirtle","água","squirtle(água)", 'agua']:
        print("Você escolheu o Squirtle; ótima escolha!\n")
        pokemon_1 = 'Squirtle'
    elif starter_pokemon in ["charmander","fogo","charmander(fogo)"]:
        print("Você escolheu o Charmander; ótima escolha!\n")
        pokemon_1 = 'Charmander'
    elif starter_pokemon in ["bulbasaur","grama","bulbasaur(grama)"]:
        print("Você escolheu o Bulbasaur; ótima escolha!\n")
        pokemon_1 = 'Bulbasaur'
    elif starter_pokemon in ["pikachu","elétrico","pikachu(elétrico)", 'eletrico']:
        print("Ah, o bom e velho Pikachu, ótima escolha!\n")
        pokemon_1 = 'Pikachu'
    escolha = input(f"Agora me diga, você gostaria de dar um apelido ao seu {pokemon_1}? (sim/nao) ").strip().lower()
    if escolha == "sim":
        pokemon_1 = str(input("Qual será o apelido do seu Pokémon? ")).strip().lower().title()
        print(f"Ótimo! A partir de agora, {pokemon_1} será o nome do seu Pokémon inicial!")
    elif escolha == "nao":
        print(f"Entendido! {pokemon_1} será o nome do seu Pokémon inicial!")
        print('Agora que você escolheu seu Pokémon inicial, você está pronto para começar sua jornada! Boa sorte!\n')
    
    
def pokemon_team():
    global pokemon_1, pokemon_2, pokemon_3, pokemon_4, pokemon_5, pokemon_6
    print(f"Seu time de pokémons é: \n{pokemon_1} \n{pokemon_2} \n{pokemon_3} \n{pokemon_4} \n{pokemon_5} \n{pokemon_6}")
    
        
if __name__ == "__main__":
    escolha_inicial()