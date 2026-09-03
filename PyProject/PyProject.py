import os
from pickle import FALSE
import random
from re import A
import sys
from Encounter import encounter
from colorama import Fore, Back, Style, init

name = ""
health = 25
maxHealth = 0
shield = 10
atkPwr = 5
potions = 5
gold = 10

init(autoreset=True)

def consoleClear():
    os.system("cls")

class Player:
    def __init__(self, name, health, maxHealth, shield, atkPwr, potions, gold):
        self.name = name
        self.health = health
        self.maxHealth = maxHealth
        self.shield = shield
        self.atkPwr = atkPwr
        self.potions = potions
        self.gold = gold

class encounters:
    def startEncounterE2S1():
        goblin_encounter = encounter("Goblin", 75, 5, 30, 50, 2, 5)
        goblin_encounter.start(player, encounters)
    def startEncounterE3S1():
        skeleton_encounter = encounter("Skeleton", 100, 8, 50, 75, 3, 5)
        skeleton_encounter.start(player, encounters)
    def startEncounterE4S1():
        zombie_encounter = encounter("Zombie", 125, 10, 75, 100, 4, 5)
        zombie_encounter.start(player, encounters)
    def startEncounterE5S1():
        dragon_encounter = encounter("Dragon", 150, 15, 100, 150, 5, 5)
        dragon_encounter.start(player, encounters)

#intro to game
#region
hasEnteredName = False

while hasEnteredName == False:
    consoleClear()
    print(Fore.GREEN + "Welcome to the Catacombs Dungeon\nA vicious dungeon that you have been trapped in!\nA person like you do not have any identity, nothing except your name.\n")

    print(Fore.LIGHTGREEN_EX + "Do you remember your name? ", end='')
    name = input(Fore.CYAN)

    print(Fore.GREEN + "\nHello" + Fore.CYAN + f" {name}" + Fore.GREEN + ". Did I read your name correctly? " + Fore.LIGHTRED_EX + "Y/N")
    ans1 = input(Fore.CYAN)

    if ans1 == "Y" or ans1 == "y":
        hasEnteredName = True

    if ans1 == "N" or ans1 == "n":
        hasEnteredName = False
        
consoleClear()
print(Fore.GREEN + "At least you remember your name, " + Fore.CYAN + f"{name}")
input()

hasChosenAClass = False
withBagQ = False

while hasChosenAClass == False:
    consoleClear()

    print(Fore.GREEN + "Embarking on this journey requires supplies. If you wish to escape that is.\nThere is a bag in the corner of the room you're in, please, pick up the bag.")
    print(Fore.GREEN + "Pick up the bag? " + Fore.LIGHTRED_EX + "Y/N")

    ans2 = input(Fore.CYAN)

    if ans2 == "Y" or ans2 == "y":
        hasChosenAClass = True
        withBagQ = True
    if ans2 == "N" or ans2 == "n":
        hasChosenAClass = True
        withBagQ = False
    
consoleClear()

if withBagQ == True:
    print(Fore.GREEN + "You picked up the bag, and inside it you found a few supplies.\nYou have been given " + Fore.CYAN + "five health potions, fifteen gold, and something special." + Fore.GREEN + "\nBehind the bag you found a sword made of stone, the edges sharp and the handle grippy.\nAdditionally, there is a small chestplate which you put on.")
    potions = 5
    gold = 15
    atkPwr = 10
    maxHealth = 50
    shield = 15
    input()
    consoleClear()
    print(Fore.GREEN + "Prepared for your journey, you look around for the door.\nUpon finding it in the other corner of the room, you decide to throw the door wide open.\nOn the other side of the new room, stands a hulking enemy, bent on your destruction!")
if withBagQ == False:
    print(Fore.GREEN + "Yet another brave soul.\nYou throw open the door without hesitation and find yourself in a dark room with a powerful foe!")
    potions = 0
    gold = 0
    atkPwr = 5
    maxHealth = 50
    shield = 0

input()

health = maxHealth
player = Player(name, health, maxHealth, shield, atkPwr, potions, gold)
slime_encounter = encounter("Slime", 50, 3, 20, 30, 1, 5)
slime_encounter.start(player, encounters)

#endregion