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
            print("That was not even a choice can you even read?")
    else:
        print("Attacked by Kraken.\nGame Over")
else:
    print("Not a choice CaN YoU ReAd?\nGAME OVER")
