import random as r

class playerClass():
    def __init__(self, hp, damage, trap_risk, weapon):
        self.hp = hp
        self.damage = damage
        self.trap_risk = trap_risk
        self.weapon = weapon

Bruiser = playerClass(200, 15, 1.5, "Rusty Axe")
Archer = playerClass(120, 15, 2, "Broken Bow")
Assassin = playerClass(70, 28, 2.5, "Crooked Dagger") 

def startInput():
    answer = ""
    while answer != "1":
        answer = input("""
            
        1. Start the game          2. Check the leaderboard

        """)
        if answer == "1":
            print("spelet startar")
        elif answer == "2":
            print("leaderboard") 
        else:
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
            return answer
        elif answer == "3":
            return answer
        else:
            print("\nPlease enter one of the available options!")

def continueAdventure():
    answer = input("""
            Choose one of the following three doors 
          
            1. Wooden door  2. Rusty door   3. Glowing door

    
    """)
    #fixa felhantering


def chooseClass(name):
    answer = ""
    while answer != "1" and answer != "2" and answer != "3":
        answer = input("""
                
        What class do you want to play?
                            
        1. Bruiser  2. Archer   3. Assassin   4. More about the classes

        """)
        if answer == "1":
            print(f"""\n   You choose Bruiser, Good luck, {name}!""")
            return Bruiser
        elif answer == "2":
            print(f"""\n   You choose Archer, Good luck, {name}!""")
            return Archer
        elif answer == "3":
            print(f"""\n   You choose Assassin, Good luck, {name}!""")
            return Assassin
        elif answer == "4":
            print("""
                  
                Bruiser: High HP, Medium DMG, High risk to fall into traps
                
                Archer: Medium HP, Medium DMG, Medium risk to fall into traps
                  
                Assassin: Low HP, High DMG, Low risk to fall into traps
                  
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

    print(f"""

            Inventory
        
        Money: {gold} gold

        Your weapons: {weapons}
        
        Your potions: {potions}
    
    """)
    input("Press 'Enter' to continue!")

def main():
    bruiserWeapons  = ["Steel Axe", "Broad Axe", "Swift Axe", "Double-edged Axe", "Enchanted Double-edged Axe"]
    archerWeapons  = ["Wooden Bow", "Black Bow", "Light Bow", "Swift Bow", "Enchanted Silver Bow"]
    assassinWeapons  = ["Steel Dagger", "Heavy Sword", "Longsword", "Magic Dagger", "Flaming Dagger"]
    weaponStrength = [1.2, 1.4, 1.6, 1.8, 2]
    #weapon och strenght ska bara vara i openChest()
    lvl = 0  
    alive = True
    time = 0
    
    startInput()
    
    name = input("""
            
        What is your name?

        """)
    
    chosenClass = chooseClass(name)
    currentPlayerclass = playerClass(chosenClass.hp, chosenClass.damage, chosenClass.trap_risk, chosenClass.weapon)
    currentWeapon = currentPlayerclass.weapon
    weapons = [currentWeapon]
    
    while alive:
        answer, time = chooseAction(time)
        if answer == "1":
            x = continueAdventure()
            if x < 40:
                pass
            elif x >= 40 and x < 65:
                pass
            elif x >= 90:
                pass
        elif answer == "2":
            checkInventory(weapons)
        elif answer == "3":
            checkStats(currentPlayerclass.hp, currentPlayerclass.damage, currentPlayerclass.trap_risk, lvl)
        
        #if lvl > lvl i leaderboarden
        #add lvl i leaderboard
    
main()