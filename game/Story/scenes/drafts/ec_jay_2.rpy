label ec_jay_2:
    "This scene is not yet ready to play, I will work on it as soon as I find the time. Thanks for your understanding."
    return #todo remove this and line above
    #todo asset: https://www.daz3d.com/sawmill-props https://www.daz3d.com/picnic-area-exterior https://www.daz3d.com/backwoods-shooting-range-for-genesis-3-and-8-male-s-and-female-s
    scene black at topleft with dis #todo
    j "Welcome, Miss Vague."
    j "Are you prepared for our little hike?"
    mc "I am, but I feel like you can call me Ellen now, considering I allow you to literally drag me into the woods at night."
    j "That is true. So, come on then, let us surround ourselves with trees."
    mc "Where are we going, anyway?"
    mc "Or is that a secret?"
    j "Not anymore, it isn't."
    j "First, I thought we could briefly explore the old sawmill, and then we can carve out a path to the old lumberyard."
    j "It will be fully dark by the time we get there, so I hope your flashlight batteries are topped up."
    mc "Yep."
    j "Good, then let's go."
    #todo explore sawmill
    scene black at topleft with dis #todo
    mc "What's so special about that lumberyard, by the way?"
    j "Nothing, and everything."
    j "It has some personal meaning to me, because it was still active when I was young - and I worked my first summer job there."
    j "Apart from that, it really isn't anything special."
    j "Still a good hike, though."
    scene black at topleft with dis #todo show shadow watching them.
    menu:
        "Say nothing":
            $ec_jay_2_said_nothing_about_presence = True

            pass #todo fill choice
        "Say, I can't shake the feeling that we aren't alone out here...":
            $ec_jay_2_mentioned_the_presence = True
            mc "Say, I can't shake the feeling that we aren't alone out here..."
            j "Oh, that would be the queen of the forest."
            mc "Hah, I should have known you would say that."
            j "There are enough square miles out here to put the chance of meeting someone else during daylight hours is already in the low single digits."
            j "Now at night? Pretty unlikely."
            mc "Yes, I know, but still..."
            j "Don't worry, I'm only teasing you - but it's not like I don't get it."
            j "And for you, coming out of the city, I'm sure it comes with the added difficulty of having to adapt to everything."
            mc "Ugh, tell me about it."
            mc "I mean, it's all so...different."
            mc "Calmer, and friendly."
            mc "Makes me wonder why people in the city can't be like that."
            j "Well, let's not pretend that people out here can't have their darker sides."
            menu ec_jay_2_menu_dark:
                "Well, of course, but...":
                    $ec_jay_2_well_of_course_but_ = True
                    mc "Well, of course, but..."

                    pass #todo fill choice
                    jump next_morning
                "How dark are we talking, here?":
                    $ec_jay_2_how_dark_are_we_talking_here = True
                    mc "How dark are we talking, here?"
                    j "Nothing I could prove, so I will keep my mouth shut about it."
                    j "All I'm saying is that people will always be people."
                    mc "Ah yes, that is true."
                    j "Sorry I started about it, I usually try not to talk when I don't have anything to say."
                    mc "Oh, don't worry, I somehow needed you to set me straight on this matter."
                    j "Good, then let us focus on what we can see and know for sure is here again, shall we?"
                    mc "I can't see shit."
                    j "That doesn't mean you can't step into it."
                    mc "Hah, good one."
                    j "So, tell me, do you feel anything special about this place?"
                    menu:
                        "Not really, no.":
                            $ec_jay_2_not_really_no = True
                            mc "Not really, no."
                            mc "I mean, don't get me wrong, it's pretty cool, but..."
                            mc "Nothing special."
                            j "Hah, that's fair enough."
                            j "I guess it's just my own fading nostalgia about growing up around here, then."
                            mc "Can you explain what it is that you feel?"
                            j "I can try."
                            j "There is something about this place that makes me feel like it was frozen in time."
                            j "You see that little hut over there?"
                            j "It was there just like that, more than thirty years ago."
                            j "Us workers used to take our break there, and my girlfriend and I used to meet here, where nobody could see us."
                            scene black at topleft with dis #todo
                            j "I know it's probably stupid and nostalgic, but...you know."
                            menu:
                                "Oh, I can totally understand that, it's rare for a place to not change at all.":
                                    $ec_jay_2_oh_i_can_totally_understand_that_its_rare_for_a_place_to_not_change_at_all = True
                                    mc "Oh, I can totally understand that, it's rare for a place to not change at all."
                                    j "Yes, a lot of water has gone downstream since then."
                                    menu:
                                        "And how much have you changed in all that time?":
                                            $ec_jay_2_and_much_how_have_you_changed_in_all_that_time = True
                                            mc "And how much have you changed in all that time?"
                                            j "A lot, and very little."
                                            j "How's that for a non-answer?"
                                            mc "Hah, but it's not like I don't get it."
                                            j "I would say my main beliefs haven't really changed much, but everything around that has turned around."
                                            j "Or even turned over, coming out where I started, with a few stops in between."
                                            mc "Grown up, huh?"
                                            j "Indeed."
                                            menu:
                                                "How grown are we talking here, exactly?":
                                                    $ec_jay_2_how_grown_are_we_talking_here_exactly = True
                                                    mc "How grown are we talking here, exactly?"
                                                    j "I can tell you one thing:"
                                                    j "I am older and wiser now, able to pick up on those subtle clues."
                                                    mc "I wouldn't exactly call myself subtle right now."
                                                    j "Then I won't do, either."
                                                    j "Do you want to undress yourself, or should I do it for you?"
                                                    jump ec_jay_2_sex_with_jay
                                                "Well, thanks for showing me this place":
                                                    $ec_jay_2_well_thanks_for_showing_me_this_place = True
                                                    mc "Well, thanks for showing me this place."
                                                    mc "I feel like we should get going, now, before I fall asleep standing."
                                                    j "Then that's what we'll do."
                                                    j "Watch your steps, I would hate for you to come out of our little trip with visible bruises."
                                                    scene black at topleft with dis #todo
                                                    j "There we go, that's the main road again."
                                                    j "Congratulations, you made it back out of the woods safe and healthy."
                                                    mc "Thank you, this was fun."
                                                    j "I'm glad you enjoyed this little adventure."
                                                    menu:
                                                        "I wouldn't mind doing this again sometime.":
                                                            $ec_jay_2_i_wouldnt_mind_doing_this_again_sometime = True
                                                            $unlocked_ec_jay_3 = True
                                                            mc "I wouldn't mind doing this again sometime."
                                                            j "In that case, I will let you know the next time I come up with a trip worth taking."
                                                            mc "I look forward to that."
                                                            mc "And now, have a good night."
                                                            j "In my role as the owner of the hotel you'll be sleeping in, I doubly hope you will have a good night."
                                                            mc "Hah, I'm sure I will."
                                                            jump next_morning
                                                        "Thanks, have a good night.":
                                                            $ec_jay_2_thanks_have_a_good_night = True
                                                            mc "Thanks, have a good night."
                                                            j "In my role as the owner of the hotel you'll be sleeping in, I doubly hope you will have a good night."
                                                            mc "Hah, I'm sure I will."
                                                            jump next_morning

                                        "Well, thanks for showing me this place.":
                                            $ec_jay_2_well_thanks_for_showing_me_this_place = True
                                            mc "Well, thanks for showing me this place."
                                            mc "I feel like we should get going, now, before I fall asleep standing."
                                            j "Then that's what we'll do."
                                            j "Watch your steps, I would hate for you to come out of our little trip with visible bruises."
                                            scene black at topleft with dis #todo
                                            j "There we go, that's the main road again."
                                            j "Congratulations, you made it back out of the woods safe and healthy."
                                            mc "Thank you, this was fun."
                                            j "I'm glad you enjoyed this little adventure."
                                            menu:
                                                "I wouldn't mind doing this again sometime.":
                                                    $ec_jay_2_i_wouldnt_mind_doing_this_again_sometime = True
                                                    $unlocked_ec_jay_3 = True
                                                    mc "I wouldn't mind doing this again sometime."
                                                    j "In that case, I will let you know the next time I come up with a trip worth taking."
                                                    mc "I look forward to that."
                                                    mc "And now, have a good night."
                                                    j "In my role as the owner of the hotel you'll be sleeping in, I doubly hope you will have a good night."
                                                    mc "Hah, I'm sure I will."
                                                    jump next_morning
                                                "Thanks, have a good night.":
                                                    $ec_jay_2_thanks_have_a_good_night = True
                                                    mc "Thanks, have a good night."
                                                    j "In my role as the owner of the hotel you'll be sleeping in, I doubly hope you will have a good night."
                                                    mc "Hah, I'm sure I will."
                                                    jump next_morning
                                "And what did you do to your girlfriend when you were out here all alone?":
                                    $ec_jay_2_and_what_did_you_do_to_your_girlfriend_when_you_were_out_here_all_alone = True
                                    scene black at topleft with dis #todo
                                    mc "And what did you do to your girlfriend when you were out here all alone?"
                                    scene black at topleft with dis #todo
                                    j "You want me to tell you?"
                                    menu:
                                        "As long as you don't get any ideas...":
                                            $ec_jay_2_as_long_as_you_dont_get_any_ideas_ = True
                                            mc "As long as you don't get any ideas..."
                                            j "Oh, don't worry, I know how to behave around a lady of class, who trusts me enough to even walk out here with me."
                                            j "I wouldn't betray that trust."
                                            mc "Charming."
                                            j "That about describes my attempts with the aforementioned lady, as well."
                                            mc "And did it work?"
                                            j "More often than not."
                                            mc "I have no trouble believing that, it's a very romantic place."
                                            j "You will understand if I shroud the rest of this story in the cloak of secrecy."
                                            menu:
                                                "Don't you dare, I want the gritty details!":
                                                    $ec_jay_2_don_t_you_dare_i_want_the_gritty_details = True
                                                    mc "Don't you dare, I want the gritty details!"
                                                    j "Do you, now?"
                                                    mc "Yes."
                                                    j "But I'm sure you wouldn't want me to talk about you, if you were in her spot, right?"
                                                    mc "I really don't care if you tell the next girl you bring out here about what you did to me tonight."
                                                    j "I wasn't aware I would be doing anything to you at all."
                                                    menu:
                                                        "Oh come on, we both know where tonight would lead...":
                                                            $ec_jay_2_oh_come_on_we_both_know_where_tonight_would_lead_ = True
                                                            mc "Oh come on, we both know where tonight would lead..."
                                                            j "To be honest, I gave us about a thirty percent chance for one of us to uphold our morals."
                                                            mc "That's sweet, but I really don't want you to hold anything other than my hips."
                                                            j "A chore that I quite look forward to."
                                                            mc "I'm sure you do."
                                                            jump ec_jay_2_sex_with_jay
                                                        "You are really too classy for your own good, Mister High Morals.":
                                                            $ec_jay_2_you_are_really_too_classy_for_your_own_good_mister_high_morals = True
                                                            mc "You are really too classy for your own good, Mister High Morals."
                                                            mc "But fine, suit yourself."
                                                            mc "I hope you are aware that you're purposefully missing out here."
                                                            scene black at topleft with dis #todo
                                                            j "I am, and that may just be for the best."
                                                            j "Thank you for trusting me enough for this conversation to deviate from it's path like that."
                                                            mc "Don't thank me, just walk me home now."
                                                            j "Follow me, then."
                                                            scene black at topleft with dis #todo
                                                            j "There we go, that's the main road again."
                                                            j "Congratulations, you made it back out of the woods safe and healthy."
                                                            mc "Thank you, this was fun."
                                                            j "I'm glad you enjoyed this little adventure."
                                                            menu:
                                                                "I wouldn't mind doing this again sometime.":
                                                                    $ec_jay_2_i_wouldnt_mind_doing_this_again_sometime = True
                                                                    $unlocked_ec_jay_3 = True
                                                                    mc "I wouldn't mind doing this again sometime."
                                                                    j "In that case, I will let you know the next time I come up with a trip worth taking."
                                                                    mc "I look forward to that."
                                                                    mc "And now, have a good night."
                                                                    j "In my role as the owner of the hotel you'll be sleeping in, I doubly hope you will have a good night."
                                                                    mc "Hah, I'm sure I will."
                                                                    jump next_morning
                                                                "Thanks, have a good night.":
                                                                    $ec_jay_2_thanks_have_a_good_night = True
                                                                    mc "Thanks, have a good night."
                                                                    j "In my role as the owner of the hotel you'll be sleeping in, I doubly hope you will have a good night."
                                                                    mc "Hah, I'm sure I will."
                                                                    jump next_morning
                                                "Thank you.":
                                                    $ec_jay_2_thank_you = True
                                                    mc "Thank you."
                                                    mc "I wouldn't mind heading home now."
                                                    j "Follow me, then."
                                                    scene black at topleft with dis #todo
                                                    j "There we go, that's the main road again."
                                                    j "Congratulations, you made it back out of the woods safe and healthy."
                                                    mc "Thank you, this was fun."
                                                    j "I'm glad you enjoyed this little adventure."
                                                    menu:
                                                        "I wouldn't mind doing this again sometime.":
                                                            $ec_jay_2_i_wouldnt_mind_doing_this_again_sometime = True
                                                            $unlocked_ec_jay_3 = True
                                                            mc "I wouldn't mind doing this again sometime."
                                                            j "In that case, I will let you know the next time I come up with a trip worth taking."
                                                            mc "I look forward to that."
                                                            mc "And now, have a good night."
                                                            j "In my role as the owner of the hotel you'll be sleeping in, I doubly hope you will have a good night."
                                                            mc "Hah, I'm sure I will."
                                                            jump next_morning
                                                        "Thanks, have a good night.":
                                                            $ec_jay_2_thanks_have_a_good_night = True
                                                            mc "Thanks, have a good night."
                                                            j "In my role as the owner of the hotel you'll be sleeping in, I doubly hope you will have a good night."
                                                            mc "Hah, I'm sure I will."
                                                            jump next_morning
                                        "It's better if you show me...":
                                            $ec_jay_2_it_s_better_if_you_show_me_ = True
                                            mc "It's pretty hard to see or hear in this darkness."
                                            mc "I think it's better if you just show me..."
                                            scene black at topleft with dis #todo
                                            j "I have to warn you, though..."
                                            mc "Spare me the act, Jay."
                                            mc "Don't spare me the touches."
                                            scene black at topleft with dis #todo
                                            mc "The kisses."
                                            scene black at topleft with dis #todo
                                            mc "And for the love of god, don't spare me the part where you take my pants off..."
                                            jump ec_jay_2_sex_with_jay
                        "It feels...heavy, somehow.":
                            $ec_jay_2_it_feels_heavy_somehow = True
                            mc "It feels...heavy, somehow."
                            pass #todo fill choice
                            jump next_morning
                "And what's your dark side?":
                    $care_to_share_your_darker_side_with_me = True
                    mc "And what's your dark side?"
                    j "Oh, that's easy."
                    j "I like to find out how far someone's trust will carry them."
                    mc "That does sound dangerous."
                    j "I like to think that I am worth any trust that's placed in me, but yes, it's a gamble, of course."
                    menu:
                        "I don't know about my trust, but my feet have carried me enough now. So go on, do your thing with me.":
                            $ec_jay_2_i_dont_know_about_my_trust_but_my_feet_have_carried_me_enough_now_so_go_on_do_your_thing_with_me = True
                            mc "I don't know about my trust, but my feet have carried me enough now. So go on, do your thing with me."
                            if ec_jay_1_can_share_bed_tonight:
                                j "That is now the second time you have offered yourself to me."
                                mc "And has your answer changed?"
                                j "Like I said before, you make me curious."
                                mc "Curious enough to take advantage of my helpless situation here?"
                                j "If that's what you want."
                                mc "I want to stop having to beg."
                                j "In that case, let's see if we can't make our desires align."
                                jump ec_jay_2_sex_with_jay
                            scene black at topleft with dis #todo
                            j "I find it worth mentioning that coming out of this forest again does not require you to do anything you are uncomfortable with."
                            mc "I am glad to hear that, now stop being polite."
                            j "I will adjust my set of manners accordingly."
                            mc "And stop talking to me like I'm any sort of lady tonight."
                            j "Agreed, you look more like a slut in this light."
                            mc "Now that's what I'm talking about."
                            jump ec_jay_2_sex_with_jay
                        "As long as I get home safe, I'd call this a win.":
                            $ec_jay_2_as_long_as_i_get_home_safe_id_call_this_a_win = True
                            mc "As long as I get home safe, I'd call this a win."
                            j "Then that's what we'll do."
                            j "Watch your steps, I would hate for you to come out of our little trip with visible bruises."
                            scene black at topleft with dis #todo
                            j "There we go, that's the main road again."
                            j "Congratulations, you made it back out of the woods safe and healthy."
                            mc "Thank you, this was fun."
                            j "I'm glad you enjoyed this little adventure."
                            menu:
                                "I wouldn't mind doing this again sometime.":
                                    $ec_jay_2_i_wouldnt_mind_doing_this_again_sometime = True
                                    $unlocked_ec_jay_3 = True
                                    mc "I wouldn't mind doing this again sometime."
                                    j "In that case, I will let you know the next time I come up with a trip worth taking."
                                    mc "I look forward to that."
                                    mc "And now, have a good night."
                                    j "In my role as the owner of the hotel you'll be sleeping in, I doubly hope you will have a good night."
                                    mc "Hah, I'm sure I will."
                                    jump next_morning
                                "Thanks, have a good night.":
                                    $ec_jay_2_thanks_have_a_good_night = True
                                    mc "Thanks, have a good night."
                                    j "In my role as the owner of the hotel you'll be sleeping in, I doubly hope you will have a good night."
                                    mc "Hah, I'm sure I will."
                                    jump next_morning
    jump next_morning


