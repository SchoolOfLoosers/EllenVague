label ec_jay_1:
    scene 112 at topleft with dis
    j "Good evening, Miss Vague, here for a drink?"
    mc "Please, I can use one."
    j "And can you also use company?"
    mc "Of course, if you have the time to spare."
    j "I do, these have been a quiet few weeks."
    mc "How come, I thought the big parade is just around the corner?"
    j "It is, and that is precisely the reason why."
    j "Everyone schedules their vacations so that they arrive no more than a few days ahead, and then leave again the morning or the week after."
    mc "Ah yes, of course, that makes sense."
    mc "I was wondering why I am seeing so few other tourists around."
    "There it was again, this fluent conversation between us, like he hadn't just asked one of his guests out for drinks, and like I wasn't allowing him the transgression with barely a nod of acknowledgment."
    scene 113 with dis
    menu ec_jay_1_menu_conversation:
        "So, how long have you been living here?" if not ec_jay_1_asked_how_long_living:
            $ec_jay_1_asked_how_long_living = True
            scene 114 with dis
            j "For most of my life, really."
            j "I spent the first ten years of my life learning the trades and crafts of the hotel business in various places, but I always had Bryatt Fowls to return to, and to call it my home."
            j "My family has lived around these parts for generations, and now that it falls to me to uphold the tradition, I have sold off most other ventures to concentrate on this hotel."
            scene 115 with dis
            mc "That is quite interesting."
            mc "You said you are upholding the tradition, but it does not appear to me that you have anyone to pass it on to?"
            mc "I hope you don't mind me asking, it is none of my business."
            scene 114 with dis
            j "I don't take offense, especially since you are correct."
            j "I will be honest with you, Miss Vague, and say that I feel a certain unease with inherited wealth."
            j "We live in a country that prides itself on making \"the dream\" available to everyone, and yet the wealth and opportunities are held in the hands of the few."
            j "Now, as people, we are naturally inclined to protect what we have, and to aspire for what others around us own that we don't."
            j "And, don't get me wrong, I would protect my legal rights to this property, now that I have it."
            j "But what irks me is that if not for my inheritance, I would have never even tried to carve out my own life path in the hotel business."
            scene 115 with dis
            mc "Interesting, then what would you have done instead?"
            scene 114 with dis
            j "It is hard to say, isn't it? There are things that I enjoy, like woodworking - but they are passing interests whenever I find myself with spare time on my hands."
            j "So, the likely answer is that I would have carved out a career out of anything that may have been available during my youth, and there is no saying what that would have been."
            j "Maybe, I would be a plumber repairing your kitchen sink on a hot summer day, for us to have this conversation."
            j "Or a farmer who is so occupied by his strict schedules and many hours of work that we would be unlikely to ever meet."
            j "In short, I have no definite answer to your question, Miss Vague, but that is the reason why I feel unwilling to produce any heirs, and shaping their paths for them."
            j "Or, even worse, to do the same purely for the reason of \"not seeing my work go to waste\" - which is the ultimate arrogance in my opinion."
            scene 115 with dis
            mc "Fascinating, thank you for that insight."
            scene 114 with dis
            j "And what about you, Miss Vague?"
            j "What is it that makes you eccentric in the eyes of the many, and fascinating to the eyes of the few?"
            jump ec_jay_1_menu_conversation
        "Do you flirt with all your guests?":
            $ec_jay_1_asked_if_he_flirts_with_all_guests = True
            scene 114 with dis
            j "Only the ones worth flirting with."
            "He wasn't even denying it - and frankly, I liked that about him."
            j "You see, Miss Vague, my family has never been hurting for money."
            j "That is why I have long stopped running this hotel the way most others would, and as long as I come out more or less around a black zero, then I am fine with it."
            j "And that, it gives me the opportunity to talk to the interesting people who stay here, to encourage them to tell their stories, and to maybe leave a tiny bit of themselves here when they inevitably leave again."
            scene 115 with dis
            mc "How...fascinating, really."
            mc "Most people wouldn't be able to do that."
            scene 114 with dis
            j "Yes, and that is only in part because most people can not afford to live this way."
            j "There are many flaws to everyone of us - but the one I find most despicable is when someone has the means to live well, and doesn't."
            scene 115 with dis
            mc "You have a way with words, I'll give you that."
            scene 114 with dis
            j "And so do you, from what I am hearing."
            scene 115 with dis
            mc "Hearing?"
            scene 114 with dis
            j "I figured since your authorship path and my readership habits have not crossed before, I would spare you the act of brushing up on your literary works after you booked your stay with us."
            scene 115 with dis
            mc "That is...honest."
            scene 114 with dis
            j "I like to think that you will come to appreciate that most about me, if we end up sharing more than the occasional conversation."
            menu ec_jay_1_menu_share:
                "Don't get ahead of yourself" if not ec_jay_1_can_share_bed_tonight:
                    $ec_jay_1_dont_get_ahead_of_yourself = True
                    j "I won't, but I will also spare you the act of making it seem like you aren't making me curious."
                    j "You have something about you that many people lack, a sort of determination."
                    j "And also, having found your own place in life, too many people will never reach that stage."
                    scene 115 with dis
                    mc "Hah, thank you."
                    mc "Takes one to know one, I guess."
                    scene 114 with dis
                    j "I like where I am in life, yes."
                    j "And since you are here to do some things you normally wouldn't get around to, I feel it appropriate to offer myself as a guide."
                    j "Bryatt Fowls is a peculiar little town, with many places that escape the passing glance"
                    jump ec_jay_1_menu_share
                "What do you have in mind?":
                    $ec_jay_1_what_have_in_mind = True
                    $unlocked_ec_jay_2 = True
                    scene 114 with dis
                    j "I would like to get a better feel for what you are really about, Miss Vague."
                    scene 115 with dis
                    mc "In what regard?"
                    scene 114 with dis
                    j "I want to know who you are when nobody is around to witness you do it."
                    j "Apart from me, of course, but that can not be helped."
                    j "There is a hiking path leading up from the main road near the old lumberyard, not a lot of people know about it."
                    scene 115 with dis
                    mc "You want to drag me into the woods?"
                    scene 114 with dis
                    j "At night, no less."
                    scene 115 with dis
                    mc "Everyone else has been warning me of exactly that, telling me not to set even a foot into the wilderness at night."
                    scene 114 with dis
                    j "And that is clearly the smart choice, though not necessarily the most interesting one."
                    j "Well, an offer has been made, and I now play the ball back into your court, should you consider to accept it some day."
                    j "I will still be here when you leave again, so do not feel rushed to make a decision."
                    j "And now, I will leave you alone with yourself, and your own thoughts."
                    j "Have a good night, Miss Vague."
                    scene 115 with dis
                    mc "Uh, you too, have a good night."
                    jump next_morning
                "We can share something tonight, if you want." if not ec_jay_1_can_share_bed_tonight:
                    $ec_jay_1_can_share_bed_tonight = True
                    j "While I do appreciate your bluntness, I am still unsure as of yet of what to make of you."
                    scene 114 with dis
                    mc "I am very soft and pliable in the right hands, so you could make of me whatever you like."
                    scene 115 with dis
                    j "Is that so?"
                    j "Then tell me, what would those right hands do to you?"
                    scene 114 with dis
                    mc "They would be very skilled at avoiding things I might object to..."
                    mc "And yet, pushing the boundaries of what is socially acceptable between a man and a woman who have only just met."
                    scene 115 with dis
                    j "A smart answer, Miss Vague, and I will admit I am inclined to remember this conversation at a later date."
                    j "But before that, I would first like to get to know you a little better."
                    jump ec_jay_1_menu_share
        "Are there any places you can recommend that are worth a visit?":
            $unlocked_ec_jay_2 = True
            $ec_jay_1_asked_places_to_visit = True
            scene 115 with dis
            j "Oh yes, several, in fact."
            j "Say, I could tell you, or I could show you."
            j "I would like to get a better feel for what you are really about, Miss Vague."
            scene 114 with dis
            mc "In what regard?"
            scene 115 with dis
            j "I want to know who you are when nobody is around to witness you do it."
            j "Apart from me, of course, but that can not be helped."
            j "There is a hiking path leading up from the main road near the old lumberyard, not a lot of people know about it."
            scene 114 with dis
            mc "You want to drag me into the woods?"
            scene 115 with dis
            j "At night, no less."
            scene 114 with dis
            mc "Everyone else has been warning me of exactly that, telling me not to set even a foot into the wilderness at night."
            scene 115 with dis
            j "And that is clearly the smart choice, though not necessarily the most interesting one."
            j "Well, an offer has been made, and I now play the ball back into your court, should you consider to accept it some day."
            j "I will still be here when you leave again, so do not feel rushed to make a decision."
            j "And now, I will leave you alone with yourself, and your own thoughts."
            j "Have a good night, Miss Vague."
            scene 114 with dis
            mc "Uh, you too, have a good night."
            jump next_morning
    jump next_morning