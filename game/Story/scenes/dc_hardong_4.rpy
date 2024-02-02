label dc_hardong_4:
    scene black at topleft with dis #todo
    na "I woke up in my bed, weirdly aware of the fact that I was not alone."
    na "And of course, it couldn't be some hot dude I had spent the night with, getting up early to make us breakfast..."
    na "...Kissing me in places he should not even be able to see, just to wake me up..."
    na "No, of course it had to be the stupid head nurse, ruthless in her desire to displease the world with her continued existence."
    v "Good morning, pretty bird."
    v "Good news."
    mc "(Good news for whom?)"
    v "You earned your stay yesterday, so you will now be allowed into the general ward."
    v "That's what you're here for, isn't it?"
    v "To talk to the other crazy people who are locked up here?"
    v "So you can use them to write your shoddy little books. Isn't that right, pretty bird?"
    v "No need to answer that, I know that you have no shame."
    v "So come on, time to go."
    mc "So, I get my clothes back now, don't I?"
    v "What, your socks aren't enough for you?"
    v "We both know that you only need clothes so that you can take them off in front of any men who smile at you."
    v "But, since I do not want to upset the other patients, you will get this gown."
    v "Try not to get it dirty."
    scene black at topleft with dis #todo
    na "For something so thin, the gown really made a world of a difference, more than I had thought it would."
    na "Over the past days, I had almost gotten used to being naked around people who were dressed..."
    na "But having some fabric around me gave me a sense of security that I had never gotten from a piece of clothing before."
    na "And I felt ready for just about anything that might be coming my way..."
    na "After all, I was pretty sure that no patient could be any more crazy than the head nurse herself."
    scene black at topleft with dis #todo
    na "Whatever I had expected though, it wasn't the downright cozy atmosphere of the general ward."
    na "After the days that lay behind me, I hadn't expected things to be...normal."
    na "As normal as things can get in a mental clinic."
    scene black at topleft with dis #todo
    na "Everything was clean, cozy, and decorated in a style that could have fooled you into thinking you had walked into a movie set."
    na "And the people were all calm, talking to one another..."
    na "At least until they noticed the newcomer."
    scene black at topleft with dis #todo
    v "Everyone, this is Ellen. She will be staying with us for a while."
    scene black at topleft with dis #todo
    c "Ah, Miss Vague."
    c "I told you we would meet again."
    scene black at topleft with dis #todo
    ru "You know this woman?"
    c "I told you about the tourist whom I met at the diner, didn't I?"
    ru "Oh, now I remember."
    c "Careful with this one, Miss Vague, he WILL ask you to let him paint you."
    mc "Please, you can call me Ellen."
    scene black at topleft with dis #todo
    na "I just couldn't help myself, everything felt...cozy."
    na "Warming to the soul, and calming to my nerves."
    na "Only now did I realize how much a few short days had messed with my mind, pushed me into a dark place that only now did I emerge from..."
    na "And how much I needed the comfort of people who clearly stood above the pettiness of the head nurse."
    #todo
    menu dc_hardong_4_afternoon_conversations:
        "Talk to Rupert Lane" if not dc_hardong_4_talked_to_rupert_lane:
            $dc_hardong_4_talked_to_rupert_lane = True
            call dc_hardong_4_talk_to_rupert_lane
            jump dc_hardong_4_afternoon_conversations
        "Talk to Cecilia" if not dc_hardong_4_talked_to_cecilia:
            $dc_hardong_4_talked_to_cecilia = True
            call dc_hardong_4_talk_to_cecilia
            jump dc_hardong_4_afternoon_conversations
        "I think I'll head back to my room, now." if not dc_hardong_4_i_think_ill_head_back_to_my_room_now:
            $dc_hardong_4_i_think_ill_head_back_to_my_room_now = True
            mc "I think I'll head back to my room, now."
            jump dc_hardong_4_evening

label dc_hardong_4_talk_to_cecilia:
    scene black at topleft with dis #todo
    #todo we learn from cecilia about the fact that vivian goes into an abandoned part of the clinic every Friday.
    return

