"""This module will contain my Pokemon class that defines my attributes
"""

import pprint
import sys
import time
import Pokelist


class Pokemon:

    def __init__(self, name, type, hp, attack, defense, weight):
        self.name = name
        self.type = type
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.weight = weight

    def show(self):
        print(self.name)
        print(self.type)
        print(self.hp)
        print(self.attack)
        print(self.defense)
        print(self.weight)

    # poke = "Bulbasaur"
    # for p in objlist:
        # p.name == 'Bulbasaur'
            # p.show()


def slow_print(string):
    for letter in string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)


def welcome():

    slow_print('\nWelcome Trainer!')
    time.sleep(0.5)
    slow_print('\nMy name is Professor Pine.')
    time.sleep(0.5)
    slow_print('\nThis here is a Pokedex..')
    time.sleep(0.5)
    slow_print('\nIt allows you access the information of any existing Pokemon!')
    time.sleep(0.5)
    slow_print('\nEnter the name of any First Generation Pokemon to access their data: ')

    poke = input()

    slow_print('\n...')
    time.sleep(1)
    slow_print('\n......')
    time.sleep(1)
    slow_print('\n............')
    time.sleep(1)

    for poke in Pokelist.pokelist:
        print(poke)

        welcome_2()
    # else:
        # print('Whoops! Check your spelling and try again below.')


def welcome_2():
    time.sleep(1)
    print("\nFascinating isn't it? Enter the name of any other First Gen Pokemon to access their data:")

    poke = input()

    slow_print('\n...')
    time.sleep(1)
    slow_print('\n......')
    time.sleep(1)
    slow_print('\n............')
    time.sleep(1)

    for poke in Pokelist.pokelist:
        print(poke)

        welcome_2()

    # if str(poke) == input():
        # print(poke)
    # else:
        # print('Whoops! Check your spelling and try again below.')


# create a list of pokemon
# objlist = []

# for stat in Pokelist.pokelist:
    # poke = Pokemon(stat['name'], stat['type'], stat['HP'], stat['attack'], stat['defense'], stat['weight(kg)'])
   # objlist.append(poke)

# print the pokemon
# for poke in objlist:
    # poke.show()


# this main function is acting as the start of your program once the program is initially run
# this will make sure that the welcome() function is run first thing after defining functions
if __name__ == '__main__':
    welcome()

