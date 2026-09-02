import random
import os
import sys
from Shop import shop
from colorama import Fore, Back, Style, init

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
                print(Fore.LIGHTRED_EX + "You've died!")
                input(Fore.CYAN)
                print(Fore.LIGHTRED_EX + "You have failed the journey and thus the experiment. You may close the game now.")
                sys.exit()

            os.system('cls')
            print(Fore.GREEN + f"- Encounter {self.encounterNum} of {self.encounterNumMax} -")
            print(Fore.LIGHTRED_EX + f"{self.enemyName}" + Fore.GREEN + f" |" + Fore.LIGHTRED_EX + f" HP: {self.enemyHealth:.2f}" + Fore.GREEN + f" |" +Fore.LIGHTRED_EX + f" Power: {self.enemyAtkPower}")
            print(Fore.GREEN + "|-------Actions-------|")
            print(Fore.GREEN + f"| (a)ttack  |  (h)eal |")
            print(Fore.GREEN + f"|   (g)uard | (r)un   |")
            print(Fore.GREEN + "|-------Actions-------|")
            print(Fore.LIGHTBLUE_EX + f"{Player.name} | HP: {Player.health:.2f} / {Player.maxHealth} | Potions Left: {Player.potions}\n")

            en1 = input(Fore.CYAN)

            # attack
            if en1 == "a":
                self.enemyHealth -= Player.atkPwr

                if Player.health < (Player.maxHealth/2):
                    Player.dmg = (self.enemyAtkPower / 0.25)
                if Player.health >= (Player.maxHealth / 1.25):
                    Player.dmg = (self.enemyAtkPower / 0.3)

                a_rand = random.randint(1, 2)

                if a_rand == 1:
                    Player.dmg -= random.randint(1, 3)
                if a_rand == 2:
                    Player.dmg += random.randint(1, 3)

                Player.health -= Player.dmg
                print(Fore.GREEN + f"You deal {Player.atkPwr} damage! However, the {self.enemyName} attacks back dealing {Player.dmg:.2f} damage!")

            # heal
            if en1 == "h":
                if Player.potions <= 0:
                    Player.potions = 0
                    print(Fore.LIGHTRED_EX + "You reach for a flask, however, you discover that you have run out!")
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
                    print(Fore.GREEN + f"You reach for a flask and pop open the cork. Taking a swig you regain {regainHealth:.2f}!")

            # guard
            if en1 == "g":
                g_dmgCalc = self.enemyAtkPower + (self.enemyAtkPower * 2.5)
                g_dmgCalc -= Player.shield
        
                if g_dmgCalc < 0:
                    g_dmgCalc = random.randint(1, 3)

                Player.health -= g_dmgCalc

                print(Fore.GREEN + f"The {self.enemyName} reaches out, tackling you as hard as it can!\nThe {self.enemyName} deals {g_dmgCalc:.2f} damage!")

            # run
            if en1 == "r":
                canRunAway = random.randint(1, 2)

                if canRunAway == 1:
                    print(Fore.GREEN + f"You ran away from the {self.enemyName} successfully! You move onto the next room.")
                    input(Fore.CYAN)
                    ranAwayFromEnemy = True
                    break
                if canRunAway == 2:
                    print(Fore.LIGHTRED_EX + f"You attempt to sprint past the {self.enemyName} into the next room, however, the {self.enemyName} slaps you back into the far wall and keeps you boxed in!")
            
                    r_dmgCalc = self.enemyAtkPower + (self.enemyAtkPower * 2.5)
                    r_dmgCalc -= Player.shield
        
                    if r_dmgCalc < 0:
                        r_dmgCalc = random.randint(1, 3)

                    Player.health -= r_dmgCalc
                    print(Fore.LIGHTRED_EX + f"You take {r_dmgCalc:.2f} damage!")
        
            input(Fore.CYAN)

        os.system('cls')

        if ranAwayFromEnemy == False:
            print(Fore.GREEN + f"Congrats! You beat the {self.enemyName}!")
            award = random.randint(self.rewardLower, self.rewardHigher)
            Player.gold += award
            print(Fore.GREEN + f"You are awarded {award} gold!")
            input(Fore.CYAN)
            shop(Player, self.encounterNum, encounters)
    
        shop(Player, self.encounterNum, encounters)