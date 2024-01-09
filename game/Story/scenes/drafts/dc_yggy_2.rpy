label dc_yggy_2:
    scene 189 at topleft with dis
    y "Oh hey, you are back!"
    y "Let me guess, you need some more batteries for your flashlight, because you used it all night long?"
    mc "Yggy, what the fuck was that?"
    y "I see you had your fun."
    mc "I'm having the fucking worst leg cramps of my life, or else I would kick your ass so hard you'd finally explain to me what this stuff is and how it works."
    y "Hah, alright."
    y "So, the crucial ingredient are the leaves of a very specific herb that only grows in a very select few places."
    y "I found out about it in a downright ancient tome of a book, handwritten recipes in something that barely resembles modern English."
    mc "You really take this stuff seriously, don't you?"
    y "Only the best for my customers."
    y "Also, I love to read these old books that make you translate and study."
    y "It can take a whole month for me to read a single book sometimes."
    y "And sometimes, it really pays off."
    mc "That actually sounds really fascinating, I'm not gonna lie."
    y "It really is."
    y "And so is finding these books in the first place."
    y "A lot of charlatans and neverdowells out there, hoping to take advantage of passionate people like me."
    mc "Oh, I can imagine."
    mc "So what, you test these on yourself before you peddle them to unsuspecting customers?"
    y "Yes, but this particular example has no effect on the male brain."
    mc "Oh really?"
    y "That's how it is sometimes, I could drink a gallon of this stuff and all that would happen is me getting drunk off the alcohol."
    mc "So, who was the lucky first customer, then?"
    y "A woman long lost to my quickly fading memory."
    mc "Don't ask, don't tell, huh?"
    mc "Don't worry, I won't pry."
    mc "As long as you sell me another one of those."
    y ""


    scene black at topleft with dis #todo
    y "I have another potion here that will allow you to remember everything that happens between losing control and gaining it back again in the morning."
    mc "You do, huh?"
    y "Just think about what you could achieve if you had a full night of hyper-focused time on your hands."
    mc "Okay, I'll bite, let's say I'm interested. How much?"
    y "I won't sell it to you, but I'll give it to you for free."
    mc "Oh, I was wondering what your angle was on this whole matter."
    y "I wouldn't mind being a part of those memories."
    mc "And you think you can keep up with me when I'm hyped up like that?"
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