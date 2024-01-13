label day_choices:
    menu menu_intro_choices:
        "Drive to the Diner" if not completed_dc_diner_1:
            $completed_dc_diner_1 = True
            jump dc_diner_1
        "Check into the hotel" if not completed_dc_hotel_1:
            $completed_dc_hotel_1 = True
            jump dc_hotel_1

    menu menu_day_choices:
        "Talk to Karen, the ferrywoman" if not completed_dc_karen_1 and unlocked_dc_karen_1:
            $completed_dc_karen_1 = True
            $day_of_last_day_activity = current_day
            jump dc_karen_1
        "Drive to the sheriff station to sign the witness report" if not completed_dc_sarah_1:
            $completed_dc_sarah_1 = True
            $day_of_last_day_activity = current_day
            jump dc_sarah_1
        "Buy new flashlight batteries" if not completed_dc_yggy_1 and unlocked_dc_yggy_1:
            $completed_dc_yggy_1 = True
            $day_of_last_day_activity = current_day
            jump dc_yggy_1
        "Ask Yggy what the fuck that potion thingy was." if not completed_dc_yggy_2 and unlocked_dc_yggy_2:
            $completed_dc_yggy_2 = True
            $day_of_last_day_activity = current_day
            jump dc_yggy_2
        "(I could swing by Yggy's shop and ask if he has any more of that stuff)" if not completed_dc_yggy_3 and unlocked_dc_yggy_3:
            $completed_dc_yggy_3 = True
            $day_of_last_day_activity = current_day
            jump dc_yggy_3
        "Visit Dr. Hardong" if not completed_dc_hardong_1 and unlocked_dc_hardong_1:
            $day_of_last_day_activity = current_day
            $completed_dc_hardong_1 = True
            jump dc_hardong_1
        "Get a coffee at the diner" if not completed_dc_cock_lady_1 and unlocked_dc_cock_lady_1:
            $day_of_last_day_activity = current_day
            $completed_dc_cock_lady_1 = True
            jump dc_cock_lady_1
        "Visit Cecilia Beaver" if not completed_dc_cock_lady_2 and unlocked_dc_cock_lady_2:
            $completed_dc_cock_lady_2 = True
            $day_of_last_day_activity = current_day
            jump dc_cock_lady_2
        "I think that's enough for one day.":
            jump evening_choices
        #todo uncomment once ready
        # "Visit Cecilia Beaver" if not completed_dc_cock_lady_3 and unlocked_dc_cock_lady_3:
        #     $completed_dc_cock_lady_3 = True
        #     jump dc_cock_lady_3
        #todo uncomment once ready
        # "Check yourself into Dr. Hardong's clinic" if not completed_dc_hardong_2 and unlocked_dc_hardong_2:
        #     $completed_dc_hardong_2 = True
        #     jump dc_hardong_2
    jump evening_choices