label dc_hardong_4_talk_to_rupert_lane:
    scene black at topleft with dis #todo
    #todo talk about vivian and he tells us that there are secret passageways, so we unlock the pathway to follow vivian
    mc "Hey, you are Rupert, right?"
    ru "That would be me, yes."
    mc "And you are a painter?"
    ru "Also correct."
    ru "Do you want to see my paintings?"
    menu:
        "Of course":
            $dc_hardong_4_looked_at_ruperts_paintings = True
            mc "Of course"
            ru "Really?"
            ru "Most people around here don't care."
            mc "Not everyone is intelligent enough to understand art when they see it."
            ru "Gosh, I know right?"
            ru "Anyway, come with me, and I'll show you."
            jump dc_hardong_4_look_at_ruperts_paintings
        "Not really":
            $dc_hardong_4_not_really = True
            mc "Not really."
            mc "Nothing against you, I'm just not in much of a mood for art right now."
            ru "Fair enough."
            ru "Well, time is aplenty in here, and I won't go anywhere."
            ru "Just let me know if you're ever in the mood."
            pass #todo fill choice
    #todo jump menu_name or return
    return

label dc_hardong_4_evening:
    scene black at topleft with dis #todo

    menu:
        "Follow Vivian":
            $dc_hardong_4_follow_vivian = True
            #todo we sneak after her, but she locks a door behind her that we can not open.
            menu:
                "Look for a secret passageway" if 1!=1: #todo change this to proper variable if we talked to Rupert
                    $dc_hardong_4_look_for_a_secret_passageway = True
                    $dc_hardong_4_saw_vivian_tied_up = True
                    scene black at topleft with dis #todo
                    na "With Rupert's words in mind, I had this prominent feeling that there had to be a way around this door..."
                    na "And sure enough, I found the entryway, just like Rupert had said I would."
                    na "It was hard to explain, but it was almost like I KNEW where to look."
                    na "And a moment later, I was inside a dark corridor, inside the wall..."
                    na "And I was so close on Vivian's heels that I could hear her faint footsteps somewhere in front of me."
                    na "Until, eventually, they stopped, allowing me to catch up."
                    na "And boy, was I not ready for what I saw."
                    na "There she was, the scary head nurse who liked to torture others so much..."
                    na "Getting a little bit of her own medicine."
                    na "Willingly, it seemed."
                    v "Oh god, harder."
                    ba "Are you sure, Ma'am?"
                    v "Do I speak in riddles, Baker?"
                    v "I said hit me."
                    ba "Yes, Ma'am."
                    v "Ugh, just like that."
                    v "Keep going, until I tell you to stop."
                    ba "Yes, Ma'am."
                    na "It was one of the weirdest sights I had ever seen..."
                    na "And, after the past few days..."
                    na "It was one of the hottest things I had ever seen."
                    na "I wanted to be there, right in front of her..."
                    na "Doing things to her that she was begging him for..."
                    na "And I wasn't going to ask twice."
                    na "I wasn't going to ask her anything."
                    na "I was going to give her what she wanted, what she deserved..."
                    na "And anytime Baker hit her again, anytime she squirmed and begged and groaned in pain..."
                    na "I had to put a hand over my own mouth so that they wouldn't be alerted to my presence."
                    na "I just couldn't stop touching myself."
                    na "Couldn't stop rubbing, couldn't stop squeezing my breasts..."
                    na "And I couldn't stop coming."
                    scene black at topleft with dis #todo
                    v "That's enough now."
                    ba "Yes, Ma'am."
                    v "Now, what do I do with you?"
                    v "You don't want me to tell the doctor what you are doing in here, do you?"
                    ba "No, Ma'am."
                    v "Then tell me, what am I supposed to do with you?"
                    v "I need to punish you for your sins."
                    v "Get on your knees."
                    v "Now, if you spill a single drop, I'll tell the doctor everything, and he will have no choice but to fire you."
                    v "And we both know you would never find another place to work at."
                    v "Nobody would hire you."
                    v "Nobody else would waste time and money to train you to do a job you aren't good at."
                    v "You can consider yourself lucky the doctor and I have such a soft spot for people like you."
                    na "With that, she put her clothes back on, then walked out of the room, leaving him behind like a stuffed animal she no longer loved."
                    na "And I had nothing left to do, other than returning to my room."
                    na "And trying to catch a little shuteye, and trying not to think too much about all the weird stuff that was going on in this clinic..."
                    jump dc_hardong_5
                "Use the time to sneak into Vivian's room":
                    $dc_hardong_4_use_the_time_to_sneak_into_vivians_room = True
                    pass #todo fill choice
                    #todo if we do this, we have to hide under the bed because she returns too quickly, then wait until she has fallen asleep to sneak out again.
                    menu dc_hardong_4_menu_hide_from_vivian:
                        "Hide under the bed" if not dc_hardong_4_hide_under_the_bed:
                            $dc_hardong_4_hide_under_the_bed = True
                            pass #todo fill choice
                        "Try to flee through the window" if not dc_hardong_4_try_to_flee_through_the_window:
                            $dc_hardong_4_try_to_flee_through_the_window = True
                            na "My first thought was to flee through the window and hide in the bushes outside..."
                            na "But the window was locked just the same as all the others in the whole clinic."
                            na "And it was probably good, because Vivian would have immediately spotted the open window anyway."
                            jump dc_hardong_4_menu_hide_from_vivian
                        "Hide in the wardrobe" if not dc_hardong_4_hide_in_the_wardrobe:
                            $dc_hardong_4_hide_in_the_wardrobe = True
                            pass #todo fill choice
                    scene black at topleft with dis #todo
                    na "Just in time before Vivian opened the door, I had stowed myself away."
                    na "Even though, I could hear my own heart beating so loud that I was sure Vivian had to be able to hear it as well."
                    na "And, true to form, I could tell that she sensed something off about the room..."
                    na "Luckily though, she seemed preoccupied, and tired."
                    na "She walked across the room restlessly, and I could hear her picking things up only to put them down again."
                    na "She pranced for a while, and I didn't even dare to move a single inch."
                    na "The dust was tickling my nose, but I wasn't going to let that happen."
                    na "As much as I liked my nose, I wasn't going to listen to it that night."
                    na "I valued my life more."
                    na "Eventually, she sighed, then started undressing..."
                    if dc_hardong_4_hide_under_the_bed:
                        na "And every time one of her clothes hit the floor, the air waves pushed more dust into my face..."
                    else:
                        na "And all the time, the only thing I could think about was that I hoped to god she slept naked, and didn't need any clothes from the wardrobe..."
                        na "And that already, my legs were starting to hurt in the cramped space of the wardrobe..."
                        na "And there was no telling how quickly she would fall asleep..."
                    scene black at topleft with dis #todo
                    na "Once she was fully naked, she sat down on her bed..."
                    na "Lying down, her legs spread wide..."
                    if dc_hardong_4_hide_under_the_bed:
                        na "I could feel the mattress and bed frame shifting under her weight..."
                    else:
                        na "I could see her through the small crack in the door..."
                    scene black at topleft with dis #todo
                    na "And then, she started running her fingers across her body..."
                    na "Not even knowing she had a silent witness in the room with her..."
                    na "And all I could do was to wait for her to finish, and to fall asleep, before I could hightail it out of the room."
                    scene black at topleft with dis #todo
                    menu:
                        "Masturbate along with her.":
                            $dc_hardong_4_masturbate_along_with_her = True
                            na "I knew I had to pass the time somehow..."
                            if dc_hardong_4_hide_under_the_bed:
                                na "And what else was I supposed to do, while lying under her bed?"
                                na "Read a book?"
                            else:
                                na "My legs were already starting to get cramps, so I figured I might as well."
                            scene black at topleft with dis #todo
                            na "It just seemed like the logical choice..."
                            na "And frankly, the risk involved made it all the hotter..."
                            na "And before I knew it, I felt my mind transcending the realms of reality again..."
                            na "And suddenly, I was there, with her."
                            if inventory_has_dream_dick:
                                na "And when I looked down between my legs, the unfamiliar feeling was explained by my...brand new dick, happily flopping around."
                                na "And, seeing her lying there, naked...well, it didn't stay soft and flopping around for long."
                                na "She looked so...ready, so willing..."
                                menu:
                                    "Start fucking her like she deserves.":
                                        $dc_hardong_4_start_fucking_her_like_she_deserves = True
                                        mc "Hello, Vivian..."
                                        v "Hello, doctor."
                                        na "In my dream, this was how it worked."
                                        na "She saw a dick in front of her, and that could only mean one thing to her..."
                                        na "That her biggest wish was finally getting fulfilled."
                                        mc "Spread your legs, Vivian."
                                        v "I thought you would never ask."
                                        mc "But you are such a beautiful woman, with such a beautiful mind."
                                        v "Oh, doctor, you don't have to FLIRT with me."
                                        v "You know I was yours from the day we met."
                                        v "I always wanted you, not like that stupid bitchy wife of yours."
                                        v "She never deserved you."
                                        v "She had the perfect life here with you, and all she ever did was complain."
                                        v "She deserved everything that happened to her."
                                        menu:
                                            "YOU deserve everything that's happening to you.":
                                                $dc_hardong_4_you_deserve_everything_thats_happening_to_you = True
                                                mc "YOU deserve everything that's happening to you."
                                                v "Ugh, I know, right?"
                                                v "Please don't stop, Doctor..."
                                                v "Never stop..."
                                                v "You waited so long for this..."
                                                v "You could have always had me like this..."
                                                v "Even while she was still alive..."
                                                v "You just would have needed to say the word."
                                                v "I could have been your little secret..."
                                                v "I never liked her, anyway."
                                            "What happened to my wife?":
                                                $dc_hardong_4_what_happened_to_my_wife = True
                                                $dc_hardong_4_learned_about_the_letter_to_his_wife = True
                                                mc "What happened to my wife?"
                                                v "You know what happened, doc."
                                                mc "Act like I have no clue."
                                                v "Hah, okay then."
                                                v "She left you."
                                                v "She even wrote you a letter, didn't she?"
                                                v "And then, she just left."
                                                v "Never returned."
                                                menu:
                                                    "How do you know about the letter?":
                                                        $dc_hardong_4_how_do_you_know_about_the_letter = True
                                                        mc "How do you know about the letter?"
                                                        v "You were never supposed to know this, doc, but I am like wax in your fingers."
                                                        v "I saw how down you were when she left you, how much you craved to hear her voice just one last time..."
                                                        v "Explaining to you why she left you..."
                                                        v "As if that would have made a difference."
                                                        v "One day, I could no longer take it, seeing you sitting there, barely interested in the work that you love."
                                                        v "So, I sat down, and wrote that letter for you."
                                                        v "And it was the right choice, it got you back into our world, the real world."
                                                        pass #todo fill choice
                                                    "Remind me again what was in the letter?":
                                                        $dc_hardong_4_remind_me_again_what_was_in_the_letter = True
                                                        mc "Remind me again what was in the letter?"
                                                        v "Don't tell me you forgot."
                                                        mc "I will never forget those words, but tell them to me regardless."
                                                        v "Alright, I know those words by heart..."
                                                        v "She told you why she left, that she couldn't stand it all anymore..."
                                                        v "The place, the silence, the crazy people..."
                                                        v "And she told you that she saw you looking at me, flirting behind her back..."
                                                        v "Even though you never did..."
                                                        v "Even though you always could have..."
                                                        v "You were so loyal to her..."
                                                        v "She never deserved you..."
                                                pass #todo fill choice
                                            "I always wanted you, Vivian.":
                                                $dc_hardong_4_i_always_wanted_you_vivian = True
                                                mc "I always wanted you, Vivian."
                                                pass #todo fill choice
                                        pass #todo fill choice
                                    "Leave her":
                                        $dc_hardong_4_Leave her = True
                                        pass #todo fill choice
                                #todo
                            elif inventory_has_dream_vibrator:
                                #todo
                            pass #todo fill choice
                        "Just wait.":
                            $dc_hardong_4_just_wait = True
                            pass #todo fill choice

                    #todo

                "Go back to your room":
                    $dc_hardong_4_go_back_to_your_room = True
                    pass #todo fill choice
            pass #todo fill choice
        "Nah, I don't want to waste any more time on this woman than necessary.":
            $dc_hardong_4_nah_i_dont_want_to_waste_any_more_time_on_this_woman_than_necessary = True
            mc "Nah, I don't want to waste any more time on this woman than necessary."
            pass #todo fill choice
            jump dc_hardong_5
    #todo we can sneak through the clinic and spy on the nurse who is tied up and excessively tickled by Baker until she orgasms (make this optional and only available if we find a secret passageway). If we masturbate while watching her, we enter a shadow state and can follow her and have to hide while she thinks she is being followed (all in dream), maybe with some image buttons to pick where to hide. If we manage to follow her back to her room, then we can watch her talking to herself (in dream). We learn about her affection for the doctor, and her disdain for him still being attached to his wife, even decades after she left him. And then, some cryptic hint at "he doesn't even know how near she is" etc., or "if only he knew she never really left him.". This will spark a new quest series where we can sleep with baker to have him tie her up longer / go slower so we have more time to physically go through her stuff, and
    #todo jump menu_name or return

