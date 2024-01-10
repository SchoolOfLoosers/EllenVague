label dc_hardong_1:
    scene black at topleft with dis #todo
    #todo meet him at his clinic, talk about your books, and he begins to analyze your "problems" and we can either cut him off, or agree to stay at his resort for a few days and start a new questline where we can use machinery and the tied-up-chair etc.
    e "Good morning, Miss Vague."
    mc "Good morning, doctor Hardong."
    mc "Thank you for agreeing to meet with me, especially on such short notice."
    e "Of course. I make it a habit to keep free unscheduled time everyday."
    e "Somehow, that hardly ever results in boredom."
    mc "Hah, I know what you're talking about."
    e "I must admit, your call made me curious."
    mc "I know our respective occupations put us at a bit of professional odds..."
    e "Oh, not at all, Miss Vague, not at all."
    e "Part of my work here is to allow people to come to terms with themselves, their own unique desires and problems."
    e "I would argue that your work achieves the same, in that it allows your readers to come to terms with their own sexuality."
    e "Although it might be dangerous to give someone the tools, without teaching them how to use them."
    e "And how to hammer a nail into the wood without also hammering their own thumbs."
    mc "Hah, that is a good analogy."
    e "Trust me, you have to expect no judgement from me for the work you do."
    e "I will say, however, that I would be VERY interested in talking to you about yourself."
    mc "What do you want to know?"
    e "Everything you are willing to share with me."
    e "I will answer any questions you have come here to ask today, but I would like to offer you a stay at my resort if you can be convinced of that."
    mc "You want to take me in as a patient?"
    e "Yes, and no."
    e "Like I said, I would be very interested in speaking to you, professionally."
    e "I think my own work here could profit from your insights, as well as my own interpretations."
    e "You see, around these parts, it is hard for me to get either input, or feedback, and thus my work is unlikely to improve past the point I can achieve on my own accord."
    e "But, the older I get, the more I realize that growing in a vacuum can only bring you that far, and growth happens that much quicker when any action is met with an equal and opposite reaction."
    e "Forgive the limping analogy, but as they say: no battle plan ever survives contact with the enemy."
    e "Not that you, or any other patient, would ever come close to being considered an enemy."
    mc "No, I get it."
    mc "That is actually quite interesting, most people in your position would not go out of their way to ask for any kind of feedback."
    e "And we both know what happens to these people."
    e "They stall their own progress in life, in love, in...every aspect of their lives."
    e "And wasting your own potential like that is just a pity."
    e "Something I would like to avoid."
    mc "Interesting."
    e "So, what do you say, is there a chance I could convince you?"
    menu:
        "Honestly, I am not here to check myself into a clinic":
            $dc_hardong_1_honestly_i_am_not_here_to_check_myself_into_a_clinic = True
            mc "Honestly, I am not here to check myself into a clinic"

            e "A pity, but I understand."
            e "And if that ever changes, you are welcome to reconsider."
            e "We always operate below maximum capacity here, to keep our staff away from needing a clinic stay of their own."
            e "Which means that we always have room to spare."
        "I have done worse for a few days of free cost and stay":
            $dc_hardong_1_i_have_done_worse_for_a_few_days_of_free_cost_and_stay = True
            mc "I have done worse for a few days of free cost and stay"
            pass #todo fill choice
    scene black at topleft with dis #todo
    e "With that out of the way..."
    e "Like I said, you have come to ask questions, and I am prepared to answer them."
    mc "Thank you, then let me get started."
    menu dc_hardong_1_menu_ask_questions:
        "I am interested in what motivates someone to cheat on their spouse." if not dc_hardong_1_i_am_interested_in_what_motivates_someone_to_cheat_on_their_spouse:
            $dc_hardong_1_i_am_interested_in_what_motivates_someone_to_cheat_on_their_spouse = True
            mc "I am interested in what motivates someone to cheat on their spouse."
            e "Ah, now that is an interesting question - and a multi-faceted one."
            e "First off, I appreciate that you ar taking the time to research possible motivations for your characters."
            e "That puts you ahead of several authors who require semi trucks to get their first edition from the printing presses."
            mc "Hah, it really does appear that some people get lazy at the top, doesn't it?"
            e "That certainly seems to be the case."
            e "Which brings me back to my earlier point about unchecked egos, and my own attempts to attempt that fate."
            e "But, to get back to your original question..."
            e "I feel everyone's motivation for cheating on their spouses may be unique, and yet somehow not unique at all."
            mc "You mean they all have the basic motivation?"
            e "I believe so, yes."
            e "In my own unscientific opinion, it comes down to the fact that the human mind does not, generally, take well to stability."
            e "At least not for prolonged periods of time."
            e "To me, intelligent people realize that stability is a deceiving concept, and that flexibility is the main skill that differentiates the successful people from the rest."
            e "But then, there are the many who would pick the stable job over the higher paying one, or choose another person to marry at their earliest convenience."
            e "In general, there are people who have never really moved on with their lives out of their own free will, and who die in the town they grew up in."
            e "Someone told them that being married is the ultimate path to happiness, so they marry the first person who doesn't beat them."
            e "And here, I feel, is the root cause of your question: Some people grow up to be smarter than that."
            e "When we are young, we are all impressionable, and there is really no telling in what way those who surround us in our early years will shape our own thoughts and personality."
            e "But then, as time progresses, some people realize that their own choices may not, in fact, have been their own choices."
            e "And those are the people who cheat, because they themselves have been cheated out of a choice."
            mc "Fascinating. So, you're saying that cheating is almost like...a sign of intelligence, then?"
            e "Yes, like many things in life, there are several shades of something that people assume are black and white."
            e "And, to no ones surprise, intelligence is one of the most diverse aspects, and trying to put a number to it only really shows the lack of intelligence on the part of the person who's trying."
            e "So, to be more precise..."
            e "I would call a person intelligent who marries the second or third person who proposes to them, at a point when they have lived enough of their own lives to know what kind of person can compliment their lives."
            e "And a smart person would be one who becomes a character in your books, for realizing that it is never too late to take charge of their own fates."
            mc "Fascinating, thank you for this detailed answer."
            e "I would appreciate if you took my words as what they are. A personal, if educated, opinion."
            mc "Of course."
            e "I am glad to hear that."
            e "And, should you come to your own conclusions, then I would love to discuss this topic in the future."
            e "Now, is there anything else you wanted to ask?"
            jump dc_hardong_1_menu_ask_questions
        "I am interested in why we consider some sex acts as taboo, or dirty, and others as more acceptable." if not dc_hardong_1_i_am_interested_in_why_we_consider_some_sex_acts_as_taboo_or_dirty:
            $dc_hardong_1_i_am_interested_in_why_we_consider_some_sex_acts_as_taboo_or_dirty = True
            mc "I am interested in why we consider some sex acts as taboo, or dirty, and others as more acceptable."
            e "Oh, now that is an interesting question, let me think about that."
            e "At first glance, it appears to me that we are forced to work with shifting goal posts, by ways of societal shift."
            e "Not that long ago, you would have been excused to believe that babies are delivered by birds, because everything that can happen between a man and woman would have been too taboo to talk about."
            e "While these days, it would not be totally unheard of for someone to engage in conversations with strangers about taboo topics."
            e "Or, more bluntly: You and I would not have had this conversation thirty years ago."
            mc "Hah, that is true."
            e "So, working with that shifting baseline, your actual question still offers a lot of room for thought."
            e "So, I feel we have to differentiate two different forms of taboo here."
            e "There might be many more, and shades as well, but the two ones that spring to my mind are these:"
            e "The taboos that embarrass us, but are our own free choices..."
            e "And the ones that pass on our self control to others, in hopes that they can handle the responsibility."
            e "One person might walk down an empty street at night, seeing the lack of proper street lanterns as an opportunity to quietly pee their own pants."
            e "They mull it over, decide for and against it - and pretty much whatever outcome they choose, the excitement is in the choice, in their own resistance against established norms."
            scene black at topleft with dis #todo
            e "While another person, walking down that same unlit street, might find themselves thinking about how someone could be waiting around that next corner, ready to take their agency of choice from them."
            e "And even though we have all been taught to respect this agency, as well as to always protect it for ourselves..."
            e "There is a fascination to be found in the inability to escape."
            e "Now, obviously, that fascination is lost on many - but then again, we are all aware these days of clubs where people willingly walk in to have their own free will restricted."
            e "And the safe words are really just professional courtesy, there is absolutely no guarantee that the utterance of it will be respected."
            e "Another little self-deception, much like the attempt to gain and protect absolute stability in our lives."
            mc "Fascinating insight, thank you for that."
            e "Again, these are just my personal thoughts on the matter, there is absolutely zero scientific backing for any of my thoughts and claims."
            mc "No, I get that."
            e "Good."
            e "Was there something else you wanted to ask?"
            jump dc_hardong_1_menu_ask_questions
        "I wonder why our first reaction to boredom always seems to be masturbation." if not dc_hardong_1_first_reaction_masturbation:
            $dc_hardong_1_first_reaction_masturbation = True
            mc "I wonder why our first reaction to boredom always seems to be masturbation."
            mc "At least when we are alone in a room, with nobody there to see us."
            mc "I mean, my mind could jump to literally anything else, couldn't it?"
            mc "But my first thought isn't to sit down and read a book, or even to smoke a cigarette."
            mc "It is more like \"I am alone in here, might as well take my pants off.\""
            e "Ah, masturbation habits in general are an interesting topic for discussion, aren't they?"
            e "While this may just be the most individual outlet of the human mind's ability for free will..."
            e "Almost all of us seem to develop a certain set of habits."
            e "And, like you say, the absence of other people being a factor suggests to me that the presence of other people is a determining factor."
            e "And that our mind sort of rebells against the oppression of societal norms, by defaulting to this instinctive need to touch ourselves anytime our brain thinks we might get away with it."
            e "Tell me something, Miss Vague:"
            e "If I were to leave this room, and promise not to walk back in for a while - how long would you say before you would stop staring at the ceiling, and start taking your pants off?"
            mc "Hm, that's a good question, actually."
            menu:
                "In this unfamiliar location, probably something long like a day or so.":
                    $dc_hardong_1_in_this_unfamiliar_location_probably_something_long_like_a_day_or_so = True
                    mc "In this unfamiliar location, probably something long like a day or so."

                    pass #todo fill choice
                "Probably an hour or so.":
                    $dc_hardong_1_probably_an_hour_or_so = True
                    mc "Probably an hour or so."
                    pass #todo fill choice
                "Honestly, there is enough in here to make me snoop through everything first.":
                    $dc_hardong_1_honestly_there_is_enough_in_here_to_make_me_snoop_through_everything_first = True
                    mc "Honestly, there is enough in here to make me snoop through everything first."
                    pass #todo fill choice
            scene black at topleft with dis #todo
            e "Well, thank you for your honest answer, Miss Vague."
            mc "Please, if we are discussing my masturbation habits, you are free to call me Ellen."
            e "Alright, thank you Ellen."
            e "Say, since you are open enough to discuss your own habits in this regard..."
            e "Would you mind demonstrating them?"
            mc "What?"
            mc "You mean here and now?"
            e "I know it is, with societal concerns in mind, an unusual request."
            mc "No kidding."
            e "But it would bring both of us quite a large step closer to answering your very own question."
            e "Since you are, by definition, not alone in this room, you could see for yourself how that changes your experience."
            e "And since you are quite engaged in our little conversation here, you are also not bored, so your mind does not default to this conclusion, like you said it would."
            e "So why don't we find out together what it takes for you to break your own habits."
            menu:
                "Yeah, sorry but no way.":
                    $dc_hardong_1_yeah_sorry_but_no_way = True
                    mc "Yeah, sorry but no way."
                    mc "I mean, nothing against you, but..."
                    e "No, I get it, that was the most likely response."
                    e "I hope you don't mind the attempt, it was purely out of scientific interest."
                    mc "I get it, don't worry."
                "I can't believe I am doing this...":
                    $dc_hardong_1_i_cant_believe_i_am_doing_this_ = True
                    mc "I can't believe I am doing this..."
                    e "I must say, I am fascinated that you are rested in yourself enough to consider this option."
                    e "Would it throw you off if I took some notes here?"
                    mc "By all means, doctor, study my every movement if you will"
                    e "Then that's what I shall do."
                    e "Please, carry on, Ellen."
                    mc "Okay, so...do you want me to talk about what I feel?"
                    e "Since I am just here as an observer, you can say anything you want, or don't."
                    e "Yell it, if you like, or tell it to me with clenched teeth."
                    e "The one thing I would like to know is how it makes you feel to be watched."
                    menu:
                        "Honestly, this is quite fun.":
                            $dc_hardong_1_honestly_this_is_quite_fun = True
                            mc "Honestly, this is quite fun."

                            pass #todo fill choice
                        "It makes me pretty uncomfortable, actually...":
                            $dc_hardong_1_it_makes_me_pretty_uncomfortable_actually_ = True
                            mc "It makes me pretty uncomfortable, actually..."
                            pass #todo fill choice
                        "You know you could do more than just watch, right?":
                            $dc_hardong_1_you_know_you_could_do_more_than_just_watch_right = True
                            mc "You know you could do more than just watch, right?"
                            pass #todo fill choice
                    pass #todo fill choice

            e "Well, were there any other questions you wanted to ask me?"
            jump dc_hardong_1_menu_ask_questions
        "That's all the questions I had.":
            scene black at topleft with dis #todo
            e "Well, in that case, let me thank you for this interesting conversation."
            e "It is quite rare to find anyone around these parts who doesn't think I'm either a god or the devil incarnate."
            mc "Hah, and I thank you for your answers, regular man without any personality quirks."
            if dc_hardong_1_first_reaction_masturbation:
                e "I look forward to seeing you again in the future, Miss Vague."
            else:
                e "I look forward to seeing you again in the future, Ellen."

    jump evening_choices