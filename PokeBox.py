import utils
import escolha as e
import CompiladorJogo as cj
import Pokemons as p

global pokemon_party, pokemon_box
pokemon_party = [ (p.Pikachu),(p.Groudon)]
pokemon_box = []   
    
def player_party():
    print()
    utils.delay_print(f'''\nOlá, {utils.player_name}! Essa é a sua equipe de Pokémons atual:''')
    for i in pokemon_party:
        utils.delay_print(f"\n{i.nome}")
    utils.delay_print('''\nGostaria de acessar a sua box para editar sua party?
[1] sim
[2] não\n''')
    escolha = input()
    if escolha == "1":
        box()
        
    elif escolha == "2":
        utils.delay_print('Voltando para o menu principal...\n')
        cj.menu()
    else:
        utils.delay_print("Escolha inválida, tente novamente.\n")
        player_party()        
        
if __name__ == "__main__":
    player_party()
    
def box():
    utils.delay_print(f'''Olá, {utils.player_name}! Essa é a sua PokéBox atual:''')
    for pokemon in pokemon_box:
        utils.delay_print(f"\n{pokemon.nome}")
    utils.delay_print('''\nO que você deseja fazer agora?
[1] Guardar um pokemon da sua party na sua PokéBox
[2] Adicionar um Pokémon da sua box a sua equipe de Pokémons
[3] Sair\n''')
    escolha = input()
    if escolha == "1":
        utils.delay_print("Qual Pokémon você deseja adicionar à sua PokéBox? (Digite 'exit' para voltar)\n")
        for pokemon in pokemon_party:
            utils.delay_print (f"{pokemon} \n")
            
        escolha = input().capitalize()
        while escolha not in pokemon_party:
            if escolha == "Exit":
                box()
            else:
                utils.delay_print("\nPor favor, escolha um Pokémon válido!\n")
        if len(pokemon_party) == 1:
            utils.delay_print("\nSua party ficará vazia! Por favor, adicione um Pokémon antes de remover outro.\n")
            box()
        elif len(pokemon_party) > 1:    
            pokemon_box.append(escolha)
            pokemon_party.remove(escolha)
            utils.delay_print(f"\n{escolha} foi removido de sua party e adicionado à sua PokéBox!\n")
            box()
    elif escolha == "2":
        utils.delay_print("Qual Pokémon você deseja adicionar à sua party? (Digite 'exit' para voltar)\n")
        for pokemon in pokemon_box:
            utils.delay_print(f"{pokemon} \n")
        escolha = input().capitalize()
        while escolha not in pokemon_box:
            if escolha == "Exit":
                box()
            else:    
                utils.delay_print("\nPor favor, escolha um Pokémon válido!\n")
        if len(pokemon_party) == 6:
            utils.delay_print("\nSua party está cheia! Por favor, remova um Pokémon antes de adicionar outro.\n")
            box()
        elif len(pokemon_party) < 6:
            pokemon_party.append(escolha)
            escolha = escolha.capitalize()
            pokemon_box.remove(escolha)
            utils.delay_print(f"\n{escolha} foi removido de sua PokéBox e adicionado à sua party!\n")
            box()
    elif escolha == "3":
        utils.delay_print("Saindo...")
        cj.menu()
    
    else:
        utils.delay_print("Escolha inválida, tente novamente.")
        box()