#Project3

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')

print("Welcome to the Treasure island.\nYour goal is to find the TREASURE!")

cross=input("You are at a crossroad, which direction would you like to go? LEFT OR RIGHT:")
if cross=="RIGHT":
    print("Game Over!")
else:
    lake=input("You've come to a lake. " \
    "Type 'WAIT' to wait for the boat or 'SWIM' to swim to the other side")

    if lake=="SWIM":
            print("You were attacked by a crocodile. Game Over!")
    else:
        color=input("You have reached a bungalow and there are 3 gates of different colors." \
    " Enter the COLOR to open the gate:")
        if color=="RED":
            print("Burned by fire. Game Over")
        elif color=="BLUE":
            print("Eaten by beasts. Game Over")
        elif color=="YELLOW":
            print("YOU WON!")
        else:
            print("Game Over")