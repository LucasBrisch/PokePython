import utils
import PokeBox
import Pokemons as p
        
def escolha_inicial():
    print()
    utils.delay_print('''Olá, meu nome é Professor Carvalho, bem-vindo ao mundo dos Pokémons! Este mundo é habitado 
por criaturas chamadas Pokémons! Para algumas pessoas, os Pokémons são animais de estimação. Outros os usam para lutar. 
Eu mesmo... Estudo Pokémons como profissão.\n\nAgora me diga, qual é o seu nome?\n''')
    player_name = str(input()) 
    
    utils.delay_print(f'''É um prazer! {player_name}, agora me diga, qual vai ser o seu pokemon inicial?\n
[1] Squirtle(água), [2] Charmander(fogo), [3] Bulbasaur(grama) ou [4] Pikachu(elétrico)? \n''')
    starter_pokemon = str(input())
    
    while starter_pokemon not in ["1", "2", "3", "4", "squirtle","água","squirtle(água)","charmander","fogo","charmander(fogo)",
    "bulbasaur","grama","bulbasaur(grama)","pikachu","elétrico","pikachu(elétrico)"]:
        print()
        utils.delay_print("este não é um pokémon inicial válido, por favor, escolha um dos pokémons iniciais disponíveis!\n")
        ("Então, vai ser o Squirtle(água), Charmander(fogo), Bulbasaur(grama) ou Pikachu(eletrico)? ").strip().lower()
        starter_pokemon = str(input())
    if starter_pokemon in ["1", "squirtle","água","squirtle(água)", 'agua']:
        utils.delay_print("Você escolheu o Squirtle; ótima escolha!\n")
        pokemon_1 = p.Squirtle
    elif starter_pokemon in ["2", "charmander","fogo","charmander(fogo)"]:
        utils.delay_print("Você escolheu o Charmander; ótima escolha!\n")
        pokemon_1 = p.Charmander
    elif starter_pokemon in ["3", "bulbasaur","grama","bulbasaur(grama)"]:
        utils.delay_print("Você escolheu o Bulbasaur; ótima escolha!\n")
        pokemon_1 = p.Bulbasaur
    elif starter_pokemon in ["4", "pikachu","elétrico","pikachu(elétrico)", 'eletrico']:
        utils.delay_print("Ah, o bom e velho Pikachu, ótima escolha!\n")
        pokemon_1 = p.Pikachu

    utils.delay_print('\nAgora que você escolheu seu Pokémon inicial, você está pronto para começar sua jornada! Boa sorte!\n')
    utils.player_name = player_name
    PokeBox.pokemon_party.append(utils.criar_copia(pokemon_1))
            

    
        
if __name__ == "__main__":
    escolha_inicial()