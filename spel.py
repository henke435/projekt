import keyboard
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
            print(f.read()) 
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
    textVariation = r.randint(0,2)
    while answer not in ["1", "2", "3"]: 
        if textVariation == 0:
            answer = input("""
        Choose one of the following three doors!
            
        1. Wooden door              2. Rusty door   
                     3. Stone gate   
        
        """)
        if textVariation == 1:
            answer = input("""
        Choose one of the following three doors!
            
        1. Elven Tree Portal       2. Steampunk Gear Door   
                    3. Wizard's Rune Gate   

        """)
        if textVariation == 2:
            answer = input("""
        Choose one of the following three doors!
        
        1. Elven Tree Archway    2. Dragonforged Iron Door   
                      3. Runestone Gateway   

        """)

        if answer not in ["1", "2", "3"]:
            print("\nPlease enter one of the available options!")
        
    return r.randint(0,100)

def chooseClass(name):
    answer = ""
    while answer not in ["1", "2", "3"]: 
        answer = input("""
                
        What class do you want to play?
                            
        1. Bruiser  2. Archer   3. Assassin   4. More about the classes

        """)
        if answer == "1":
            print(f"""\n        You chose Bruiser, Good luck, {name}!""")
            input("\nPress 'Enter' to continue!")
            currentClass = playerClass(200, 15, 0.8, "Bruiser")
            return currentClass
        elif answer == "2":
            print(f"""\n        You chose Archer, Good luck, {name}!""")
            input("\nPress 'Enter' to continue!")
            currentClass = playerClass(120, 15, 1.1, "Archer")
            return currentClass
        elif answer == "3":
            print(f"""\n        You chose Assassin, Good luck, {name}!""")
            input("\nPress 'Enter' to continue!")
            currentClass = playerClass(70, 28, 1.4, "Assassin")
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
    while answer not in ["1", "2"] and len(potions) != 0:
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
        if monster.hp <= 0:
            break
        chosenClass.hp = chosenClass.hp - monster.damage
    
    addedGold = r.randint(50, 100)
    time.sleep(2)
    if chosenClass.hp <= 0:
        print(f"\n        You get brutally killed by the {monster.name} and the lose the game")
        time.sleep(1.5)
        input("\nPress 'Enter' to return to the beginning!")
        return chosenClass, lvl, gold, False
    elif monster.hp <= 0:
        print(f"\n        You slay the {monster.name} and gain 1 lvl and collect {addedGold} gold from its corpse")
        print(f"\n        You now have {chosenClass.hp} hp left")
        time.sleep(1.5)
        input("\nPress 'Enter' to continue!")
        return chosenClass, lvl + 1, gold + addedGold, True
    
def openChest(chosenClass, gold, currentWeapon, potions, weapons):
    bruiserWeapons  = ["Steel Axe", "Broad Axe", "Swift Axe", "Double-edged Axe", "Enchanted Double-edged Axe"]
    archerWeapons  = ["Wooden Bow", "Black Bow", "Light Bow", "Swift Bow", "Enchanted Silver Bow"]
    assassinWeapons  = ["Steel Dagger", "Heavy Sword", "Longsword", "Magic Dagger", "Flaming Dagger"]
    weaponStrength = [1.4, 1.8, 2.2, 2.5, 3]
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
    if recievedItem == "Gold":
        gold += amount
        return gold, currentWeapon, potions, weapons
    
    elif recievedItem == "Health Potion":
        potions.append(recievedItem)
        return gold, currentWeapon, potions, weapons
    
    else:
        recievedItem = Item(recievedItem, weaponStrength[index])
        weapons.append(recievedItem)
        
        if recievedItem.strength > currentWeapon.strength:
            currentWeapon = recievedItem

        return gold, currentWeapon, potions, weapons

def merchant(chosenClass, gold, currentWeapon, potions, weapons):
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
                    1. Yes                           2. No
                               3. Sell something
                   
        """)
    #fixa bidding
    while answer not in ["1", "2", "3"]:
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
        potions, weapons, gold, currentWeapon = bidding(gold, merchantInventory, weapons, potions, currentWeapon)
        
        return gold, currentWeapon, potions, weapons
    elif answer == "2":
        print("""

        Okay then traveller, good luck on your journey!
                  
