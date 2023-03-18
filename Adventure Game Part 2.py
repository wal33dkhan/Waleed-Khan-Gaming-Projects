
#Using named constants
ONE = '1'
TWO = '2'
THREE = '3'
FOUR = '4'

LIVINGROOM = "Living Room"
ATTIC = "Attic"
BEDROOM = "Bed Room"

DRY = "Dry"
FERTILIZED = "Fertilized"

GROUND = "Ground"
INVENTORY = "Inventory"
DOWN = "Down"

def livingRoom(soilState, ballOfString):
    loop = True
    while(loop == True):
        if(ballOfString == INVENTORY or ballOfString == DOWN):
            actions = input("\nYou are in the Living Room\n"
                            "1 - View the pot of soil\n"
                            "2 - Take the stairs up (to the attic)\n"
                            "3 - Take the dark entrance way (to the bed room)\n"
                            "Your Selection: ")
        else:
            actions = input("\nYou are in the Living Room\n"
                  "1 - View the pot of soil\n"
                  "2 - Take the stairs up (to the attic)\n"
                  "3 - Take the dark entrance way (to the bed room)\n"
                  "4 - Pick up the ball of String\n"
                  "Your Selection: ")
            if (actions == FOUR):
                return INVENTORY
        if (actions == ONE):
            if(soilState == DRY):
                print("\nThe pot of soild looks dry")
            else:
                print("\nThere appears to be a fully grown vine that can take you to paradise")
                return True
        elif (actions == TWO):
            return ATTIC
        elif (actions == THREE):
            return BEDROOM
        else:
            print("Please select one of the commands shown.")
            continue

def attic(cheese, ballOfString):
    loop = True
    while (loop == True):
        if (ballOfString == INVENTORY):
            actions = input("\nYou are in the Attic\n"
                            "1 - Pick up some cheese and drop it down the whole\n"
                            "2 - Pick up cheese\n"
                            "3 - Take the stairs down (to the living room)\n"
                            "4 - Drop the string down the hole\n"
                            "Your Selection: ")
            if (actions == FOUR):
                return DOWN
        else:
            actions = input("\nYou are in the Attic\n"
                            "1 - Pick up some cheese and drop it down the whole\n"
                            "2 - Pick up cheese\n"
                            "3 - Take the stairs down (to the living room)\n"
                            "Your Selection: ")
        if (actions == ONE):
            print("\nCheese is too big for the whole")
            return cheese + 1
        elif (actions == TWO):
            print("\nCheese picked up")
            return cheese + 1
        elif (actions == THREE):
            return LIVINGROOM
        else:
            print("Please select one of the commands shown.")
            continue

def bedRoom(ballOfString, cheese):
    loop = True
    while (loop == True):
        if(ballOfString == INVENTORY):
            actions = input("1 - Take the dark entrance way (to the living room)\n"
                            "2 - Use the string to play with the cat\n"
                            "Your Selection: ")
            if (actions == ONE):
                return LIVINGROOM
            elif (actions == TWO):
                print("\Cat looks briefly at you and then goes back to watching the mouse hole")
        elif (ballOfString == DOWN):
            print("\There is a mouse in the room\n"
                  "1 - Take the dark entrance way (to the living room)")
            if(cheese > 0):
                print("2 - Feed the mouse\n"
                      "Your Selection: ")
                actions = input()
                if (actions == TWO):
                    print("\nMouse is leaving the room")
                    print("\nMouse is back in the room")
                    return FERTILIZED
            else:
                print("Your Selection: ")
        else:
            actions = input("1 - Take the dark entrance way (to the living room)\n"
                            "Your Selection: ")
        if (actions == ONE):
            return LIVINGROOM
        else:
            print("\nPlease select one of the commands shown.")
            continue

def start():
    location = LIVINGROOM
    soilState = DRY
    ballOfString = GROUND
    cheese = 0

    gameOver = False
    location = LIVINGROOM

    while (gameOver == False):
        if (location == LIVINGROOM):
            value = livingRoom(soilState, ballOfString)
            if (value == INVENTORY):
                ballOfString = value
            elif (value == FERTILIZED):
                soilState = value
            elif (value == True):
                gameOver = value
                print("Congratulations Game Won!")
            else:
                location = value
        elif (location == ATTIC):
            value = attic(cheese, ballOfString)
            if (type(value) == int):
                cheese = value
            elif (value == DOWN):
                ballOfString = value
            else:
                location = value
        elif (location == BEDROOM):
            value = bedRoom(ballOfString, cheese)
            if (value == FERTILIZED):
                soilState = value
            else:
                location = value

start()
