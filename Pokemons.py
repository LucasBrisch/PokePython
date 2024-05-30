# Description: Arquivo que contém as classes de Pokemons, Movimentos e itens do jogo.

class Pokemon:
    def __init__(self, nome, nivel, hp, movimentos, tipo, hp_max):
        self.nome = nome
        self.nivel = nivel
        self.hp = hp
        self.movimentos = movimentos
        self.tipo = tipo
        self.hp_max = hp_max

class Movimento:
    def __init__(self, nome, dano, tipo):
        self.nome = nome
        self.dano = dano
        self.tipo = tipo
        
class Item: 
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

# Movimentos
Tackle = Movimento('Tackle', 10, 'Normal')
Leech_Life = Movimento('Leech Life', 15, 'Bug')
Rock_Throw = Movimento('Rock Throw', 20, 'Rock')
iron_tail = Movimento('Iron Tail', 30, 'Steel')
Karate_Chop = Movimento('Karate Chop', 25, 'Fighting')
Dig = Movimento('Dig', 30, 'Ground')
Thunderbolt = Movimento('Thunderbolt', 35, 'Electric')
Ember = Movimento('Ember', 30, 'Fire')
Water_Gun = Movimento('Water Gun', 35, 'Water')
Vine_Whip = Movimento('Vine Whip', 25, 'Grass')
Confusion = Movimento('Confusion', 30, 'Psychic')
Ice_Beam = Movimento('Ice Beam', 35, 'Ice')
Thunder = Movimento('Thunder', 40, 'Electric')
Fire_Blast = Movimento('Fire Blast', 40, 'Fire')
Hydro_Pump = Movimento('Hydro Pump', 40, 'Water')
Solar_Beam = Movimento('Solar Beam', 40, 'Grass')
Psychic = Movimento('Psychic', 40, 'Psychic')
Blizzard = Movimento('Blizzard', 45, 'Ice')
Thunderbolt = Movimento('Thunderbolt', 45, 'Electric')
Flamethrower = Movimento('Flamethrower', 45, 'Fire')
Surf = Movimento('Surf', 45, 'Water')
Giga_Drain = Movimento('Giga Drain', 45, 'Grass')
Psybeam = Movimento('Psybeam', 45, 'Psychic')
Bone_club = Movimento('Bone club', 45, 'Ground')
Earthquake = Movimento('Earthquake', 45, 'Ground')
Quick_Attack = Movimento('Quick Attack', 45, 'Normal')
Absorb = Movimento('Absorb', 45, 'Grass')
Acid = Movimento('Acid', 45, 'Poison')
String_Shot = Movimento('String Shot', 45, 'Bug')
Vine_Whip = Movimento('Vine Whip', 25, 'Grass')
Gust = Movimento('Gust', 45, 'Flying')
#########################################################################


# Pokemons
Zubat = Pokemon('Zubat', 5, 100, [Tackle, Leech_Life], 'Poison', 100)
Geodude = Pokemon('Geodude', 5, 100, [Tackle, Rock_Throw], 'Rock', 100)
Onix = Pokemon('Onix', 20, 100, [Tackle, Rock_Throw], 'Rock', 100)
Machop = Pokemon('Machop', 5, 100, [Karate_Chop, Dig], 'Fighting', 100)
Cubone = Pokemon('Cubone', 5, 100, [Bone_club, Dig], 'Ground', 100)
Mewtwo = Pokemon('Mewtwo', 70, 100, [Psychic, Thunderbolt], 'Psychic', 100)
Mew = Pokemon('Mew', 70, 100, [Psychic, Psybeam], 'Psychic', 100)
Articuno = Pokemon('Articuno', 70, 100, [Ice_Beam, Blizzard], 'Ice', 100)
Zapdos = Pokemon('Zapdos', 70, 100, [Thunder, Thunderbolt], 'Electric', 100)
Moltres = Pokemon('Moltres', 70, 100, [Fire_Blast, Flamethrower], 'Fire', 100)
Groundon = Pokemon('Groundon', 70, 100, [Earthquake, Fire_Blast], 'Ground', 100)
Pidgey = Pokemon('Pidgey', 5, 100, [Tackle, Gust], 'Flying', 100)
Rattata = Pokemon('Rattata', 5, 100, [Tackle, Quick_Attack], 'Normal', 100)
Oddish = Pokemon('Oddish', 5, 100, [Absorb, Acid], 'Grass', 100)
Bellsprout = Pokemon('Bellsprout', 5, 100, [Vine_Whip, Acid], 'Grass', 100)
Caterpie = Pokemon('Caterpie', 5, 100, [Tackle, String_Shot], 'Bug', 100)
Celebi = Pokemon('Celebi', 70, 100, [Psychic, Giga_Drain], 'Grass', 100)
Raikou = Pokemon('Raikou', 70, 100, [Thunder, Thunderbolt], 'Electric', 100)
Entei = Pokemon('Entei', 70, 100, [Fire_Blast, Flamethrower], 'Fire', 100)
Suicune = Pokemon('Suicune', 70, 100, [Surf, Blizzard], 'Ice', 100)
Lugia = Pokemon('Lugia', 70, 100, [Hydro_Pump, Psychic], 'Psychic', 100)
Kyogre = Pokemon('Kyogre', 70, 100, [Hydro_Pump, Surf], 'Water', 100)
Charmander = Pokemon('Charmander', 5, 80, [Tackle, Ember], 'Fire', 80)
Squirtle = Pokemon('Squirtle', 5, 70, [Tackle, Water_Gun], 'Water', 70)
Bulbasaur = Pokemon('Bulbasaur', 5, 90, [Tackle, Vine_Whip], 'Grass', 90)
Pikachu = Pokemon('Pikachu', 5, 100, [Tackle, Thunderbolt], 'Electric', 100)
#########################################################################

# Itens
Pocao = Item('Pocao', 'Recupera 20 de HP')
#########################################################################

#essa lista tb servirá como um banco de dados para os pokemons que o jogador poderá capturar, vulgo Pokedex
Pokemons_no_jogo = [Zubat, Geodude, Onix, Machop, Cubone, Mewtwo, Mew, Articuno, Zapdos, Moltres, Groundon, Pidgey, Rattata,
Oddish, Bellsprout, Caterpie, Celebi, Raikou, Entei, Suicune, Lugia, Kyogre, Charmander, Squirtle, Bulbasaur, Pikachu]


