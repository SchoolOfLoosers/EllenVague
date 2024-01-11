label ec_patty_2:
    scene 61 at topleft with dis #todo
    p "Well, folks, looks like our vacationing author is back on the show, eager and willing to chat the day away."
    p "Welcome back, Miss Vague."
    scene 65 at topleft with dis #todo
    p "Or, do I get to call you Ellen, now that you are back for more?"
    scene 64 at topleft with dis
    mc "Oh, of course."
    mc "Thanks for having me back on, I really enjoyed our last conversation."
    scene 63 at topleft with dis
    p "Likewise, and from what I've been hearing, our listeners out there won't mind another round, either."
    scene 65 at topleft with dis
    p "Isn't that right, folks?"
    scene 65 at topleft with dis #todo
    p "Well, Ellen, it has been a hot minute since you last sat in that chair, why don't you tell our listeners how you have been faring in our lovely little town?"
    menu:
        "It is a beautiful little town":
            $ec_patty_2_beautiful_town = True
            scene 66 at topleft with dis #todo
            mc "It is a beautiful little town."
            scene 65 at topleft with dis #todo
            p "I know, right?"
            p "I have lived her pretty much all my life, and I still fail to get bored by the views."
        "The more time I spend here, the more I start thinking about selling my big city apartment":
            $ec_patty_2_selling_apartment = True
            scene 66 at topleft with dis #todo
            mc "The more time I spend here, the more I start thinking about selling my big city apartment"
            scene 65 at topleft with dis #todo
            p "Is that right?"
            p "Well, folks, it does appear that Bryatt Fowls has not lost its ability to charm the tourists, now has it?"
            p "What to you say, Ellen, should I put the word out that a rich and famous author is looking for some affordable real estate?"
            scene 67 at topleft with dis #todo
            mc "Hah, more like starving and barely able to feed myself, if we are going into any sort of negotiations."
            scene 65 at topleft with dis #todo
            p "Smart."
        "Everyone I've met has been so friendly":
            $ec_patty_2_people_friendly = True
            scene 64 at topleft with dis #todo
            mc "Everyone I've met has been so friendly."
            scene 66 at topleft with dis #todo
            mc "I'm simply not used to that."
            mc "At home, you get yelled at the moment you step out of the door, and standing in line for a coffee makes you clutch your purse and look over your shoulder."
            scene 65 at topleft with dis #todo
            p "Hah, that can't happen to you out here."
            scene 64 at topleft with dis #todo
            mc "I know, right?"
            scene 65 at topleft with dis #todo
            p "It's been a long time since I've seen a queue forming anywhere."
            scene 64 at topleft with dis #todo
            mc "Hah, good one."
            mc "That caught me by surprise."
            scene 68 at topleft with dis #todo
            p "Yes, us townsfolk are full of surprises."
            p "You should try it sometime."
            "I couldn't shake the feeling that there was an undertone to her voice, one that I couldn't quite figure out."
    scene 63 at topleft with dis #todo
    p "So, I'm curious, Ellen, what kind of places have you visited so far?"
    menu:
        "I took the ferry and hiked up to Lover's Peak":
            $ec_patty_2_talked_about_lovers_peak = True
            scene 65 at topleft with dis #todo
            p "Ah, the classic choice for any discerning tourist."
            p "And, on a scale of one to ten, how disappointed were you when you reached the top?"
            scene 64 at topleft with dis #todo
            mc "Hah, I actually enjoyed the view quite a lot."
            scene 65 at topleft with dis #todo
            p "For more than five minutes, you mean?"
            scene 67 at topleft with dis #todo
            mc "I'm pretty sure I lasted almost an hour before I got bored and had to head back down."
            scene 68 at topleft with dis #todo
            p "If you ask me, that is the most impressive feat of patience I have heard all week."
            p "What did you even do up there, all alone?"
            menu:
                "Oh, you know, I just enjoyed spending some time with my own thoughts":
                    $ec_patty_2_talked_about_spending_time_wiht_yourself_on_lovers_peak = True
                    scene 66 at topleft with dis #todo
                    mc "Oh, you know, I just enjoyed spending some time with my own thoughts."
                    scene 68 at topleft with dis #todo
                    p "Working on a new book, huh?"
                    scene 66 at topleft with dis #todo
                    mc "Always, yes. At least a little."
                    scene 65 at topleft with dis #todo
                    p "Hah, I get that."
                    scene 69 at topleft with dis #todo
                    p "I always think of something for the show in the middle of the day, then I immediately have to stop what I'm doing and write that down."
                    scene 67 at topleft with dis #todo
                    mc "Yep, that sounds familiar." #todo maybe a bit more text here later?
                "Oh, you know, I just enjoyed spending some time with my own thoughts (point at your crotch)" if dc_karen_1_masturbated_on_lovers_peak:
                    $ec_patty_2_pointed_at_crotch = True
                    mc "Oh, you know, I just enjoyed spending some time with my own thoughts"
                    scene 69 at topleft with dis #todo
                    p "Oh, is that so?"
                    p "Well, I can understand that, I sometimes do the same..."
                    menu:
                        "Go on with the interview like normal":
                            $ec_patty_2_naked = False
                            scene 67 at topleft with dis #todo
                            p "So, I bet you were working on a new book, huh?"
                            scene 66 at topleft with dis #todo
                            mc "Always, yes. At least a little."
                            scene 68 at topleft with dis #todo
                            p "Hah, I get that."
                            scene 69 at topleft with dis #todo
                            p "I always think of something for the show in the middle of the day, then I immediately have to stop what I'm doing and write that down."
                            scene 67 at topleft with dis #todo
                            mc "Yep, that sounds familiar." #todo maybe a bit more text here later?
                        "Take your pants off quietly":
                            $ec_patty_2_naked = True
                            scene black at topleft with dis #todo finger shush lips
                            p "Why don't you tell us a bit more about your...explorations, Ellen?"
                            scene black at topleft with dis #todo
                            mc "I'm not sure how interesting it is to listen to that, it is a lot of walking alone down empty paths."
                            scene black at topleft with dis #todo patty takes her own pants off
                            p "Yep, that's hiking for you, isn't it?"
                            scene black at topleft with dis #todo 69 as base
                            mc "Hiking, sure."
                            scene black at topleft with dis #todo
                            mc "Listen, uh, what was the question again?"
                            scene black at topleft with dis #todo
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
                            scene black at topleft with dis #todo
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
                            scene black at topleft with dis #todo
        "I spent a day fishing down by the pier": #todo condition
            $ec_patty_2_talked_about_fishing_at_pier = True
            scene 66 at topleft with dis #todo
            mc "I spent a day fishing down by the pier."
            scene 65 at topleft with dis #todo
            p "Oh, that sounds relaxing."
            p "You guys caught anything?"
            scene 62 at topleft with dis #todo
            mc "Yes, a shark, it was about this long"
            scene 64 at topleft with dis #todo
            mc "Not really, no."
            scene 67 at topleft with dis #todo
            mc "It was still fun, though."
            scene 68 at topleft with dis #todo
            p "Yep, I get that."
            p "I haven't been out for a long time now, really need to get back into it myself."
        "I explored the old lumberyard" if completed_ec_jay_2:
            $ec_patty_2_talked_about_exploring_lumberyard = True
            scene 66 at topleft with dis #todo
            mc "I explored the old lumberyard."
            scene 61 at topleft with dis #todo
            p "Oh, I haven't been there in ages."
            scene 62 at topleft with dis #todo
            mc "I really enjoyed it. A very...mysterious place, if you ask me."
            scene 67 at topleft with dis #todo
            mc "Made the hair on my neck stand up, like there was somethere there with me."
            mc "Watching me."
            scene 63 at topleft with dis #todo
            p "Yep, that tracks."
            scene 61 at topleft with dis #todo
            p "It's also a great place for first kisses - or so I've heard."
            scene 62 at topleft with dis #todo
            mc "Oh really, huh?"
            scene 61 at topleft with dis #todo
            p "Yep."
            scene 69 at topleft with dis #todo
            p "I mean, not that I still think about him from time to time or anything, but..."
            scene 67 at topleft with dis #todo
            mc "But me mentioning the place brought some memories back, huh?"
            scene 69 at topleft with dis #todo
            p "Exactly."
    scene 65 at topleft with dis #todo
    s "Well, Ellen, it was great having you over again, thank you for coming."
    scene 63 at topleft with dis #todo
    mc "Oh, I am such a sucker for this view here, there was no way I would decline your invitation."
    s "I know, right?"
    s "Okay, folks, that is it for tonight, thank you all for tuning in."
    scene 69 at topleft with dis #todo
    s "And now, I will let you off into the evening with another of my songs that I create up in my little studio in the skies."
    s "It's called \"Trunk Music\" - and if you think you know what that means, then think again."
    scene black at topleft with dis
    play music trunkmusic.mp3
    pause 30 #todo change this
    stop music fadeout 1.0
    if ec_patty_2_naked:
        scene 65 at topleft with dis #todo
        p "Okay...microphones off, all systems shut off - done."
        scene 69 at topleft with dis #todo
        p "Jesus Christ, Ellen, that was the HOTTEST thing ever!"
        p "I barely managed to talk anymore!"
        scene black at topleft with dis #todo
        mc "Still better than I faired, with my mumbling and drifting thoughts."
        mc "I'm sorry, I don't know what's gotten into me."
        scene black at topleft with dis #todo
        p "Yeah, I don't know about you, but there is no way I'll make it home tonight."
        scene black at topleft with dis #todo
        p "And I REALLY need you to stay here with me."
        p "We have a lot of things left to...discuss."
        scene black at topleft with dis #todo
        p "And you are still wearing your sweater."
        scene black at topleft with dis #todo
        mc "I really like yours, by the way."
        scene black at topleft with dis #todo
        p "I know, right?"
        p "I bought it last year, and I don't think I've really left it out of my sight for a day since."
        p "So what, you here to trade compliments?"
        scene black at topleft with dis #todo
        mc "I'm here to make sure you're taking that sweater off, and leaving it out of sight for the first time in years."
    jump next_morning