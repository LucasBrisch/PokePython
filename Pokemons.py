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
Zubat = Pokemon('Zubat', 5, 100, 'Poison', [Tackle, Leech_Life], 'Poison')
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

def escolhido(pokemon_ativo):
    if pokemon_ativo == "Pikachu":
        return Pikachu
    elif pokemon_ativo == "Charmander":
        return Charmander
    elif pokemon_ativo == "Squirtle":
        return Squirtle
    elif pokemon_ativo == "Bulbasaur":
        return Bulbasaur
    elif pokemon_ativo == "Zubat":
        return Zubat
    elif pokemon_ativo == "Geodude":
        return Geodude
    elif pokemon_ativo == "Onix":
        return Onix
    elif pokemon_ativo == "Machop":
        return Machop
    elif pokemon_ativo == "Cubone":
        return Cubone
    elif pokemon_ativo == "Mewtwo":
        return Mewtwo
    elif pokemon_ativo == "Mew":
        return Mew
    elif pokemon_ativo == "Articuno":
        return Articuno
    elif pokemon_ativo == "Zapdos":
        return Zapdos
    elif pokemon_ativo == "Moltres":
        return Moltres
    elif pokemon_ativo == "Groundon":
        return Groundon
    elif pokemon_ativo == 'Kyogre':
        return Kyogre
    elif pokemon_ativo == 'Lugia':
        return Lugia
    elif pokemon_ativo == 'Suicune':
        return Suicune
    elif pokemon_ativo == 'Entei':
        return Entei
    elif pokemon_ativo == 'Raikou':
        return Raikou
    elif pokemon_ativo == 'Celebi':
        return Celebi
    elif pokemon_ativo == 'Caterpie':
        return Caterpie
    elif pokemon_ativo == 'Bellsprout':
        return Bellsprout
    elif pokemon_ativo == 'Oddish':
        return Oddish
    elif pokemon_ativo == 'Rattata':
        return Rattata
    elif pokemon_ativo == 'Pidgey':
        return Pidgey

pokemon_classes = {
        "Bulbasaur": Bulbasaur,
        "Charmander": Charmander,
        "Squirtle": Squirtle,
        "Pikachu": Pikachu,
        "Zubat": Zubat,
        "Geodude": Geodude,
        "Onix": Onix,
        "Machop": Machop,
        "Cubone": Cubone,
        "Mewtwo": Mewtwo,
        "Mew": Mew,
        "Articuno": Articuno,
        "Zapdos": Zapdos,
        "Moltres": Moltres,
        "Groundon": Groundon,
        "Pidgey": Pidgey,
        "Rattata": Rattata,
        "Oddish": Oddish,
        "Bellsprout": Bellsprout,
        "Caterpie": Caterpie,
        "Celebi": Celebi,
        "Raikou": Raikou,
        "Entei": Entei,
        "Suicune": Suicune,
        "Lugia": Lugia,
        "Kyogre": Kyogre
    }

