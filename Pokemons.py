# Description: Arquivo que contém as classes de Pokemons, Movimentos e itens do jogo.
import utils

class Pokemon:
    def __init__(self, nome, nivel, hp, movimentos, tipo, hp_max, xp_max, xp = 0, evolucao=None, nivel_evolucao=None):
        self.nome = nome
        self.nivel = nivel
        self.hp = hp
        self.movimentos = movimentos
        self.tipo = tipo
        self.hp_max = hp_max
        self.xp = xp
        self.xp_max = xp_max
        self.evolucao = evolucao
        self.nivel_evolucao = nivel_evolucao


class Movimento:
    def __init__(self, nome, dano, tipo):
        self.nome = nome
        self.dano = dano
        self.tipo = tipo
        
class Pocao: 
    def __init__(self, nome, descricao, cura, qtd, condicao = False):
        self.nome = nome
        self.descricao = descricao
        self.cura = cura
        self.qtd = qtd
        self.condicao = condicao
        

def nivel_up(pkmn):
        pkmn.nivel += 1
        pkmn.hp_max += 10
        pkmn.xp = 0
        pkmn.xp_max = int(pkmn.xp_max * 1.1)
        if pkmn.evolucao and pkmn.nivel >= pkmn.nivel_evolucao:
            utils.delay_print(f"Parabéns! Seu {pkmn.nome} evoluiu para {pkmn.evolucao.nome}!")
            pkmn = pkmn.evolucao
        else:
            utils.delay_print(f"Parabéns! Seu {pkmn.nome} subiu de nível! Nível atual: {pkmn.nivel}!")
            
#itens
Potion = Pocao('Potion', 'Cura 20 de HP', 20, 0)
Super_Potion = Pocao('Super Potion', 'Cura 50 de HP', 50, 0)
Hyper_Potion = Pocao('Hyper Potion', 'Cura 200 de HP', 200, 0)
Revive = Pocao('Revive', 'Revive um pokemon com 50% de HP', 0, 0, True)
        