label dc_hardong_4_look_at_ruperts_paintings:
    scene black at topleft with dis #todo
    #todo
    ru "Would you allow me to paint you?"
    menu:
        "But only if you paint me naked.":
            $dc_hardong_4_but_only_if_you_paint_me_naked = True
            mc "But only if you paint me naked."
            #todo
            ru "Okay, I am almost done."
            ru "If you want, I can paint one special detail, anything that you want."
            ru "And who knows, maybe with the power of art, those things will become a reality."
            menu:
                "Can you paint a little vibrator into my hands?":
                    $dc_hardong_4_can_you_paint_a_little_vibrator_into_my_hands = True
                    $inventory_has_dream_vibrator = True
                    mc "Can you paint a little vibrator into my hands?"
                    mc "God knows I could use a little friend in here."
                    ru "Consider it done."
                    ru "There you go, that was easy."
                    mc "That's a cute one."
                    ru "But it's very powerful."
                    ru "You only need to touch yourself with it, and you'll start shaking immediately."
                    mc "That's not how vibrators work..."
                    ru "Not the ones you're used to."
                    mc "So this one is magic, huh?"
                    ru "Very powerful."
                    menu:
                        "Well, thank you for that.":
                            $dc_hardong_4_well_thank_you_for_that = True
                            mc "Well, thank you for that."
                            ru "Pleasure to help."
                            mc "As I'm sure it will be mine, if I ever find myself living in a painting."
                            ru "They do say that my paintings bring emotions into reality."
                            mc "That is such an art magazine review."
                        "I could really use something powerful in me right now.":
                            $dc_hardong_4_i_could_really_use_something_powerful_in_me_right_now = True
                            mc "I could really use something powerful in me right now."
                            na "At first, I thought he somehow missed the tone in my voice, or the meaning of the actual words..."
                            na "Luckily, he only took some time to adapt, to realize I was serious."
                            na "And he was smart enough not to ask too many questions."
                            call dc_hardong_4_sex_with_rupert
                "Can you draw me with a dick?":
                    $dc_hardong_4_can_you_draw_me_with_a_dick = True
                    $inventory_has_dream_dick = True
                    mc "Can you draw me with a dick?"
                    mc "I've always wanted a dick."
                    ru "Really? For what?"
                    mc "To fuck hot chicks, what else?"
                    mc "And to piss in the kitchen sink of people I don't like."
                    mc "That's what dicks are for, right?"
                    ru "They also get in the way a lot, let me tell you."
                    ru "At least when they are big enough."
                    menu:
                        "Ignore his remark":
                            $dc_hardong_4_ignore_his_remark = True
                        "Oh, so you have a big dick, huh?":
                            $dc_hardong_4_oh_so_you_have_a_big_dick_huh = True
                            mc "Oh, so you have a big dick, huh?"
                            ru "You want to see it?"
                            menu:
                                "Uh, I'm good, thanks.":
                                    $dc_hardong_4_uh_im_good_thanks = True
                                    mc "Uh, I'm good, thanks."
                                    ru "You don't know what you're missing, but okay."
                                "Sure, let's see it.":
                                    call dc_hardong_4_sex_with_rupert
                    scene black at topleft with dis #todo
                    ru "Anyway, that's that."
                    ru "Here you go, with a big long shlong."
                    mc "Perfect, just what I needed."
                "I like myself the way I am.":
                    $dc_hardong_4_i_like_myself_the_way_i_am = True
                    mc "I like myself the way I am."
                    ru "You certainly look pretty."
                    mc "Thank you."
            pass #todo fill choice
        "As long as I get to keep my clothes on.":
            $dc_hardong_4_as_long_as_i_get_to_keep_my_clothes_on = True
            mc "As long as I get to keep my clothes on."
            ru "Well, of course, you don't have to worry about me."
            mc "That's rare for guys."
            ru "That view seems jaded to me."
            ru "But then again, a pretty lady like you probably draws the eyes of every passerby."
            na "Say what you wanted about the guy, but he seemed almost effortless about his flirting."
            na "Just as his paintstrokes seemed effortless, determined..."
            na "And the quick, controlled motions were a clear testament to his craft and years of practice..."
            pass #todo fill choice
        "I don't really have time for that.":
            $dc_hardong_4_i_dont_really_have_time_for_that = True
            mc "I don't really have time for that."
            pass #todo fill choice
    scene black at topleft with dis #todo
    ru "Well, I don't want to keep you any longer."
    mc "You mean you have get back to your art?"
    ru "You really inspired me, Ellen."
    mc "Uh, thanks."
    mc "See you around, Rupert."
    #todo we can let him draw us, and if we do, he asks us what he should draw us with. We can then get that item in our dream sequences, like a vibrator that we can use to wake up right before being discovered. we can also get a dick for the dreams, and then we can fuck Vivian in our dreams to get back at her.
    return

