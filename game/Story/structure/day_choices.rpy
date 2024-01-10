label day_choices:
    menu menu_intro_choices:
        "Drive to the Diner" if not completed_dc_diner_1:
            $completed_dc_diner_1 = True
            pass #todo fill choice
            jump dc_diner_1
        "Check into the hotel" if not completed_dc_hotel_1:
            $completed_dc_hotel_1 = True
            pass #todo fill choice
            jump dc_hotel_1

    menu menu_day_choices:
        "Talk to Karen, the ferrywoman" if not completed_dc_karen_1 and unlocked_dc_karen_1:
            $completed_dc_karen_1 = True
            jump dc_karen_1
        "Drive to the sheriff station to sign the witness report" if not completed_dc_sarah_1:
            $completed_dc_sarah_1 = True
            jump dc_sarah_1
        "Buy new flashlight batteries" if not completed_dc_yggy_1 and unlocked_dc_yggy_1:
            $completed_dc_yggy_1 = True
            jump dc_yggy_1
        "Ask Yggy what the fuck that potion thingy was." if not completed_dc_yggy_2 and unlocked_dc_yggy_2:
            $completed_dc_yggy_2 = True
            jump dc_yggy_2
        "Visit Dr. Hardong" if not completed_dc_hardong_1 and unlocked_dc_hardong_1:
            $completed_dc_hardong_1 = True
            jump dc_hardong_1
        "Visit Cecilia Beaver" if not completed_dc_cock_lady_2 and unlocked_dc_cock_lady_2:
            $completed_dc_cock_lady_2 = True
            jump dc_cock_lady_2
        "Check yourself into Dr. Hardong's clinic" if not completed_dc_hardong_2 and unlocked_dc_hardong_2:
            $completed_dc_hardong_2 = True
            jump dc_hardong_2
    jump evening_choices