label ec_jay_2_sex_with_jay:
    $ec_jay_2_had_sex_with_jay = True
    $unlocked_ec_jay_3 = True
    scene black at topleft with dis #todo picnic table location in the dark
    #todo
    mc "So, was I everything you thought I would be?"
    scene black at topleft with dis #todo
    j "I'll have to try this again to really make sure."
    mc "Hah, nice try. Keep your hands off of me, you creep."
    j "You're just too proud to admit that you're exhausted."
    mc "And you aren't?"
    j "Dead tired, if I'm honest."
    mc "Yep, I kinda felt it when you exhausted yourself there."
    j "Should we get dressed again?"
    mc "It's pretty chilly, not gonna lie."
    j "Please accept my apologies, that was not a way to treat a lady of class."
    mc "No, it really wasn't."
    mc "Thank you, in case it needs to be said out loud."
    j "What do you say, shall we embark on the laborious trip back to our cars?"
    mc "Yes please, I really need a soft and comfy mattress under my butt, not this hard wood."
    j "Well, I hope you will find the sleeping arrangements at my hotel to your liking."
    mc "Hah, damn right I do."
    mc "If I may be serious here for a moment, that's easily the best mattress I have ever slept on."
    j "I'm glad to hear they were worth the money."
    scene black at topleft with dis #todo
    j "Well, here we are, it appears the time has come to say good night."
    mc "Good night."
    j "And like I said when we first met: I am always just a call away in case you need anything."
    mc "You are the worst."
    j "I appreciate the compliment, milady."
    mc "Get out of my sight."
    j "Right away, Ma'am."
    jump next_morning