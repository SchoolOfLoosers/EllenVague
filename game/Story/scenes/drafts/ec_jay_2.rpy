label ec_jay_2:
    "This scene is not yet ready to play, I will work on it as soon as I find the time. Thanks for your understanding."
    return #todo remove this and line above
    scene black at topleft with dis #todo
    #todo asset: https://www.daz3d.com/sawmill-props https://www.daz3d.com/picnic-area-exterior https://www.daz3d.com/backwoods-shooting-range-for-genesis-3-and-8-male-s-and-female-s
    j "Welcome, Miss Vague."
    j "Are you prepared for our little hike?"
    mc "I am, but I feel like you can call me Ellen now, considering I allow you to literally drag me into the woods at night."
    j "That is true. So, come on then, let us surround ourselves with trees."
    mc "Where are we going, anyway?"
    mc "Or is that a secret?"
    j "Not anymore, it isn't."
    j "First, I thought we could briefly explore the old sawmill, and then we can carve out a path to the old lumberyard."
    j "It will be fully dark by the time we get there, so I hope your flashlight batteries are topped up."
    mc "Yep."
    j "Good to know, then let's go."
    #todo explore sawmill
    scene black at topleft with dis #todo
    mc "What's so special about that lumberyard, by the way?"
    j "Nothing, and everything."
    j "It has some personal meaning to me, because it was still active when I was young - and I worked my first summer job there."
    j "Apart from that, it really isn't anything special."
    j "Still a good hike, though."
    scene black at topleft with dis #todo
    menu:
        "Say nothing":
            $ec_jay_2_said_nothing_about_presence = True

            pass #todo fill choice
        "Say, I can't shake the feeling that we aren't alone out here...":
            $ec_jay_2_mentioned_the_presence = True
            pass #todo fill choice unlock jay_3 here
    #todo go hiking
    jump next_morning