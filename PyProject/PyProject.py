import os
import random
import sys

#variables
#region
name = ""
health = 25
maxHealth = 0
shield = 10
atkPwr = 5
potions = 5
gold = 10
#endregion

#intro to game
#region
hasEnteredName = False

while hasEnteredName == False:
    os.system('cls')
    print("What is your name: ")
    name = input()

    if name != '':
        hasEnteredName = True

print("\nHello", name)
print("Welcome to the PyProject Testing Environment")
input()

hasChosenAClass = False

while hasChosenAClass == False:
    os.system('cls')

    print("Please, choose a class to embark on this journey:\n")
    print("|========Class Selection========|")
    print("| (1) Knight   |  (2) Alchemist |")
    print("|  (3) Warrior | (4) Archer     |")
    print("|-------------------------------|")

    print()

    classNumber = input()

    if classNumber != '':
        hasChosenAClass = True

os.system('cls')

if classNumber == '1':
    print(f"Congrats {name}, you choose the Knight class!")
    maxHealth = 45
    shield = 30
    gold = 25
    atkPwr = 15
    
if classNumber == '2':
    print(f"Congrats {name}, you choose the Alchemist class!")
    maxHealth = 40
    shield = 15
    gold = 15
    atkPwr = 13

if classNumber == '3':
    print(f"Congrats {name}, you choose the Warrior class!")
    maxHealth = 50
    shield = 35
    gold = 20
    atkPwr = 20
    
if classNumber == '4':
    print(f"Congrats {name}, you choose the Archer class!")
    maxHealth = 40
    shield = 10
    gold = 30
    atkPwr = 20

input()

os.system('cls')
print("Your stats have been adjusted to the following:\n")

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
print(f"Your task is to clear dungeons, there are three.\nYou will begin with the Dun-A. Enjoy {name}, and may luck be on your side!")
print("\nEmbark on your journey? Y/N\n")

inA = input()

if inA == "Y":
    print("The journey begins")

if inA == "N":
    sys.exit()

input()
os.system('cls')

#endregion

#ENCOUNTER 1
#region
slimeHealth = 50
slimeAtkPower = 3

health = maxHealth

ranAwayFromSlime = False

while slimeHealth > 0:
    if health > maxHealth:
        health = maxHealth

    if health <= 0:
        os.system('cls')
        print("You've died!")
        input()
        print("You have failed the journey and thus the experiment. You may close the game now.")
        sys.exit()

    os.system('cls')
    print("- Encounter 1 of 5 -")
    print(f"Slime | HP: {slimeHealth:.2f} | Power: {slimeAtkPower}")
    print( "|-------Actions-------|")
    print(f"| (a)ttack  |  (h)eal |")
    print(f"|   (g)uard | (r)un   |")
    print( "|-------Actions-------|")
    print(f"{name} | HP: {health:.2f} / {maxHealth} | Potions Left: {potions}\n")

    en1 = input()

    # attack
    if en1 == "a":
        slimeHealth -= atkPwr

        if health < (maxHealth/2):
            dmg = (slimeAtkPower / 0.25)
        if health >= (maxHealth / 1.25):
            dmg = (slimeAtkPower / 0.3)

        a_rand = random.randint(1, 2)

        if a_rand == 1:
            dmg -= random.randint(1, 3)
        if a_rand == 2:
            dmg += random.randint(1, 3)

        health -= dmg
        print(f"You deal {atkPwr} damage! However, the Slime attacks back dealing {dmg:.2f} damage!")

    # heal
    if en1 == "h":
        if potions <= 0:
            potions = 0
            print("You reach for a flask, however, you discover that you have run out!")
        if potions > 0:
            potions -= 1

            if health < (maxHealth / 2):
                regainHealth = (health * 0.25 + 5)
            if health >= (maxHealth / 2):
                regainHealth = (health * 0.25 + 2)

            h_rand = random.randint(1, 2)

            if h_rand == 1:
                regainHealth -= random.randint(1, 2)
            if h_rand == 2:
                regainHealth += random.randint(1, 2)

            health += regainHealth
            print(f"You reach for a flask and pop open the cork. Taking a swig you regain {regainHealth:.2f}!")

    # guard
    if en1 == "g":
        g_dmgCalc = slimeAtkPower + (slimeAtkPower * 2.5)
        g_dmgCalc -= shield
        
        if g_dmgCalc < 0:
            g_dmgCalc = random.randint(1, 3)

        health -= g_dmgCalc

        print(f"The slime reaches out, tackling you as hard as it can!\nThe slime deals {g_dmgCalc:.2f} damage!")

    # run
    if en1 == "r":
        canRunAway = random.randint(1, 2)

        if canRunAway == 1:
            print("You ran away from the slime successfully! You move onto the next room.")
            input()
            ranAwayFromSlime = True
            break
        if canRunAway == 2:
            print("You attempt to sprint past the slime into the next room, however, the slime slaps you back into the far wall and keeps you boxed in!")
            
            r_dmgCalc = slimeAtkPower + (slimeAtkPower * 2.5)
            r_dmgCalc -= shield
        
            if r_dmgCalc < 0:
                r_dmgCalc = random.randint(1, 3)

            health -= r_dmgCalc
            print(f"You take {r_dmgCalc:.2f} damage!")
        
    input()

