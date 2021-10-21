screen houseMap():
    
    text "โปรดคลิกที่ห้องต่างๆเพื่อตามหาพี่สาวของคุณ" size 40 xalign 0.5 yalign 0.15

    imagemap:
        ground "houseMap.png" xalign 0.5 yalign 0.5
        hotspot((11, 9, 161, 135)) action Jump("playingroom")
        hotspot((277, 255, 129, 114)) action Jump("bathroom")
        hotspot((333, 108, 167, 148)) action Jump("bedroomsister")
        hotspot((13, 144, 156, 162)) action Jump("chickenroom")
        hotspot((170, 61, 164, 152)) action Jump("myroom")
