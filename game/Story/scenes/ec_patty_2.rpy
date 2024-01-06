label ec_patty_2:
    "This scene is not yet ready to play, I will work on it as soon as I find the time. Thanks for your understanding."
    return #todo remove this and line above
    #todo another interview, and we have the chance to take our pants off and secretly mutually masturbate with Patty. Intro:
    scene black at topleft with dis #todo
    p "Well, folks, looks like our vacationing author is back on the show, eager and willing to chat the day away."
    p "Welcome back, Miss Vague."
    p "Or, do I get to call you Ellen, now that you are back for more?"
    mc "Oh, of course."
    mc "Thanks for having me back on, I really enjoyed our last conversation."
    p "Likewise, and from what I've been hearing, our listeners out there won't mind another round, either."
    p "Isn't that right, folks?"
    scene black at topleft with dis #todo
    p "Well, Ellen, it has been a hot minute since you last sat in that chair, why don't you tell our listeners how have you been faring in our lovely little town?"
    menu:
        "It is a beautiful little town":
            $ec_patty_2_beautiful_town = True
            p "I know, right?"
            p "I have lived her pretty much all my life, and I still fail to get bored by the views."

            pass #todo fill choice
        "The more time I spend here, the more I start to think about selling my big city apartment":
            $ec_patty_2_selling_apartment = True
            pass #todo fill choice
        "Everyone I've met has been so friendly":
            $ec_patty_2_people_friendly = True
            pass #todo fill choice
    scene black at topleft with dis #todo
    p "So, I'm curious, Ellen, what kind of places have you visited so far?"
    menu:
        "I took the ferry and hiked up to Lover's Peak":
            $ec_patty_2_talked_about_lovers_peak = True
            p "Ah, the classic choice for any discerning tourist."
            p "And, on a scale of one to ten, how disappointed were you when you reached the top?"
            mc "Hah, I actually enjoyed the view quite a lot."
            p "For more than five minutes, you mean?"
            mc "I'm pretty sure I lasted almost an hour before I got bored and had to head back down."
            p "If you ask me, that is the most impressive feat of patience I have heard all week."
            p "What did you even do up there, all alone?"
            menu:
                "Oh, you know, I just enjoyed spending some time with my own thoughts":
                    $ec_patty_2_talked_about_spending_time_wiht_yourself_on_lovers_peak = True

                    pass #todo fill choice
                "Oh, you know, I just enjoyed spending some time with my own thoughts (point at your crotch)": #todo make this dependent on choice in karen_1 / lovers peak masturbation scene
                    $ec_patty_2_pointed_at_crotch = True
                    scene black at topleft with dis #todo
                    p "Oh, is that so?"
                    p "Well, I can understand that, I sometimes do the same..."
                    menu:
                        "Go on with the interview like normal":
                            $ec_patty_2_naked = False

                            pass #todo fill choice
                        "Take your pants off quietly":
                            $ec_patty_2_naked = True
                            scene black at topleft with dis #todo finger shush lips
                            p "Why don't you tell us a bit more about your...explorations, Ellen?"
                            scene black at topleft with dis #todo
                            mc "I'm not sure how interesting it is to listen to that, it is a lot of walking down empty paths."
                            scene black at topleft with dis #todo patty takes her own pants off
                            p "Yep, that's hiking for you, isn't it?"
                            scene black at topleft with dis #todo
                            mc "Hiking, sure."
                            scene black with dis #todo
                            mc "Listen, uh, what was the question again?"
                            scene black with dis #todo
                            p "Hah, I kinda forgot myself, let us try this again."
                            p "So, uh, why don't you tell us a little about your life in the city?"
                            p "I know I always come home completely exhausted whenever I spend a day out there."
                            mc "Oh yes, that can be...quite exhausting, for sure."
                            mc "But then again, so can this here, right?"
                            p "What do you mean?"
                            mc "I mean, all this calm, and quiet, it can really get to you sometimes."
                            p "Oh, now I get what you mean."
                            p "I thought you meant something else there for a second."
                            mc "But, and that's a big...but."
                            mc "Out here, you have a choice, am I right?"
                            mc "You can always go out, have a coffee, talk to someone..."
                            mc "You can't quite stick to yourself in the city, life always finds a way to get to you."
                            mc "I'm pretty sure life would start a fire in my apartment complex or something if I dared to stay inside for a week."
                            scene black with dis #todo
                            p "Hah, that's probably true."
                            p "So, what you're saying is, you go out at least once per week?"
                            mc "That sounds about right, yes."
                            mc "And, there is always something to do, you know?"
                            mc "Buying groceries, doing PR stuff that my editors force me to do..."
                            p "So, showing up to radio shows to...drop your pants, so to speak?"
                            mc "Exactly, that kind of stuff."
                            mc "Just...less exciting, really."
                            mc "A lot of those shows aren't really...how do I put it..."
                            mc "Dynamic, or conversations at all."
                            mc "Especially if you're like me, and everything I say has to go through legal checkups to see if the adult audience out there can handle what I have to say."
                            p "You would think that we live in modern times, and people could freely choose what they do with their own lives, right?"
                            mc "Right, you would."
                            mc "But in my line of business, you really start to see how little has changed over the past hundred years, in some regards, at least."
                            p "You mean the only real change is that the prudes of today have a phone in their pocket that allows them to do enjoy their prudishness that much quicker?"
                            mc "Hah, that hits the nail on the head."
                            p "Now, please, we don't use words like nailing around here."
                            mc "Hah, good one."
                            mc "I'll try to keep my raunchy language in check from now on."
                            p "Oh yes, please, it's better to keep that stuffed where it belongs."
                            mc "That's a good idea, I will do that right away."

                            scene black with dis #todo


                            pass #todo fill choice
                    pass #todo fill choice
            pass #todo fill choice
        "I spent a day fishing down by the pier": #todo condition
            $ec_patty_2_talked_about_fishing_at_pier = True
            pass #todo fill choice
        "I explored the old lumberyard": #todo condition
            $ec_patty_2_talked_about_exploring_lumberyard = True
            pass #todo fill choice
    jump next_morning