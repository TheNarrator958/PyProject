import os
import random

class shop:
    def __init__(self, Player, lastEncounter, encounters):
        moveOnEn = False

        while moveOnEn == False:
            os.system('cls')
    
            print("SHOP")
            print( "|-----------------Actions-----------------|")
            print(f"| (h) increase max health - 10 gold       |")
            print(f"|   (g) increase guard points - 12 gold   |")
            print(f"| (a) increase attack power - 15 gold     |")
            print(f"|  (p) buy potions (x1) - 5 gold          |")
            print(f"|    (m) move onto next encounter         |")
            print( "|-----------------Actions-----------------|")
            print(f"{Player.name} | HP: {Player.health:.2f} / {Player.maxHealth:.2f} | Shield: {Player.shield:.2f} | Attack Power: {Player.atkPwr:.2f} \n Potions Left: {Player.potions} | Gold: {Player.gold}\n")

            shopEn1 = input()

            # increase max health
            if shopEn1 == "h":
                increaseHealth = (Player.maxHealth * 0.25) + random.randint(5, 10)
                Player.maxHealth += increaseHealth
                Player.gold -= 10
                print(f"Your max health has been increased by {increaseHealth:.2f}")

            # increase guard points/shield
            if shopEn1 == "g":
                increaseGuard = (Player.shield * 0.25) + random.randint(4, 8)
                Player.shield += increaseGuard
                Player.gold -= 12
                print(f"Your guard points has been increased by {increaseGuard:.2f}")

            # increase attack power
            if shopEn1 == "a":
                increaseAttackPower = (Player.atkPwr * 0.25) + random.randint(2, 6)
                Player.atkPwr += increaseAttackPower
                Player.gold -= 15
                print(f"Your attack power has been increased by {increaseAttackPower:.2f}")

            # buy potions
            if shopEn1 == "p":
                doublePotions = random.randint(1, 2)
                Player.gold -= 5

                if doublePotions == 1:
                    Player.potions += 1
                    print("You have bought 1 potion")
                if doublePotions == 2:
                    Player.potions += 2
                    print("Congrats! The shopkeeper decided to give you a 2nd potion for the price of 1!")

            # move onto next encounter
            if shopEn1 == "m":
                moveOnEn = True

            input()

        # move onto next encounter
        if lastEncounter == 1:
            encounters.startEncounterE2S1()
        if lastEncounter == 2:
            encounters.startEncounterE3S1()
        if lastEncounter == 3:
            encounters.startEncounterE4S1()
        if lastEncounter == 4:
            encounters.startEncounterE5S1()