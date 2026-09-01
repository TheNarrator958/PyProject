import random
import os
import sys
from Shop import shop

class encounter:
    def __init__(self, enemyName, enemyHealth, enemyAtkPower, rewardLower, rewardHigher, encounterNum, encounterNumMax):
        self.enemyName = enemyName
        self.enemyHealth = enemyHealth
        self.enemyAtkPower = enemyAtkPower
        self.rewardLower = rewardLower
        self.rewardHigher = rewardHigher
        self.encounterNum = encounterNum
        self.encounterNumMax = encounterNumMax

    def start(self, Player, encounters):
        ranAwayFromEnemy = False
        while self.enemyHealth > 0:
            if Player.health > Player.maxHealth:
               Player.health = Player.maxHealth
            if Player.health <= 0:
                os.system('cls')
                print("You've died!")
                input()
                print("You have failed the journey and thus the experiment. You may close the game now.")
                sys.exit()

            os.system('cls')
            print(f"- Encounter {self.encounterNum} of {self.encounterNumMax} -")
            print(f"{self.enemyName} | HP: {self.enemyHealth:.2f} | Power: {self.enemyAtkPower}")
            print( "|-------Actions-------|")
            print(f"| (a)ttack  |  (h)eal |")
            print(f"|   (g)uard | (r)un   |")
            print( "|-------Actions-------|")
            print(f"{Player.name} | HP: {Player.health:.2f} / {Player.maxHealth} | Potions Left: {Player.potions}\n")

            en1 = input()

            # attack
            if en1 == "a":
                self.enemyHealth -= Player.atkPwr

                if Player.health < (Player.maxHealth/2):
                    dmg = (self.enemyAtkPower / 0.25)
                if Player.health >= (Player.maxHealth / 1.25):
                    dmg = (self.enemyAtkPower / 0.3)

                a_rand = random.randint(1, 2)

                if a_rand == 1:
                    dmg -= random.randint(1, 3)
                if a_rand == 2:
                    dmg += random.randint(1, 3)

                Player.health -= dmg
                print(f"You deal {Player.atkPwr} damage! However, the {self.enemyName} attacks back dealing {dmg:.2f} damage!")

            # heal
            if en1 == "h":
                if Player.potions <= 0:
                    Player.potions = 0
                    print("You reach for a flask, however, you discover that you have run out!")
                if Player.potions > 0:
                    Player.potions -= 1
                    if Player.health < (Player.maxHealth / 2):
                        regainHealth = (Player.health * 0.25 + 5)
                    if Player.health >= (Player.maxHealth / 2):
                        regainHealth = (Player.health * 0.25 + 2)

                    h_rand = random.randint(1, 2)

                    if h_rand == 1:
                        regainHealth -= random.randint(1, 2)
                    if h_rand == 2:
                        regainHealth += random.randint(1, 2)

                    Player.health += regainHealth
                    print(f"You reach for a flask and pop open the cork. Taking a swig you regain {regainHealth:.2f}!")

            # guard
            if en1 == "g":
                g_dmgCalc = self.enemyAtkPower + (self.enemyAtkPower * 2.5)
                g_dmgCalc -= Player.shield
        
                if g_dmgCalc < 0:
                    g_dmgCalc = random.randint(1, 3)

                Player.health -= g_dmgCalc

                print(f"The {self.enemyName} reaches out, tackling you as hard as it can!\nThe {self.enemyName} deals {g_dmgCalc:.2f} damage!")

            # run
            if en1 == "r":
                canRunAway = random.randint(1, 2)

                if canRunAway == 1:
                    print(f"You ran away from the {self.enemyName} successfully! You move onto the next room.")
                    input()
                    ranAwayFromEnemy = True
                    break
                if canRunAway == 2:
                    print(f"You attempt to sprint past the {self.enemyName} into the next room, however, the {self.enemyName} slaps you back into the far wall and keeps you boxed in!")
            
                    r_dmgCalc = self.enemyAtkPower + (self.enemyAtkPower * 2.5)
                    r_dmgCalc -= Player.shield
        
                    if r_dmgCalc < 0:
                        r_dmgCalc = random.randint(1, 3)

                    Player.health -= r_dmgCalc
                    print(f"You take {r_dmgCalc:.2f} damage!")
        
            input()

        os.system('cls')

        if ranAwayFromEnemy == False:
            print(f"Congrats! You beat the {self.enemyName}!")
            award = random.randint(self.rewardLower, self.rewardHigher)
            Player.gold += award
            print(f"You are awarded {award} gold!")
            input()
            shop(Player, self.encounterNum, encounters)