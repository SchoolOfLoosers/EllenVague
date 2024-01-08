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

    if completed_ec_potion_masturbation_1:
        scene black at topleft with hpunch #todo bright day, make this the same pose as in masturbation scene final render
        mc "Woah, that was intense."
        mc "Wait what?"
        mc "How can it be morning already?"
        scene black at topleft with dis #todo
        mc "No way, what the heck happened?"
        mc "I must have fallen asleep..."
        scene black at topleft with dis #todo
        mc "But...I remember sitting here in this very pose, certainly I did not fall asleep like that..."
        mc "And oh my god, my legs are cramped..."
        scene black at topleft with dis #todo roll over on back
        mc "Holy moly, I can't believe that happened."
        scene black at topleft with dis #todo sit up
        mc "What on earth is in that stuff?"
    jump day_choices