# Movimentos
Tackle = Movimento('Tackle', 40, 'Normal')
Leech_Life = Movimento('Leech Life', 20, 'Bug')
Rock_Throw = Movimento('Rock Throw', 50, 'Rock')
Karate_Chop = Movimento('Karate Chop', 50, 'Fighting')
Dig = Movimento('Dig', 80, 'Ground')
Bone_Club = Movimento('Bone Club', 65, 'Ground')
Psychic = Movimento('Psychic', 90, 'Psychic')
Thunderbolt = Movimento('Thunderbolt', 90, 'Electric')
Psybeam = Movimento('Psybeam', 65, 'Psychic')
Ice_Beam = Movimento('Ice Beam', 90, 'Ice')
Blizzard = Movimento('Blizzard', 110, 'Ice')
Thunder = Movimento('Thunder', 110, 'Electric')
Fire_Blast = Movimento('Fire Blast', 110, 'Fire')
Flamethrower = Movimento('Flamethrower', 90, 'Fire')
Earthquake = Movimento('Earthquake', 100, 'Ground')
Gust = Movimento('Gust', 40, 'Flying')
Quick_Attack = Movimento('Quick Attack', 40, 'Normal')
Absorb = Movimento('Absorb', 20, 'Grass')
Acid = Movimento('Acid', 40, 'Poison')
Vine_Whip = Movimento('Vine Whip', 45, 'Grass')
String_Shot = Movimento('String Shot', 0, 'Bug')
Giga_Drain = Movimento('Giga Drain', 75, 'Grass')
Surf = Movimento('Surf', 90, 'Water')
Hydro_Pump = Movimento('Hydro Pump', 110, 'Water')
Water_Gun = Movimento('Water Gun', 40, 'Water')
Ember = Movimento('Ember', 40, 'Fire')
Scratch = Movimento('Scratch', 40, 'Normal')
Wing_Attack = Movimento('Wing Attack', 60, 'Flying')
Hyper_Beam = Movimento('Hyper Beam', 150, 'Normal')
Bubble = Movimento('Bubble', 40, 'Water')
Bug_Bite = Movimento('Bug Bite', 60, 'Bug')
Defense_Curl = Movimento('Defense Curl', 0, 'Normal')
Harden = Movimento('Harden', 0, 'Normal')
Teleport = Movimento('Teleport', 0, 'Psychic')
Hypnosis = Movimento('Hypnosis', 0, 'Psychic')
Shadow_Ball = Movimento('Shadow Ball', 80, 'Ghost')
Lick = Movimento('Lick', 30, 'Ghost')
Magical_Leaf = Movimento('Magical Leaf', 60, 'Grass')
Drill_Peck = Movimento('Drill Peck', 80, 'Flying')
Flame_Wheel = Movimento('Flame Wheel', 60, 'Fire')
Bubble_Beam = Movimento('Bubble Beam', 65, 'Water')
Solar_Beam = Movimento('Solar Beam', 120, 'Grass')
Thunder_Punch = Movimento('Thunder Punch', 75, 'Electric')
Ice_Punch = Movimento('Ice Punch', 75, 'Ice')
Fire_Punch = Movimento('Fire Punch', 75, 'Fire')
Leaf_Blade = Movimento('Leaf Blade', 90, 'Grass')
Dragon_Rage = Movimento('Dragon Rage', 40, 'Dragon')
Dragon_Breath = Movimento('Dragon Breath', 60, 'Dragon')
Iron_Tail = Movimento('Iron Tail', 100, 'Steel')
Aqua_Jet = Movimento('Aqua Jet', 40, 'Water')
Aqua_Tail = Movimento('Aqua Tail', 90, 'Water')
Air_Slash = Movimento('Air Slash', 75, 'Flying')
Crunch = Movimento('Crunch', 80, 'Dark')
Moonblast = Movimento('Moonblast', 95, 'Fairy')
Meteor_Mash = Movimento('Meteor Mash', 90, 'Steel')
Aura_Sphere = Movimento('Aura Sphere', 80, 'Fighting')
Close_Combat = Movimento('Close Combat', 120, 'Fighting')
Dragon_Claw = Movimento('Dragon Claw', 80, 'Dragon')
Force_Palm = Movimento('Force Palm', 60, 'Fighting')
Rock_Smash = Movimento('Rock Smash', 40, 'Fighting')
Swift = Movimento('Swift', 60, 'Normal')
Body_Slam = Movimento('Body Slam', 85, 'Normal')
Bite = Movimento('Bite', 60, 'Dark')
Pursuit = Movimento('Pursuit', 40, 'Dark')
Take_Down = Movimento('Take Down', 90, 'Normal')
Confusion = Movimento('Confusion', 50, 'Psychic')
Psycho_Cut = Movimento('Psycho Cut', 70, 'Psychic')
Dragon_Pulse = Movimento('Dragon Pulse', 85, 'Dragon')
Razor_Leaf = Movimento('Razor Leaf', 55, 'Grass')
Slam = Movimento('Slam', 80, 'Normal')
Mega_Kick = Movimento('Mega Kick', 120, 'Normal')
Aeroblast = Movimento('Aeroblast', 100, 'Flying')
Origin_Pulse = Movimento('Origin Pulse', 110, 'Water')
Extrasensory = Movimento('Extrasensory', 80, 'Psychic')
#########################################################################


# Pokemons
#nome, nivel, hp, movimentos, tipo, hp_max, xp_max, xp, evolucao=None, nivel_evolucao=None

