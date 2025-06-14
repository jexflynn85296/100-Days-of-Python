print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You come to a deserted island what will you do?")
direction = input("Right or Left? ")
if direction == "right" or direction == "Right" or direction == "RIGHT":
    print("Got shot in the head by flaming arrows.\nGAME OVER")
elif direction == "left" or direction == "Left" or direction == "LEFT":
    print("You come to a large river. ")
    action = input("What will you do swim or wait?")
    if action == "swim" or action == "Swim" or action == "SWIM":
        print("Attacked by Kraken.\nGame Over")
    elif action == "wait" or action == "Wait" or action == "WAIT":
        print("You searched around and found three doors\nRed, Blue, and Yellow")
        door = input("Which door will you choose? ")
        if door == "red" or door == "Red" or door == "RED":
            print("Attacked by Babbadook.\nGAME OVER")
        elif door == "blue" or door == "Blue" or door == "BLUE":
            print("Attacked by John Cena.\nGAME OVER")
        elif door == "yellow" or door == "Yellow" or door == "YELLOW":
            print("You found the treasure chest!\nWait nothing is inside.\nWho really won here?")
        else:
            print("Hey you, you're finally awake.")
    else:
        print("The Pringles man is now out for blood!\nGAME OVER")
else:
    print("A lobster comes of of nowhere and knock you out.\nGAME OVER")
    