label dc_hardong_4_sex_with_rupert:
    $dc_hardong_4_had_sex_with_rupert = True
    mc "Sure, let's see it."
    na "Say what you want, but I kinda liked the guy."
    na "He hadn't done a single disrespectful thing so far, and that really elevated him above the staff."
    na "And he had something in his eyes that made me do a double take..."
    na "It was like he was seeing things that others could not..."
    na "And he was seeing something in me."
    na "And the more he saw of me, the more I saw him inside of me, using me as inspiration..."
    na "Just like he inspired me..."
    na "And it seemed like we both needed A LOT of inspiration..."
    na "Big inspiration..."
    na "Because he hadn't lied about that..."
    na "And I was pretty helpless against this man's desire, and helpless against my own."
    na "It was like he had the hunger of years without a woman in his eyes, and like I was the first person in years to truly understand what he was all about..."
    na "And he was the first guy in years who understood my own creative struggles..."
    na "Or the struggles of trying to get a hold of something to hold on to."
    ru "Do you think you can stay like that for a while?"
    ru "I need to paint that pose."
    na "I guess I could keep still a little while longer, bathing in the sun as I was breathing in the atmosphere..."
    na "Plus, he was a fast painter."
    na "And a strong lover, who had worn me out enough to make me not want to move anywhere, anytime soon."
    ru "That is perfect."
    ru "You are quite a beautiful woman."
    na "After the last few days, that was exactly what I needed to hear."
    mc "Thank you."
    return