Charizard = Pokemon('Charizard', 36, 0, [Ember, Flamethrower, Wing_Attack, Hyper_Beam], 'Fire', 150, 100)
Charmeleon = Pokemon('Charmeleon', 16, 80, [Ember, Flamethrower, Scratch, Wing_Attack], 'Fire', 80, 50, evolucao=Charizard, nivel_evolucao=36)
Charmander = Pokemon('Charmander', 5, 20, [Tackle, Ember, Scratch, Dig], 'Fire', 20, 10, evolucao=Charmeleon, nivel_evolucao=16)

Blastoise = Pokemon('Blastoise', 36, 150, [Water_Gun, Hydro_Pump, Surf, Earthquake], 'Water', 150, 100)
Wartortle = Pokemon('Wartortle', 16, 80, [Water_Gun, Hydro_Pump, Surf, Dig], 'Water', 80, 50, evolucao=Blastoise, nivel_evolucao=36)
Squirtle = Pokemon('Squirtle', 5, 20, [Tackle, Water_Gun, Bubble, Dig], 'Water', 20, 10, evolucao=Wartortle, nivel_evolucao=16)

Venusaur = Pokemon('Venusaur', 36, 150, [Vine_Whip, Giga_Drain, Absorb, Earthquake], 'Grass', 150, 100)
Ivysaur = Pokemon('Ivysaur', 16, 80, [Vine_Whip, Giga_Drain, Absorb, Dig], 'Grass', 80, 50, evolucao=Venusaur, nivel_evolucao=36)
Bulbasaur = Pokemon('Bulbasaur', 5, 20, [Tackle, Vine_Whip, Absorb, Dig], 'Grass', 20, 10, evolucao=Ivysaur, nivel_evolucao=16)

Raichu = Pokemon('Raichu', 40, 100, [Quick_Attack, Thunderbolt, Slam, Mega_Kick], 'Electric', 100, 100)
Pikachu = Pokemon('Pikachu', 20, 60, [Quick_Attack, Thunderbolt, Slam, Iron_Tail], 'Electric', 60, 50, evolucao=Raichu, nivel_evolucao=30)

Pidgeot = Pokemon('Pidgeot', 36, 120, [Gust, Quick_Attack, Wing_Attack, Hyper_Beam], 'Flying', 120, 100)
Pidgeotto = Pokemon('Pidgeotto', 18, 60, [Gust, Quick_Attack, Wing_Attack, Tackle], 'Flying', 60, 50, evolucao=Pidgeot, nivel_evolucao=36)
Pidgey = Pokemon('Pidgey', 5, 20, [Tackle, Gust, Quick_Attack, Wing_Attack], 'Flying', 20, 10, evolucao=Pidgeotto, nivel_evolucao=18)

Raticate = Pokemon('Raticate', 20, 55, [Tackle, Quick_Attack, Hyper_Beam, Dig], 'Normal', 55, 50)
Rattata = Pokemon('Rattata', 5, 20, [Tackle, Quick_Attack, Bite, Dig], 'Normal', 20, 10, evolucao=Raticate, nivel_evolucao=20)

Butterfree = Pokemon('Butterfree', 10, 60, [Tackle, String_Shot, Psybeam, Gust], 'Bug', 60, 50)
Metapod = Pokemon('Metapod', 7, 30, [Tackle, String_Shot, Harden, Gust], 'Bug', 30, 20, evolucao=Butterfree, nivel_evolucao=10)
Caterpie = Pokemon('Caterpie', 5, 20, [Tackle, String_Shot, Bug_Bite, Dig], 'Bug', 20, 10, evolucao=Metapod, nivel_evolucao=7)

Beedrill = Pokemon('Beedrill', 10, 65, [Tackle, String_Shot, Bug_Bite, Dig], 'Bug', 65, 50)
Kakuna = Pokemon('Kakuna', 7, 25, [Tackle, String_Shot, Harden, Dig], 'Bug', 25, 20, evolucao=Beedrill, nivel_evolucao=10)
Weedle = Pokemon('Weedle', 5, 15, [Tackle, String_Shot, Bug_Bite, Dig], 'Bug', 15, 10, evolucao=Kakuna, nivel_evolucao=7)

