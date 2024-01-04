label start:
    scene 1 at topleft with dis #todo
    na "Stephen Wry once said: You are who you are when no one is watching."
    na "Well, I, for one, was horny as hell, and somehow unable to turn that into words on a page."
    na "But that's the thing about cute little sexy stories, they have to keep you at the edge of your seat all the way through, yearning for that release that may never come."
    na "In a sex story, there can be no logic, and it shouldn't really require any."
    na "Logic, by definition, is the anti-thesis of sexy, and so it has no place in a naughty story."
    scene main_menu at topleft with dis #todo
    mc "My name is Ellen Vague, and I'm a writer."
    scene black at topleft with hpunch #todo
    #todo play swerving sound
    mc "Fuck!"
    scene black at topleft with dis #todo
    mc "Hey, are you okay? Oh my god, please tell me I didn't hit you!"
    na "Stephen Fry once said, you are who you are when nobody is watching."
    na "Well, this man was definitely dead, and nobody had watched him die."
    na "And that was just my welcome to the town of Bryat Fowls. It got worse, after."
    scene black at topleft with dis #todo
    s "911, what is your emergency?"
    mc "Yes, hello, uh, there is this man, in the middle of the road, and I think he's dead! I nearly drove over him with my car!"
    s "Ma'am, do not panic, we are coming. I just need to know where you are right now, and I'll come out immediately."
    mc "God, I...I don't know, I'm not from around here. I just came out of a tunnel, and now..."
    s "A tunnel, that's good. We don't have a lot of tunnels. Is there...a bend in the road right after it?"
    mc "Yes! Exactly!"
    s "Okay, then I know where you are, that's Rushmoore Pass. Don't move, it will take about half an hour for me to get there. Can you do that for me?"
    mc "Yes, of course. And... Thank you, I'm really shaken up."
    s "Just sit down in your car and wait, I'll come immediately."
    scene black at topleft with dis #todo
    na "For such a slow town, everything happened pretty fast."
    scene black at topleft with dis #todo
    s "Are you the one who called us?"
    mc "Yes, thank you for coming so quickly."
    s "Of course. My name is Sarah Fuse, I am the Sheriff of Bryatt Fowls."
    s "I will need your name in a minute, but let us first see if there is anything we can do here."
    s "Has he...moved at all since you called?"
    mc "He, I...no, he hasn't."
    s "Okay, you can stay here if you want."
    mc "Uh, yes please."
    scene black at topleft with dis #todo
    s "Oh my god, that is..."
    mc "Do you know him?"
    s "Yes, his name is...was Pike, Pike Enyason."
    s "Ma'am, can you tell me what happened?"
    s "Oh, and start with your name, please."
    mc "Okay, sure."
    scene black at topleft with dis #todo
    mc "My name is Ellen Vague, and I'm just here on vacation."
    mc "Or, that was the plan at least."
    s "Well, I wish we could have welcomed you under more enjoyable circumstances, but rest assured that you aren't at fault here."
    s "In fact, you reacted just in time, I can tell by the brake marks."
    mc "Thank you, I wasn't sure. It all... Happened so quickly."
    mc "What happened to him, then?"
    s "I can't tell, I see no blood and no visible injuries."
    s "But Miss Vague, this is police business, as I'm sure you will understand."
    mc "Oh, of course, I'm sorry."
    s "Oh no, don't be, I'm just saying I can't share any further details."
    s "I will have to wait here for a pickup, but you are free to leave and head for the town, it's not long from here."
    menu:
        "Thank you, I really need a coffee now.":
            $intro_said_need_coffee = True
            s "Hah, I can imagine."
            s "Well, Mary at the Odin's Diner serves a mean coffee that will pick you right back up."
            s "You can't miss it when you drive into town."
            mc "Thank you, then that's my first stop."
            s "Once you are settled in, I need you to come to the station and sign a written report. I know it's annoying, but..."
            mc "Oh, don't worry, of course I'll come."
            jump day_choices
        "I'm calmer now, if you need some company here.":
            $intro_stayed_with_sarah = True
            s "Hah, I actually wouldn't mind if you could stay a little longer."
            s "I really didn't look forward to waiting here all alone with a dead man."
            mc "No, I can imagine."
            mc "Can I ask, how come you are so...calm about this? Especially if you knew him?"
            s "Oh, that comes with the job, you learn to expect the unexpected."
            s "And honestly, it's not like I had much to do with him. He mostly stuck to himself."
            s "But, I have to ask you a question back."
            mc "Sure."
            s "Why does your name sound so familiar?"
            scene black at topleft with dis #todo
            mc "Uh, you might have read one of my books."
            s "No way that's actually you!"
            s "I thought for sure you'd say something like \"you might mistake me for that book author who has the same name.\""
            mc "No it's really me."
            mc "Honestly, it's weird to get recognized way out here."
            s "I love your books!"
            s "I mean, I have confiscated this filth from criminals of the worst sort."
            mc "Hah, and then you were forced to read through them from start to finish?"
            s "Yes, exactly. Oh, what a painful experience it was!"
            mc "Don't worry, I won't ask how painful, exactly."
            s "So, please tell me you are on a promo tour, and have brought many samples of your newest book with you."
            mc "Hah, I'm afraid not, I was actually hoping to...catch a break, for a while."
            mc "Just, you know, going somewhere for vacation and refreshing my mind."
            s "Oh, of course, I get it."
            s "Well, I totally wouldn't mind to have a drink or two with you sometime, if you want to that is."
            s "I've never met any of my favorite authors or anything like that before, this is super cool!"
            $unlocked_ec_sarah_1 = True
            mc "Uh, sure, I'd like that!"
            s "Cool! Just let me know when you feel like it, I have most of my evenings off."
            mc "Really? I thought police officers were always on call?"
            s "I mean, sure, but someone has to call us for that to matter."
            s "You know, I know you got hit with the crazy stuff that can happen to here right as you landed, but Bryatt Fowls is usually a pretty quiet town."
            mc "That's what I thought I would drive into, to be honest."
            mc "Just a quiet sleepy town in the middle of nowhere."
            s "That really depends, you have come just in time for the big parade."
            mc "Oh yeah, I read about that in the brochure!"
            s "I like to call it the last rear of summer, before fall really sets in."
            s "And it gets real quiet almost immediately after."
            mc "Nice, best of both worlds, then."
            s "Totally, you picked the perfect time to stay."
            s "Where are you staying, by the way?"
            scene black at topleft with dis #todo
            mc "Oh, I booked a room at the Hotel, nothing fancy."
            s "Not a bad choice, the rooms there are cheap and good."
            s "You could have rented one of the cabins by the lake, though, to really get that quiet and away from everything feel."
            mc "I would probably just get scared."
            mc "I like being able to call for help, and people actually being around to hear me."
            s "Hah, that's a smart approach to life in general."
            scene black at topleft with dis #todo
            na "If there had been any doubt as to how backwoods the place was..."
            na "...then the way the Sheriff had called a friend with a pickup to come fetch the body settled things."
            scene black at topleft with dis #todo
            "And also that the guy looked like a literal poster boy for Backwoods Magazine."
            scene black at topleft with dis #todo
            b "Shit, Sarah, that ain't right. Pike is dead?"
            b "He didn't even drink. What happened?"
            scene black at topleft with dis #todo
            s "Nobody knows yet, Bubba. But if we can, we'll find that out."
            b "And who are you?"
            mc "I'm Ellen, I came here for a vacation, I was coming from there and nearly drove over him."
            b "Well, good thing you didn't, that wouldn't have been a particularly nice thing to do to him, now would it?"
            "I had meant to ask something, but I just couldn't remember. The guy was slowing time around him, and my brain had trouble adapting."
            "At least I hoped it was that."
            scene black at topleft with dis #todo
            s "Miss Vague, can I ask for your help here? I know it's ugly work, but we need to get him on this tarp and on the truck bed."
            mc "Uh, of course."
            scene black at topleft with dis #todo
            s "Thank you."
            mc "Can I ask something?"
            s "Of course."
            mc "It's early morning now, so this must have happened at night."
            mc "Why would anyone come out here in the dark?"
            mc "Was he a hunter?"
            scene black at topleft with dis #todo
            b "Well, he was, but nobody hunts at night 'round these parts."
            scene black at topleft with dis #todo
            mc "Why are you so sure?"
            scene black at topleft with dis #todo
            b "Ain't nobody go'n out to the forest by night, everyone knows that."
            scene black at topleft with dis #todo
            "Yes, it definitely wasn't his intellect that...drew me in."
            scene black at topleft with dis #todo
            s "Thank you, Bubba, you were very helpful."
            scene black at topleft with dis #todo
            b "I was?"
            scene black at topleft with dis #todo
            s "Yes, thank you."
            scene black at topleft with dis #todo
            b "Oh, of course, for you always, Sarah."
            scene black at topleft with dis #todo
            "Was he actually flirting with her? Was he even aware?"
            scene black at topleft with dis #todo
            s "Now, remember, you have to drive reaaal careful."
            scene black at topleft with dis #todo
            b "I know, because we can't strap him down like a doe. Don't want poor Pike bouncing off the bed, even though he ain't feeling it no more."
            scene black at topleft with dis #todo
            s "..."
            scene black at topleft with dis #todo
            s "Thank you, Miss Vague, now we can really leave."
            s "Thank you for staying to help."
            mc "Of course, it was the least I could do."
            s "Again, I hope the rest of your stay will be more enjoyable!"
            mc "That makes two of us."
            mc "Now: Coffee."
            jump day_choices