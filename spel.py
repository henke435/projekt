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
    def __init__(self, name, strength):
        self.name = name
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

def checkStats(chosenClass, lvl, currentWeapon):  
    print(f"""
            Stats
          
        Health: {chosenClass.hp} HP
                
        Damage: {chosenClass.damage} damage

        Current weapon: {currentWeapon.name} 
            Strength: {currentWeapon.strength}/2
            
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
        print(f"            {i + 1}. {weapons[i].name}")
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

def monsterFight(chosenClass, lvl, gold):
    print("You encountered a monster!")
    monsterNameList = ["Zargothrax", "Azazel", "Behemoth", "Cthulhu", "Dracula", "Echidna", "Fenrir", "Gorgon", "Hydra", "Ifrit", "Jormungandr", "Kelpie", "Leviathan", "Minotaur", "Nemean", "Orcus", "Phoenix", "Quetzalcoatl", "Ravana", "Sphinx",
    "Tiamat", "Undine", "Vampire", "Wendigo", "Xolotl",
    "Yeti", "Zombie"]
    
    monsterStrength = r.randint(7*round(math.sqrt(lvl)), 12*round(math.sqrt(lvl)))
    monsterHp = r.randint(30*round(math.sqrt(lvl)), 60*round(math.sqrt(lvl)))
    monster = monsterClass(monsterHp, monsterStrength, monsterNameList[r.randint(0, len(monsterNameList) - 1 )])

    print(f" You've encountered a {monster.name} with {monster.hp} hp and {monster.damage} damage")

    print(f"You have {chosenClass.hp} hp and {chosenClass.damage} damage")

    while chosenClass.hp > 0 and monster.hp > 0:
        monster.hp = monster.hp - chosenClass.damage
        chosenClass.hp = chosenClass.hp - monster.damage
    
    addedGold = r.randint(50, 100)

    if chosenClass.hp < 0:
        print("You lost the fight and the Game")
        input("\nPress 'Enter' to return to the beginning!")
        return chosenClass.hp, lvl, gold + 0, False
    elif monster.hp < 0:
        print(f"\n You won the fight and gain 1 lvl and {addedGold} gold")
        input("\nPress 'Enter' to continue!")
        return chosenClass.hp, lvl + 1, gold + addedGold, True
    
    
    
#i fight tickar dmg från båda hpn tills en är död å då returnas hp och lvl ökar


def openChest(chosenClass):
    #fixa en clean chest öppning
    bruiserWeapons  = ["Steel Axe", "Broad Axe", "Swift Axe", "Double-edged Axe", "Enchanted Double-edged Axe"]
    archerWeapons  = ["Wooden Bow", "Black Bow", "Light Bow", "Swift Bow", "Enchanted Silver Bow"]
    assassinWeapons  = ["Steel Dagger", "Heavy Sword", "Longsword", "Magic Dagger", "Flaming Dagger"]
    weaponStrength = [1.2, 1.4, 1.6, 1.8, 2]
    amount = "a"
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
    if recievedItem == "Gold":
        amount = r.randint(30,100)
    print(f"""
        
        You found {amount} {recievedItem} in a hidden chest!

        """)
    input("\nPress 'Enter' to continue!")
    if recievedItem == "Health Potion":
        return recievedItem, recievedItem
    
    if recievedItem == "Gold":
        return recievedItem, amount
    else:
        return recievedItem, Item(recievedItem, weaponStrength[index])


def merchant(gold, chosenClass):
    bruiserWeapons  = ["Steel Axe", "Broad Axe", "Swift Axe", "Double-edged Axe", "Enchanted Double-edged Axe"]
    archerWeapons  = ["Wooden Bow", "Black Bow", "Light Bow", "Swift Bow", "Enchanted Silver Bow"]
    assassinWeapons  = ["Steel Dagger", "Heavy Sword", "Longsword", "Magic Dagger", "Flaming Dagger"]
    weaponStrength = [1.2, 1.4, 1.6, 1.8, 2]
    merchantInventory = []
    answer = ""
    if chosenClass.className == "Bruiser":
        for i in range(r.randint(2, 5)):
            index = r.randint(0, len(bruiserWeapons) - 1)
            merchantItem = Item(bruiserWeapons[index], weaponStrength[index])
            merchantInventory.append(merchantItem)

    elif chosenClass.className == "Archer":
        for i in range(r.randint(2, 5)):
            index = r.randint(0, len(archerWeapons) - 1)
            merchantItem = Item(archerWeapons[index], weaponStrength[index])
            merchantInventory.append(merchantItem)
    else:
        for i in range(r.randint(2, 5)):
            index = r.randint(0, len(assassinWeapons) - 1)
            merchantItem = Item(assassinWeapons[index], weaponStrength[index])
            merchantInventory.append(merchantItem)
    answer = input("""
          
        Hello there traveler! Would you like a gander at my little shop?
                    1. Yes                           2. No
                   
        """)
    #fixa bidding
    while answer != "1" and answer != "2":
        print("\nPlease enter one of the available options!")
    if answer == "1":
        print("""
                  
        Thats what I like to hear! Here's what I have in stock!
                  
        """)
        for i in range(len(merchantInventory)):
            print(f"        {i + 1}. {merchantInventory[i].name}  ({merchantInventory[i].strength}/2)")
                
        print(f"        {i + 2}. Health Potion")
        bidding(gold, merchantInventory)
    elif answer == "2":
        print("""

        Okay then traveller, have it your way! Good luck on your journey!
                  
""")
        input("Press 'Enter' to continue!")        
def bidding(gold, merchantInventory):
    answerIsOk = False

    while answerIsOk == False:
        answer = input("""

        What would you like to bid on?

        """)
        try:
            x = int(answer)
            
        except ValueError:
            print("\nPlease enter one of the available options!")
        else:
            if int(answer) <= len(merchantInventory) + 1 and int(answer) > 0:
                answerIsOk = True
    if int(answer) <= len(merchantInventory) and int(answer) > 0:
        merchantBid = merchantInventory[answer-1].strength * r.randint(100,180)
    else:
        merchantBid = r.randint(100,180)
    bid = input(f"""
                
                How much would you like to bid?
                
                """)


        
    

def fallInTrap():
    print("You fell in a trap!")

def main():
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
    boughtWeapon = ""
    
    while alive:
        answer, time = chooseAction(time)
        if answer == "1":
            odds = continueAdventure()
            if odds < 0:
                chosenClass.hp, lvl, gold, alive = monsterFight(chosenClass, lvl, gold)
            elif odds == 0 and odds == 1:
                itemType, recievedItem = openChest(chosenClass)
                if itemType == "Gold":
                    gold += recievedItem
                elif itemType == "Health Potion":
                    potions.append(recievedItem)
                else:
                    weapons.append(recievedItem)
                    if recievedItem.strength > currentWeapon.strength:
                        currentWeapon = recievedItem
            elif odds > 0 and odds < 100:
                merchant(gold, chosenClass)
                #gold, boughtWeapon = 
            elif odds == 0:
                fallInTrap()
        elif answer == "2":
            checkInventory(weapons, gold, potions)
        elif answer == "3":
            checkStats(chosenClass, lvl, currentWeapon)
        
        #if lvl > lvl i leaderboarden
        #add lvl i leaderboard
        #fixa odds för allt
    
main()