# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    call screen houseMap
    pause
    return

label bedroom:
    scene bg room
    "Here is my bedroom"
    return