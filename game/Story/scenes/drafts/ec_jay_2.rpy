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
                            j ""
                            pass #todo fill choice
                        "It feels...heavy, somehow.":
                            $ec_jay_2_it_feels_heavy_somehow = True
                            mc "It feels...heavy, somehow."
                            pass #todo fill choice
                    #todo
                    jump next_morning
                "And what's your dark side?":
                    $care_to_share_your_darker_side_with_me = True
                    mc "And what's your dark side?"
                    j "Oh, that's easy."
                    j "I like to find out how far someone's trust will carry them."
                    mc "That does sound dangerous."
                    j "I like to think that I am worth any trust that's placed in me, but yes, it's a gamble, of course."
                    menu ec_jay_2_menu_name:
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
    scene black at topleft with dis #todo

    #todo
    jump next_morning