''''A dictionary of Pokémon in a Pokédex format that the user can Input the name of a Pokémon
#they wish to see information for'''

import pprint
import time

#Need a way to make stats appear on separate lines and looking good while doing it
#How to use a dictionary properly for the Pokemon listings; Currently not working
Pokedex = {'Bulbasaur': {"ID": "#001", "Type": "Grass/Poison", "HP": 128, "Attack": 118, "Max CP": 115, "Defense": 111,
                         "Weight(kg)": 6.9},

           'Ivysaur': {"ID": "#001", "Type": "Grass/Poison", "HP": 128, "Attack": 118, "Max CP": 115, "Defense": 111,
                            "Weight(kg)": 6.9}}


def welcome():
    print('Welcome Trainer!')
    time.sleep(1)
    print('My name is Professor Pine.')
    time.sleep(1)
    print('This here is a Pokédex. It allows you access the information of any existing Pokémon!')
    time.sleep(1)
    print('\nEnter the name of any First Gen Pokémon below to access their data:')

    pokemon_name = input()
    print('...')
    time.sleep(1)
    print('......')
    time.sleep(1)
    print('............')
    time.sleep(1)

    for pokemon_name in Pokedex:
        pprint.pprint(Pokedex)
        
        welcome_2()
    else:
        print('Whoops! Check your spelling and try again below.')


def welcome_2():
    time.sleep(1)
    print("\nFascinating isn't it? Enter the name of any other First Gen Pokémon to access their data:")

    if str(Pokedex) == input():
        pprint.pprint(Pokedex)
    else:
        print('Whoops! Check your spelling and try again below.')


if __name__ == '__main__':
    welcome()

#this main function is acting as the start of your program once the program is initially run
#this will make sure that the welcome() function is run first thing after defining functions