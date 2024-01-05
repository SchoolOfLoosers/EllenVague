label dc_diner_1:
    scene 4 at topleft with dis
    "The diner looked like a proper small town diner is supposed to look like."
    "Dimly lit, a few tired faces, and a waitress walking around with free refills."
    scene 5 at topleft with dis
    "You could have been excused for thinking that it was a regular ol' Diner, and that the Odin part of the name was just a word picked from the dictionary at random."
    "Luckily, the waitress dressed in all black, and the other guests both told the keen eye a different story."
    "This was where the people met who felt out of place elsewhere."
    "But somehow, it lacked the volatility of a biker bar, or the unhomely atmosphere of a small town bar where people have lived in their own heads for too long."
    "No, this place seemed...friendly, making me feel out of place, and not, at the same time."
    menu menu_dc_diner_1:
        "Talk to the waitress" if not dc_diner_1_talked_to_mary:
            $dc_diner_1_talked_to_mary = True
            call dc_diner_1_talk_to_mary
            jump menu_dc_diner_1
        "Talk to Ragnar and Iggy" if not dc_diner_1_talked_to_ragnar_and_iggy and dc_diner_1_talked_to_mary:
            $dc_diner_1_talked_to_ragnar_and_iggy = True
            call dc_diner_1_talk_to_ragnar_and_iggy
            jump menu_dc_diner_1
        "Leave":
            pass
    if not completed_dc_hotel_1:
        mc "Well, I better check into the hotel, before they close up for the night."
        jump day_choices
    jump evening_choices


label dc_diner_1_talk_to_mary:
    scene 6 at topleft with dis
    m "Welcome to the Odin's Diner! I don't think I have seen you around here before."
    mc "No, that is right, I am here on vacation."
    mc "My name is Ellen, nice to meet you."
    scene 7 with dis
    m "I'm Mary, welcome again. Coffee?"
    mc "Oh my god, please."
    m "Long trip?"
    mc "That and..."
    mc "I guess everyone will know sooner rather than later, anyway."
    mc "When I came out of the tunnel at Rushmoore Pass, there was a dead man lying in the street, I nearly drove over him."
    scene 8 with dis
    m "Wait, what? Who's dead?"
    mc "The sheriff said his name was...Pike, I think."
    m "No way."
    scene 9 with dis
    m "Guys, did you hear that? Pike is dead."
    scene 10 at topleft with dis
    r "Say that again?"
    y "You have to excuse my friend here, he is Deaf, with a big huge D."
    y "Guess that is what happens when you spend your life on stage."
    m "I said Ellen here just told me that Pike is dead, he was lying on the road."
    r "Now who's selling pike on a stick?"
    y "Ragnar, you are one dense..."
    y "Pike is DEAD, you remember Pike Enyason?"
    r "Oh, he is? Since when?"
    y "Today, you moron, that's what the lady just told us."
    r "Well, I hope they burn him."
    r "Give him a real viking's funeral, you know?"
    y "I say we drink in his honor tonight."
    r "We'll all meet again one day, in Valhalla."
    scene 11 at topleft with dis
    m "Don't mind them much, they had a long night."
    mc "I...can tell, yes."
    scene 12 at topleft with dis
    m "Well, here is your coffee. I hope you like it black, because I had a long night as well and forgot to buy milk this morning."
    scene 13 at topleft with dis
    mc "That's perfect, I am really tired."
    m "Long drive, huh?"
    mc "That, and I'm honestly still a little shaken, I damn near drove over him."
    m "Understandable. So, he was just lying in the road? Was it an accident?"
    mc "The sheriff said no blood and visible injuries, so it might have just been a heart attack or something."
    mc "But I have absolutely no clue, don't take my word for anything other than that he was lying there."
    m "No, I get it."
    m "I would get a heart attack too, if I was out on Rushmoore Pass in the dark."
    mc "I've been wondering what anyone would do out there. Is there anything worth seeing?"
    m "Not really, no."
    m "And even if there was, nobody with more than two brain cells goes out into the forests at night."
    m "Everybody knows that."
    m "Everybody other than tourists, that is."
    m "I hope that serves as a good example for you that these forests can be dangerous."
    m "I'm not sure anyone has told you yet, but there are some rules that everyone sticks to."
    m "I guess I might as well tell you, before nobody else does, and you end up not coming back from what could have been a relaxing vacation."
    mc "Uh, sure, that would be nice."
    scene 14 with dis
    m "What I'm known for."
    m "So, it's not a lot, but that doesn't make them any less important."
    m "Always carry a flashlight on you, night falls quick around these parts."
    m "Always stick to the paths, no matter how interesting that flower may look."
    m "Could be a massive drop down into the river right behind that line of trees, and you might not see it before you are already falling."
    m "And lastly, do not startle the witch."
    mc "Wait what?"
    m "Hah, don't worry, it's just an old folk tale around here."
    m "Something we love to scare tourists with."
    scene 15 at topleft with dis
    r "Now, do not talk lightly about ol' Queen of the Forest!"
    scene 16 at topleft with dis
    m "Ragnar, how can you be deaf one second, then have a condenser microphone for ears the next?"
    scene 15 at topleft with dis
    r "And now just think about, if I can hear you, then the Queen of the Forest most definitely can."
    r "Listen, young lady, if you ever have the misfortune of meeting her, this is what you do."
    r "You say hello to her, and you take all your clothes off, so she can see that you carry no harm."
    scene 17 at topleft with dis
    m "Ragnar, you better zip it before I zip it for you."
    scene 15 at topleft with dis
    r "Aye, you are no fun, girl."
    scene 14 at topleft with dis
    m "Sorry about that, you know how old guys get when they can't get it up anymore."
    r "I heard that!"
    m "I'm sure you did, you old fool."
    m "Anyway, listen, sorry I started about the witch."
    m "Maybe an extra tip: Don't take your clothes off when you meet a stranger in the woods, okay?"
    mc "Hah, good to know."
    scene 13 with dis
    m "Now, I have to prepare some stuff, I hope you enjoy your time in Bryatt Fowls."
    mc "Thank you."
    return