""")
        input("Press 'Enter' to continue!")   
        return gold, currentWeapon, potions, weapons
    else:
        weapons, gold, currentWeapon = selling(gold, weapons, currentWeapon)
        return gold, currentWeapon, potions, weapons  
    
def selling(gold, weapons, currentWeapon):
    keepSelling = True
    if len(weapons) > 1:
        while keepSelling:
            print("""

            Alrighty, what would you like to sell?

    """)
            answerIsOk = False
            for i in range (len(weapons)):
                print(f"        {i + 1}. {weapons[i].name}  ({weapons[i].strength}/3)")
                time.sleep(1)

            while answerIsOk == False:
                weaponToSell = input("\n        ")
                try:
                    x = int(weaponToSell)
                except ValueError:
                    print("\nPlease enter one of the available options!")
                else:
                    if int(weaponToSell) > 0 and int(weaponToSell) <= i + 1:
                        answerIsOk = True
            print("\n        Hmmm....")
            
            time.sleep(2)
            merchantBid = round(r.randint(40, 80)*weapons[int(weaponToSell) - 1].strength)
            print(f"""\n        I think I can give you about {merchantBid} gold for that {weapons[int(weaponToSell) - 1].name}, whaddaya think?
              1. Yes that will be great.     2. No, sorry, that's too little.
                           3. I would rather sell something else.
    """)                                            
            answer = input("\n       ")
            while answer not in ["1", "2", "3"]:
                print("\nPlease enter one of the available options!")
                answer = input("\n\n       ")
            
            if answer == "1":
                weapons.pop(int(weaponToSell)-1)
                gold += merchantBid
                
                if len(weapons) > 1:
                    print("""\n       Pleasure doing business with you, would you like to sell me something else?
                                    1. Yes                   2. No
    """)
                    answer_2 = input("\n       ")
                    while answer_2 != "1" and answer_2 != "2":
                        print("\nPlease enter one of the available options!")
                        answer_2 = input("\n\n       ")
                    if answer_2 == "1":
                        pass
                    if answer_2 == "2":
                        keepSelling = False
                else: 
                    keepSelling = False
           
            elif answer == "2":
                keepSelling = False
                print("\n       Good luck on the path!")
    else:
        print("\n        Sorry but you don't seem to have enough items to sell")
    if currentWeapon not in weapons:
        currentWeapon = weapons[0]
        for i in range(0, len(weapons)):
            if currentWeapon.strength < weapons[i].strength:
                currentWeapon = weapons[i]    
    return weapons, gold, currentWeapon
        
def bidding(gold, merchantInventory, weapons, potions, currentWeapon):
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
            return potions, weapons, gold
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
        return potions, weapons, gold, currentWeapon
    elif frustration < 100:
        print("""

        Pleasure doing business with you, traveller! Hope I see you around!

