import keyboard
import msvcrt
import random as r
import math
import time


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

def checkStats(chosenClass, lvl, currentWeapon, maxHp):  
    print(f"""
            Stats
          
        Health: {chosenClass.hp}/{maxHp} HP
                
        Damage: {chosenClass.damage} damage

        Current weapon: {currentWeapon.name} 
            Strength: {currentWeapon.strength}/3
            
        Clumsiness: {chosenClass.trapRisk} seconds reaction time

        Level: {lvl}
""")
    input("Press 'Enter' to continue!")

def checkInventory(weapons, gold, potions, chosenClass, maxHp):
    answer = ""
    print(f"""

            Inventory
        
        Money: {gold} gold
        """)
    print("\n        Potions:")
    print(f"            Health Potion {len(potions)}x")
    
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
            if chosenClass.hp + 100 > maxHp:
                chosenClass.hp = maxHp
            else:
                chosenClass.hp += 100
            print(f"\n        You used a Health Potion and your Health is now {chosenClass.hp}/{maxHp}")
            potions.pop(0)
            
        elif answer != "2":
            print("\nPlease enter one of the available options!")
    return chosenClass, potions

def monsterFight(chosenClass, lvl, gold, currentWeapon):
    monsterNameList = ["Zargothrax", "Azazel", "Behemoth", "Cthulhu", "Dracula", "Echidna", "Fenrir", "Gorgon", "Hydra", "Ifrit", "Jormungandr", "Kelpie", "Leviathan", "Minotaur", "Nemean", "Orcus", "Phoenix", "Quetzalcoatl", "Ravana", "Sphinx",
    "Tiamat", "Undine", "Vampire", "Wendigo", "Xolotl",
    "Yeti", "Zombie"]
    
    monsterStrength = r.randint(7*round(math.sqrt(lvl)), 12*round(math.sqrt(lvl)))
    monsterHp = r.randint(30*round(math.sqrt(lvl)), 60*round(math.sqrt(lvl)))
    monster = monsterClass(monsterHp, monsterStrength, monsterNameList[r.randint(0, len(monsterNameList) - 1 )])

    print(f"\n        You encounter a {monster.name} with {monster.hp} hp and {monster.damage} damage")

    print(f"\n        You have {chosenClass.hp} hp and {chosenClass.damage * currentWeapon.strength} damage")

    print("\n         ***Fighting***")
    while chosenClass.hp > 0 and monster.hp > 0:
        monster.hp = monster.hp - (chosenClass.damage * currentWeapon.strength)
        chosenClass.hp = chosenClass.hp - monster.damage
    
    addedGold = r.randint(50, 100)
    time.sleep(2)
    if chosenClass.hp < 0:
        print(f"\n        You get brutally killed by the {monster.name} and the lose the game")
        time.sleep(1.5)
        input("\nPress 'Enter' to return to the beginning!")
        return chosenClass, lvl, gold, False
    elif monster.hp < 0:
        print(f"\n        You slay the {monster.name} and gain 1 lvl and collect {addedGold} gold from its corpse")
        print(f"\n        You now have {chosenClass.hp} hp left")
        time.sleep(1.5)
        input("\nPress 'Enter' to continue!")
        return chosenClass, lvl + 1, gold + addedGold, True
    
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
    weaponStrength = [1.4, 1.8, 2.2, 2.5, 3]
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
    print("""

        ***You see a merchant in the distance and start approaching him***
""")
    time.sleep(2)
    answer = input("""
          
        Hello there traveler! Would you like a gander at my little shop?
                    1. Yes                          2. No
                   
        """)
    #fixa bidding
    while answer != "1" and answer != "2":
        print("\nPlease enter one of the available options!")
        answer = input("\n\n       ")
    if answer == "1":
        print("""
                  
        Thats what I like to hear! Here's what I have in stock!
                  
        """)
        for i in range(len(merchantInventory)):
            print(f"        {i + 1}. {merchantInventory[i].name}  ({merchantInventory[i].strength}/3)")
            time.sleep(1)
                
        print(f"        {i + 2}. Health Potion")
        time.sleep(1)
        return bidding(gold, merchantInventory)
    elif answer == "2":
        print("""

        Okay then traveller, good luck on your journey!
                  
""")
        input("Press 'Enter' to continue!")   
        return "", gold     

