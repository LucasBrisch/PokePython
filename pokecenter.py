import PokeBox as pb
import utils as utils
import Pokemons as p
import CompiladorJogo as cj
import batalhasv3 as b

def pokecenter():
    if not b.esta_vivo_party(pb.pokemon_party):
        utils.delay_print("Bem vindo ao PokeCenter, vejo que todos os seus pokemons estão desmaiados. Deixe-me curá-los para você.")
        for i in range(len(pb.pokemon_party)):
                pb.pokemon_party[i].hp = pb.pokemon_party[i].hp_max
        utils.delay_print_s("...")
        utils.delay_print("Seus pokemons foram curados! Até mais!\n")
        cj.menu()
    else:
        utils.delay_print("Bem vindo ao PokeCenter!")
        utils.delay_print("Deseja curar seus pokemons? (S/N)")
        resposta = input().capitalize()
        if resposta == "S":
            for i in range(len(pb.pokemon_party)):
                pb.pokemon_party[i].hp = pb.pokemon_party[i].hp_max
            utils.delay_print_s("...")
            utils.delay_print("Seus pokemons foram curados! Até mais!\n")
            cj.menu()
        else:
            utils.delay_print("Até mais!")
            cj.menu()