label dc_hotel_1:
    scene black at topleft with dis #todo
    j "Welcome, you must be Miss Vague, we have been expecting you."
    j "We have prepared you our nicest room, we hope you enjoy your stay."
    mc "Oh thank you, that is nice of you."
    j "Of course. My name is Jay Killhide, always just a call away if you need anything."
    mc "That is a...peculiar name, if you don't mind me saying."
    mc "Your ancestors must have been hunters."
    j "Hah, that's a fair guess."
    j "Around these parts, everyone was, and many of us still are."
    j "It's still the quickest way to make a buck, or eat one, I guess."
    "I couldn't tell what it was, but the conversation between us was just...smooth."
    "Fluent, even, like we had known each other for years."
    scene black with dis #todo
    j "Anyway, I won't keep you any longer, I bet you are tired from the drive."
    mc "Oh, you have no idea."
    scene black with dis #todo use this asset: https://www.daz3d.com/winter-vacation-house-bundle
    mc "Wow, the pictures didn't lie, this room is beautiful!"
    mc "My god, this is literally perfect."


    #todo unpack
    if not completed_dc_diner_1:
        mc "Well, I better visit the Diner now, before I die of coffee starvation."
        jump day_choices
    jump evening_choices