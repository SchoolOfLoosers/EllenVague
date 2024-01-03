menu evening_choices:
    "Drinks with Sheriff Fuse" if not completed_ec_sarah_1:
        $completed_ec_sarah_1 = True

        pass #todo fill choice
        jump ec_sarah_1
    "Drinks with Mary Rosegold" if not completed_ec_mary_1 and unlocked_ec_mary_1:
        $completed_ec_mary_1 = True
        pass #todo fill choice
        jump ec_karen_1