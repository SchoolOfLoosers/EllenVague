label dc_cock_lady_1:
    scene black at topleft with dis #todo
    #todo meet her at the diner, large dildo in hand, telling everyone "my cock tells me that ..."
    mc "Hey Mary, good to see you!"
    m "Hey Ellen, welcome back."
    mc "Say, is there any chance for a coffee around here?"
    m "Hmm, let me see..."
    m "Well, looks like you are in luck!"
    mc "Thank the heavens, I knew I could count on you."
    m "Always."
    m "Here you go."
    m "Oh no, here she comes again."
    mc "Who's coming?"
    m "Well, you better prepare for your daily dose of crazy."
    m "Just let it wash over you, there is nothing we can do."
    mc "Uh, okay?"
    scene black at topleft with dis #todo
    c "Good morning, you heathens."
    c "What a fine morning."
    m "Uh, yeah, totally."
    m "How's your cock feeling today, Cecilia?"
    c "Very well, thank you for asking."
    "Yep, Mary hadn't exaggerated when she said to prepare."
    "Whatever this woman's reasoning might have been, everyone seemed so used to her walking around, carrying a massive dildo..."
    "One that apparently had...feelings, and an opinion that mattered."
    "Definitely out there, even as far as out-there people went."
    c "And you, young lady, you must be this Ellen Vague I've been hearing about."
    mc "That is correct, yes."
    c "Well, in that case, I hope you enjoy your stay."
    mc "I'm sure I will, it's a beautiful town."
    c "Well, don't let the friendly people fool ya, this town is as dangerous as any during the night."
    c "Maybe more so than the city you come from."
    m "Cecilia, stop scaring our guests."
    c "Oh silly, Miss Vague knows better than to be scared by an old hag like me."
    c "But she does need to be warned, doesn't she?"
    m "Uh, sure, go ahead."
    m "But Cecilia, after that, you have to leave, I have to run a business around here."
    c "Very well, then I shall deliver my warnings, and then be on my way."
    c "Listen, Miss Vague, my cock has been telling me a lot of things about you."
    mc "Oh it has?"
    c "Yes, I talk to it every night, and it's telling me things about the world around me."
    mc "I'm sure it does."
    mc "So, uh, what does your cock tell you about me?"
    c "Ah, a young lady who is willing to listen!"
    c "You should know that a man is coming after you, from outside of this world."
    mc "A man, huh?"
    c "His name may be Mockingbird, but he doesn't fly here, he is coming by car."
    if dc_sarah_1_snooped_through_file:
        "A shiver ran through my spine, and at first I couldn't quite place the name."
        "I didn't know anyone by the name of Mockingbird, which was such a silly name that I would have remembered..."
        "Until I did, and I recalled reading about him in the Sheriff's files."
        "He had written a letter asking her to be kept up to date on a case..."
        "And now I realized that it must have been about the dead man in the road..."
    menu dc_cock_lady_1_menu_name:
        "Thank you for the warning, Miss...":
            $dc_cock_lady_1_thank_you_for_the_warning_miss_ = True
            mc "Thank you for the warning, Miss..."
            c "Oh, where are my manners."
            "Yes, that was a good question..."
            c "My name is Cecilia Beaver."
            mc "Nice to meet you, Miss Beaver."
            menu dc_cock_lady_1_menu_name:
                "Have a nice day.":
                    $dc_cock_lady_1_have_a_nice_day = True
                    mc "Have a nice day."
                    c "And you as well, Miss Vague."
                "Does your cock have any other warnings for me?":
                    $dc_cock_lady_1_does_your_cock_have_any_other_warnings_for_me = True
                    mc "Does your cock have any other warnings for me?"
                    c "You are actually willing to listen to my cock?"
                    c "Now that is rare, for certain."
                    mc "What do you mean, it squirts out wisdom."
                    c "That it does, Miss Vague, but few people are ready to face the truth."
                    mc "Ain't that the truth."
                    c "Well, there is one other thing that my cock has told me..."
                    c "Not everyone who is friendly to you has your best interest in mind..."
                    c "And not everyone who shuns you, does so for nefarious reasons."
                    c "And that is all I have to say about this town for now, Miss Vague."
                    c "If you ever want to hear more of what my cock has to say, you are invited to my home, and we can talk there."
                    mc "Uh, thank you, I will keep that in mind."
        "You are crazy, just let me enjoy my coffee in peace, okay?":
            $dc_cock_lady_1_you_are_crazy_just_let_me_enjoy_my_coffee_in_peace_okay = True
            mc "You are crazy, just let me enjoy my coffee in peace, okay?"
            c "Now, that is not nice, but hardly unexpected."
            c "People just aren't able to handle my cock."
            mc "Just leave me alone, okay?"
            c "I'll be on my way, then."
            c "Enjoy your coffee, and know that it could always be the last coffee if you aren't careful."
            m "Jesus, Cecilia, leave her alone."
            scene black at topleft with dis #todo
            c "I'm going, I'm going."
    scene black at topleft with dis #todo
    m "Well, you handled that one better than most."
    mc "That was weird."
    m "Aye, that's Cecilia for you."
    mc "What's her deal?"
    m "Nobody really knows."
    m "She's been like this since before I was born, always spouting nonsense, then going on about her day."
    m "It's weird like you say, but it's usually short enough to not bother me much."
    mc "Yep, that seems like the right way to go about it."
    if dc_cock_lady_1_does_your_cock_have_any_other_warnings_for_me:
        $unlocked_dc_hardong_1 = True
        m "She lives at Dr. Hardong's clinic, in case you ever want to \"hear what her cock has to say\"."
        mc "I'm fine, but thank you."
        m "Hah, that's what I thought."
        mc "Who's Dr. Hardong, by the way?"
        m "Oh, of course you wouldn't know."
        m "He's a popular psychiatrist, I think you would say."
        m "Has a clinic on the other side of the lake, out in the forest."
        m "Actually, maybe it is worth talking to him, for you, I mean."
        m "I mean, uh, not because you're crazy or anything..."
        m "Sorry, I mean as inspiration for your books."
        m "Ragnar said you're an author, and..."
        m "Sorry, I try not to gossip so much, normally."
        mc "Hah, it's all good."
        mc "Thank you for the idea, I might see if he's willing to talk to me."
        m "You can always talk slower than normal and look around like you're seeing shadows everywhere."
        mc "Hah, that's a good idea."
    scene black at topleft with dis #todo
    mc "Thanks, Mary."
    m "All the time."
    jump evening_choices