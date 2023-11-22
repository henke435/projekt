import random as r
import math

class playerClass():
    def __init__(self, hp, damage, trap_risk, weapon):
        self.hp = hp
        self.damage = damage
        self.trap_risk = trap_risk
        self.weapon = weapon

class monsterClass():
    def __init__(self, hp, damage, name):
        self.hp = hp
        self.damage = damage
        self.name = name



def startInput():
    answer = ""
    while answer != "1":
        answer = input("""
            
        1. Start the game          2. Check the leaderboard

        """)
        if answer == "2":
            print("leaderboard") 
        elif answer != "1":
            print("\nPlease enter one of the available options!")

def chooseAction(time):
    answer = ""
    while answer != "1":   
        if time == 0:
            answer = input(f"""
                    
        What do you want do?
                    
        1. Begin your adventure      2. Check your inventory  
                        3. Check your stats

        """)
        else:
            answer = input(f"""
                    
        What do you want do?
                    
        1. Continue your adventure   2. Check your inventory  
                        3. Check your stats

        """)
        if answer == "1":
            time += 1
            return answer, time
        elif answer == "2":
            return answer, time
        elif answer == "3":
            return answer, time
        else:
            print("\nPlease enter one of the available options!")

def continueAdventure():
    answer = ""
    while answer != "1" and answer != "2"  and answer != "3": 
        answer = input("""
        Choose one of the following three doors!
            
        1. Wooden door              2. Rusty door   
                     3. Stone gate   
        
        """)

        if answer != "1" and answer != "2"  and answer != "3":
            print("\nPlease enter one of the available options!")
        
    return r.randint(0,101)

def chooseClass(name):
    Bruiser = playerClass(200, 15, 1.5, "Rusty Axe")
    Archer = playerClass(120, 15, 2, "Broken Bow")
    Assassin = playerClass(70, 28, 2.5, "Crooked Dagger") 
    answer = ""
    while answer != "1" and answer != "2" and answer != "3":
        answer = input("""
                
        What class do you want to play?
                            
        1. Bruiser  2. Archer   3. Assassin   4. More about the classes

        """)
        if answer == "1":
            print(f"""\n        You chose Bruiser, Good luck, {name}!""")
            input("\nPress 'Enter' to continue!")
            return Bruiser
        elif answer == "2":
            print(f"""\n        You chose Archer, Good luck, {name}!""")
            input("\nPress 'Enter' to continue!")
            return Archer
        elif answer == "3":
            print(f"""\n        You chose Assassin, Good luck, {name}!""")
            input("\nPress 'Enter' to continue!")
            return Assassin
        elif answer == "4":
            print("""
        Bruiser: High HP, Medium DMG, Little reaction-time for traps
                
        Archer: Medium HP, Medium DMG, Medium reaction-time for traps
                  
        Assassin: Low HP, High DMG, High reaction-time for traps

                  
            """)
            input("Press 'Enter' to continue!")
        else:
            print("\nPlease enter one of the available options!")

def checkStats(hp, dmg, trap_risk, lvl):  
    print(f"""
            Stats
          
        Health: {hp} HP
                
        Damage: {dmg} damage
                  
        Clumsiness: {trap_risk} seconds reaction time

        Level: {lvl}
""")
    input("Press 'Enter' to continue!")

def checkInventory(weapons, gold, potions):
    answer = ""
    print(f"""

            Inventory
        
        Money: {gold} gold

        Your weapons: {weapons}
        
        Your potions: {potions}
    
    """)
    while answer != "1" and answer != "2" and len(potions) != 0:
        answer = input("""
        Do you want to use a potion?
                    
        1. Yes                2. No
                    
        """)
        if answer == "1":
            print("\n        Which potion would you like to use?\n")
            for i in range(len(potions)):
                print(f"        {i + 1}. {potions[i]}")
            input("""
        """)
        elif answer != "2":
            print("\nPlease enter one of the available options!")

def monsterFight(lvl):
    print("You encountered a monster!")
    monsterNameList = [
    "Zargothrax", "Azazel", "Behemoth", "Cthulhu", "Dracula",
    "Echidna", "Fenrir", "Gorgon", "Hydra", "Ifrit",
    "Jormungandr", "Kelpie", "Leviathan", "Minotaur", "Nemean",
    "Orcus", "Phoenix", "Quetzalcoatl", "Ravana", "Sphinx",
    "Tiamat", "Undine", "Vampire", "Wendigo", "Xolotl",
    "Yeti", "Zombie"]
    
    monsterStrength = r.randint(7*round(math.sqrt(lvl)), 12*round(math.sqrt(lvl)))
    monsterHp = r.randint(30*round(math.sqrt(lvl)), 60*round(math.sqrt(lvl)))
    monster = monsterClass(monsterHp, monsterStrength, monsterNameList[r.randint(0, len(monsterNameList))])

    print(monsterHp, monsterStrength, monsterNameList)
#i fight tickar dmg från båda hpn tills en är död å då returnas hp och lvl ökar


def openChest(dmg):
    #lägg till så den returnar gold, weapon, potion
    print("Chest")
    gold = 34
    weapon = None
    potions = None
    return gold, weapon, potions
def merchantBid():
    print("You encountered a merchant")
def fallInTrap():
    print("You fell in a trap!")

def main():
    bruiserWeapons  = ["Steel Axe", "Broad Axe", "Swift Axe", "Double-edged Axe", "Enchanted Double-edged Axe"]
    archerWeapons  = ["Wooden Bow", "Black Bow", "Light Bow", "Swift Bow", "Enchanted Silver Bow"]
    assassinWeapons  = ["Steel Dagger", "Heavy Sword", "Longsword", "Magic Dagger", "Flaming Dagger"]
    weaponStrength = [1.2, 1.4, 1.6, 1.8, 2]
    #weapon och strenght ska bara vara i openChest()

    lvl = 0  
    alive = True
    time = 0
    gold = 0
    potions = ["Health Potion"]
    
    startInput()
    
    name = input("""
            
        What is your name?

        """)
    
    chosenClass = chooseClass(name)
    currentPlayerclass = playerClass(chosenClass.hp, chosenClass.damage, chosenClass.trap_risk, chosenClass.weapon)
    currentWeapon = currentPlayerclass.weapon
    weapons = [currentWeapon]
    addedGold = 0
    addedWeapons = ""
    addedPotions = ""
    
    while alive:
        answer, time = chooseAction(time)
        if answer == "1":
            odds = continueAdventure()
            if odds < 40:
                monsterFight(lvl)
            elif odds >= 40 and odds < 65:
                addedGold, addedWeapons, addedPotions = openChest(currentPlayerclass.damage)
                gold += addedGold
                weapons = weapons.append(addedWeapons)
                potions = potions.append(addedPotions)
                print(weapons)
                print(potions)
                print(gold)
            elif odds >= 65 and odds < 90:
                merchantBid()
            elif odds >= 90:
                fallInTrap()
        elif answer == "2":
            checkInventory(weapons, gold, potions)
        elif answer == "3":
            checkStats(currentPlayerclass.hp, currentPlayerclass.damage, currentPlayerclass.trap_risk, lvl)
        
        #if lvl > lvl i leaderboarden
        #add lvl i leaderboard
    
main()