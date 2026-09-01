import os
from pickle import FALSE
import random
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
    os.system('cls')
    print(Fore.GREEN + "What is your name: ")
    name = input(Fore.CYAN)

    if name != '':
        hasEnteredName = True

print(Fore.GREEN + "\nHello" + Fore.CYAN + f" {name}")
print(Fore.GREEN + "Welcome to the PyProject Testing Environment")
input(Fore.CYAN)

hasChosenAClass = False

while hasChosenAClass == False:
    os.system('cls')

    print(Fore.GREEN + "Please, choose a class to embark on this journey:\n")
    print(Fore.LIGHTRED_EX + "|========Class Selection========|")
    print(Fore.LIGHTRED_EX + "| (1) Knight   |  (2) Alchemist |")
    print(Fore.LIGHTRED_EX + "|  (3) Warrior | (4) Archer     |")
    print(Fore.LIGHTRED_EX + "|-------------------------------|")

    print()

    classNumber = input(Fore.CYAN)

    if classNumber != '':
        hasChosenAClass = True

os.system('cls')

if classNumber == '1':
    print(Fore.GREEN + "Congrats" + Fore.CYAN + f" {name}" + Fore.GREEN + ", you choose the Knight class!")
    maxHealth = 45
    shield = 30
    gold = 25
    atkPwr = 15
    
if classNumber == '2':
    print(Fore.GREEN + "Congrats" + Fore.CYAN + f" {name}" + Fore.GREEN + ", you choose the Alchemist class!")
    maxHealth = 40
    shield = 15
    gold = 15
    atkPwr = 13

if classNumber == '3':
    print(Fore.GREEN + "Congrats" + Fore.CYAN + f" {name}" + Fore.GREEN + ", you choose the Warrior class!")
    maxHealth = 50
    shield = 35
    gold = 20
    atkPwr = 20
    
if classNumber == '4':
    print(Fore.GREEN + "Congrats" + Fore.CYAN + f" {name}" + Fore.GREEN + ", you choose the Archer class!")
    maxHealth = 40
    shield = 10
    gold = 30
    atkPwr = 20

input()

os.system('cls')
print(Fore.GREEN + "Your stats have been adjusted to the following:\n")

print("|===================|")
print(f"| Health: {maxHealth}        |")
print(f"| Shield: {shield}        |")
if classNumber != '2':
    print(f"| Attack Power: {atkPwr}  |")
if classNumber == '2':
    print(f"| Attack Power: {atkPwr}   |")
print(f"| Gold: {gold}          |")
print(f"| Potions: {potions}        |")
print("|===================|")

input()

os.system('cls')
print(Fore.GREEN + f"Your task is to clear the Python Dungeon.\nEnjoy" + Fore.CYAN + f" {name}" + Fore.GREEN + ", and may luck be on your side!")
print("\nEmbark on your journey? Y/N\n")

inA = input(Fore.CYAN)

if inA == "Y":
    print(Fore.GREEN + "The journey begins")

if inA == "N":
    sys.exit()

input()
os.system('cls')

health = maxHealth
player = Player(name, health, maxHealth, shield, atkPwr, potions, gold)
slime_encounter = encounter("Slime", 50, 3, 20, 30, 1, 5)
slime_encounter.start(player, encounters)

#endregion