import random
import time
import sys

def delay_print(s):
    # print one character at a time
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

def safari():
    delay_print("Você quer encontrar um Pokémon? (s/n): ")
    escolha = input()
    if escolha == "s":
        delay_print ('''Você gostaria de ir para uma caverna ou para uma floresta?
[1] Caverna
[2] Floresta\n''')
        escolha = input()
        if escolha == "1":
            delay_print("indo para a caverna...")
            time.sleep(1)
            caverna()
        if escolha == "2":
            delay_print("indo para a floresta...")
            time.sleep(1)
            floresta()
    elif escolha == "n":
        delay_print("\nTudo bem, até a próxima!")
        exit()
    else:
        delay_print("\nEscolha inválida, tente novamente.")
        safari()
        
def caverna():
    pokemon = ' '
    pokemons_caverna = ['Zubat', 'Geodude', 'Onix', 'Machop', 'Cubone']
    delay_print("\nVocê entrou na caverna\n")
    time.sleep(1)
    delay_print("procurando um Pokémon...")
    time.sleep(1)
    pokemon = random.choice(pokemons_caverna)
    delay_print(f"\nUm {pokemon} apareceu!\n")
    delay_print('''Você quer capturar o Pokémon?
[1] sim
[2] não
''')
    escolha = input()
    if escolha == "1":
        delay_print("Pokébola vai!\n")
        time.sleep(1)
        delay_print("...")
        time.sleep(1)
        delay_print(f"Parabéns! Você capturou um {pokemon}!\n")
        #futuramente vai mandar ele pra box
    if escolha == "2":
        delay_print(f"Você fugiu de {pokemon}!")
        safari()
    
def floresta():
    pokemon = ' '
    pokemons_floresta = ['Pidgey', 'Rattata', 'Caterpie', 'Weedle', 'Sparrow']
    delay_print("\nVocê entrou na floresta")
    time.sleep(2)
    delay_print("procurando um Pokémon...")
    time.sleep(2)
    pokemon = random.choice(pokemons_floresta)
    delay_print(f"\nUm {pokemon} apareceu!")
    delay_print('''Você quer capturar o Pokémon?
[1] sim
[2] não
''')
    escolha = input()
    if escolha == "1":
        delay_print("Pokébola vai!")
        time.sleep(1)
        delay_print("...")
        time.sleep(1)
        delay_print(f"Parabéns! Você capturou um {pokemon}!")
        #futuramente vai mandar ele pra box
    if escolha == "2":
        delay_print(f"Você fugiu de {pokemon}!")
        safari()


if __name__ == "__main__":
    safari()      