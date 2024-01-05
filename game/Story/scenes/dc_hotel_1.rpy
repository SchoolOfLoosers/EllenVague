label dc_hotel_1:
    scene 27 at topleft with dis
    #todo write introduction of hotel
    scene 28 at topleft with dis
    j "Welcome, you must be Miss Vague, we have been expecting you."
    j "We have prepared you our nicest room, we hope you enjoy your stay."
    scene 29 at topleft with dis
    mc "Oh thank you, that is nice of you."
    scene 30 at topleft with dis
    j "Of course. My name is Jay Killhide, always just a call away if you need anything."
    scene 31 at topleft with dis
    mc "That is a...peculiar name, if you don't mind me saying."
    mc "Your ancestors must have been hunters."
    scene 32 at topleft with dis
    j "Hah, that's a fair guess."
    j "Around these parts, everyone was, and many of us still are."
    j "It's still the quickest way to make a buck, or eat one, I guess."
    "I couldn't tell what it was, but the conversation between us was just...smooth."
    "Fluent, even, like we had known each other for years."
    scene 33 with dis
    j "Anyway, I won't keep you any longer, I bet you are tired from the drive."
    scene 34 with dis
    mc "Oh, you have no idea."
    scene black with dis #todo use this asset: https://www.daz3d.com/winter-vacation-house-bundle
    mc "Wow, the pictures didn't lie, this room is beautiful!"
    mc "My god, this is literally perfect."


    #todo unpack
    if not completed_dc_diner_1:
        mc "Well, I better visit the Diner now, before I die of coffee starvation."
        jump dc_hotel_1
    jump evening_choices