label dc_diner_1_talk_to_ragnar_and_iggy:
    scene 18 at topleft with dis
    m "Hi, Ragnar, right? And... Sorry, I didn't catch your name."
    y "I'm Yggy."
    mc "how are you?"
    y "Hungover."
    r "You can say that twice."
    y "And you? How are you holding up?"
    y "You must be pretty shaken, coming into town for vacation only to find a dead man."
    mc "Right, but I'm doing better now, thanks for asking."
    y "Glad to hear that."
    y "What brings you to town, anyway?"
    r "Can't you tell? She's a writer, looking for inspiration."
    mc "How on earth could you possibly know that?"
    r "Ma'am, I may be old, but I am not blind."
    r "You have that look in your eyes that tells me you are driven by that urge to write more, and faster."
    r "Taken, you could say."
    scene 19 at topleft with dis
    mc "Hah, I guess that is my curse, yeah."
    scene 20 at topleft with dis
    $unlocked_dc_karen_1 = True
    y "Well, in that case, you should really talk to Karen at the ferry."
    y "She can bring you over to the other side of the lake."
    scene 21 with dis
    r "It's not a lake, Yggy, it's an ocean."
    y "Maybe for someone as narrow minded as you, Ragnar."
    y "It's not an ocean when you can see the other side of it."
    r "You don't even get what I'm saying, do you?"
    y "Nobody does, Ragnar."
    scene 20 at topleft with dis
    y "Anyway, talk to Karen, she will bring you over to the other side."
    mc "And then?"
    y "Then, you can hike up the path to Lover's Peak, you can overlook the whole valley from there."
    mc "That sounds beautiful!"
    y "If that doesn't inspire you, I don't know what else will."
    mc "Thank you so much for the recommendation."
    y "All the time, lady, all the time."
    y "Oh, wait, before I forget."
    y "Put this coin in your pocket, it brings good luck."
    mc "Oh thank you."
    scene 21 with dis
    r "Throw a dime to the cockslut, and she takes it all off."
    scene 22 with dis
    mc "Excuse me?!"
    scene 23 with dis
    y "Jesus Christ, Ragnar, that song again?"
    scene 20 with dis
    y "Don't mind him, that's an old song that used to come up on the radio sometimes."
    r "Yeah, exactly!"
    y "You just go on and talk to Karen, let me deal with him."
    r "Hah, I'd like to see you try."
    scene 19 at topleft with dis
    mc "Thanks for the pointer."
    scene 24 at topleft with dis
    mc "And you, Mary, thanks for the coffee!"
    scene 25 at topleft with dis
    m "All the time!"
    m "Just make sure you come back for more!"
    mc "Yep, flashlight on hand, and don't startle the witch."
    scene 26 at topleft with dis
    m "Exactly!"
    return