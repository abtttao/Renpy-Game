# Characters
define me = Character("Me", color="#c8c8ff")
define sv = Character("Sylvie",)

# s
default score = 0
# define doll1 = True
# define doll2 = True
# define doll3 = True


# Start game
label start:
    # show a house plan
    show screen mapScreen
    pause
    return

label bedroom:
    #" hide screen mapScreen"
    scene bg bedroom sister
    show pee nomal
    sv "This is my bedroom"

    # quest
    menu:
        sv "What do you think"
        "It looks very nice":
            show pee happy
            # score +1
            $score +=1
          
        "You should clean it often ;(":
             # score -1
             $score -=1
           
    pause
    jump bye

label bathroom:
    #" hide screen mapScreen"
    scene bg bath room
    me "Is this your bath room"
    show pee angry
    sv "Please get out!"

    # quest
    menu:
        "No, I want to see it":
            show pee angry
            # score +1
            $score -=1
          
        "Sorry, I leave now":
            show pee happy
             # score -1
            $score +=1
           
    pause
    jump bye



label bye:
    scene black with dissolve
    "Chose another room or click anywhere to end the games"
    hide screen mapScreen
    if score >0:
            "Good ending. Sylvie like your action"
    else:
            "Bad ending. Sylvie dislike your action"
    