Golem = Pokemon('Golem', 36, 150, [Rock_Throw, Earthquake, Tackle, Dig], 'Rock', 150, 100)
Graveler = Pokemon('Graveler', 25, 100, [Rock_Throw, Earthquake, Tackle, Dig], 'Rock', 100, 50, evolucao=Golem, nivel_evolucao=36)
Geodude = Pokemon('Geodude', 5, 25, [Tackle, Rock_Throw, Dig, Defense_Curl], 'Rock', 25, 10, evolucao=Graveler, nivel_evolucao=25)

Machamp = Pokemon('Machamp', 36, 160, [Karate_Chop, Dig, Tackle, Hyper_Beam], 'Fighting', 160, 100)
Machoke = Pokemon('Machoke', 28, 100, [Karate_Chop, Dig, Tackle, Rock_Throw], 'Fighting', 100, 50, evolucao=Machamp, nivel_evolucao=36)
Machop = Pokemon('Machop', 5, 25, [Karate_Chop, Dig, Tackle, Rock_Throw], 'Fighting', 25, 10, evolucao=Machoke, nivel_evolucao=28)

Alakazam = Pokemon('Alakazam', 36, 120, [Psychic, Thunderbolt, Psybeam, Hyper_Beam], 'Psychic', 120, 100)
Kadabra = Pokemon('Kadabra', 16, 60, [Psychic, Thunderbolt, Psybeam, Dig], 'Psychic', 60, 50, evolucao=Alakazam, nivel_evolucao=36)
Abra = Pokemon('Abra', 5, 25, [Tackle, Psybeam, Teleport, Dig], 'Psychic', 25, 10, evolucao=Kadabra, nivel_evolucao=16)

Gengar = Pokemon('Gengar', 36, 120, [Psychic, Leech_Life, Hypnosis, Shadow_Ball], 'Ghost', 120, 100)
Haunter = Pokemon('Haunter', 25, 60, [Psychic, Leech_Life, Hypnosis, Shadow_Ball], 'Ghost', 60, 50, evolucao=Gengar, nivel_evolucao=36)
Gastly = Pokemon('Gastly', 5, 25, [Leech_Life, Hypnosis, Lick, Dig], 'Ghost', 25, 10, evolucao=Haunter, nivel_evolucao=25)

Feraligatr = Pokemon('Feraligatr', 30, 150, [Water_Gun, Aqua_Tail, Crunch, Ice_Punch], 'Water', 150, 100)
Croconaw = Pokemon('Croconaw', 18, 80, [Water_Gun, Bite, Crunch, Ice_Punch], 'Water', 80, 50, evolucao=Feraligatr, nivel_evolucao=30)
Totodile = Pokemon('Totodile', 5, 20, [Scratch, Water_Gun, Bite, Ice_Punch], 'Water', 20, 10, evolucao=Croconaw, nivel_evolucao=18)

Typhlosion = Pokemon('Typhlosion', 30, 150, [Flame_Wheel, Flamethrower, Swift, Earthquake], 'Fire', 150, 100)
Quilava = Pokemon('Quilava', 18, 80, [Flame_Wheel, Ember, Swift, Dig], 'Fire', 80, 50, evolucao=Typhlosion, nivel_evolucao=30)
Cyndaquil = Pokemon('Cyndaquil', 5, 20, [Tackle, Ember, Quick_Attack, Dig], 'Fire', 20, 10, evolucao=Quilava, nivel_evolucao=18)

Meganium = Pokemon('Meganium', 30, 150, [Vine_Whip, Solar_Beam, Body_Slam, Earthquake], 'Grass', 150, 100)
Bayleef = Pokemon('Bayleef', 18, 80, [Vine_Whip, Razor_Leaf, Body_Slam, Dig], 'Grass', 80, 50, evolucao=Meganium, nivel_evolucao=30)
Chikorita = Pokemon('Chikorita', 5, 20, [Tackle, Vine_Whip, Razor_Leaf, Dig], 'Grass', 20, 10, evolucao=Bayleef, nivel_evolucao=18)

