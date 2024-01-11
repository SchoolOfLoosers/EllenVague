label next_morning:
    $rng = renpy.random.randint (1, 3)
    if rng == 2:
        call dream_sequence

    scene black at topleft with dis
    if ec_sarah_1_had_sex_with_sarah and not played_ec_sarah_1_had_sex_with_sarah_reaction:
        $played_ec_sarah_1_had_sex_with_sarah_reaction = True
        scene 198 at topleft with dis
        mc "Jesus Christ."
        scene 199 at topleft with dis
        s "Sarah is fine."
        scene 200 at topleft with dis
        mc "Oh my god, she's talking..."
        s "How's your head?"
        mc "Hurts."
        mc "You?"
        s "I'm totally fine."
        mc "No you're not."
        mc "You look fine, but you aren't fine. Don't lie to me."
        s "Not even if I lie next to you?"
        scene 201 at topleft with dis
        mc "That was bad."
        s "Unlike you, Miss Writer."
        mc "I can't believe you are flirting with me."
        s "You want me to stop?"
        mc "Nah."
        s "That's what I thought."
        mc "You have such an arresting smile."
        s "Now who's making the bad jokes here?"
        mc "Let's agree to share the blame."
        s "Okay, but only if we can also share another hour here."
        mc "I don't mind."
        s "I thought you big city folks were always in a rush to be...productive?"
        mc "The only thing I wanna rush to this morning are conclusions."
        s "Oh, is that so?"
        s "And what do you conclude happened here?"
        mc "A police matter that I, as a civilian, am not privy to."
        s "That sounds about right."
        s "So, in that case, let us put the cover of silence on this matter, shall we?"
        mc "I won't say a word."
        s "Not if my lips can prevent it."
        scene 202 at topleft with dis
        mc "Oh my god, what time is it?"
        s "Too late to get up early."
        mc "Don't you have somewhere to be?"
        s "Did my phone ring?"
        mc "Not that I heard."
        s "Then I don't have anywhere to be."
        s "But if you want to leave, then be my guest."
        scene 203 at topleft with dis
        s "Actually, feel free to be my guest again sometime."
        mc "I wouldn't mind that."
        scene 200 at topleft with dis
        s "Then you better get your cute little butt out of my bed, get dressed and get going."
        mc "You are throwing me out?"
        s "I think your pants are still upstairs, in case you forgot."
        s "Just close the door when you leave."
        mc "And what are you doing while I do that?"
        s "What does it look like that I'm doing?"
        s "I'm gonna get some shuteye, it was a long night and Sarah needs her sleep."
        mc "You go, girl."
        s "Not for a while, I won't."
        s "See you around, cutiepie."

    if ec_patty_1_masturbated_at_home and not played_ec_patty_1_masturbated_at_home_reaction:
        $played_ec_patty_1_masturbated_at_home_reaction = True
        scene 93 at topleft with dis
        mc "Ugh, I am such a mess, aren't I?"
        mc "Light of day didn't exactly put my choices into a better light, now did it?"
        mc "Come on, Ellen, get a grip."
        mc "What's done is done, there is no way back."
        mc "And wouldn't you know, that's the first page of a new book, and at least one person will chuckle when she reads that sentence."
        mc "That's fan service's finest hour, isn't it? Writing for an audience of one?"
        mc "Come on, Ellen, time to get up, get dressed, get kicking."

    if completed_ec_potion_masturbation_1 and not played_completed_ec_potion_masturbation_1_reaction:
        $played_completed_ec_potion_masturbation_1_reaction = True
        scene 261 at topleft with hpunch
        mc "Woah, that was intense."
        mc "Wait what?"
        mc "How can it be morning already?"
        scene 262 at topleft with dis
        mc "No way, what the heck happened?"
        mc "I must have fallen asleep..."
        scene 263 at topleft with dis
        mc "But...I remember sitting here in this very pose, certainly I did not fall asleep like that..."
        mc "And oh my god, my legs are cramped..."
        scene 264 at topleft with dis
        mc "Holy moly, I can't believe that happened."
        scene 265 at topleft with dis
        mc "What on earth is in that stuff?"

    if ec_jay_1_can_share_bed_tonight and not played_ec_jay_1_can_share_bed_tonight_reaction:
        $played_ec_jay_1_can_share_bed_tonight_reaction = True
        scene 35 at topleft with dis
        mc "Oh my god, that was SO embarrassing!"
        mc "I can't believe he said no."
        mc "What kind of asshole does that?!"
        menu:
            "Fine, I'll just do it myself...":
                $next_morning_fine_ill_just_do_it_myself = True
                mc "Fine, I'll just do it myself..."
                scene 94 at topleft with dis
                mc "You see this, Mister Fancy Hotel Owner Fucktard?"
                mc "This is what you're missing out on, you idiot."
                mc "God, I hope he at least has cameras installed in here"
                scene 93 at topleft with dis
                mc "He probably has, hasn't he?"
                mc "That asshole is probably sitting somewhere, watching me here..."
                mc "\"I am inclined to remember this conversation at a later date\"..."
                scene 93 at topleft with hpunch
                mc "My ass you'll remember this, you sucker."
            "I guess I'll just cringe my way to sleep...":
                $i_guess_ill_just_cringe_my_way_to_sleep_ = True
                mc "I guess I'll just cringe my way to sleep..."
        scene 264 at topleft with dis
        mc "Well, another day, another me, I guess."
        scene 255 at topleft with dis
        mc "The new me that can totally handle being rejected, without losing her mind."
        scene 254 at topleft with dis
        mc "Time to get dressed, and have breakfast downstairs."
        scene 72 at topleft with dis
        mc "And try not to stare him down, Ellen, you are better than that."
        mc "No need to add insult to injury."


    if ec_jay_2_had_sex_with_jay and not played_ec_jay_2_had_sex_with_jay_reaction:
        $played_ec_jay_2_had_sex_with_jay_reaction = True
        scene 93 at topleft with dis
        mc "Oh my god, what have I done?"
        mc "Now I can't even go and have breakfast without seeing him..."
        mc "I mean, not that I regret it or anything..."
        mc "That was actually pretty special."
        scene 257 at topleft with dis
        mc "The way he looked at me, when he stopped caring about me..."
        mc "And started caring only about himself..."
        scene 257 at topleft with hpunch
        mc "That was so good..."
        scene 258 at topleft with dis
        mc "Come on, Ellen, get a grip!"
        scene 264 at topleft with dis
        mc "Time to get ready for breakfast."
        scene 255 at topleft with dis
        mc "And wipe that stupid smile off your face!"

    jump day_choices