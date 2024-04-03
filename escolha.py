import time
import sys

global delay_print
def delay_print(s):
    # print one character at a time
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
        
def escolha_inicial():
    global player_name, starter_pokemon, pokemon_1
    print()
    delay_print('''Olá, meu nome é Professor Carvalho, bem-vindo ao mundo dos Pokémons! Este mundo é habitado 
por criaturas chamadas Pokémons! Para algumas pessoas, os Pokémons são animais de estimação. Outros os usam para lutar. 
Eu mesmo... Estudo Pokémons como profissão.\n\nAgora me diga, qual é o seu nome?\n''')
    player_name = str(input()) 
    
    delay_print(f'''É um prazer! {player_name}, agora me diga, qual vai ser o seu pokemon inicial?\n
Squirtle(água), Charmander(fogo), Bulbasaur(grama) ou Pikachu(elétrico)? \n''')
    starter_pokemon = str(input())
    
    while starter_pokemon not in ["squirtle","água","squirtle(água)","charmander","fogo","charmander(fogo)",
    "bulbasaur","grama","bulbasaur(grama)","pikachu","elétrico","pikachu(elétrico)"]:
        print()
        delay_print("este não é um pokémon inicial válido, por favor, escolha um dos pokémons iniciais disponíveis!\n")
        ("Então, vai ser o Squirtle(água), Charmander(fogo), Bulbasaur(grama) ou Pikachu(eletrico)? ").strip().lower()
        starter_pokemon = str(input())
    if starter_pokemon in ["squirtle","água","squirtle(água)", 'agua']:
        delay_print("Você escolheu o Squirtle; ótima escolha!\n")
        pokemon_1 = 'Squirtle'
    elif starter_pokemon in ["charmander","fogo","charmander(fogo)"]:
        delay_print("Você escolheu o Charmander; ótima escolha!\n")
        pokemon_1 = 'Charmander'
    elif starter_pokemon in ["bulbasaur","grama","bulbasaur(grama)"]:
        delay_print("Você escolheu o Bulbasaur; ótima escolha!\n")
        pokemon_1 = 'Bulbasaur'
    elif starter_pokemon in ["pikachu","elétrico","pikachu(elétrico)", 'eletrico']:
        delay_print("Ah, o bom e velho Pikachu, ótima escolha!\n")
        pokemon_1 = 'Pikachu'
    delay_print(f'''Agora me diga, você gostaria de dar um apelido ao seu {pokemon_1}? 
[1] sim
[2] nao) ''')
    escolha = input()
    
    while escolha not in ["1","2"]:
        print()
        delay_print("Por favor, escolha uma opção válida!\n")
        delay_print(f'''Agora me diga, você gostaria de dar um apelido ao seu {pokemon_1}? 
[1] sim
[2] nao) ''').strip().lower() 
        escolha = input ()
    if escolha == "1":
        delay_print("Qual será o apelido do seu Pokémon? ")
        pokemon_1 = input()
        delay_print(f"Ótimo! A partir de agora, {pokemon_1} será o nome do seu Pokémon inicial!")
    elif escolha == "2":
        delay_print(f"Entendido! {pokemon_1} será o nome do seu Pokémon inicial!")

    delay_print('Agora que você escolheu seu Pokémon inicial, você está pronto para começar sua jornada! Boa sorte!\n')

    
        
if __name__ == "__main__":
    escolha_inicial()