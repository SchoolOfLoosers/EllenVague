label ec_jay_1:
    scene black at topleft with dis #todo
    j "Good evening, Miss Vague, here for a drink?"
    mc "Please, I can use one."
    j "And can you also use company?"
    mc "Of course, if you have the time to spare."
    j "I do, these have been a quiet few weeks."
    mc "How come, I thought the big parade is just around the corner?"
    j "It is, and that is precisely the reason why."
    j "Everyone schedules their vacations so that they arrive no more than a few days ahead, and then leave again the morning or the week after."
    mc "Ah yes, of course, that makes sense."
    mc "I was wondering why I am seeing so few other tourists around."
    "There it was again, this fluent conversation between us, like he hadn't just asked one of his guests out for drinks, and like I wasn't allowing him the transgression with barely a nod of acknowledgment."
    menu:
        "So, how long have you been living here?":
            $ec_jay_1_asked_how_long_living = True

            pass #todo fill choice
        "Do you flirt with all your guests?":
            $ec_jay_1_asked_if_he_flirts_with_all_guests = True
            j "Only the ones worth flirting with."
            "He wasn't even denying it - and frankly, I liked that about him."
            j "You see, Miss Vague, my family has never been hurting for money."
            j "That is why I have long stopped running this hotel the way most others would, and as long as I come out more or less around a black zero, then I am fine with it."
            j "And that, it gives me the opportunity to talk to the interesting people who stay here, to encourage them to tell their stories, and to maybe leave a tiny bit of themselves here when they inevitably leave again."
            mc "How...fascinating, really."
            mc "Most people wouldn't be able to do that."
            j "Yes, and that is only in part because most people can not afford to live this way."
            j "There are many flaws to everyone of us - but the one I find most despicable is when someone has the means to live well, and doesn't."
            mc "You have a way with words, I'll give you that."
            j "And so do you, from what I am hearing."
            mc "Hearing?"
            j "I figured since our authorship path and my readership habits have not crossed before, I would spare you the act of brushing up on your literary works after you booked your stay with us."
            mc "That is...honest."
            j "I like to think that you will come to appreciate that most about me, if we end up sharing more than the occasional conversation."
            menu ec_jay_1_menu_share:
                "Don't get ahead of yourself" if not ec_jay_1_can_share_bed_tonight:
                    $ec_jay_1_dont_get_ahead_of_yourself = True

                    pass #todo fill choice
                "What do you have in mind?":
                    $ec_jay_1_what_have_in_mind = True
                    j "I would like to get a better feel for what you are really about, Miss Vague."
                    mc "In what regard?"
                    j "I want to know who you are when nobody is around to witness you do it."
                    j "Apart from me, of course, but that can not be helped."
                    j "There is a hiking path leading up from the main road near the old lumberyard, not a lot of people know about it."
                    mc "You want to drag me into the woods?"
                    j "At night, no less."
                    mc "Everyone else has been warning me of exactly that, telling me not to set even a foot into the wilderness at night."
                    j "And that is clearly the smart choice, though not necessarily the most interesting one."
                    j "Well, an offer has been made, and I now play the ball back into your court, should you consider to accept it some day."
                    j "I will still be here when you leave again, so do not feel rushed to make a decision."
                    j "And now, I will leave you alone with yourself, and your own thoughts."
                    j "Have a good night, Miss Vague."
                    mc "Uh, you too, have a good night."
                    jump next_morning
                "We can share something tonight, if you want.":
                    $ec_jay_1_can_share_bed_tonight = True
                    pass #todo fill choice
                    jump ec_jay_1_menu_share
            pass #todo fill choice
        "Are there any places you can recommend that are worth a visit?":
            $ec_jay_1_asked_places_to_visit = True
            pass #todo fill choice
    #todo drink at hotel bar, flirt with him but trying to have sex with him leads to "I would like to get to know you better", with plenty of possibiities for him to dislike what we do (interview with patty for example, the two can't stand each other.)
    jump next_morning