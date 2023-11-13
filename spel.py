import random as r

class playerClass():
    def __init__(self, hp, damage, trap_risk):
        pass

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

def chooseClass():
    answer = ""
    while answer != "1" and answer != "2" and answer != "3":
        answer = input("""
                
            What class do you want to play?
                            
            1. Bruiser  2. Archer   3. Assassin   4. More about the classes

            """)
        if answer == "1":
            print("You choose Bruiser, Good luck!")
            return Bruiser
        elif answer == "2":
            print("You choose Archer, Good luck!")
            return Archer
        elif answer == "3":
            print("You choose Assassin, Good luck!")
            return Assassin
        elif answer == "4":
            print("""
                  
                Bruiser: High HP, Medium DMG, High risk to fall in to traps
                
                Archer: Medium HP, Medium DMG, Medium risk to fall in to traps
                  
                Assassin: Low HP, High DMG, Low risk to fall in to traps
                  
            """)
            input("Press 'Enter' to continue!")
        else:
            print("Please enter one of the available options!")

def main():
    startInput()
    name = input("""
            
        What is your name?

        """)
    chooseClass()
    
main()