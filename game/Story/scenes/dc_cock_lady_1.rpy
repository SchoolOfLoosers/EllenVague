label dc_cock_lady_1:
    scene 6 at topleft with dis
    mc "Hey Mary, good to see you!"
    m "Hey Ellen, welcome back."
    mc "Say, is there any chance for a coffee around here?"
    m "Hmm, let me see..."
    m "Well, looks like you are in luck!"
    mc "Thank the heavens, I knew I could count on you."
    m "Always."
    scene 12 at topleft with dis
    m "Here you go."
    scene 9 at topleft with dis
    m "Oh no, here she comes again."
    scene 13 at topleft with dis
    mc "Who's coming?"
    scene 11 at topleft with dis
    m "Well, you better prepare for your daily dose of crazy."
    m "Just let it wash over you, there is nothing we can do."
    scene 13 at topleft with dis
    mc "Uh, okay?"
    scene 238 at topleft with dis
    c "Good morning, you heathens."
    c "What a fine morning."
    scene 239 at topleft with dis
    m "Uh, yeah, totally."
    scene 240 at topleft with dis
    m "How's your cock feeling today, Cecilia?"
    scene 242 at topleft with dis
    c "Very well, thank you for asking."
    scene 241 at topleft with dis
    "Yep, Mary hadn't exaggerated when she said to prepare."
    "Whatever this woman's reasoning might have been, everyone seemed so used to her walking around, carrying a massive dildo..."
    "One that apparently had...feelings, and an opinion that mattered."
    "Definitely out there, even as far as out-there people went."
    scene 243 at topleft with dis
    c "And you, young lady, you must be this Ellen Vague I've been hearing about."
    scene 244 at topleft with dis
    mc "That is correct, yes."
    scene 243 at topleft with dis
    c "Well, in that case, I hope you enjoy your stay."
    scene 245 at topleft with dis
    mc "I'm sure I will, it's a beautiful town."
    scene 246 at topleft with dis
    c "Well, don't let the friendly people fool ya, this town is as dangerous as any during the night."
    c "Maybe more so than the city you come from."
    scene 241 at topleft with dis
    m "Cecilia, stop scaring our guests."
    c "Oh silly, Miss Vague knows better than to be scared by an old hag like me."
    c "But she does need to be warned, doesn't she?"
    m "Uh, sure, go ahead."
    scene 17 at topleft with dis
    m "But Cecilia, after that, you have to leave, I have to run a business around here."
    c "Very well, then I shall deliver my warnings, and then be on my way."
    scene 246 at topleft with dis
    c "Listen, Miss Vague, my cock has been telling me a lot of things about you."
    scene 247 at topleft with dis
    mc "Oh it has?"
    c "Yes, I talk to it every night, and it's telling me things about the world around me."
    mc "I'm sure it does."
    scene 245 at topleft with dis
    mc "So, uh, what does your cock tell you about me?"
    c "Ah, a young lady who is willing to listen!"
    c "You should know that a man is coming after you, from outside of this world."
    scene 247 at topleft with dis
    mc "A man, huh?"
    c "His name may be Mockingbird, but he doesn't fly here, he is coming by car."
    if dc_sarah_1_snooped_through_file:
        scene 245 at topleft with dis
        "A shiver ran through my spine, and at first I couldn't quite place the name."
        "I didn't know anyone by the name of Mockingbird, which was such a silly name that I would have remembered..."
        "Until I did, and I recalled reading about him in the Sheriff's files."
        "He had written a letter asking her to be kept up to date on a case..."
        "And now I realized that it must have been about the dead man in the road..."
    menu:
        "Thank you for the warning, Miss...":
            $dc_cock_lady_1_thank_you_for_the_warning_miss_ = True
            mc "Thank you for the warning, Miss..."
            c "Oh, where are my manners."
            "Yes, that was a good question..."
            c "My name is Cecilia Beaver."
            mc "Nice to meet you, Miss Beaver."
            menu:
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
            scene 22 at topleft with dis
            mc "You are crazy, just let me enjoy my coffee in peace, okay?"
            c "Now, that is not nice, but hardly unexpected."
            c "People just aren't able to handle my cock."
            scene 22 at topleft with dis
            mc "Just leave me alone, okay?"
            c "I'll be on my way, then."
            c "Enjoy your coffee, and know that it could always be the last coffee if you aren't careful."
            scene 17 at topleft with dis
            m "Jesus, Cecilia, leave her alone."
            scene 248 at topleft with dis
            c "I'm going, I'm going."
    scene 25 at topleft with dis
    m "Well, you handled that one better than most."
    scene 24 at topleft with dis
    mc "That was weird."
    scene 11 at topleft with dis
    m "Aye, that's Cecilia for you."
    scene 24 at topleft with dis
    mc "What's her deal?"
    scene 11 at topleft with dis
    m "Nobody really knows."
    m "She's been like this since before I was born, always spouting nonsense, then going on about her day."
    m "It's weird like you say, but it's usually short enough to not bother me much."
    scene 24 at topleft with dis
    mc "Yep, that seems like the right way to go about it."
    if dc_cock_lady_1_does_your_cock_have_any_other_warnings_for_me:
        $unlocked_dc_hardong_1 = True
        scene 14 at topleft with dis
        m "She lives at Dr. Hardong's clinic, in case you ever want to \"hear what her cock has to say\"."
        scene 13 at topleft with dis
        mc "I'm fine, but thank you."
        m "Hah, that's what I thought."
        scene 24 at topleft with dis
        mc "Who's Dr. Hardong, by the way?"
        scene 11 at topleft with dis
        m "Oh, of course you wouldn't know."
        scene 25 at topleft with dis
        m "He's a popular psychiatrist, I think you would say."
        m "Has a clinic on the other side of the lake, out in the forest."
        scene 7 at topleft with dis
        m "Actually, maybe it is worth talking to him, for you, I mean."
        scene 8 at topleft with dis
        m "I mean, uh, not because you're crazy or anything..."
        scene 11 at topleft with dis
        m "Sorry, I mean as inspiration for your books."
        m "Ragnar said you're an author, and..."
        scene 9 at topleft with dis
        m "Sorry, I try not to gossip so much, normally."
        scene 24 at topleft with dis
        mc "Hah, it's all good."
        mc "Thank you for the idea, I might see if he's willing to talk to me."
        scene 14 at topleft with dis
        m "You can always talk slower than normal and look around like you're seeing shadows everywhere."
        scene 24 at topleft with dis
        mc "Hah, that's a good idea."
    scene 24 at topleft with dis
    mc "Thanks, Mary."
    m "All the time."
    jump evening_choices