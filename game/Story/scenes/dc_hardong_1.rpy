label dc_hardong_1:
    scene 302 at topleft with dis
    e "Good morning, Miss Vague."
    mc "Good morning, doctor Hardong."
    mc "Thank you for agreeing to meet with me, especially on such short notice."
    e "Of course. I make it a habit to keep free unscheduled time everyday."
    e "Somehow, that hardly ever results in boredom."
    mc "Hah, I know what you're talking about."
    e "I must admit, your call made me curious."
    mc "I know our respective occupations put us at a bit of professional odds..."
    scene 303 at topleft with dis
    e "Oh, not at all, Miss Vague, not at all."
    e "Part of my work here is to allow people to come to terms with themselves, their own unique desires and problems."
    e "I would argue that your work achieves the same, in that it allows your readers to come to terms with their own sexuality."
    e "Although it might be dangerous to give someone the tools, without teaching them how to use them."
    e "And how to hammer a nail into the wood without also hammering their own thumbs."
    mc "Hah, that is a good analogy."
    e "Trust me, you have to expect no judgement from me for the work you do."
    scene 304 at topleft with dis
    e "But please, Miss Vague, sit down"
    scene 305 at topleft with dis #todo
    e "I will say, however, that I would be VERY interested in talking to you about yourself."
    scene 306 at topleft with dis #todo
    mc "What do you want to know?"
    scene 305 at topleft with dis #todo
    e "Everything you are willing to share with me."
    e "I will answer any questions you have come here to ask today, but I would like to offer you a stay at my resort if you can be convinced of that."
    scene 307 at topleft with dis #todo
    mc "You want to take me in as a patient?"
    scene 305 at topleft with dis #todo
    e "Yes, and no."
    e "Like I said, I would be very interested in speaking to you, professionally."
    e "I think my own work here could profit from your insights, as well as my own interpretations."
    e "You see, around these parts, it is hard for me to get either input, or feedback, and thus my work is unlikely to improve past the point I can achieve on my own accord."
    e "But, the older I get, the more I realize that growing in a vacuum can only bring you that far, and growth happens that much quicker when any action is met with an equal and opposite reaction."
    e "Forgive the limping analogy, but as they say: no battle plan ever survives contact with the enemy."
    e "Not that you, or any other patient, would ever come close to being considered an enemy."
    scene 308 at topleft with dis #todo
    mc "No, I get it."
    mc "That is actually quite interesting, most people in your position would not go out of their way to ask for any kind of feedback."
    scene 309 at topleft with dis #todo
    e "And we both know what happens to these people."
    e "They stall their own progress in life, in love, in...every aspect of their lives."
    e "And wasting your own potential like that is just a pity."
    e "Something I would like to avoid."
    mc "Interesting."
    scene 305 at topleft with dis #todo
    e "So, what do you say, is there a chance I could convince you?"
    scene 309 at topleft with dis #todo
    menu:
        "Honestly, I am not here to check myself into a clinic":
            $dc_hardong_1_honestly_i_am_not_here_to_check_myself_into_a_clinic = True
            mc "Honestly, I am not here to check myself into a clinic"
            scene 305 at topleft with dis #todo
            e "A pity, but I understand."
            e "And if that ever changes, you are welcome to reconsider."
            e "We always operate below maximum capacity here, to keep our staff away from needing a clinic stay of their own."
            e "Which means that we always have room to spare."
        "I have done worse for a few days of free cost and stay":
            $dc_hardong_1_i_have_done_worse_for_a_few_days_of_free_cost_and_stay = True
            $unlocked_dc_hardong_2 = True
            scene 308 at topleft with dis #todo
            mc "I have done worse for a few days of free cost and stay."
            scene 305 at topleft with dis #todo
            e "Well, I am thrilled you would consider my offer."
            scene 308 at topleft with dis #todo
            mc "I'll need some more details first, of course."
            mc "I really don't want to be treated like a mental patient, and you better not lock me away."
            scene 309 at topleft with dis #todo
            e "Oh, I can assure you, that's not how we do things around here."
            e "I very much believe in leaving everyone a choice to...leave, if they so choose."
            scene 308 at topleft with dis #todo
            mc "Oh, so that's why Miss Beaver was at the diner the other day."
            scene 305 at topleft with dis #todo
            e "Ah yes, a peculiar lady, isn't she?"
            scene 308 at topleft with dis #todo
            mc "That's one way of putting it."
            scene 309 at topleft with dis #todo
            e "I wondered how you even got my name, and thought to seek my out in the first place."
            e "Out of interest: Did you converse with her cock?"
            scene 308 at topleft with dis #todo
            mc "Hah, I sure did."
            if dc_cock_lady_1_does_your_cock_have_any_other_warnings_for_me:
                mc "We actually had quite an interesting conversation."
                mc "She warned me about a man, then told me I should not take people at face value, and to rather judge them by their long-term actions."
                mc "Both pretty sound advice, if you ask me."
                scene 305 at topleft with dis #todo
                e "See, I knew someone like you would not wave her off immediately."
                e "I could already tell when we spoke on the phone that you have the capability to listen to someone, no matter where they might be standing or coming from."
                e "Most people could use a pinch of that salt."
                scene 308 at topleft with dis #todo
                mc "Hah, I know, right?"
            scene 309 at topleft with dis #todo
            e "Well, the doors of my resort are always open for you, whenever you decide to honor us with your stay."
            scene 308 at topleft with dis #todo
            mc "Your resort, huh? Is that what you call it?"
            scene 305 at topleft with dis #todo
            e "What else would you prefer?"
            e "We have good food, motivated staff, and lodgings that appeal to the discerning hotel critic."
            scene 309 at topleft with dis #todo
            mc "Hah, point taken."
    scene 309 at topleft with dis #todo
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
            scene 310 at topleft with dis #todo
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
                    e "Interesting."
                    e "So, familiarity with the place plays a role for you."
                    mc "Oh, absolutely."
                    e "That tells me that you are looking for both mental and physical comfort, more than you are looking for the excitement and thrill."
                    mc "Are you calling me boring?"
                    e "Very much not so, Miss Vague."
                    e "You are an exciting woman in your own right, but it does appear you are looking for it in other places, in the outside world."
                    e "While your own home is the comfort zone you retreat to for peace and quiet."
                "Probably an hour or so.":
                    $dc_hardong_1_probably_an_hour_or_so = True
                    mc "Probably an hour or so."
                    e "Interesting."
                    mc "How so?"
                    e "Because it tells me that you have the rare ability to be yourself, and to make your own choices."
                    e "I would say it isn't so much boredom that would steer you, as rather an interesting ability to adapt to the situation, and doing so in reasonably timely fashion."
                    e "You wouldn't be unable to control yourself, and yet unwilling to adhere to rules in the absence of a judge."
                "Honestly, there is enough in here to make me snoop through everything first.":
                    $dc_hardong_1_honestly_there_is_enough_in_here_to_make_me_snoop_through_everything_first = True
                    mc "Honestly, there is enough in here to make me snoop through everything first."
                    e "See, I find that a highly fascinating answer, Miss Vague."
                    mc "How so?"
                    e "Because it tells me that you are, in fact, reacting to boredom and the lack of more interesting choices, as opposed to seeking the thrill through an incredibly monotonous task."
                    e "Your first instinct was to explore this place, not yourself, having long explored yourself sufficiently to make it an option in the absence of better options, rather than a necessity."
            scene 310 at topleft with dis #todo
            e "Well, thank you for your honest answer, Miss Vague."
            scene 308 at topleft with dis #todo
            mc "Please, if we are discussing my masturbation habits, you are free to call me Ellen."
            scene 310 at topleft with dis #todo
            e "Alright, thank you Ellen."
            e "Say, since you are open enough to discuss your own habits in this regard..."
            e "Would you mind demonstrating them?"
            scene 307 at topleft with dis #todo
            mc "What?"
            mc "You mean here and now?"
            scene 310 at topleft with dis #todo
            e "I know it is, with societal concerns in mind, an unusual request."
            scene 307 at topleft with dis #todo
            mc "No kidding."
            scene 310 at topleft with dis #todo
            e "But it would bring both of us quite a large step closer to answering your very own question."
            e "Since you are, by definition, not alone in this room, you could see for yourself how that changes your experience."
            e "And since you are quite engaged in our little conversation here, you are also not bored, so your mind does not default to this conclusion, like you said it would."
            e "So why don't we find out together what it takes for you to break your own habits."
            menu:
                "Yeah, sorry but no way.":
                    $dc_hardong_1_yeah_sorry_but_no_way = True
                    scene 307 at topleft with dis #todo
                    mc "Yeah, sorry but no way."
                    mc "I mean, nothing against you, but..."
                    scene 310 at topleft with dis #todo
                    e "No, I get it, that was the most likely response."
                    e "I hope you don't mind the attempt, it was purely out of scientific interest."
                    scene 308 at topleft with dis #todo
                    mc "I get it, don't worry."
                "I can't believe I am doing this...":
                    $dc_hardong_1_i_cant_believe_i_am_doing_this_ = True
                    mc "I can't believe I am doing this..."
                    scene 310 at topleft with dis #todo
                    e "I must say, I am fascinated that you are rested in yourself enough to consider this option."
                    e "Would it throw you off if I took some notes here?"
                    scene 308 at topleft with dis #todo
                    mc "By all means, doctor, study my every movement if you will"
                    scene 311 at topleft with dis #todo
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
                            if dc_hardong_1_i_am_interested_in_why_we_consider_some_sex_acts_as_taboo_or_dirty:
                                e "Which tells me that you fall more in the category of enjoying the potential embarrassment of your own actions."
                                menu:
                                    "Who says I don't also enjoy having my agency taken away from me?":
                                        $dc_hardong_1_who_says_i_dont_also_enjoy_having_my_agency_taken_away_from_me = True
                                        mc "Who says I don't also enjoy having my agency taken away from me?"
                                        e "If that was a thinly veiled attempt to get me to cross every single professional line in the book, then I have to disappoint you."
                                        mc "What a pity, to think you could have taken control here, but are too shy for it."
                                        e "Well, my patient's trust in me is the most important tool I have at my disposal, and I am not willing to dull it over some fleeting form of entertainment."
                                        e "Besides, it wouldn't really work, since you all but encouraged me, and thereby acted out of your own free will."
                                        e "This wouldn't quite test the actual experience of having your agency taken away from you."
                                        mc "Ugh, I guess you're right."
                                        e "I'm glad we agree on this matter."
                                        mc "Do we, though?"
                                    "That seems to be a fair assessment, doctor.":
                                        $dc_hardong_1_that_seems_to_be_a_fair_assessment_doctor = True
                                        mc "That seems to be a fair assessment, doctor."
                                        e "Well, I am sorry that I can't quite deliver you any laughter or sneering looks, I am too fascinated by this opportunity to study you."
                                        mc "Oh, believe me, you sitting there to take notes is plenty embarrassing already."
                                        e "I am glad to hear that."
                                        e "Please, carry on."
                            else:
                                e "Interesting."
                                mc "Are you judging me?"
                                e "This is a judgement free zone, Ellen."
                                mc "Jesus christ, leave me alone with your psycho nonsense."
                                e "In that case, yes I am judging you quite heavily right now."
                                mc "I knew it!"
                                e "And I am starting to think that you are a dirty little slut."
                                mc "Should you be talking to me like that, doctor?"
                                mc "What happened to being so incessantly forthcoming and helpful and willing to listen?"
                                e "That's reserved for my patients."
                                e "Sluts get talked to like they deserve."
                                mc "Mhm, keep talking."
                                e "You like being called a slut?"
                                mc "Only when I behave like one."
                                e "Which you are doing right now."
                                mc "Mhm-hm."
                                mc "You like what you're seeing?"
                                e "Any man would."
                                mc "Then why don't you do what any man would?"
                                e "Because I am here as an observer, not to get my hands dirty."
                                mc "First a slut, now you're also calling me dirty?"
                                e "God knows I wouldn't want to stick my dick into that unprotected."
                                mc "Ugh, you are so mean."
                                e "Want me to stop?"
                                mc "I want you to get over yourself."
                                e "Maybe next time, I'm busy here."
                                mc "Oh for fuck's sake..."
                                scene black at topleft with hpunch #todo
                                mc "You are such an ass."
                                e "And you are such a mess."
                                mc "What kind of mess?"
                                e "A dirty little mess."
                                mc "Ugh, I would fight you on that, if..."
                                e "If it wasn't the truth, you mean?"
                                mc "Such a dirty little mess."
                                e "I'm glad you enjoyed yourself."
                                mc "You know, I actually did."
                                mc "Thank you for being there when I needed you."
                                e "You know, a true lady of class wouldn't thank me for the things I've said, and the names I've called you."
                                mc "Feels like you made a scientific breakthrough there, you should write that down."
                                e "Subject is receptive to its own touches, and reacts favorably when called derogatory and demeaning terms."
                                mc "Ugh, tell me about it."
                                e "Well, was there something else you wanted to ask?"
                                jump dc_hardong_1_menu_ask_questions
                        "It makes me pretty uncomfortable, actually...":
                            $dc_hardong_1_it_makes_me_pretty_uncomfortable_actually_ = True
                            mc "It makes me pretty uncomfortable, actually..."
                            e "Good, I want you to hold on to that feeling."
                            e "Now imagine yourself in a cold room, bright neon lights that hurt your eyes even when closed."
                            e "Cameras in every corner, so you know that someone is watching you..."
                            e "But you don't know who, or how many, and what they are doing with the information gained from studying you."
                            scene black at topleft with hpunch #todo
                            e "All you know is that the louder you yell, the more the silence you get for an answer is weighing on you."
                            scene black at topleft with hpunch #todo
                            "I didn't know what it was, but him sitting there..."
                            "Judging me, and saying those horrible things to me..."
                            "I don't know, it just did the trick..."
                            scene black at topleft with dis #todo
                            mc "Ugh, that was really mean."
                            e "I'm glad to see that you enjoyed yourself."
                            mc "You know, I actually did."
                            e "I can tell, that's quite the messy state you're in."
                            mc "You expect me to say sorry?"
                            e "No, I expect you to tell me if there are any other questions you want me to answer."
                            jump dc_hardong_1_menu_ask_questions
                        "You know you could do more than just watch, right?":
                            $dc_hardong_1_you_know_you_could_do_more_than_just_watch_right = True
                            mc "You know you could do more than just watch, right?"
                            e "And is that what you want?"
                            e "Let me rephrase: Is that what you are thinking about as you are touching yourself?"
                            mc "How could I not?"
                            e "Well, you could be afraid of me getting ideas here, for one thing."
                            e "But it does appear to me that my presence here is more of a net positive in your eyes."
                            menu:
                                "Please tell me you aren't going to keep just sitting there...":
                                    $dc_hardong_1_please_tell_me_you_arent_going_to_keep_just_sitting_there_ = True
                                    mc "Please tell me you aren't going to keep just sitting there..."
                                    jump dc_hardong_1_sex_with_doctor
                                "Well, watch this part extra closely now, Doctor...":
                                    $dc_hardong_1_well_watch_this_part_extra_closely_now_doctor_ = True
                                    mc "Well, watch this next part extra closely now, Doctor..."
                                    scene black at topleft with hpunch #todo
                                    "I didn't know what it was, but him sitting there, watching me..."
                                    "It just did the trick."
                                    scene black at topleft with dis #todo
                                    mc "You enjoyed that?"
                                    e "Looks like you did, too."
                                    mc "I'm not going to lie, I've done worse, and had less fun doing it."
                                    e "I'm glad to hear that."
                                    mc "Are you not going to write this down in your little notebook there?"
                                    mc "Before I get the impression that this wasn't actually about a new scientific discovery?"
                                    e "Good idea, let me write this down."
                                    e "Test subject receptive to own touches, clear signs of an intelligent life form."
                                    mc "You just had to get that little compliment in there, didn't you?"
                                    e "Subject able to detect subtle remarks, clear sign of intelligence."
                                    mc "Oh come on now."
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

