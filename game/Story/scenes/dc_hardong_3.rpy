label dc_hardong_3:
    scene black at topleft with dis #todo
    "This is as far as the clinic quest line goes at the moment."
    na "You will be directed to the main day choices for now to keep the game playable"
    na "But in the future, this story will span several days, so I recommend you make a savegame now to finish playing this later:) "
    na "Thanks for playing so far!"
    jump next_morning #todo remove
    scene black at topleft with dis #todo
    na "I woke up alone, a cold in my bones that the thin blanket did not even try to hold at bay."
    na "After the day before, my brain hurt just as much as my pride..."
    if dc_hardong_2_had_sex_with_baker_in_shower and dc_hardong_2_had_sex_with_doctor
        na "And my body was just as tired and worn out after letting not one, but two guys have their way with me..."
        na "What the heck was I thinking?"
        na "But as much as my body complained, it wasn't exactly complaining loudly."
        na "More like a cozy, lazy complaint, with my eyes still closed and just allowing me to FEEl every muscle and neve ending."
        na "In fact, I felt more myself than I had in a long time."
        na "So of course, the nurse had to waltz in and destroy any hint of cozy morning atmosphere."
        na "Not that the room lend itself to that anyway, now that I had both eyes open..."
    else:
        pass #todo
    scene black at topleft with dis #todo
    v "Good morning."
    v "I am glad you are still here."
    if (dc_hardong_2_had_sex_with_baker_in_shower and dc_hardong_2_evaded_mud_bath) or dc_hardong_2_had_sex_with_doctor:
        v "And I can smell that I was right about you."
        v "This whole room smells like sweat and sex."
        v "I knew a pretty bird like you wouldn't be able to keep her legs shut when the doctor comes to visit."
        v "Pathetic."
    scene black at topleft with dis #todo
    v "Now, come with me, we have some special treatment for you today."
    v "I am sure a pathetic slut like you will like it."
    na "There was something powerless about her words, like she desperately clung to a sense of authority she no longer possessed."
    na "And the more she used words like pathetic to describe me, the more it felt like she was talking about herself."
    na "Like she saw something in me that reminded her of herself."
    na "It made it real easy to go along with her bullying."
    na "In a few days, I would be out of there, and she would always remain the head nurse, always remain stuck in her own head."
    na "And that seemed like a worse fate than anything she could dish out herself."
    na "Or at least I thought so, until I walked into the room and saw the chair."
    mc "The fuck is this?"
    v "This is a relaxed day of just sitting around, doing nothing."
    v "A pathetic lazy slut like you should be used to that."
    v "Get inside."
    menu:
        "Okay, this looks like fun.":
            $dc_hardong_3_okay_this_looks_like_fun = True
            mc "Okay, this looks like fun."

            pass #todo fill choice
        "I am not getting in that chair.":
            $dc_hardong_3_i_am_not_getting_in_that_chair = True
            mc "I am not getting in that chair."
            pass #todo fill choice
        "Okay, this is enough. I'm leaving.":
            $dc_hardong_3_okay_this_is_enough_im_leaving = True
            mc "Okay, this is enough. I'm leaving."
            pass #todo fill choice
            jump next_morning
    scene black at topleft with dis #todo
    na "It was excessively weird to lie there, completely unable to move."
    na "Completely unable to leave."
    na "Before I got into that chair, I had at least had the choice of leaving."
    na "And now, for the first time in ages, I was completely out of options."
    na "And in the hands of a woman who clearly enjoyed bullying anyone who had the misfortune of ending up under her control."
    na "And she knew exactly that the worst part about this process was the wait, and not knowing what was coming."
    na "Or who was coming."
    na "I certainly wasn't, just as much as I wasn't going."
    na "It almost relieved me when I head the heavy footsteps walking down the hallway."
    na "Say what you want about that Baker guy, but at least he was human, someone to speak to."
    na "But then, the steps walked past the door without even pausing, fading quickly as he moved along."
    na "And part of me had to compliment Vivian for her cunning."
    na "Baker probably didn't even know I was in here, she could have sent him on any kind of errand that led him past the door."
    na "The woman was smart, I had to give her that."
    na "No matter how ugly her hatred might have made her, that was nothing against the ugliness of her mind."
    na "So I just closed my eyes and tried to rest my mind."
    na "And of course, my mind started racing, and spiraling out of control."
    na "I saw all the people I had wronged in the past, and relived all the memories of times when I had embarrassed myself..."
    na "All the guys who I had been sure about, only to find out that they had little interest in me past the point where we got dressed again."
    na "That one guy in particular whom I would have married, and who saw nothing in my eyes that interested him."
    na "And then, the steps returned."
    menu:
        "Call out.":
            $dc_hardong_3_call_out = True

            pass #todo fill choice
        "Stay silent.":
            $dc_hardong_3_stay_silent = True
            pass #todo fill choice
    scene black at topleft with dis #todo
    na "Another eternity passed, and I had no way of determining time in there."
    na "It was a room without windows, so not even the sun could have given me any hints."
    na "All I knew was that there was a clock over the door, set to precisely 12 o'clock, with the batteries taken out."
    na "Clearly on purpose, to fuck with the mind of whoever had the misfortune of ending up in that chair."
    na "And it began to occur to me that there was a non-zero chance that she would not come back to fetch me today."
    na "And tell the doctor something about not being able to take visitors..."
    na "Or telling him that I didnt want to see anyone..."
    na "Nothing I could do about that."
    na "Nothing I could do about pretty much anything."
    na "Like the fact I had to pee."
    na "And more so by the minute, or whatever frame of time was passing."
    menu:
        "Hold it in.":
            $dc_hardong_3_hold_it_in = True

            pass #todo fill choice
        "Just pee on the floor.":
            $dc_hardong_3_just_pee_on_the_floor = True
            pass #todo fill choice
    scene black at topleft with dis #todo
    na "Suddenly, and without any prior warning, the door opened up."
    na "And the gloating face of that stupid nurse appeared in front of me."
    v "Good evening, I hope you had a relaxing time."
    if dc_hardong_3_just_pee_on_the_floor:
        v "I knew a stupid slut like you couldn't be left alone for five minutes before peeing herself."
        v "Pathetic, like the rest of you."
    if dc_hardong_3_had_sex_with_baker_in_chair:
        scene black at topleft with dis #todo
        v "Hard to believe that even while tied up, you still find a way to get that cunt of yours stretched."
        v "I hope you know how pathetic that is, that you would beg a guy to fuck you."
        v "No class, no shame."
        v "No self respect."
        if not dc_hardong_3_just_pee_on_the_floor:
            na "I barely noticed anything she said, or the mean look in her eyes..."
            na "All I could think about was that I needed to pee..."
            na "And that she was standing close..."
            na "So close..."
            menu:
                "Pee all over her.":
                    $dc_hardong_3_peed_all_over_vivian = True

                    pass #todo fill choice
                "Please, let me out, I have to pee so bad.":
                    $dc_hardong_3_please_let_me_out_i_have_to_pee_so_bad = True
                    mc "Please, let me out, I have to pee so bad."
                    pass #todo fill choice
    #todo