os.system('cls')

if ranAwayFromSlime == False:
    print(f"Congrats! You beat the slime!")
    award = random.randint(20, 35)
    gold += award
    print(f"You are awarded {award} gold!")
    input()

#SHOP BEFORE ENCOUNTER 2
moveOnEn1 = False

while moveOnEn1 == False:
    if health > maxHealth:
        health = maxHealth

    os.system('cls')
    
    print("SHOP")
    print( "|-----------------Actions-----------------|")
    print(f"| (h) increase max health - 12 gold       |")
    print(f"|   (g) increase guard points - 10 gold   |")
    print(f"| (a) increase attack power - 8 gold      |")
    print(f"|  (p) buy potions (x1) - 5 gold          |")
    print(f"|  (m) move onto next encounter           |")
    print( "|-----------------Actions-----------------|")
    print(f"{name} | HP: {health:.2f} / {maxHealth:.2f} | Shield: {shield:.2f} | Attack Power: {atkPwr:.2f} \n Potions Left: {potions} | Gold: {gold}\n")

    shopEn1 = input()

    # increase max health
    if shopEn1 == "h":
        increaseHealth = (maxHealth * 0.25) + random.randint(5, 10)
        maxHealth += increaseHealth
        health += (increaseHealth + 5)

        gold -= 12
        print(f"Your max health has been increased by {increaseHealth}")

    # increase guard points/shield
    if shopEn1 == "g":
        increaseGuard = (shield * 0.25) + random.randint(4, 8)
        shield += increaseGuard
        gold -= 10
        print(f"Your guard points has been increased by {increaseGuard}")

    # increase attack power
    if shopEn1 == "a":
        increaseAttackPower = (atkPwr * 0.25) + random.randint(2, 6)
        atkPwr += increaseAttackPower
        gold -= 8
        print(f"Your attack power has been increased by {increaseAttackPower}")

    # buy potions
    if shopEn1 == "p":
        doublePotions = random.randint(1, 2)
        gold -= 5

        if doublePotions == 1:
            potions += 1
            print("You have bought 1 potion")
        if doublePotions == 2:
            potions += 2
            print("Congrats! The shopkeeper decided to give you a 2nd potion for the price of 1!")

    # move onto next encounter
    if shopEn1 == "m":
        moveOnEn1 = True

    input()
#endregion

#ENCOUNTER 2
#region
skeletonHealth = 75
skeletonAtkPower = 6

ranAwayFromSkeleton = False

while skeletonHealth > 0:
    if health > maxHealth:
        health = maxHealth

    if health <= 0:
        os.system('cls')
        print("You've died!")
        input()
        print("You have failed the journey and thus the experiment. You may close the game now.")
        sys.exit()

    os.system('cls')
    print("- Encounter 2 of 5 -")
    print(f"Skeleton | HP: {skeletonHealth:.2f} | Power: {skeletonAtkPower}")
    print( "|-------Actions-------|")
    print(f"| (a)ttack  |  (h)eal |")
    print(f"|   (g)uard | (r)un   |")
    print( "|-------Actions-------|")
    print(f"{name} | HP: {health:.2f} / {maxHealth:.2f} | Potions Left: {potions}\n")

    en1 = input()

    # attack
    if en1 == "a":
        skeletonHealth -= atkPwr

        if health < (maxHealth/2):
            dmg = (skeletonAtkPower / 0.25)
        if health >= (maxHealth / 1.25):
            dmg = (skeletonAtkPower / 0.3)

        a_rand = random.randint(1, 2)

        if a_rand == 1:
            dmg -= random.randint(1, 3)
        if a_rand == 2:
            dmg += random.randint(1, 3)

        health -= dmg
        print(f"You deal {atkPwr} damage! However, the Skeleton attacks back dealing {dmg:.2f} damage!")

    # heal
    if en1 == "h":
        if potions <= 0:
            potions = 0
            print("You reach for a flask, however, you discover that you have run out!")
        if potions > 0:
            potions -= 1

            if health < (maxHealth / 2):
                regainHealth = (health * 0.25 + 5)
            if health >= (maxHealth / 2):
                regainHealth = (health * 0.25 + 2)

            h_rand = random.randint(1, 2)

            if h_rand == 1:
                regainHealth -= random.randint(1, 2)
            if h_rand == 2:
                regainHealth += random.randint(1, 2)

            health += regainHealth
            print(f"You reach for a flask and pop open the cork. Taking a swig you regain {regainHealth}!")

    # guard
    if en1 == "g":
        g_dmgCalc = skeletonAtkPower + (skeletonAtkPower * 2.5)
        g_dmgCalc -= shield
        
        if g_dmgCalc < 0:
            g_dmgCalc = random.randint(1, 3)

        health -= g_dmgCalc

        print(f"The skeleton reaches out, tackling you as hard as it can!\nThe skeleton deals {g_dmgCalc} damage!")

    # run
    if en1 == "r":
        canRunAway = random.randint(1, 2)

        if canRunAway == 1:
            print("You ran away from the skeleton successfully! You move onto the next room.")
            input()
            ranAwayFromSkeleton = True
            break
        if canRunAway == 2:
            print("You attempt to sprint past the skeleton into the next room, however, the skeleton slaps you back into the far wall and keeps you boxed in!")
            
            r_dmgCalc = skeletonAtkPower + (skeletonAtkPower * 2.5)
            r_dmgCalc -= shield
        
            if r_dmgCalc < 0:
                r_dmgCalc = random.randint(1, 3)

            health -= r_dmgCalc
            print(f"You take {r_dmgCalc} damage!")
        
    input()

