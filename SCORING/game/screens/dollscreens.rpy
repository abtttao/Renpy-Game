default dolls = 0
default dollDraw = [True, True, True,]
default dollPos = [(640, 362), (170, 95), (1136, 388)]


# Mini game, we have to find all dool
screen dollScreen:
    # overlay
    # modal True
    # add bg
    add "bg playing room.jpg"
    text "Help Sylvie find all her missing doll" pos( 10, 10 )
    text"{i} Found [dolls] dolls {/i}" color "#0000ff" xalign 1.0

    # place dolls

    # if dollDraw[0]:
    #     imagebutton:
    #         pos(640, 362)
    #         idle "side person.png"
    #         action [SetVariable("dolls", dolls + 1), SetVariable("doll1", False]

    # if doll2:
    #      imagebutton:
    #         pos(170, 95)
    #         idle "side person.png"
    #     # update the dolls
    #         action [SetVariable("dolls", dolls + 1), SetVariable("doll2", False]

    # if doll2:
    #     imagebutton:
    #         pos(1136, 388)
    #         idle "side person.png"
    #         action [SetVariable("dolls", dolls + 1), SetVariable("doll3", False]

    for i in range (0, len(dollPos)):
        if dollDraw[i]:
            imagebutton:
                pos(dollPos[i])
                idle "doll.png"
                action Function


    imagebutton:
        xalign 1.0 yalign 0.5
        idle "exit.png"
        action [Hide{"dollScreen"}, Jump("bye")]


init python:
    def findDoll():
        global dolls, dollDraw, score
        dolls +-1
        dollDraw[i] = False
        if dolls == len(dollDraw):
            score +-1
        renpy.restrart_iinteraction()

       
