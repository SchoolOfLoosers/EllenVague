menu evening_choices:
    "Drinks with Sheriff Fuse" if not completed_ec_sarah_1 and unlocked_ec_sarah_1:
        $completed_ec_sarah_1 = True

        pass #todo fill choice
        jump ec_sarah_1
    "Drinks with Mary Rosegold" if not completed_ec_mary_1 and unlocked_ec_mary_1:
        $completed_ec_mary_1 = True
        pass #todo fill choice
        jump ec_mary_1
    "Interview with Patty Maynard" if not completed_ec_patty_1 and unlocked_ec_patty_1:
        $completed_ec_patty_1 = True
        pass #todo fill choice
        jump ec_patty_1