os.system('cls')

if ranAwayFromSkeleton == False:
    print(f"Congrats! You beat the skeleton!")
    award = random.randint(30, 45)
    gold += award
    print(f"You are awarded {award} gold!")
    input()


#SHOP BEFORE ENCOUNTER 3
moveOnEn2 = False

while moveOnEn2 == False:
    os.system('cls')
    
    print("SHOP")
    print( "|-----------------Actions-----------------|")
    print(f"| (h) increase max health - 14 gold       |")
    print(f"|   (g) increase guard points - 12 gold   |")
    print(f"| (a) increase attack power - 10 gold     |")
    print(f"|  (p) buy potions (x1) - 6 gold          |")
    print(f"|  (m) move onto next encounter           |")
    print( "|-----------------Actions-----------------|")
    print(f"{name} | HP: {health:.2f} / {maxHealth:.2f} | Shield: {shield:.2f} | Attack Power: {atkPwr:.2f} \n Potions Left: {potions} | Gold: {gold}\n")

    shopEn1 = input()

    # increase max health
    if shopEn1 == "h":
        increaseHealth = (maxHealth * 0.25) + random.randint(5, 10)
        maxHealth += increaseHealth
        gold -= 14
        print(f"Your max health has been increased by {increaseHealth:.2f}")

    # increase guard points/shield
    if shopEn1 == "g":
        increaseGuard = (shield * 0.25) + random.randint(4, 8)
        shield += increaseGuard
        gold -= 12
        print(f"Your guard points has been increased by {increaseGuard:.2f}")

    # increase attack power
    if shopEn1 == "a":
        increaseAttackPower = (atkPwr * 0.25) + random.randint(2, 6)
        atkPwr += increaseAttackPower
        gold -= 10
        print(f"Your attack power has been increased by {increaseAttackPower:.2f}")

    # buy potions
    if shopEn1 == "p":
        doublePotions = random.randint(1, 2)
        gold -= 6

        if doublePotions == 1:
            potions += 1
            print("You have bought 1 potion")
        if doublePotions == 2:
            potions += 2
            print("Congrats! The shopkeeper decided to give you a 2nd potion for the price of 1!")

    # move onto next encounter
    if shopEn1 == "m":
        moveOnEn2 = True

    input()
#endregion

#ENCOUNTER 3
#region
zombieHealth = 75
zombieAtkPower = 8

ranAwayFromZombie = False

