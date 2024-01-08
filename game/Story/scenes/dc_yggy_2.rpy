label dc_yggy_2:
    scene 189 at topleft with dis
    #todo talk to yggy about potion, optionally buy a new one, at which point he flirts with us and tells us that he can sell us another potion that will allow us to remember what happens in the time between orgasm and waking up.


    scene black at topleft with dis #todo
    y "I have another potion here that will allow you to remember everything that happens between losing control and gaining it back again in the morning."
    mc "You do, huh?"
    mc "Okay, I'll bite, let's say I'm interested. How much?"
    y "I won't sell it to you, but I'll give it to you for free."
    mc "Oh, I was wondering what your angle was on this whole matter."
    y "I wouldn't mind being a part of those memories."
    mc "And you think you can keep up with me when I'm lost like that?"
    y "Believe it or not, I have a tincture here that can help with that."
    mc "You are right, I do not believe it."
    mc "I can't believe you are thinking this will work."
    y "It's not stupid if it works."
    y "And the choice is all yours, that's the best part about all of this."
    mc "Way to go acting like you're taking the high road here."
    menu:
        "So, let's say we do this...":
            $dc_yggy_2_lets_say_we_do_this = True
            mc "So, let's say we do this..."

            pass #todo fill choice
        "I'm gonna take a hard pass, but thanks for the effort":
            $dc_yggy_2_hard_pass = True
            mc "I'm gonna take a hard pass, but thanks for the effort"
            pass #todo fill choice

    jump evening_choices