Gardevoir = Pokemon('Gardevoir', 30, 150, [Psychic, Moonblast, Thunderbolt, Shadow_Ball], 'Psychic', 150, 100)
Kirlia = Pokemon('Kirlia', 20, 60, [Psychic, Magical_Leaf, Shadow_Ball, Thunderbolt], 'Psychic', 60, 50, evolucao=Gardevoir, nivel_evolucao=30)
Ralts = Pokemon('Ralts', 5, 20, [Confusion, Magical_Leaf, Shadow_Ball, Dig], 'Psychic', 20, 10, evolucao=Kirlia, nivel_evolucao=20)

Salamence = Pokemon('Salamence', 50, 200, [Dragon_Breath, Dragon_Rage, Crunch, Hyper_Beam], 'Dragon', 200, 100)
Shelgon = Pokemon('Shelgon', 30, 100, [Dragon_Breath, Dragon_Rage, Bite, Rock_Throw], 'Dragon', 100, 50, evolucao=Salamence, nivel_evolucao=50)
Bagon = Pokemon('Bagon', 5, 20, [Tackle, Dragon_Breath, Bite, Dig], 'Dragon', 20, 10, evolucao=Shelgon, nivel_evolucao=30)

Metagross = Pokemon('Metagross', 45, 200, [Meteor_Mash, Psychic, Hyper_Beam, Earthquake], 'Steel', 200, 100)
Metang = Pokemon('Metang', 30, 100, [Meteor_Mash, Psychic, Pursuit, Earthquake], 'Steel', 100, 50, evolucao=Metagross, nivel_evolucao=45)
Beldum = Pokemon('Beldum', 5, 20, [Tackle, Take_Down, Pursuit, Dig], 'Steel', 20, 10, evolucao=Metang, nivel_evolucao=30)

Garchomp = Pokemon('Garchomp', 48, 200, [Dragon_Claw, Earthquake, Crunch, Hyper_Beam], 'Dragon', 200, 100)
Gabite = Pokemon('Gabite', 24, 100, [Dragon_Claw, Earthquake, Bite, Dig], 'Dragon', 100, 50, evolucao=Garchomp, nivel_evolucao=48)
Gible = Pokemon('Gible', 5, 20, [Tackle, Dragon_Rage, Bite, Dig], 'Dragon', 20, 10, evolucao=Gabite, nivel_evolucao=24)

Lucario = Pokemon('Lucario', 32, 150, [Aura_Sphere, Close_Combat, Iron_Tail, Dragon_Pulse], 'Fighting', 150, 100)
Riolu = Pokemon('Riolu', 5, 20, [Quick_Attack, Force_Palm, Rock_Smash, Dig], 'Fighting', 20, 10, evolucao=Lucario, nivel_evolucao=32)

Electivire = Pokemon('Electivire', 40, 160, [Thunder_Punch, Thunderbolt, Earthquake, Quick_Attack], 'Electric', 160, 100)
Electabuzz = Pokemon('Electabuzz', 20, 80, [Thunder_Punch, Thunderbolt, Quick_Attack, Dig], 'Electric', 80, 50, evolucao=Electivire, nivel_evolucao=40)
Elekid = Pokemon('Elekid', 5, 20, [Quick_Attack, Thunder_Punch, Swift, Dig], 'Electric', 20, 10, evolucao=Electabuzz, nivel_evolucao=20)

Magmortar = Pokemon('Magmortar', 40, 160, [Fire_Punch, Flamethrower, Thunderbolt, Earthquake], 'Fire', 160, 100)
Magmar = Pokemon('Magmar', 20, 80, [Fire_Punch, Flamethrower, Thunderbolt, Dig], 'Fire', 80, 50, evolucao=Magmortar, nivel_evolucao=40)
Magby = Pokemon('Magby', 5, 20, [Ember, Fire_Punch, Thunder_Punch, Dig], 'Fire', 20, 10, evolucao=Magmar, nivel_evolucao=20)

