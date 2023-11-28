import random as r
import math

class playerClass():
    def __init__(self, hp, damage, trapRisk, className):
        self.hp = hp
        self.damage = damage
        self.trapRisk = trapRisk
        self.className = className

class monsterClass():
    def __init__(self, hp, damage, name):
        self.hp = hp
        self.damage = damage
        self.name = name

class Item():
    def __init__(self, item_type, strength):
        self.item_type = item_type
        self.strength = strength

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
        
    return r.randint(0,100)

def chooseClass(name):
    answer = ""
    while answer != "1" and answer != "2" and answer != "3":
        answer = input("""
                
        What class do you want to play?
                            
        1. Bruiser  2. Archer   3. Assassin   4. More about the classes

        """)
        if answer == "1":
            print(f"""\n        You chose Bruiser, Good luck, {name}!""")
            input("\nPress 'Enter' to continue!")
            currentClass = playerClass(200, 15, 1.5, "Bruiser")
            return currentClass
        elif answer == "2":
            print(f"""\n        You chose Archer, Good luck, {name}!""")
            input("\nPress 'Enter' to continue!")
            currentClass = playerClass(120, 15, 2, "Archer")
            return currentClass
        elif answer == "3":
            print(f"""\n        You chose Assassin, Good luck, {name}!""")
            input("\nPress 'Enter' to continue!")
            currentClass = playerClass(70, 28, 2.5, "Assassin")
            return currentClass
        elif answer == "4":
            print("""
        Bruiser: High HP, Medium DMG, Little reaction-time for traps
                
        Archer: Medium HP, Medium DMG, Medium reaction-time for traps
                  
        Assassin: Low HP, High DMG, High reaction-time for traps

                  
            """)
            input("Press 'Enter' to continue!")
        else:
            print("\nPlease enter one of the available options!")

def checkStats(chosenClass, lvl):  
    print(f"""
            Stats
          
        Health: {chosenClass.hp} HP
                
        Damage: {chosenClass.damage} damage
                  
        Clumsiness: {chosenClass.trapRisk} seconds reaction time

        Level: {lvl}
""")
    input("Press 'Enter' to continue!")

def checkInventory(weapons, gold, potions):
    answer = ""
    print(f"""

            Inventory
        
        Money: {gold} gold
        """)
    print("\n        Potions:")
    for i in range(len(potions)):
        print(f"            {i + 1}. {potions[i]}")
    
    print("\n        Weapons:")
    for i in range(len(weapons)):
        print(f"            {i + 1}. {weapons[i].item_type}")
    input("\nPress 'Enter' to continue!")
    while answer != "1" and answer != "2" and len(potions) != 0:
        answer = input("""
        Do you want to use a potion?
                    
        1. Yes                2. No
                    
        """)
        if answer == "1":
            pass #öka hp
        elif answer != "2":
            print("\nPlease enter one of the available options!")

def monsterFight(lvl):
    print("You encountered a monster!")
    monsterNameList = ["Zargothrax", "Azazel", "Behemoth", "Cthulhu", "Dracula", "Echidna", "Fenrir", "Gorgon", "Hydra", "Ifrit", "Jormungandr", "Kelpie", "Leviathan", "Minotaur", "Nemean", "Orcus", "Phoenix", "Quetzalcoatl", "Ravana", "Sphinx",
    "Tiamat", "Undine", "Vampire", "Wendigo", "Xolotl",
    "Yeti", "Zombie"]
    
    monsterStrength = r.randint(7*round(math.sqrt(lvl)), 12*round(math.sqrt(lvl)))
    monsterHp = r.randint(30*round(math.sqrt(lvl)), 60*round(math.sqrt(lvl)))
    monster = monsterClass(monsterHp, monsterStrength, monsterNameList[r.randint(0, len(monsterNameList) - 1 )])

    print(monster.hp, monster.damage, monster.name)
#i fight tickar dmg från båda hpn tills en är död å då returnas hp och lvl ökar


def openChest(chosenClass):
    #fixa en clean chest öppning
    bruiserWeapons  = ["Steel Axe", "Broad Axe", "Swift Axe", "Double-edged Axe", "Enchanted Double-edged Axe"]
    archerWeapons  = ["Wooden Bow", "Black Bow", "Light Bow", "Swift Bow", "Enchanted Silver Bow"]
    assassinWeapons  = ["Steel Dagger", "Heavy Sword", "Longsword", "Magic Dagger", "Flaming Dagger"]
    weaponStrength = [1.2, 1.4, 1.6, 1.8, 2]
    if chosenClass.className == "Bruiser":
        chestList = bruiserWeapons
    if chosenClass.className == "Archer":
        chestList = archerWeapons
    if chosenClass.className == "Assassin":
        chestList = assassinWeapons
    chestList.append("Health Potion")
    chestList.append("Health Potion")
    chestList.append("Gold")
    chestList.append("Gold")
    index = r.randint(0, len(chestList) - 1)
    recievedItem = chestList[index]
    if recievedItem == "Health Potion":
        return recievedItem, recievedItem
    
    if recievedItem == "Gold":
        amount = r.randint(30,100)
        return recievedItem, amount
    else:
        return recievedItem, Item(recievedItem, weaponStrength[index])
    print("Chest")
    gold = 34
    weapon = bruiserWeapons[2]
    potions = None
    return gold, weapon, potions


def merchantBid():
    print("You encountered a merchant")
def fallInTrap():
    print("You fell in a trap!")

def main():
    #weapon och strenght ska bara vara i openChest()

    lvl = 1
    alive = True
    time = 0
    gold = 100
    potions = ["Health Potion"]
    
    startInput()
    
    name = input("""
            
        What is your name?

        """)
    
    chosenClass = chooseClass(name)
    currentWeapon = Item("Rusty Knife", 1)
    weapons = [currentWeapon]
    
    while alive:
        answer, time = chooseAction(time)
        if answer == "1":
            odds = continueAdventure()
            if odds < 40:
                monsterFight(lvl)
# fixa så chest funkar
            elif odds >= 40 and odds < 65:
                itemType, recievedItem = openChest(chosenClass)
                if itemType == "Gold":
                    gold += recievedItem
                elif itemType == "Health Potion":
                    potions.append(recievedItem)
                else:
                    weapons.append(recievedItem)
                print(weapons, potions, gold)
            elif odds >= 65 and odds < 90:
                merchantBid()
            elif odds >= 90:
                fallInTrap()
        elif answer == "2":
            checkInventory(weapons, gold, potions)
        elif answer == "3":
            checkStats(chosenClass, lvl)
        
        #if lvl > lvl i leaderboarden
        #add lvl i leaderboard
    
main()