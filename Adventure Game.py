
gameOver = False
locked = True

#Using named constants
LEFT = "l"
RIGHT = "r"
CENTER = "c"
BACK = "b"

ENTRANCE = "Entrance"
PANTRY = "Pantry"
KITCHEN = "Kitchen"
INNER_DOOR = "Inner Door"

SILVER_LOCK_POSITION = "left"
GOLD_LOCK_POSITION = "center"
LOCATION = "Entrance"

print("Welcome to Dungeon of Doom")
while(gameOver != True):
    while (LOCATION == ENTRANCE):
        print ("\n\nYou're in the enterance hallway. The door that brought you in from\noutside is gone.\n")
        print ("In front of you there is a door that leads deeper into the house.\nTo your left is an entranceway into the pantry. To your right is\nan entranceway into the kitchen.\n")

        entranceRoomPrompt = print("Room: Entrance\n\nRoom actions\n"
                                    + "c - Try to open the inner door\n"
                                    + "l - Go through the left entryway (the Pantry)\n"
                                    + "r - Go through the right entryway (the Kitchen)\n")
        entranceRoomPrompt = input("Your selection: ")
        if (entranceRoomPrompt == CENTER):
            if (SILVER_LOCK_POSITION == "right" and GOLD_LOCK_POSITION == "left"):
                locked = False
            if (locked == True):
                print("The door remains stubbornly locked!")
            else:
                print("Congratulations You Unlocked the Inner Door. You Won!")
                gameOver = True
                LOCATION = INNER_DOOR
        elif (entranceRoomPrompt == LEFT):
            LOCATION = PANTRY
        elif (entranceRoomPrompt == RIGHT):
            LOCATION = KITCHEN
        else:
            print("Unknown command. Please enter one of the commands shown.\n")
            LOCATION = ENTRANCE

    while (LOCATION == PANTRY):
        print("\n\nYou're in the pantry that contains the usual foodstuffs. In front\nof you is a silver lock with 3 positions: left, center and right. Behind you is the doorway to the entranceway.")
        pantryPrompt = print( "\nRoom: Pantry\n\n"
                             + "The silver lock is currently set to the " + SILVER_LOCK_POSITION + " position.\n"
                             + "l - Turn the silver lock to the left position\n"
                             + "r - Turn the silver lock to the right position\n"
                             + "c - Turn the silver lock to the center position\n"
                             + "b - Don't change the position of the lock! Return to Entranceway\n")
        pantryPrompt = input("Your selection: ")
        
        if (pantryPrompt == LEFT):
            print("Silver Lock turn Left")
            SILVER_LOCK_POSITION = "left"
        elif (pantryPrompt == RIGHT):
            print("Silver Lock turn Right")
            SILVER_LOCK_POSITION = "right"
        elif (pantryPrompt == CENTER):
            print("Silver Lock turn Center")
            SILVER_LOCK_POSITION = "center"
        elif (pantryPrompt == BACK):
            LOCATION = ENTRANCE
        else:
            print("Unknown command. Please enter one of the commands shown.\n\n")
            LOCATION = PANTRY

    while (LOCATION == KITCHEN):
        print ("\n\nYou're in the kitchen with many modern appliances. In front\nof you is gold lock with 3 positions: left, center and right. Behind you is the doorway to the entranceway.")
        kitchenPrompt = print( "\nRoom: Kitchen\n\n"
                             + "The gold lock is currently set to the " + GOLD_LOCK_POSITION + " position.\n"
                             + "l - Turn the gold lock to the left position\n"
                             + "r - Turn the gold lock to the right position\n"
                             + "c - Turn the gold lock to the center position\n"
                             + "b - Don't change the position of the lock! Return to Entranceway\n")
        kitchenPrompt = input("Your selection: ")
        if (kitchenPrompt == LEFT):
            print("Gold Lock turn Left")
            GOLD_LOCK_POSITION = "left"
        elif (kitchenPrompt == RIGHT):
            print("Gold Lock turn Right")
            GOLD_LOCK_POSITION = "right"
        elif (kitchenPrompt == CENTER):
            print("Gold Lock turn Center")
            GOLD_LOCK_POSITION = "center"
        elif (kitchenPrompt == BACK):
            LOCATION = ENTRANCE
        else:
            print("Unknown command. Please enter one of the commands shown.\n")
            LOCATION = KITCHEN
