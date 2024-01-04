label dc_diner_1:
    scene black at topleft with dis #todo

    #todo

    menu menu_dc_diner_1:
        "Talk to the waitress" if not dc_diner_1_talked_to_mary:
            $dc_diner_1_talked_to_mary = True
            call dc_diner_1_talk_to_mary
            jump menu_dc_diner_1
        "Talk to Iggy Drasil" if not dc_diner_1_talked_to_iggy:
            $dc_diner_1_talked_to_iggy = True
            call dc_diner_1_talk_to_iggy
            jump menu_dc_diner_1
        "Talk to Ragnar Oki" if not dc_diner_1_talked_to_ragnar:
            $dc_diner_1_talked_to_ragnar = True
            call dc_diner_1_talk_to_ragnar
            jump menu_dc_diner_1
        "Leave":
            pass
    if not completed_dc_hotel_1:
        mc "Well, I better check into the hotel, before they close up for the night."
        jump day_choices
    jump evening_choices


label dc_diner_1_talk_to_mary:
    scene black at topleft with dis #todo
    #todo unlock karen ferry, we tell mary we are looking for inspiration, and she tells us to take the ferry. Karen then slips the information that a writer is in town to patty, which unlocks the interview with her.
    return

label dc_diner_1_talk_to_iggy:
    scene black at topleft with dis #todo
    #todo
    return

label dc_diner_1_talk_to_ragnar:
    scene black at topleft with dis #todo
    #todo
    return