def bidding(gold, merchantInventory):
    answerIsOk = False
    frustration = 0
    merchantItem = ""

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
            else: 
                print("\nPlease enter one of the available options!")
    if int(answer) <= len(merchantInventory) and int(answer) > 0:
        merchantBid = merchantInventory[int(answer)-1].strength * r.randint(100,180)
    else:
        merchantBid = r.randint(100,180)
        merchantItem = "Health Potion"
    answerIsOk = False
    while answerIsOk == False:
        try:
            bid = int(input(f"""
                    
        How much gold would you like to bid?    Your money: {gold} gold
                    
        """))
        except ValueError:
            print("\nPlease enter a number!")
        else:
            answerIsOk = True

    while bid < merchantBid and frustration < 100:
        frustration += (merchantBid - bid)/2
        if frustration >= 100:
            print("""
        
        Get the hell out of here! Are you just here to waste my time!?
            
        """)
            input("Press 'Enter' to continue!") 
            return "", gold
        else:
            print("\n        That's too low. Try a higher bid!\n\n")
            print(f"        Frustration: {round(frustration)}/100")
            print(f"        Your money: {gold} gold")
            answerIsOk = False
            while answerIsOk == False:
                try:
                    bid = int(input("\n        "))
                except ValueError:
                    print("\n        Please enter a number!")
                else:
                    break

    if bid > gold:
        print("""

        You don't even have that much gold! Get out of here!!

""")    
        input("Press 'Enter' to continue!") 
        return "", gold
    elif frustration < 100:
        print("""

        Pleasure doing business with you, traveller! Hope I see you around!

""")
        input("Press 'Enter' to continue!")  
        gold = gold - bid
        if merchantItem == "Health Potion":
            return merchantItem, gold
        else:
            return merchantInventory[int(answer)-1], gold
    
def fallInTrap(chosenClass, alive):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    print("\n       You see a chest up ahead in the distance and start approaching it.")
    time.sleep(2)
    print("\n       A few meters from it, you feel the planks under your feet start to fall. ")
    time.sleep(2)
    print("\n       You try to hold yourself to the wall")
    time.sleep(1)
    print("\n       ***Quickly press the prompted key to save yourself***")
    time.sleep(3)
    letter = alfabet[r.randint(0,len(alfabet) - 1)]
    print(f"\n       Press '{letter}' in under {chosenClass.trapRisk} seconds")
    startTime = time.perf_counter()
    print(startTime)
    pressedKey = keyboard.getch()
    print(pressedKey)
    if time.perf_counter() - startTime < chosenClass.trapRisk and pressedKey.lower() == letter:
        print("U WON")
    else:
        print("du torska")
    return chosenClass, alive

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
    maxHp = chosenClass.hp
    currentWeapon = Item("Rusty Knife", 1)
    weapons = [currentWeapon]
    
    while alive:
        answer, time = chooseAction(time)
        if answer == "1":
            odds = continueAdventure()
            if odds < 30:
                chosenClass, lvl, gold, alive = monsterFight(chosenClass, lvl, gold,currentWeapon)
            elif odds >= 30 and odds < 50:
                itemType, recievedItem = openChest(chosenClass)
                if itemType == "Gold":
                    gold += recievedItem
                elif itemType == "Health Potion":
                    potions.append(recievedItem)
                else:
                    weapons.append(recievedItem)
                    if recievedItem.strength > currentWeapon.strength:
                        currentWeapon = recievedItem
            elif odds >= 50 and odds < 75:
                recievedItem, gold = merchant(gold, chosenClass)
                if recievedItem == "Health Potion":
                    potions.append(recievedItem)
                elif recievedItem != "" and recievedItem.strength > currentWeapon.strength:
                    currentWeapon = recievedItem
                    weapons.append(recievedItem)
                elif recievedItem != "":
                    weapons.append(recievedItem)
                
            elif odds >= 75:
                chosenClass, alive = fallInTrap(chosenClass, alive)
        elif answer == "2":
            chosenClass, potions = checkInventory(weapons, gold, potions, chosenClass, maxHp)
        elif answer == "3":
            checkStats(chosenClass, lvl, currentWeapon, maxHp)
        
        #if lvl > lvl i leaderboarden
        #add lvl i leaderboard
        #fixa odds för allt
    
main()