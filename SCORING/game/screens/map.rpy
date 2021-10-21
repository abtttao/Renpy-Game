screen mapScreen:
    # score
    text "score [score]"
    # add "houseMap.png"
    # add image map

    imagemap:
        # xpos 50 ypos 50
        pos(50, 20) 
        ground "houseMap.png"
        hotspot((10, 9, 163, 136)) action Show("dollScreen")
        hotspot((169, 54, 171, 153)) action Jump("bedroom")
        hotspot((278, 258, 130, 114)) action Jump("bathroom")