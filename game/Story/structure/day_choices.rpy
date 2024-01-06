label day_choices:
    menu menu_day_choices:
        "Drive to the Diner" if not completed_dc_diner_1:
            $completed_dc_diner_1 = True
            pass #todo fill choice
            jump dc_diner_1
        "Check into the hotel" if not completed_dc_hotel_1:
            $completed_dc_hotel_1 = True
            pass #todo fill choice
            jump dc_hotel_1
        "Talk to Karen, the ferrywoman" if not completed_dc_karen_1 and unlocked_dc_karen_1 and completed_dc_hotel_1 and completed_dc_diner_1:
            $completed_dc_karen_1 = True
            pass #todo fill choice
            jump dc_karen_1
    jump evening_choices