""")
        input("Press 'Enter' to continue!")  
        gold = gold - bid
        if merchantItem == "Health Potion":
            potions.append(merchantItem)
            return potions, weapons, gold, currentWeapon
        else:
            merchantItem = Item(merchantInventory[int(answer)-1].name, merchantInventory[int(answer)-1].strength)
            weapons.append(merchantItem)
            if merchantItem.strength > currentWeapon.strength:
                currentWeapon = merchantItem
            return potions, weapons, gold, currentWeapon
    
def fallInTrap(chosenClass, alive, gold, maxHp):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    textVariation = r.randint(0,3)
    addedGold = 0
    if textVariation == 0:
        print("\n       ***You see a chest up ahead in the distance and start approaching it.***")
        time.sleep(3)
        print("\n       ***A few meters from it, you feel the planks under your feet start to fall***")
        time.sleep(3)
        print("\n       ***You try to hold yourself to the wall***")
        time.sleep(3)
        print("\n       ***Quickly press the prompted key to save yourself***")
        time.sleep(3)
    elif textVariation == 1:
        print("\n       ***You come across a mystical orb shimmering with magical energy. As you approach, the ground begins to shake.***")
        time.sleep(3)
        print("\n       ***A magical forcefield surrounds you, and you realize that the only way to unlock it is by solving a code puzzle.***")
        time.sleep(3)
        print("\n       ***Symbols and glyphs float in the air, forming a complex code.***")
        time.sleep(3)
        print("\n       ***Quickly press the prompted key to decipher the magical code and unlock the forcefield, or face the consequences.***")
        time.sleep(3)
    elif textVariation == 2:
        print("\n       ***You stumble upon an ancient library hidden deep within a mysterious forest.***")
        time.sleep(3)
        print("\n       ***As you explore, the library's guardian, an ancient elf, locks you in and challenges you with a riddle.***")
        time.sleep(3)
        print("\n       ***The words on its pages rearrange themselves into a cryptic code.***")
        time.sleep(3)
        print("\n       ***Quickly press the prompted key to solve the riddle to regain your freedom.***")
        time.sleep(3)
    elif textVariation == 3:
        print("\n       ***You find yourself in an abandoned laboratory filled with strange contraptions and flickering lights.***")
        time.sleep(3)
        print("\n       ***A holographic message materializes in front of you, presenting a complex mathematical problem.***")
        time.sleep(3)
        print("\n       ***Equations and symbols float in the air, forming a code that is the key to your freedom.***")
        time.sleep(3)
        print("\n       ***Quickly press the prompted key to solve the mathematical code and regain your freedom.***")
        time.sleep(3)
    letter = alfabet[r.randint(0,len(alfabet) - 1)]
    print(f"\n       ***Press '{letter}' in under {chosenClass.trapRisk} seconds***")
    startTime = time.perf_counter()
    keyboard.wait(letter)
    endTime = time.perf_counter()
    if endTime - startTime < chosenClass.trapRisk:
        solvedPuzzle = True
        if textVariation == 0:
            print("\n       ***You successfully grab onto the wall and climb out.***")
            time.sleep(3)
            print("\n       ***You escape the trap and leave without any harm.***")
        elif textVariation == 1:
            print("\n       ***The symbols align perfectly, and the forcefield dissipates. The forcefield opens before you.***")
            time.sleep(3)
            print("\n       ***You step out of the forcefield, stepping without harm.***")

        elif textVariation == 2:
            print("\n       ***The pages of the book settle, and the guardian nods approvingly.***")
            time.sleep(3)
            print("\n       ***The library opens again, and you leave without the guardian hurting you***")
        elif textVariation == 3:
            print("\n       ***The equations align perfectly, and the holographic message dissolves. The laboratory's doors open.***")
            time.sleep(3)
            print("\n       ***You walk out unscathed.***")
        
    else:
        solvedPuzzle = False
        if textVariation == 0:
            print("\n       ***You try to grab ahold of the wall, but your hand slips and you fall down a small cliff***")
            time.sleep(3)
            print("\n       ***You take some damage which leaves you halting out.***")
        elif textVariation == 1:
            print("\n       ***The symbols blur together, and the forcefield reacts violently.***")
            time.sleep(3)
            print("\n       ***A magical shockwave throws you back, and the orb sounds with an echoing hum.***")
            time.sleep(3)
            print("\n       ***Unable to withstand the magical backlash, you take damage due to the mystical forces.***")
        elif textVariation == 2:
            print("\n       ***The words on the pages become chaotic, and the guardian's eyes flash ominously.***")
            time.sleep(3)
            print("\n       ***A magical barrier seals the library's entrance, preventing you from accessing its knowledge.***")
            time.sleep(3)
            print("\n       ***Overwhelmed by the magical enchantments, you feel the guardian draining some of your health with magic.***")
        elif textVariation == 3:
            print("\n       ***The holographic message flickers, and an alarm echoes through the laboratory.***")
            time.sleep(3)
            print("\n       ***Security systems activate, releasing a swarm of nanobots that inflict damage. You stagger out of the laboratory wounded.***")
    time.sleep(2)
    if solvedPuzzle == True:
        addedGold = r.randint(60, 120)
        print(f"\n       ***After the close call, you stumble upon a small treasure of {addedGold} gold, and continue forward.***")
        time.sleep(2)
    if solvedPuzzle == False: 
        chosenClass.hp -= r.randint(int(maxHp/3), maxHp)
        if chosenClass.hp <= 0:
            print("\n       ***You stumble away from the situation with great injuries.***")
            time.sleep(2)
            print("\n       ***Sitting down by a cliff-side, you watch upon the sunset one last time before taking your last breath.")
            time.sleep(2)
            alive = False
        else:
            print("\n       ***You stumble away from the situation with great injuries, barely surviving.***")
            time.sleep(2)
        print()
    return chosenClass, alive, gold + addedGold

def leaderboard(name, lvl):
    answer = input("""
                   Do you want to save your turn in the leaderboard?

                   1. Yes                     2. No
                   """)
    if answer == "1":
        f = open("leaderboard.txt", "a")
        f.write(name, lvl)
    
        print(f.read())
    elif answer == "2": 
        print("Alrighty, good luck on your next adventure!")

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

            if odds < 0:
                chosenClass, lvl, gold, alive = monsterFight(chosenClass, lvl, gold, currentWeapon)

            elif odds >= 0 and odds < 0:
                gold, currentWeapon, potions, weapons = openChest(chosenClass, gold, currentWeapon, potions, weapons)

            elif odds >= 0 and odds < 100:
                gold, currentWeapon, potions, weapons = merchant(chosenClass, gold, currentWeapon, potions, weapons)
        
            elif odds >= 100:
                chosenClass, alive, gold = fallInTrap(chosenClass, alive, gold, maxHp)

        elif answer == "2":
            chosenClass, potions = checkInventory(weapons, gold, potions, chosenClass, maxHp)
        elif answer == "3":
            checkStats(chosenClass, lvl, currentWeapon, maxHp)
        
        #if lvl > lvl i leaderboarden
        #add lvl i leaderboard
        #fixa odds för allt

    leaderboard(name, lvl)   

main()