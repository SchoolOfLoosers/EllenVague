label evening_choices:
    menu menu_evening_choices:
        "Have a drink with Sheriff Fuse" if not completed_ec_sarah_1 and unlocked_ec_sarah_1:
            $completed_ec_sarah_1 = True
            jump ec_sarah_1
        "Drinks with Mary Rosegold" if not completed_ec_mary_1 and unlocked_ec_mary_1:
            $completed_ec_mary_1 = True
            jump ec_mary_1
        "Interview with Patty Maynard" if not completed_ec_patty_1 and unlocked_ec_patty_1:
            $completed_ec_patty_1 = True
            jump ec_patty_1
        "Have drinks with Patty" if not completed_ec_patty_2 and unlocked_ec_patty_2:
            $completed_ec_patty_2 = True
            jump ec_patty_2
        "Have a drink at the hotel bar" if not completed_ec_jay_1:
            $completed_ec_jay_1 = True
            jump ec_jay_1
        "Go hiking with Jay" if not completed_ec_jay_2 and unlocked_ec_jay_2:
            $completed_ec_jay_2 = True
            jump ec_jay_2
        "Go hunting with Jay" if not completed_ec_jay_3 and unlocked_ec_jay_3:
            $completed_ec_jay_3 = True
            jump ec_jay_3
        "Go to Ragnar's home concert" if not completed_ec_concert_1 and unlocked_ec_concert_1:
            $completed_ec_concert_1 = True
            jump ec_concert_1
        "Actually, I could just stay inside and use this \"secret potion\" that Yggy sold me..." if not completed_ec_potion_masturbation_1 and inventory_has_aphrodisiac_potion:
            $completed_ec_potion_masturbation_1 = True
            $inventory_has_aphrodisiac_potion = False
            jump ec_potion_masturbation_1
    return