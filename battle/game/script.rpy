image battle_bg = Solid("#c6ffa3")


image player syrup idle:
    "player syrup idle1"
    pause .2

    "player syrup idle2"
    pause .2

    "player syrup idle3"
    pause .2
    repeat


image enemy goop idle:
    "enemy goop idle1"
    pause .2

    "enemy goop idle2"
    pause .2

    "enemy goop idle3"
    pause .2
    repeat


label start:
    scene battle_bg

    show player syrup idle:
        xalign 0.4 yalign 0.5
        zoom 3.0

    show enemy goop idle:
        xalign 0.6 yalign 0.5
        zoom 3.0

    show screen battle_menu

    pause
    return


screen battle_menu():
    label "BATTLE!" align(0.5, 0.05)

    bar