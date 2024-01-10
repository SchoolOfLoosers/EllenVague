label dc_yggy_1:
    scene 189 at topleft with dis
    mc "Hi, I want to buy..."
    scene 190 at topleft with dis
    mc "Oh hey, Yggy!"
    mc "I didn't know this was your shop."
    scene 188 at topleft with dis
    y "Hey right back, and welcome."
    y "Yep, this humble abode is how I earn my food, and pay the bills."
    scene 191 at topleft with dis
    mc "What...is all this stuff?"
    y "Everything you need, many things you don't... and plenty of things you don't need, but want."
    y "All kidding aside, I provide a point of sale for many of our local craftsmen, and we split the profits evenly between us."
    y "Right now, things are quiet, but depending on how many folks come for the parade next week..."
    scene 192 at topleft with dis
    mc "Well, as far as tourist traps go, this has to be one of the nicest ones I've seen."
    y "I'll take the compliment and ignore the hidden insult."
    scene 193 at topleft with dis
    mc "Say, I was told that among all this...stuff I don't need, but want - I might be able to score some batteries for my flashlight."
    y "Oh yes, that is certainly a popular item, though easily the most mundane one I could sell you."
    mc "Then why don't you show me your upselling skills in action?"
    y "With pleasure."
    y "You look like someone who listens more than she talks, with a keen eye that sees what the average person will miss."
    scene 194 at topleft with dis
    mc "Compliments to sell condiments, huh?"
    scene 195 at topleft with dis
    y "And a wordsmith like you will surely appreciate the handiwork that goes into making these potions, the quiet hours that go into collecting the secret ingredients."
    mc "You are trying to sell me alcohol with some spices mixed in, aren't you?"
    y "Aye, but these secret incredients are said to possess mystical powers, and anyone who is able to set their own mind right, will learn to truly appreciate the effects."
    mc "I'm not gonna lie, you aren't doing so bad."
    y "I am glad to hear that, Miss Vague. Or may I call you Ellen?"
    mc "You may, Mister Snake Oil Salesman."
    y "In that case, let me see if I can interest you in this particular potion here."
    mc "What are its special powers?"
    y "You will find your vision temporarily reduced, but that won't matter since it will be dark anyway."
    y "And in exchange, it will allow you to HEAR the world around you that much more clearly, that is what the Owenberry does."
    mc "So, getting drunk, not seeing where I am, but hearing how people around me laugh about the drunk tourist."
    mc "Give me two of those."
    y "Pleasure doing business with you."
    mc "Likewise."
    y "Speaking of pleasure, might I introduce you to this special blend here?"
    mc "Skar's Desire? What is that supposed to do?"
    y "Well, those who use it, only speak about it in hushed tones, and they say that it's secret is that it allows for secret moments to keep you shrouded in secrecy for just a little longer."
    mc "You are selling me an aphrodisiac?"
    y "And you are thinking about buying it from me."
    menu:
        "I'm good, thanks.":
            $dc_yggy_1_did_not_buy_aphrodisiac_potion = True
            y "Your loss, but suit yourself."
            mc "You'll sell enough of those next week when everyone comes for the parade."
        "Not just thinking about it, I HAVE to get that.":
            $dc_yggy_1_bought_aphrodisiac_potion = True
            $inventory_has_aphrodisiac_potion = True
            mc "Not just thinking about it, I HAVE to get that."
            mc "Let me guess: No refunds?"
            y "Only repeat sales."
            mc "Big words, Mister."
            y "I always leave my customers satisfied."
            mc "I'm sure you do."
            y "Listen, if you want to dive into the depth of what this town has to offer, you should consider coming to Ragnar's concert."
            $unlocked_ec_concert_1 = True
            mc "Oh, and when is that?"
            y "Always, and never, but sooner rather than later."
            mc "How very mysterious."
            y "You will like it, trust me."
            mc "And if I do, I won't tell you about it."
            y "But you will buy more."
            mc "Hah, that's probably true."
    scene 196 at topleft with dis
    mc "Anyway, thanks for the batteries."
    y "For your... flashlight."
    mc "Right."
    y "Have a nice evening."
    scene 197 at topleft with dis
    mc "I'm sure I will."
    jump evening_choices