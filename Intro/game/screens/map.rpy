screen houseMap():
    # add text
    text "Choose a room" size 20
    # add image
    # add "pee angry.png" xalign 0.5 yalign 0.5 zoom 0.5

    # add image map
    imagemap:
        ground "pee angry.png"
        hotspot((385, 452)) action Jump("bedroom")
        hotspot((385, 452)) action Jump("bedroom")

    # interactive text
    textbutton "bedroom" xalign 0.5 yalign 0.5 action Jump("bedroom")
    textbutton "bedroom" :
        xalign 0.5
        yalign 0.5 
        action Jump("bedroom")

    # interactive image
    imagebutton:
        xalign 0.5
        yalign 0.5 
        idle "pee angry.png"
        hover "pee nomal.png"
        # activate_sound "audio/click.mp3"
        action Jump("bedroom")

    # vbox
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        textbutton "bedroom" xalign 0.5 yalign 0.5 action Jump("bedroom")
        textbutton "bedroom" xalign 0.5 yalign 0.5 action Jump("bedroom")
        textbutton "bedroom" xalign 0.5 yalign 0.5 action Jump("bedroom")

    # hbox
    hbox:
        xalign 0.5
        yalign 0.5
        textbutton "bedroom" xalign 0.5 yalign 0.5 action Jump("bedroom")
        textbutton "bedroom" xalign 0.5 yalign 0.5 action Jump("bedroom")
        textbutton "bedroom" xalign 0.5 yalign 0.5 action Jump("bedroom")
