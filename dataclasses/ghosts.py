from dataclasses import dataclass
from entities import *


player_name = input("Please enter you character name: ")


player1 = Player(player_name, 5, 12, 12)
enemy1 = Enemy("Wild Boar", 10, 5, 5)
healer1 = Healer("Priest", 2, 6, 6, 5)

encounter1 = input(
    "A wild board attacks you! Do you want to defend yourself?(Y/N)")
if encounter1 == "Y":

    print(f"{enemy1.name} attacks {player1.name}")
    print(f"{player1.name} defends themselves and damages {enemy1.name} for {player1.attack}!")
    enemy1.hp -= player1.attack

    print(enemy1)
else:
    print(f"{enemy1.name} attacks {player1.name} and damages them for {enemy1.attack}")
    player1.hp -= enemy1.attack
    # if player1.hp > player1.maxhp:
    #     heal()
    print(player1)
