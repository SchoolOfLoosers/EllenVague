label evening_choices:
    menu menu_evening_choices:
        "Have a drink with Sheriff Fuse" if not completed_ec_sarah_1 and unlocked_ec_sarah_1:
            $completed_ec_sarah_1 = True
            jump ec_sarah_1
        #todo remove once ready
        # "Drinks with Mary Rosegold" if not completed_ec_mary_1 and unlocked_ec_mary_1:
        #     $completed_ec_mary_1 = True
        #     jump ec_mary_1
        "Interview with Patty Maynard" if not completed_ec_patty_1 and unlocked_ec_patty_1:
            $completed_ec_patty_1 = True
            jump ec_patty_1
        "Visit Patty" if not completed_ec_patty_2 and unlocked_ec_patty_2:
            $completed_ec_patty_2 = True
            jump ec_patty_2
        "Have a drink at the hotel bar" if not completed_ec_jay_1:
            $completed_ec_jay_1 = True
            jump ec_jay_1
        "Go hiking with Jay" if not completed_ec_jay_2 and unlocked_ec_jay_2:
            $completed_ec_jay_2 = True
            jump ec_jay_2
        # "Go hunting with Jay" if not completed_ec_jay_3 and unlocked_ec_jay_3:
        #     $completed_ec_jay_3 = True
        #     jump ec_jay_3
        #todo remove comment once ready
        # "Go to Ragnar's home concert" if not completed_ec_concert_1 and unlocked_ec_concert_1:
        #     $completed_ec_concert_1 = True
        #     jump ec_concert_1
        #todo remove comment once ready
        "Actually, I could just stay inside and use this \"secret potion\" that Yggy sold me..." if not completed_ec_potion_masturbation_1 and inventory_has_aphrodisiac_potion:
            $completed_ec_potion_masturbation_1 = True
            $inventory_has_aphrodisiac_potion = False
            jump ec_potion_masturbation_1
        "Invite Yggy over to your place" if not completed_ec_yggy_1 and unlocked_ec_yggy_1:
            $completed_ec_yggy_1 = True
            jump ec_yggy_1
        #todo
        # "I wonder if Jay has time to violate my privacy..." if not completed_ec_sex_with_jay_2:
        #     $completed_ec_sex_with_jay_2 = True
        #     jump ec_sex_with_jay_2
        #todo
        # "I wonder if Jay has gotten bored of me yet..." if completed_ec_sex_with_jay_2 and not completed_ec_sex_with_jay_3:
        #     $completed_ec_sex_with_jay_3 = True
        #     jump ec_sex_with_jay_3
        #todo put this choice back in as soon as I figure out how to properly check for remaining choices
        # "I think I'll just go to sleep early today...":
        #     jump next_morning

    "Thank you for playing!"
    "This is how far the story goes at the moment, I hope you enjoyed it so far!"
    "If you want to support my work and play the new chapter 2 weeks early, you can subscribe to my Patreon."
    "Thank you for your support, it helps a lot!"
    menu evening_choices_menu_Patreon:
        "Sure, I want to play the next chapter early!":
            $renpy.run(OpenURL("https://www.patreon.com/ellenvague"))
            mc "Thank you for your support!"
            return
        "Just take me to the main menu, thanks.":
            mc "Alright, see you soon!"
            return