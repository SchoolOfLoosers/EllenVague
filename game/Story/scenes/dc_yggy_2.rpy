label dc_yggy_2:
    scene 188 at topleft with dis
    y "Oh hey, you are back!"
    y "Let me guess, you need some more batteries for your flashlight, because you used it all night long?"
    scene 282 at topleft with dis
    mc "Yggy, what the fuck was that?"
    scene 283 at topleft with dis
    y "I see you had your fun."
    scene 285 at topleft with dis
    mc "I'm having the fucking worst leg cramps of my life, or else I would kick your ass so hard you'd finally explain to me what this stuff is and how it works."
    y "Hah, alright."
    y "So, the crucial ingredient are the leaves of a very specific herb that only grows in a very select few places."
    y "I found out about it in a downright ancient tome of a book, handwritten recipes in something that barely resembles modern English."
    scene 286 at topleft with dis
    mc "You really take this stuff seriously, don't you?"
    scene 287 at topleft with dis
    y "Only the best for my customers."
    y "Also, I love to read these old books that make you translate and study."
    y "It can take a whole month for me to read a single book sometimes."
    y "And sometimes, it really pays off."
    scene 286 at topleft with dis
    mc "That actually sounds really fascinating, I'm not gonna lie."
    scene 287 at topleft with dis
    y "It really is."
    y "And so is finding these books in the first place."
    y "A lot of charlatans and neverdowells out there, hoping to take advantage of passionate people like me."
    scene 288 at topleft with dis
    mc "Oh, I can imagine."
    mc "So what, you test these on yourself before you peddle them to unsuspecting customers?"
    scene 287 at topleft with dis
    y "Yes, but this particular example has no effect on the male brain."
    scene 289 at topleft with dis
    mc "Oh really, huh?"
    mc "What a huge and unexpected surprise."
    scene 287 at topleft with dis
    y "That's how it is sometimes, I could drink a gallon of this stuff and all that would happen is me getting drunk off the alcohol."
    scene 286 at topleft with dis
    mc "So, who was the lucky first customer, then?"
    scene 290 at topleft with dis
    y "A woman long lost to my quickly fading memory."
    scene 289 at topleft with dis
    mc "Don't ask, don't tell, huh?"
    mc "Don't worry, I won't pry."
    mc "As long as you sell me another one of those."
    scene 291 at topleft with dis
    y "I had a feeling you might come back."
    scene 285 at topleft with dis
    mc "How could I not, that was an amazing night."
    mc "Even though every bone in my body hurts like hell."
    mc "I don't think I have ever felt anything close to that."
    scene 292 at topleft with dis
    y "You know what would be even better?"
    scene 289 at topleft with dis
    mc "I'm sure you're about to tell me."
    scene 287 at topleft with dis
    y "I have another potion here that will allow you to remember everything that happens between losing control and gaining it back again in the morning."
    scene 289 at topleft with dis
    mc "You do, huh?"
    scene 287 at topleft with dis
    y "Just think about what you could achieve if you had a full night of hyper-focused time on your hands."
    scene 293 at topleft with dis
    mc "Okay, I'll bite, let's say I'm interested. How much?"
    scene 291 at topleft with dis
    y "I won't sell it to you, but I'll give it to you for free."
    scene 289 at topleft with dis
    mc "Oh, I was wondering what your angle was on this whole matter."
    scene 287 at topleft with dis
    y "I wouldn't mind being a part of those memories."
    scene 293 at topleft with dis
    mc "And you think you can keep up with me when I'm hyped up like that?"
    y "Believe it or not, I have a tincture here that can help with that."
    mc "You are right, I do not believe it."
    mc "I can't believe you are thinking this will work."
    scene 291 at topleft with dis
    y "It's not stupid if it works."
    y "And the choice is all yours, that's the best part about all of this."
    scene 289 at topleft with dis
    mc "Way to go acting like you're taking the high road here."
    menu:
        "So, let's say we do this...":
            $dc_yggy_2_lets_say_we_do_this = True
            scene 294 at topleft with dis
            mc "So, let's say we do this..."
            scene 295 at topleft with dis
            mc "And I'm not saying we will..."
            scene 294 at topleft with dis
            mc "How do you see this happening?"
            scene 296 at topleft with dis
            y "Well, since you said you came here looking for inspiration..."
            y "I say we lock ourselves up in your room, where it's nice and cozy and comfortable..."
            y "And then you start writing."
            y "You'll see, your focus will allow you to write pages over pages, all in one night."
            y "And anytime you need some inspiration, I'll be there to help you out."
            scene 289 at topleft with dis
            mc "You make that sound so easy."
            scene 297 at topleft with dis
            y "Trust me, I can always make it hard for you."
            scene 298 at topleft with dis
            mc "Woah, that was bad."
            scene 297 at topleft with dis
            y "I'll make good on the offer, though."
            menu:
                "Yeah, no way we are doing that, I don't know how you can think that would work.":
                    $dc_yggy_2_yeah_no_way_we_are_doing_that_i_dont_know_how_you_can_think_that_would_work = True
                    $unlocked_ec_yggy_1 = True
                    scene 298 at topleft with dis
                    mc "Yeah, no way we are doing that, I don't know how you can think that would work."
                    scene 297 at topleft with dis
                    y "Of course, nobody expects you to say yes."
                    y "But if that changes, you can always give me a call."
                    jump evening_choices
                "I might give you a call sometime.":
                    $dc_yggy_2_i_might_give_you_a_call_sometime = True
                    $unlocked_ec_yggy_1 = True
                    scene 299 at topleft with dis
                    mc "Okay, I can't believe I'm saying this, but..."
                    mc "I might give you a call sometime."
                    scene 297 at topleft with dis
                    y "I look forward to that."
                    scene 300 at topleft with dis
                    mc "I look forward to seeing how messy we can get together."
                    scene 285 at topleft with dis
                    y "And how many pages you'll write, yes?"
                    y "At least I thought that was your main goal here."
                    scene 301 at topleft with dis
                    mc "I feel like we can mix business and pleasure here."
                    y "I'll bring everything we need for that."
                    y "If you ever end up giving me that call."
                    jump evening_choices
        "I'm gonna take a hard pass, but thanks for the effort":
            $dc_yggy_2_hard_pass = True
            scene 298 at topleft with dis
            mc "I'm gonna take a hard pass, but thanks for the effort"
            scene 297 at topleft with dis
            y "Of course, nobody expects you to say yes."
            y "But if that changes, you can always give me a call."
            jump evening_choices