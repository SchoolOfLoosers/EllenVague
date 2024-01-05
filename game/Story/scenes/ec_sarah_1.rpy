label ec_sarah_1:
    scene black at topleft with dis #todo asset winter vacation home living room
    s "There you are!"
    mc "Wow, you have a beautiful home!"
    s "I know, right? I always love coming home here, it's so...peaceful."
    s "I inherited it, just in case you wonder what being a sheriff in the middle of nowhere earns."
    mc "Hah, you read my thoughts."
    s "There's no way I could afford this place otherwise, believe me."
    s "You'd think that property prices would be low this far out and away from everything, but..."
    s "Anyway, come on in."
    s "You want a drink?"
    mc "Yes please."
    mc "What do you have?"
    s "I have wine, wine, and...let me see..."
    s "Would you look at that, a whole bottle of wine."
    mc "Hah, I'd love a glass of that."
    s "Coming right up."
    s "Sit down, I'll be right with you."



    #todo
    scene black at topleft with dis #todo
    s "But wait, before we keep talking, I need to show you something that will amaze you."
    s "Come on up, you need to see my little cozy nook up on the balcony."
    scene black at topleft with dis #todo
    mc "Woah, that IS amazing."
    s "I know, right?"
    s "We can totally move the conversation there if you aren't afraid of my shoulder touching yours."
    menu:
        "Actually, as cozy as this looks...":
            $ec_sarah_1_said_no_to_balcony_cuddling = True
            scene black at topleft with dis #todo
            s "Really? You are squeamish about cuddling?"
            s "Consider me surprised, but don't worry, I get it."
            s "Comfort zones and everything, then let's head back down."
            mc "Sorry, I don't mean to insult you, it's just..."
            s "Girl, I said don't worry, I really don't mind."
            s "Just wanted to make sure you aren't finding this spot by accident and berating me how I kept it from you."
            mc "Hah, okay, thanks."
            pass #todo fill choice back down to living room
        "You know how impossible it is to say no to that, don't you?":
            $ec_sarah_1_cuddled_on_balcony = True
            scene black at topleft with dis #todo
            s "Hah, I know, right?"
            scene black at topleft with dis #todo
            s "Okay, let me grab another bottle of wine, and we can make ourselves comfortable up here."
            scene black at topleft with dis #todo
            s "And, how does it feel?"
            mc "Amazing, I'm not gonna lie."
            s "You want a refill?"
            mc "I swear, if I didn't know any better, I would say you were TRYING to get me drunk."
            s "Hah, I have read books that started like this, that much is sure."
            mc "Well, I have written some."
            s "And how does it feel, suddenly being a character in your own story?"
            mc "Are you...actually coming on to me?"
            s "Just a little bit, no need to worry."
            s "But you DID say you came here looking for inspiration, didn't you?"
            mc "Mh-hm."
            s "Well, I could be your muse tonight."
            s "I have nowhere else to be."
            menu:
                "Actually, I don't really think we should...":
                    $ec_sarah_1_said_no_to_sex = True

                    pass #todo fill choice
                "I'm already starting to get ideas here...":
                    $ec_sarah_1_had_sex_with_sarah = True
                    scene black at topleft with dis #todo
                    s "Really? Are you gonna write about me?"
                    mc "If you like."
                    s "Not a lot about you that I don't like."
                    mc "Stop flirting!"
                    s "Make me."
                    mc "Hah, okay, what should I call your character, then?"
                    s "I don't know."
                    s "That's, like, your job, isn't it?"
                    mc "No preferences? I thought you wanted to be the muse?"
                    s "You are using my own words against me, that's pretty sexy."
                    s "Okay, how about..."
                    s "Lisa. Do you think I could be a Lisa?"
                    mc "Girl, you can be anything you like when you grow up."
                    s "Then Lisa it is."
                    s "I always wanted to be a Lisa."
                    mc "And what does this Lisa look like?"
                    s "Slutty."
                    mc "Skimpy clothes?"
                    s "Everyday to the office."
                    s "And smeared makeup when she comes out of the boss's office."
                    mc "Damn, the full nine yards, huh?"
                    s "And the full six inches."
                    mc "And then? You go right back to work?"
                    s "Gotta earn my living somehow, don't I?"
                    s "Straight to the next meeting, and nobody will dare to say a word about my makeup."
                    mc "But they will think their part."
                    s "God, I hope so."
                    s "If none of them grab my ass or whisper something inappropriate into my ear before the day is over..."
                    mc "I like the way you roll."
                    s "Then what do you say, should we roll over to my bedroom?"
                    mc "Lead the way."
                    scene black at topleft with dis #todo
                    s "You wanna take some notes? Or do you reckon you'll remember everything tomorrow?"
                    mc "Hard to forget that cute little smile of yours."
                    s "You know what I don't like about you?"
                    mc "No, tell me."
                    s "That you only use your lips for talking to me."
                    scene black at topleft with dis #todo
                    mc "Then how about that?"
                    s "Better."
                    s "Let me turn off the lights real quick, they hurt my eyes"
                    scene black at topleft with dis
                    mc "Now how am I supposed to see what I'm doing?"
                    s "I, Sarah Fuse, hereby grant you permission to get all touchy-feely as you navigate through the darkness."
                    mc "I see, so that's how it is, huh?"
                    s "That's how it is between us, now, yes."
                    mc "If I didn't know any better, I would say you planned things this way."
                    s "That would give me a lot of credit for planning skills that I do not possess."
                    mc "Girl, you are not fooling me."
                    s "Aye, but I'm feeling you."
                    mc "Stop it."
                    s "Make me."
                    mc "I'll make you do a lot of things before the night is over."
                    s "Big words, but can you back them up?"
                    mc "Let me see about that."
                    jump next_morning
            pass #todo fill choice

    #todo this asset https://www.daz3d.com/small-cozy-balcony
    jump next_morning