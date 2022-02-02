class Pokemon:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_name(self):
    return self.name

  def get_age(self):
    return self.age

class Pokedex:
  def __init__(self):
    self.list_pokemons = []

  def insert_pokemon(self, pokemon):
    self.list_pokemons.append(pokemon)

  def search_pokemon_by_name(self, name):
    for pokemon in self.list_pokemons:
      if(pokemon.get_name() == name): return pokemon

    return f'Pokemon with {name} not found'

  def remove_pokemon_by_name(self, name):
    new_list_pokemons = []
    for pokemon in self.list_pokemons:
      if(pokemon.get_name() != name): new_list_pokemons.append(pokemon) 

    self.list_pokemons = new_list_pokemons

  def print_all_pokemons(self):
    for pokemon in self.list_pokemons:
      print(pokemon.get_name(), pokemon.get_age())


def main ():
  pokedex = Pokedex()

  print('################## Pokedex ##################')
  print('1 - Inserir um pokemon')
  print('2 - Procurar um pokemon pelo nome')
  print('3 - Remover um pokemon pelo nome')
  print('4 - Imprimir todos os pokemons cadastrados')
  print('5 - Sair da pokedex')
  option = input('Insira a opção desejada: ')

  while(True):

    if(option == '5'): exit()

    if(option == '4'): pokedex.print_all_pokemons()

    if(option == '3'):
      name = input('Insira o nome do pokemon: ')

      pokedex.remove_pokemon_by_name(name)

    if(option == '2'):
      name = input('Insira o nome do pokemon: ')

      pokemon = pokedex.search_pokemon_by_name(name)

      print(pokemon.get_name(), pokemon.get_age())

    if(option == '1'):
      name = input('Insira o nome do pokemon: ')
      age_string = input('Insira a idade do pokemon: ')

      age = int(age_string)

      new_pokemon = Pokemon(name, age)

      pokedex.insert_pokemon(new_pokemon)

    option = input('Insira a opção desejada: ')

main()