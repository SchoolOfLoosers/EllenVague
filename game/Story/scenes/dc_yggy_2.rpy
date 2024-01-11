label dc_yggy_2:
    scene 188 at topleft with dis
    y "Oh hey, you are back!"
    y "Let me guess, you need some more batteries for your flashlight, because you used it all night long?"
    scene black at topleft with dis #todo 91 base
    mc "Yggy, what the fuck was that?"
    scene black at topleft with dis #todo
    y "I see you had your fun."
    scene black at topleft with dis #todo
    mc "I'm having the fucking worst leg cramps of my life, or else I would kick your ass so hard you'd finally explain to me what this stuff is and how it works."
    scene black at topleft with dis #todo
    y "Hah, alright."
    scene black at topleft with dis #todo
    y "So, the crucial ingredient are the leaves of a very specific herb that only grows in a very select few places."
    y "I found out about it in a downright ancient tome of a book, handwritten recipes in something that barely resembles modern English."
    scene black at topleft with dis #todo
    mc "You really take this stuff seriously, don't you?"
    scene black at topleft with dis #todo
    y "Only the best for my customers."
    scene black at topleft with dis #todo
    y "Also, I love to read these old books that make you translate and study."
    y "It can take a whole month for me to read a single book sometimes."
    y "And sometimes, it really pays off."
    scene black at topleft with dis #todo
    mc "That actually sounds really fascinating, I'm not gonna lie."
    scene black at topleft with dis #todo
    y "It really is."
    y "And so is finding these books in the first place."
    y "A lot of charlatans and neverdowells out there, hoping to take advantage of passionate people like me."
    scene black at topleft with dis #todo
    mc "Oh, I can imagine."
    mc "So what, you test these on yourself before you peddle them to unsuspecting customers?"
    scene black at topleft with dis #todo
    y "Yes, but this particular example has no effect on the male brain."
    scene black at topleft with dis #todo
    mc "Oh really?"
    scene black at topleft with dis #todo
    y "That's how it is sometimes, I could drink a gallon of this stuff and all that would happen is me getting drunk off the alcohol."
    scene black at topleft with dis #todo
    mc "So, who was the lucky first customer, then?"
    scene black at topleft with dis #todo
    y "A woman long lost to my quickly fading memory."
    scene black at topleft with dis #todo
    mc "Don't ask, don't tell, huh?"
    mc "Don't worry, I won't pry."
    mc "As long as you sell me another one of those."
    scene black at topleft with dis #todo
    y "I had a feeling you might come back."
    scene black at topleft with dis #todo
    mc "How could I not, that was an amazing night."
    mc "I don't think I have ever felt anything close to that."
    scene black at topleft with dis #todo
    y "You know what would be even better?"
    scene black at topleft with dis #todo
    mc "I'm sure you're about to tell me."
    scene black at topleft with dis #todo
    y "I have another potion here that will allow you to remember everything that happens between losing control and gaining it back again in the morning."
    scene black at topleft with dis #todo
    mc "You do, huh?"
    y "Just think about what you could achieve if you had a full night of hyper-focused time on your hands."
    scene black at topleft with dis #todo
    mc "Okay, I'll bite, let's say I'm interested. How much?"
    scene black at topleft with dis #todo
    y "I won't sell it to you, but I'll give it to you for free."
    scene black at topleft with dis #todo
    mc "Oh, I was wondering what your angle was on this whole matter."
    scene black at topleft with dis #todo
    y "I wouldn't mind being a part of those memories."
    scene black at topleft with dis #todo
    mc "And you think you can keep up with me when I'm hyped up like that?"
    scene black at topleft with dis #todo
    y "Believe it or not, I have a tincture here that can help with that."
    scene black at topleft with dis #todo
    mc "You are right, I do not believe it."
    mc "I can't believe you are thinking this will work."
    scene black at topleft with dis #todo
    y "It's not stupid if it works."
    y "And the choice is all yours, that's the best part about all of this."
    scene black at topleft with dis #todo
    mc "Way to go acting like you're taking the high road here."
    menu:
        "So, let's say we do this...":
            $dc_yggy_2_lets_say_we_do_this = True
            scene black at topleft with dis #todo
            mc "So, let's say we do this..."
            mc "And I'm not saying we will..."
            mc "How do you see this happening?"
            scene black at topleft with dis #todo
            y "Well, since you said you came here looking for inspiration..."
            y "I say we lock ourselves up in your room, where it's nice and cozy and comfortable..."
            y "And then you start writing."
            y "You'll see, your focus will allow you to write pages over pages, all in one night."
            y "And anytime you need some inspiration, I'll be there to help you out."
            scene black at topleft with dis #todo
            mc "You make that sound so easy."
            scene black at topleft with dis #todo
            y "Trust me, I can always make it hard for you."
            scene black at topleft with dis #todo
            mc "Woah, that was bad."
            scene black at topleft with dis #todo
            y "I'll make good on the offer, though."
            menu:
                "Yeah, no way we are doing that, I don't know how you can think that would work.":
                    $dc_yggy_2_yeah_no_way_we_are_doing_that_i_dont_know_how_you_can_think_that_would_work = True
                    $unlocked_ec_yggy_1 = True
                    scene black at topleft with dis #todo
                    mc "Yeah, no way we are doing that, I don't know how you can think that would work."
                    scene black at topleft with dis #todo
                    y "Of course, nobody expects you to say yes."
                    y "But if that changes, you can always give me a call."
                    jump evening_choices
                "I might give you a call sometime.":
                    $dc_yggy_2_i_might_give_you_a_call_sometime = True
                    $unlocked_ec_yggy_1 = True
                    scene black at topleft with dis #todo
                    mc "Okay, I can't believe I'm saying this, but..."
                    mc "I might give you a call sometime."
                    scene black at topleft with dis #todo
                    y "I look forward to that."
                    scene black at topleft with dis #todo
                    mc "I look forward to seeing how messy we can get together."
                    scene black at topleft with dis #todo
                    y "And how many pages you'll write, yes?"
                    y "At least I thought that was your main goal here."
                    scene black at topleft with dis #todo
                    mc "I feel like we can mix business and pleasure here."
                    scene black at topleft with dis #todo
                    y "I'll bring everything we need for that."
                    y "If you ever end up giving me that call."
                    jump evening_choices
        "I'm gonna take a hard pass, but thanks for the effort":
            $dc_yggy_2_hard_pass = True
            scene black at topleft with dis #todo
            mc "I'm gonna take a hard pass, but thanks for the effort"
            scene black at topleft with dis #todo
            y "Of course, nobody expects you to say yes."
            y "But if that changes, you can always give me a call."
            jump evening_choices