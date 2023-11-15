import random as r

class playerClass():
    def __init__(self, hp, damage, trap_risk):
        self.hp = hp
        self.damage = damage
        self.trap_risk = trap_risk

Bruiser = playerClass(200, 20, 1.5)
Archer = playerClass(120, 20, 2)
Assassin = playerClass(70, 35, 2.5) 

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
            continueAdventure()
            time += 1
        elif answer == "2":
            checkInventory()
        elif answer == "3":
            checkStats()
        else:
            print("\nPlease enter one of the available options!")

    
        
    

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

def main():
    score = 0  
    alive = True
    time = 0
    startInput()
    name = input("""
            
        What is your name?

        """)
    chosenClass = chooseClass(name)
    while alive:
        answer = chooseAction(time)
    #if score > score i leaderboarden
        #add score i leaderboard
    
main()