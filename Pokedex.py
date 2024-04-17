import pypokedex as pd

poke = (input("Coloque o nome do Pokémon que você quer buscar: "))
while poke not in pd.pokemon:
    print("Esse Pokémon não existe! Tente novamente.")
    poke = (input("Coloque o nome do Pokémon que você quer buscar: "))
p = pd.get(name=poke)
print(f"Nome: {p.name}")
print(f"Tipo: {p.types}")
print(f"Altura: {p.height}")
print(f"Peso: {p.weight}")