Mewtwo = Pokemon('Mewtwo', 70, 300, [Psychic, Thunderbolt, Shadow_Ball, Hyper_Beam], 'Psychic', 300, 500)
Mew = Pokemon('Mew', 70, 300, [Psychic, Psybeam, Shadow_Ball, Giga_Drain], 'Psychic', 300, 500)
Articuno = Pokemon('Articuno', 70, 300, [Ice_Beam, Blizzard, Gust, Hyper_Beam], 'Ice', 300, 500)
Zapdos = Pokemon('Zapdos', 70, 300, [Thunder, Thunderbolt, Drill_Peck, Hyper_Beam], 'Electric', 300, 500)
Moltres = Pokemon('Moltres', 70, 300, [Fire_Blast, Flamethrower, Gust, Hyper_Beam], 'Fire', 300, 500)
Groudon = Pokemon('Groudon', 70, 300, [Earthquake, Fire_Blast, Rock_Throw, Hyper_Beam], 'Ground', 300, 500)
Raikou = Pokemon('Raikou', 70, 300, [Thunder, Thunderbolt, Quick_Attack, Hyper_Beam], 'Electric', 300, 500)
Entei = Pokemon('Entei', 70, 300, [Fire_Blast, Flamethrower, Quick_Attack, Hyper_Beam], 'Fire', 300, 500)
Suicune = Pokemon('Suicune', 70, 300, [Surf, Blizzard, Water_Gun, Hyper_Beam], 'Water', 300, 500)
Celebi = Pokemon('Celebi', 70, 300, [Psychic, Giga_Drain, Magical_Leaf, Hyper_Beam], 'Grass', 300, 500)
Lugia = Pokemon('Lugia', 70, 300, [Aeroblast, Psychic, Hydro_Pump, Extrasensory], 'Psychic', 300, 500, 0)
Kyogre = Pokemon('Kyogre', 70, 300, [Hydro_Pump, Origin_Pulse, Ice_Beam, Thunder], 'Water', 300, 500, 0)
#########################################################################

#essa lista tb servirá como um banco de dados para os pokemons que o jogador poderá capturar, vulgo Pokedex
pokemons_no_jogo = [Lugia, Kyogre, Charizard, Charmeleon, Charmander, Blastoise, Wartortle, Squirtle, Venusaur, Ivysaur, Bulbasaur, Raichu, Pikachu, Pidgeot, Pidgeotto, Pidgey, Raticate, Rattata, Butterfree, Metapod, Caterpie, Beedrill, Kakuna, Weedle, Golem, Graveler, Geodude, Machamp, Machoke, Machop, Alakazam, Kadabra, Abra, Gengar, Haunter, Gastly, Feraligatr, Croconaw, Totodile, Typhlosion, Quilava, Cyndaquil, Meganium, Bayleef, Chikorita, Gardevoir, Kirlia, Ralts, Salamence, Shelgon, Bagon, Metagross, Metang, Beldum, Garchomp, Gabite, Gible, Lucario, Riolu, Electivire, Electabuzz, Elekid, Magmortar, Magmar, Magby, Mewtwo, Mew, Articuno, Zapdos, Moltres, Groudon, Raikou, Entei, Suicune, Celebi]
pokemons_lendarios = [Mewtwo, Mew, Articuno, Zapdos, Moltres, Groudon, Raikou, Entei, Suicune, Celebi]
pokemons_basicos = [Charmander, Squirtle, Bulbasaur, Pikachu, Pidgey, Rattata, Caterpie, Weedle, Geodude, Machop, Abra, Gastly, Ralts, Bagon, Beldum, Gible, Riolu, Elekid, Magby]