label dc_hardong_1_sex_with_doctor:
    $dc_hardong_1_had_sex_with_doctor = True
    scene black at topleft with dis #todo
    e "I have always prided myself on being more of a hands-on doctor than most with my specialization."
    mc "You know where you can stuff that pride of yours?"
    e "No need to say it out loud."
    mc "Good, you had me worried for a second..."
    mc "Professional concerns and bullshit like that..."
    e "Oh, I wouldn't do this if you were my patient."
    mc "Not even if I ask you?"
    e "I can see that you aren't in a dire, exploitable situation."
    mc "And that's supposed to make this okay?"
    e "It makes me think I can make an exception in your case."
    mc "Not gonna lie, this does feel pretty exceptional."
    scene black at topleft with hpunch #todo cumshot
    mc "This new therapy is working, doctor."
    e "I can see that."
    mc "What do your notes say about all this?"
    e "A detailed description of your natural beauty, with a weirdly detailed subsection describing your gender specific body parts."
    mc "Hah, that's what I thought."
    e "If you stay still like that for a while, I'll add a quick sketch as well."
    mc "Should I strike some kind of pose?"
    e "Yes, please. Any you like, and keep it there for a bit."
    e "I'll try to hurry."
    scene black at topleft with dis #todo
    e "There we go."
    mc "That's not the worst drawing I have ever seen, where'd you learn that?"
    e "I took two semesters of biology classes before I found my passion in behavioral sciences."
    mc "Well, you can always start a career as a sketch artist with a folding chair next to the shopping mall."
    e "I would hope that someone like you comes by, and that she needs illustrations for her books."
    mc "Oh, you can be my own starving artist, who depends on my continued goodwill so that he doesn't lose his mattress in the tiny room in my house."
    e "Is that something you would want?"
    mc "Please don't try to analyze my brain, doctor."
    mc "You might not like what you find."
    e "In that case, I will be more than happy to explore...other parts of you."
    e "Feel free to stop by in the future, and we can have fruitful discussions like this again."
    mc "I'll let you know if I ever end up low on my morals like this again."
    e "That's all I ask of you."
    e "And now, I wish you a splendid evening, Ellen - and don't forget what we talked about."
    mc "Same to you, doctor Hardong."
    e "Please, call me Emil."
    mc "I like your last name better, it has that certain kind of ring to it."
    jump evening_choices