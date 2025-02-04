label ec_patty_1:
    scene 61 at topleft with dis
    p "Now, folks, you won't believe who just wandered into the studio."
    p "I mean, I don't want to keep you guessing, so why don't you come with me to welcome her?"
    p "Welcome, Miss Vague, it is an honor to have you here."
    scene 62 at topleft with dis
    mc "Hah, the honor is all mine. What a cozy little studio!"
    scene 63 at topleft with dis
    p "I know, right? Why do you think I spend nearly every night in here, talking into a microphone?"
    mc "I can imagine the view has something to do with it."
    p "Oh, absolutely, there is nothing better than sitting here, watching the sun disappearing behind the trees past the lake."
    p "But enough about me, I am sure our listeners haven't tuned in tonight to hear me wax about my cozy little studio."
    p "Before we start: Do your editors know you are here tonight?"
    scene 64 at topleft with dis
    mc "Oh no, they would probably panic if they knew I go anywhere without a stack of cards full of talking points."
    scene 65 at topleft with dis
    p "In that case, let me speak for all our listeners and promise that we will keep tonight a secret."
    scene 64 at topleft with dis
    mc "Hah, thank you."
    scene 65 at topleft with dis
    p "Now, I am sure you are already well-known around here, and I would bet that not a lot of people would admit as much."
    p "But please, for those who are not yet addicted to your works, would you quickly introduce yourself?"
    scene 66 at topleft with dis
    mc "Eh, sure. My name is Ellen Vague, and I write romance books for a living."
    scene 65 at topleft with dis
    p "Now, that is clearly selling it short, folks. Because when Ellen says romance, she means romance with a capital R, as in rawr."
    scene 67 at topleft with dis
    mc "That's...actually a really good tag line, do you mind if I steal that?"
    mc "I would love to put that on the back of the next book."
    scene 65 at topleft with dis
    p "Oh, totally. My own name on a certified Vague? Now, what do we say to that, folks?"
    p "Speaking of which, is there any telling when we can expect a new book from you?"
    scene 66 at topleft with dis
    mc "To be perfectly honest, I have not yet started to work on one, which is part of the reason I even came out here."
    mc "I just needed a vacation, to...refresh my mind, I guess."
    scene 68 at topleft with dis
    p "And haven't you come to the perfect place to do so!"
    p "Well, I am sure that I speak for my listeners when I say we would all love to see our small town of Bryatt Fowls serving as inspiration for some deep and dark secrets."
    p "Another question, if you don't mind."
    scene 64 at topleft with dis
    mc "Of course, I don't have anywhere to be tonight."
    scene 68 at topleft with dis
    p "I am glad to hear that."
    p "Well, I have wondered ever since you agreed to come out and up here."
    scene 69 at topleft with dis
    p "Any of those stories true? Or, you know, loosely based on actual events?"
    scene 64 at topleft with dis
    mc "Oh heavens no."
    scene 67 at topleft with dis
    mc "Not if there is a chance that my parents and my neighbor's wives are listening."
    scene 68 at topleft with dis
    p "Well, you heard it here first, folks, you better lock your husbands up when Miss Ellen Vague is in town."
    p "Thank you for coming here tonight, Miss Vague, and I can NOT wait to hold your next book in my hands."
    scene 63 at topleft with dis
    mc "Thank you for having me, Miss Maynard."
    p "Now, folks, excuse me for a moment while I bring Miss Vague to the door."
    p "Enjoy listening to some chill late night hip hop that I whipped up in honor of tonight."
    p "I called it \"Box of dirty tricks\", and if you don't get it, you weren't old enough to listen to this interview right now."
    p "The perfect tune to clear your earwaves, and I wager to say that not even our friends at the Odin's Diner can resist to nod their heads to this."
    scene black at topleft with dis
    play music track_ec_patty_1
    pause 85
    stop music fadeout 1.0
    scene 70 at topleft with dis
    p "Wait, let me check that the microphones are turned off..."
    p "Yep, looks safe enough."
    p "I hope that was fun for you. I know we aren't the biggest station around the country, but..."
    mc "Oh come on, this was way more fun than all those staged shows I normally take part in."
    mc "You have no idea how boring it is to sit there, reading what other people have agreed I can say on air."
    mc "Can you believe they have to run most of my interviews past their legal departments?"
    p "It's impressive how prudish people still are these days."
    mc "I guess it falls to a small town radio show host to show the big names in the industry how to create a comfortable interview environment."
    p "Hah, I'm glad you liked it."
    p "Listen, the reason I made sure to turn the microphones off is that I am totally not above asking you to sign one of my books of yours."
    p "Hope that's okay."
    mc "But of course."
    mc "I'm excited to see which ones you own."
    p "Oh, I only have four anymore, but I had some more."
    p "I always give them away after I'm done reading, we have this public book exchange here."
    p "And you know, I always like to think that someone comes along, expecting nothing harmless - and boom, they stumble over \"Inside My Neighbor's Wife\"."
    mc "Hah, that's another happy customer."
    mc "Or another book burning, I guess."
    p "I can see the reviews already."
    p "\"I hated this book so much that I read it twice\"."
    mc "You joke, but you should see some of the letters we get."
    p "God, I don't even wanna know."
    p "So, here we go, I think \"The Whore of Shenandoah Village\" is actually my all-time-favorite, so I made sure to keep this."
    mc "In case you hate it enough to read it twice, you mean?"
    p "Don't tell anyone, but it's more like...seven times, now."
    p "I just love me a good lazy day on the couch, snacks and tea and maybe something stronger as the day is no longer young anymore."
    p "And your books are pretty much perfect for that, even though I know this one by heart by now."
    mc "Wow, that's actually a really nice compliment, thank you."
    mc "What should I write?"
    p "How about..."
    p "Oh, I know."
    p "Reading is to the mind what exercise is to the body."
    p "My teacher always said that, and I always giggled."
    mc "Was he hot?"
    p "Eh, in the vicinity of hot, I guess."
    p "The taboo was his major selling point, if I'm honest."
    p "And I never acted on it anyway, my grades were always as high as my morals."
    mc "Girl, you are a fountain of accidental quotes."
    p "Hah, thank you."
    mc "Here you go, I hope it will give you many more hours of exercise."
    p "You are literally the best."
    p "What's your own favorite book, by the way?"
    mc "Ugh, that is such a loaded question."
    menu:
        "Instructed by my yoga instructor":
            $ec_patty_1_picked_yoga_favorite = True
            mc "Instructed by my yoga instructor, I think."
            p "Oh, I haven't read that one yet."
            p "Is it any good?"
            mc "Well, it's the answer to your question earlier, if any story was based on true events."
            p "No way."
            mc "Don't EVER tell anyone that I told you this."
            p "Your yoga instructor?"
            mc "What can I say, he was kinda cute."
            p "Please tell me you gifted him that book when you guys broke it off."
            mc "Oh, I did. But I'm still not convinced he knew how to read."
            mc "We never talked much about books, to be honest."
            mc "Or anything intelligent, for that matter."
            mc "We just...meditated a lot."
            p "Oh my god, that's hilarious!"
            p "Thank you so much for telling me."
            mc "The pleasure was all mine."
            p "Hah, I'm sure it was."
        "Bumfucked in Bumfuck Nowhere":
            $ec_patty_1_picked_bumfuck_favorite = True
            mc "Bumfucked in Bumfuck Nowhere, probably."
            p "Oh my god, that title alone!"
            p "How on earth did you get away with getting that printed?"
            mc "I still wonder that myself to this day, but it's also one of the best selling ones we have."
            p "Yeah, no kidding."
            p "If I randomly saw that in a bookshop, I would totally buy it just to see what's going on."
            p "And there was a lot...going on."
            p "Going off, even."
        "Whispers to your wife":
            $ec_patty_1_picked_whispers_wife_favorite = True
            mc "Whispers To Your Wife, I always thought that title had a real ring to it."
            p "Oh, I read the sample chapter at the end of \"Inside my Neighbor's Wife\", but I never got to read the full story."
            mc "It's probably my favorite, because it's so...psychological."
            mc "I still don't know where all that was coming from, but I wrote the first draft in a single week."
            p "Really? A whole book?"
            mc "I mean, a lot of work still goes into making it actually readable, but yeah, a week can fit a lot of meat when you really get your mind behind it."
            p "Your mind, huh?"
            mc "And then some."
        "The laundry room affair":
            $ec_patty_1_picked_laundryroom_affair_favorite = True
            mc "That price would have to go to \"The Laundry Room Affair\""
            p "Oh, I loved that one!"
            p "I thought it was super cool that the whole story takes place in just that apartment laundry room."
            mc "Getting filthy while the clothes are getting clean."
            p "Now who's there with the quotable sentences?"
            p "But yeah, you are totally right."
            mc "I nearly gave up on writing that a couple of times, I struggled so much with keeping the tension up."
            p "Well, I'm glad that you didn't, because you really pulled that off."
            p "Actually, I have that at home, it's one of the few that avoid the trip to the book exchange."
            mc "Another line for the back of another book."
            p "You think I should start charging you?"
            mc "That would be the smart thing to do."
            p "In that case, I will charge you a drink before you head back home."
            mc "Deal."
    p "I need to get back to my listeners now, but don't be a stranger!"
    p "If you ever get bored, you know where to find me, and that I can't really escape unnoticed."
    $unlocked_ec_patty_2 = True
    p "I wouldn't mind to hang out sometime, this was a fun evening."
    mc "Likewise, I enjoyed it a lot."
    mc "Time to get home."
    p "Word to the wise, don't stop anywhere along the way."
    p "Never know what's lurking in the darkness out here."
    scene 35 at topleft with dis
    mc "Damn, this whole evening has me...worked up a bit."
    mc "I mean, that's exactly what I came here for, wasn't it?"
    mc "But still, THAT is what gets me in the mood these days? Getting interviewed?"
    mc "I guess I have to be careful the next time I get booked for an interview somewhere."
    mc "Wouldn't that be embarrassing..."
    menu:
        "Give in":
            $ec_patty_1_masturbated_at_home = True
            scene 71 at topleft with dis
            mc "Screw this, it was a losing battle from the start..."
            mc "Who would I even impress if I kept my chin and my morals up?"
            scene 72 at topleft with dis
            mc "Nobody, that's who."
            mc "And honestly, who could really blame me?"
            scene 73 at topleft with dis
            mc "This whole trip has been a complete mess from the start, so it's my time to catch up."
            mc "Time to get messy."
            scene 74 at topleft with dis
            mc "Time to stop being in charge of my own actions..."
            mc "God, that's just what I need tonight."
            scene 75 at topleft with dis
            mc "How did Patty say? In the vicinity of hot?"
            mc "Yeah, that's right, tonight was in the vicinity of hot."
            scene 76 at topleft with dis
            mc "Actually..."
            mc "That makes for a really nice first sentence."
            scene 77 at topleft with dis
            mc "\"The thing about Jason that drove me mad was that he wasn't even hot. Okay, maybe in the vicinity of hot.\""
            mc "Damn, that totally works."
            mc "\"He was your average looking guy, neighbor next door, married to a wife who had everything going for her, and little against.\""
            mc "\"So naturally, I could resist his charms as little as I could resist the temptation itself.\""
            mc "Good job, Ellen, looks like you're finding back to your old ways."
            scene 78 at topleft with dis
            mc "Fine, that's enough for one night, back to bed."
            mc "I hope I didn't wake up the neighbors with my...typing."
            jump next_morning
        "Nah, I'll stay strong":
            $ec_patty_1_did_not_masturbate_at_home = True
            $renpy.notify("Achievement unlocked:\nPlaying the game for the story, huh?")
            scene 72 at topleft with dis
            mc "Ugh, okay, FINE!"
            mc "I know I'm better than this, no need to tell me, Ellen!"
            mc "Look at yourself, you are such an embarrassment."
            mc "Grown-ass woman, barely able to spend a minute alone without touching herself."
            mc "Barely able to write a single sentence about getting touched by imaginary characters in fictitious worlds."
            mc "Screw this writer's block, you don't deserve to take the edge off, not before you learn how to write lines on paper again."
            jump next_morning