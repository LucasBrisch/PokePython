Pokemons_no_jogo = ['Zubat', 'Geodude', 'Onix', 'Machop', 'Cubone', 'Mewtwo', 'Mew', 'Articuno', 'Zapdos', 
'Moltres', 'Groundon', 'Pidgey', 'Rattata', 'Oddish', 'Bellsprout', 'Caterpie', 'Celebi', 'Raikou',
'Entei', 'Suicune', 'Lugia', 'Kyogre', 'Charmander', 'Squirtle', 'Bulbasaur', 'Pikachu']

# Deve existir um jeito melhor de fazer isso........

class Pokemon:
    def __init__(self, nome, nivel, hp, movimentos, tipo):
        self.nome = nome
        self.nivel = nivel
        self.hp = hp
        self.movimentos = movimentos
        self.tipo = tipo

class Movimento:
    def __init__(self, nome, dano, tipo):
        self.nome = nome
        self.dano = dano
        self.tipo = tipo

def batalha(pokemon1, pokemon2):
    # Implemente a lógica da batalha aqui
    pass

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


# Pokemons
Zubat = Pokemon('Zubat', 5, 100, 'Poison', [Tackle, Leech_Life])
Geodude = Pokemon('Geodude', 5, 100, [Tackle, Rock_Throw], 'Rock')
Onix = Pokemon('Onix', 20, 100, [Tackle, Rock_Throw], 'Rock')
Machop = Pokemon('Machop', 5, 100, [Karate_Chop, Dig], 'Fighting')
Cubone = Pokemon('Cubone', 5, 100, [Bone_club, Dig], 'Ground')
Mewtwo = Pokemon('Mewtwo', 70, 100, [Psychic, Thunderbolt], 'Psychic')
Mew = Pokemon('Mew', 70, 100, [Psychic, Psybeam], 'Psychic')
Articuno = Pokemon('Articuno', 70, 100, [Ice_Beam, Blizzard], 'Ice')
Zapdos = Pokemon('Zapdos', 70, 100, [Thunder, Thunderbolt], 'Electric')
Moltres = Pokemon('Moltres', 70, 100, [Fire_Blast, Flamethrower], 'Fire')
Groundon = Pokemon('Groundon', 70, 100, [Earthquake, Fire_Blast], 'Ground')
Pidgey = Pokemon('Pidgey', 5, 100, [Tackle, Gust], 'Flying')
Rattata = Pokemon('Rattata', 5, 100, [Tackle, Quick_Attack], 'Normal')
Oddish = Pokemon('Oddish', 5, 100, [Absorb, Acid], 'Grass')
Bellsprout = Pokemon('Bellsprout', 5, 100, [Vine_Whip, Acid], 'Grass')
Caterpie = Pokemon('Caterpie', 5, 100, [Tackle, String_Shot], 'Bug')
Celebi = Pokemon('Celebi', 70, 100, [Psychic, Giga_Drain], 'Grass')
Raikou = Pokemon('Raikou', 70, 100, [Thunder, Thunderbolt], 'Electric')
Entei = Pokemon('Entei', 70, 100, [Fire_Blast, Flamethrower], 'Fire')
Suicune = Pokemon('Suicune', 70, 100, [Surf, Blizzard], 'Ice')
Lugia = Pokemon('Lugia', 70, 100, [Hydro_Pump, Psychic], 'Psychic')
Kyogre = Pokemon('Kyogre', 70, 100, [Hydro_Pump, Surf], 'Water')
Charmander = Pokemon('Charmander', 5, 80, [Tackle, Ember], 'Fire')
Squirtle = Pokemon('Squirtle', 5, 70, [Tackle, Water_Gun], 'Water')
Bulbasaur = Pokemon('Bulbasaur', 5, 90, [Tackle, Vine_Whip], 'Grass')
Pikachu = Pokemon('Pikachu', 5, 100, [Tackle, Thunderbolt], 'Electric')