while zombieHealth > 0:
    if health > maxHealth:
        health = maxHealth

    if health <= 0:
        os.system('cls')
        print("You've died!")
        input()
        print("You have failed the journey and thus the experiment. You may close the game now.")
        sys.exit()

    os.system('cls')
    print("- Encounter 2 of 5 -")
    print(f"Zombie | HP: {zombieHealth:.2f} | Power: {zombieAtkPower}")
    print( "|-------Actions-------|")
    print(f"| (a)ttack  |  (h)eal |")
    print(f"|   (g)uard | (r)un   |")
    print( "|-------Actions-------|")
    print(f"{name} | HP: {health:.2f} / {maxHealth:.2f} | Potions Left: {potions}\n")

    en1 = input()

    # attack
    if en1 == "a":
        zombieHealth -= atkPwr

        if health < (maxHealth/2):
            dmg = (zombieAtkPower / 0.25)
        if health >= (maxHealth / 1.25):
            dmg = (zombieAtkPower / 0.3)

        a_rand = random.randint(1, 2)

        if a_rand == 1:
            dmg -= random.randint(1, 3)
        if a_rand == 2:
            dmg += random.randint(1, 3)

        health -= dmg
        print(f"You deal {atkPwr:.2f} damage! However, the Zombie attacks back dealing {dmg:.2f} damage!")

    # heal
    if en1 == "h":
        if potions <= 0:
            potions = 0
            print("You reach for a flask, however, you discover that you have run out!")
        if potions > 0:
            potions -= 1

            if health < (maxHealth / 2):
                regainHealth = (health * 0.25 + 5)
            if health >= (maxHealth / 2):
                regainHealth = (health * 0.25 + 2)

            h_rand = random.randint(1, 2)

            if h_rand == 1:
                regainHealth -= random.randint(1, 2)
            if h_rand == 2:
                regainHealth += random.randint(1, 2)

            health += regainHealth
            print(f"You reach for a flask and pop open the cork. Taking a swig you regain {regainHealth:.2f}!")

    # guard
    if en1 == "g":
        g_dmgCalc = zombieAtkPower + (zombieAtkPower * 2.5)
        g_dmgCalc -= shield
        
        if g_dmgCalc < 0:
            g_dmgCalc = random.randint(1, 3)

        health -= g_dmgCalc

        print(f"The zombie reaches out, tackling you as hard as it can!\nThe zombie deals {g_dmgCalc:.2f} damage!")

    # run
    if en1 == "r":
        canRunAway = random.randint(1, 2)

        if canRunAway == 1:
            print("You ran away from the zombie successfully! You move onto the next room.")
            input()
            ranAwayFromZombie = True
            break
        if canRunAway == 2:
            print("You attempt to sprint past the zombie into the next room, however, the zombie slaps you back into the far wall and keeps you boxed in!")
            
            r_dmgCalc = zombieAtkPower + (zombieAtkPower * 2.5)
            r_dmgCalc -= shield
        
            if r_dmgCalc < 0:
                r_dmgCalc = random.randint(1, 3)

            health -= r_dmgCalc
            print(f"You take {r_dmgCalc:.2f} damage!")
        
    input()

os.system('cls')

if ranAwayFromZombie == False:
    print(f"Congrats! You beat the zombie!")
    award = random.randint(30, 45)
    gold += award
    print(f"You are awarded {award} gold!")
    input()


#SHOP BEFORE ENCOUNTER 4
moveOnEn2 = False

while moveOnEn2 == False:
    os.system('cls')
    
    print("SHOP")
    print( "|-----------------Actions-----------------|")
    print(f"| (h) increase max health - 15 gold       |")
    print(f"|   (g) increase guard points - 13 gold   |")
    print(f"| (a) increase attack power - 11 gold     |")
    print(f"|  (p) buy potions (x1) - 6 gold          |")
    print(f"|  (m) move onto next encounter           |")
    print( "|-----------------Actions-----------------|")
    print(f"{name} | HP: {health:.2f} / {maxHealth:.2f} | Shield: {shield:.2f} | Attack Power: {atkPwr:.2f} \n Potions Left: {potions} | Gold: {gold}\n")

    shopEn1 = input()

    # increase max health
    if shopEn1 == "h":
        increaseHealth = (maxHealth * 0.25) + random.randint(5, 10)
        maxHealth += increaseHealth
        gold -= 15
        print(f"Your max health has been increased by {increaseHealth:.2f}")

    # increase guard points/shield
    if shopEn1 == "g":
        increaseGuard = (shield * 0.25) + random.randint(4, 8)
        shield += increaseGuard
        gold -= 13
        print(f"Your guard points has been increased by {increaseGuard:.2f}")

    # increase attack power
    if shopEn1 == "a":
        increaseAttackPower = (atkPwr * 0.25) + random.randint(2, 6)
        atkPwr += increaseAttackPower
        gold -= 11
        print(f"Your attack power has been increased by {increaseAttackPower:.2f}")

    # buy potions
    if shopEn1 == "p":
        doublePotions = random.randint(1, 2)
        gold -= 6

        if doublePotions == 1:
            potions += 1
            print("You have bought 1 potion")
        if doublePotions == 2:
            potions += 2
            print("Congrats! The shopkeeper decided to give you a 2nd potion for the price of 1!")

    # move onto next encounter
    if shopEn1 == "m":
        moveOnEn2 = True

    input()
#endregion
