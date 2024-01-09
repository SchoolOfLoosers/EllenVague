label dc_sarah_1:
    scene 204 at topleft with dis
    s "Oh good, there you are."
    mc "Yes, I came as soon as I could."
    if ec_sarah_1_had_sex_with_sarah:
        s "I know, I was there, remember?"
        mc "Really, we are going there?"
        s "Come on, it was too good of an opportunity."
        mc "Can't deny the truth."
        s "You denied me very little last night."
        mc "Seems like a trend, huh?"
        s "Feel free to drop by sometime in case you need a refresher on that subject."
        $unlocked_ec_sarah_2 = True
        mc "I might stumble against your front door sometime soonish."
        s "Anytime, girl."
    s "Well, sit down, I have already prepared the statement for you, so you can just check if I got everything right, then sign it."
    s "I'll just need to fetch it real quick, then you can be on your way again."
    scene 205 at topleft with dis
    "It was weird, being left alone in a sheriff's office, surrounded by files and secrets and the smell of...light."
    "I couldn't quite put my finger on what it was, but the whole room smelled like summer, with specks of dust being lit up by the sun."
    "Definitely not as bad as a dusty old police station office was supposed to smell."
    menu:
        "Snoop through the open file on the desk":
            $dc_sarah_1_snooped_through_file = True
            scene 206 at topleft with dis
            "Something about the file on the Sheriff's desk drew me in like the hot, kissable lips of a secret lover."
            "I knew it was wrong, and I only had time for a passing glance, without shifting any of the papers around."
            "The top paper was a letter, from some Robert Mockingbird, FBI."
            "In it, he asked for updates about \"the case\", without any hint as to what case exactly they were discussing."
            "The only thing I was sure about was that the name did not ring a bell for me - and yet, it was like the clouds opened up and a downpour of disdain and shivers washed over me."
            scene black at topleft with dis
            "I quickly went back to my seat, trying to get a hold of this feeling and trying desperately to understand it."
            "I barely got my facial expression under control again by the time Sheriff Fuse returned."
        "Leave it be":
            $dc_sarah_1_left_the_file_alone = True
    scene 207 at topleft with dis
    s "Okay, I'm back."
    s "Here is the file, I'll give you a moment to see if I wrote any garbage."
    mc "Hah, it's not like there was a lot to go wrong, was there?"
    mc "No, this all looks fine to me, have my signature."
    scene 208 at topleft with dis
    if unlocked_ec_sarah_1:
        s "Thank you."
        if completed_ec_sarah_1:
            s "Have a nice day, Miss Vague."
            scene 209 at topleft with dis
            s "(And don't forget to come around for drinks again sometime.)"
        else:
            scene 209 at topleft with dis
            s "(And don't forget about those drinks we talked about)"
    else:
        s "Uh, I've been thinking ever since you told me your name, do you have any relationship with that author?"
        scene 210 at topleft with dis
        mc "Hah, kinda."
        mc "I'm her."
        scene 211 at topleft with dis
        s "No way, that is actually you?"
        s "I'm sorry, but I never thought I would shake hands with you."
        scene 210 at topleft with dis
        mc "You mean you have read one of my books?"
        scene 211 at topleft with dis
        s "Like, yeah?!"
        s "Quite a bunch of them, in fact."
        scene 212 at topleft with dis
        s "Uh, I mean, I have confiscated this filth from criminals of the worst sort."
        scene 210 at topleft with dis
        mc "I see."
        mc "And then, you had to read through the from start to finish, to...prepare for the witness statement?"
        scene 212 at topleft with dis
        s "Oh, yes...that's exactly what happened."
        s "What a painful experience it was."
        scene 210 at topleft with dis
        mc "Don't worry, I won't ask how painful, exactly."
        scene 211 at topleft with dis
        s "Actually, would it be annoying you to have drinks with me sometime?"
        s "I promise I will only ask you two dozen questions about your books and everything before we can go over to the actual conversation."
        scene 212 at topleft with dis
        s "Sorry, fan girl moment."
        scene 210 at topleft with dis
        mc "Hah, don't worry."
        mc "I would actually like that, yes. We can trade, and you tell me about the town."
        scene 208 at topleft with dis
        s "Deal."
        s "Just swing by anytime you want, I have most of my evenings off."
        mc "Unless there is an emergency, I guess?"
        s "Yep, and what are the chances for two of those in one week?"
        mc "Don't jinx it."
        s "Better knock on some wood."
        s "Anyway, see you around, and no rush!"
        s "I am never hard to find."

    jump evening_choices