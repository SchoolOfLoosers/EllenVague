label dc_hardong_2:
    scene black at topleft with dis #todo
    #todo clinic day 1, s
    e "Welcome, Miss Vague."
    mc "Good morning, doctor."
    e "Let me thank you again for agreeing to go through our process, I am quite interested what you will say."
    e "Let me introduce you to our head nurse, Vivian."
    v "Good morning."
    e "I entrust you Miss Vague now."
    e "And you, Miss Vague, we will talk again in the evening, and you can tell me how you enjoy your stay."
    mc "Thank you, Doctor."
    v "Come with me."
    v "I will show you your room now."
    mc "Oh, this is quite nice."
    v "I am glad to hear that."
    v "Now, take your clothes off."
    mc "What?"
    v "You heard me."
    v "You won't be needing them anytime soon."
    v "Personal clothes and items are unnecessary while you are here."
    menu:
        "Uh, okay, sure.":
            $dc_hardong_2_uh_okay_sure = True
            mc "Uh, okay, sure."

            pass #todo fill choice
        "Would you mind turning around?":
            $dc_hardong_2_would_you_mind_turning_around = True
            mc "Would you mind turning around?"
            pass #todo fill choice
        "I'm not taking my clothes off.":
            $dc_hardong_2_i_m_not_taking_my_clothes_off = True
            mc "I'm not taking my clothes off."
            pass #todo fill choice
    scene black at topleft with dis #todo
    mc "Now, where's my new clothes?"
    v "Who said anything about new clothes?"
    mc "Ha ha, good one."
    v "Lady, do I look like I am in a joking mood?"
    v "I told you, you wouldn't need your clothes."
    mc "Do you expect me to walk around naked?"
    v "Lady, let me tell you something."
    v "You may be the doctor's new favorite pet..."
    v "And he is free to do with you whatever he likes."
    v "But as long as you are in my hand, you listen to what I say."
    v "Around these halls, my words are law, and I don't care if you spread your pretty legs for the doctor or not."
    v "This isn't a wellness trip, little bird."
    mc "Are you crazy?"
    v "You are crazy, or else you wouldn't be here."
    v "We are a clinic, not a hotel."
    v "You can complain to the doctor tonight."
    v "I'm sure he will be happy to listen to anything you have to say."
    v "I'm sure he will make you feel like you matter."
    v "But let me tell you something, you don't matter to me."
    v "Not any more or less than anyone else in here, so don't expect any special treatment."
    v "You will get your clothes back when the doctor declares you healed."
    v "And the doctor relies on my expertise before he makes his decisions."
    v "So you better make sure that I declare you fit and healthy."
    menu:
        "You can't do that to me!":
            $dc_hardong_2_you_cant_do_that_to_me = True
            mc "You can't do that to me!"

            pass #todo fill choice
        "I see, thank you for explaining the process to me.":
            $dc_hardong_2_i_see_thank_you_for_explaining_the_process_to_me = True
            mc "I see, thank you for explaining the process to me."
            pass #todo fill choice
    scene black at topleft with dis #todo
    v "Now, I will give you ten minutes to make yourself at home, and then another nurse will fetch you for today's treatment."
    v "I expect punctuality at all times, so you better get used to that quickly."
    scene black at topleft with dis #todo
    mc "(This woman is batshit crazy!)"
    mc "(Does the doctor know about this?)"
    mc "(He has to, doesn't he?)"
    mc "(Well, we will see about that tonight)"
    mc "(First, I'll have to get through this day.)"
    mc "(They are probably just testing how I react to stress and unknown situations)"
    scene black at topleft with dis #todo
    "A moment later, I could hear heavy footsteps coming down the hallway, the first noise since the head nurse had disappeared."
    scene black at topleft with dis #todo
    "If the declared goal was to test my handling of discomfort, then the man standing in the door did it's part to test me."
    "His eyes were all over me, passing every inch of my body."
    "The only thing safe from his hungry gaze where my eyes."
    scene black at topleft with dis #todo
    ba "Are you Ellen?"
    menu:
        "Yes":
            $dc_hardong_2_Yes = True
            mc "Yes"

            pass #todo fill choice
        "No":
            $dc_hardong_2_No = True
            mc "No"
            pass #todo fill choice
    scene black at topleft with dis #todo
    ba "Well, come with me now."
    mc "Where are we going?"
    ba "To the showers."
    "Somehow, the way he said that didn't make me feel clean."
    "But, that was the point."
    "And I could already tell where this was going."
    menu:
        "Let me guess, this is your job?":
            $dc_hardong_2_let_me_guess_this_is_your_job = True
            mc "Let me guess, this is your job?"
            ba "Yes"
        "Wait for him to say it.":
            $dc_hardong_2_wait_for_him_to_say_it = True
            pass
    scene black at topleft with dis #todo
    ba "Face the wall, and put your hands up against it."
    menu:
        "Don't you dare to touch me!":
            $don_t_you_dare_to_touch_me = True
            mc "Don't you dare to touch me!"
            ba "But the nurse said we need to get you clean."
            mc "Are you sure this is what she meant?"
            ba "Yes"
            mc "Perks of the job, huh?"
            menu:
                "Hold still":
                    $dc_hardong_2_hold_still = True
                    "I could tell that there was no way around this, and that they wanted to test my reaction more than anything."
                    "Or else, they wouldn't have undressed me, then sent me to the showers with a guy who couldn't wait to get his hands on me."
                    "And sure enough, he took his time with \"getting me clean\""
                    "His hands all over my body, his fingers digging into my skin, pressing and massaging everything he had no business touching..."
                    "And there was nothing I could reasonably do, that wouldn't just drag this process out."
                    "So I just stood there, hands against the wall, and waited for him to get bored of fondling me."
                    "And with the minutes passing, it became clear that he didn't get this chance often, and made the best of it."
                    "Or maybe, I was just really dirty, and needed a lot of soap."
                "Kick him":
                    $dc_hardong_2_kick_him = True
                    #todo he calls the nurse
                    v "Now, Baker tells me you are a dirty little slut who's afraid of showers."
                    mc "You know exactly that's not it."
                    v "Well, since you are afraid of some soap and a sponge in the hands of a man, it appears that I will have to do the work."
                    v "And I don't like it when you make me work."
                    v "Baker, hold her still."
                    ba "Yes."
                    mc "You really think I couldn't have done this myself?"
                    v "Seems to me like you like to be dirty more than you like to be clean."
                    v "Which means you are a health risk for everyone else."
                    v "Now hold still, and this will be over before you know it."
                    v "See, that wasn't so bad, was it?"
                    v "Now, don't make me do this again, because I won't be this nice again."
                    "What ever counted as nice for her."
                    "My skin had never felt so rough after taking a shower."
                    v "Don't make me come back here, I have more important things to do."
        "Say nothing":
            $dc_hardong_2_say_nothing = True
            "I could tell that there was no way around this, and that they wanted to test my reaction more than anything."
            "Or else, they wouldn't have undressed me, then sent me to the showers with a guy who couldn't wait to get his hands on me."
            "And sure enough, he took his time with \"getting me clean\""
            "His hands all over my body, his fingers digging into my skin, pressing and massaging everything he had no business touching..."
            "And there was nothing I could reasonably do, that wouldn't just drag this process out."
            "So I just stood there, hands against the wall, and waited for him to get bored of fondling me."
            "And with the minutes passing, it became clear that he didn't get this chance often, and made the best of it."
            "Or maybe, I was just really dirty, and needed a lot of soap."
    scene black at topleft with dis #todo we are naked and showered now.
    mc "Are you done?"
    ba "For now."
    ba "Come with me."
    mc "What now?"
    ba "Now, it is time for the mud bath."
    "Of course, that made sense."
    "Making me clean myself right before literally throwing me into the mud, that was just the kind of process that can wear someone down."
    "Showing you that your personal space doesn't matter, and that your time and opinion doesn't matter either."
    "So, I just shrugged, and went along with it."
    scene black at topleft with dis #todo
    ba "In with you, I will tell you when you can get out again."
    "That was the last thing he said, before sitting down and we went to watch each other, because there was nothing else in the room that either of us could have watched."
    "And sure enough, there wasn't a clock to be found anywhere, just the mud that felt almost comfortable as it protected my naked skin from his prying eyes."
    "Not that it did much to actually protect me from the hunger in his eyes."
    "You could just tell that the only thing keeping him in check was the fear of reprisals."
    "And the only thing that stood between me and Vivian letting him off the chain, were the whims of a woman who was clearly unhinged."
    "And so, what felt like hours passed, and I found myself increasingly shut into myself, counting my breathing until the numbers became too large."
    "Then I stopped counting, and started existing."
    scene black at topleft with dis #todo

    dialog

    #todo Check in, see your room, have your clothes taken away, meet the head nurse who ridicules us for being naked (you may be the doctor's new favorite pet, but around here, you do what we say), meet the male nurse who can't take their eyes off us. The nurse puts us through a rigorous course, and in the evening, we get to talk to the doctor and have a choice to snitch on the nurses. If we stay silent, the nurse gives us our socks back as a reward, and if we snitch, they take us to "the chair" where we are tied up all day, and occasionally visited by the male nurse, who masturbates in front of us. We can tell him to "at least fuck me and not just stand there."
    #todo when the head nurse visits us, we can pee on the floor, and if we do, she switches on the vibrator seat so that it vibrates for one minute every hour and tells us to to have fun, putting a clock in front of us. If we control our breathing and time it so that we orgasm, she calls us pathetic, but lets us out of the chair.
    #todo At this point, we have the option to leave the clinic, or stay, and if we complain to the doctor, he will fire the head nurse, who then becomes a shadow out of anger.
    #todo if we stay, we are allowed to go out into the main room to meet the other patients, but have to wear a buttplug tail and remain naked / with socks. This unlocks various conversations with the patients, and we can learn about the head nurse, and that she has a crush on the doctor, but that he told her off, and that is why she hates everyone he takes a liking to.
    #todo There is also a painter whom we can become friends with if we allow him to paint us naked, and he can paint us with one of various items that will help us during dream sequences.I(including a vibrator that allows us to come / wake up quickly / on demand to protect ourselves)
    #todo If we have the vibrator, we can go into the dream, enter the head nurses office, and read through her journal(?), then wake up quickly when she walks in. Here, we can discover incriminating information about her, and slip that to Sarah who then arrests the nurse. If she's arrested, we can visit her in her cell and gloat, and promise her to unlock the cell if she masturbates for us.
    #todo Going through the clinic in any way unlocks various dream sequences that are nightmare scenarios and we have to fight our way through. If we beat the shadows, then the witch becomes interested in us, and we unlock a series of rituals