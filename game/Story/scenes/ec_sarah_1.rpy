label ec_sarah_1:
    scene 117 at topleft with dis
    s "There you are!"
    mc "Wow, you have a beautiful home!"
    s "I know, right? I always love coming home here, it's so...peaceful."
    s "I inherited it, just in case you wonder what being a sheriff in the middle of nowhere earns."
    mc "Hah, you read my thoughts."
    s "There's no way I could afford this place otherwise, believe me."
    s "You'd think that property prices would be low this far out and away from everything, but..."
    scene 118 at topleft with dis
    s "Anyway, come on in."
    s "You want a drink?"
    scene 119 at topleft with dis
    mc "Yes please."
    mc "What do you have?"
    scene 120 at topleft with dis
    s "I have wine, wine, and...let me see..."
    scene 118 at topleft with dis
    s "Would you look at that, a whole bottle of wine."
    scene 119 at topleft with dis
    mc "Hah, I'd love a glass of that."
    s "Coming right up."
    s "Sit down, I'll be right with you."
    scene 121 at topleft with dis
    s "So, I've been meaning to ask..."
    s "How did you end up picking Bryatt Fowls, of all places?"
    scene 122 at topleft with dis
    mc "Uh, I pretty much looked at a map and pointed my finger at different places that I could barely reach in a day's worth of driving."
    s "That's really cool."
    s "Well, I'm glad that you pointed at us, and not some other backwoods place."
    mc "Me too, it is really...cozy here."
    s "And the people are friendly?"
    mc "Hah, that, too."
    scene 123 at topleft with dis
    mc "Actually, I haven't talked to this many people in, like, weeks."
    s "For how big the city is, it can be quite lonely out there."
    mc "Ever lived anywhere big?"
    s "Five years, through the academy and then a few more years as a patrol officer."
    scene 124 at topleft with dis
    s "But then, the position here opened up when the old sheriff retired, and I immediately sent out my application, moved back..."
    s "And never really looked back."
    mc "That's great, few people ever find their calling like that."
    s "Tell me about it, I honestly didn't expected to feel this...at home, here at home."
    s "I mean, I moved out in the first place because I had never really felt like I fit in, you know?"
    scene 125 at topleft with dis
    mc "Really?"
    mc "Somehow, I can't picture you as the purple-haired troublemaker."
    scene 126 at topleft with dis
    s "Hah, no...not like that, anyway."
    scene 124 at topleft with dis
    s "But, you know, I never really felt at ease with myself, I think that was it."
    s "Needed to get out, of this town, out of my head, out of my comfort zone."
    scene 125 at topleft with dis
    mc "Yeah, I get that."
    scene 122 at topleft with dis
    s "Where'd you grow up?"
    mc "Bad part of town, place called Hope."
    s "Sounds like the name didn't do the place justice."
    mc "Aye, it didn't."
    mc "My mom raised me and my sister on her own, my father wasn't much use."
    s "Oh, you have a sister?"
    mc "Not anymore, she died when she was seventeen."
    s "Ouch, I'm sorry."
    mc "Not your fault, and not mine, either."
    mc "But after that, my mom started drinking, and when I was seventeen myself, I hightailed it out of there, sought my luck anywhere that would take me."
    s "That's...actually quite the story, I never knew."
    mc "Yeah, it doesn't exactly say so in my author bio, does it?"
    s "No idea, to be honest."
    mc "Something about growing up in there, but it's a one-liner that says nothing."
    mc "Anyway, I roughed it for a couple of years, but then somehow I landed my first book deal, and it's been uphill ever since."
    s "Really inspiring, I must say!"
    s "So, what's your place look like, then?"
    s "Fancy, or nah?"
    mc "More like nah."
    mc "I mean, it isn't bad, and it's more expensive than it has any right to be, but..."
    mc "I never really needed much, you know?"
    mc "And it's not like out here, with plenty of space to put a second car, or a boat and an RV..."
    mc "You get what I'm saying, there is only so much stuff you can put in a city apartment before you start to dream about spring cleaning."
    s "Hah, I get that."
    s "I never had my own apartment in the city, I always lived with a friend, and two people who also lived there."
    scene 127 at topleft with dis
    mc "Ooh, that sounds like a grudge mentioned in passing."
    scene 126 at topleft with dis
    s "Oh, no biggie, they were just REALLY stupid."
    scene 128 at topleft with dis
    s "Like, the kind of guys who become a cop because other jobs won't take them."
    s "And I'm really glad that I don't have to listen to their stories anymore."
    scene 129 at topleft with dis
    mc "Silence preferable?"
    s "You have no idea the kind of flashbacks I'm getting right now."
    scene 130 at topleft with dis
    mc "Ugh..."
    s "What?"
    mc "Oh, it's nothing, go on."
    s "Oh noes, I spread that to you, didn't I? The flashbacks?"
    scene 131 at topleft with dis
    mc "Yep, but don't worry, it happens."
    scene 132 at topleft with dis
    s "You wanna vent?"
    scene 131 at topleft with dis
    mc "No, it's fine, I..."
    scene 129 at topleft with dis
    s "Nonsense, come on. It can really help and who am I, really?"
    s "Just a small town cop with enough on my plate to straight-up not care what happens to anyone in the outside world."
    mc "Hah, way to make me feel safe."
    s "I am off-duty, and I'm really not paid enough to arrest my friends."
    mc "Hah, don't worry, it's nothing illegal."
    s "Boring."
    mc "Just...really embarrassing."
    scene 126 at topleft with dis
    s "Now we're talking!"
    scene 132 at topleft with dis
    s "Come on, don't leave me hanging like this."
    s "I'll be embarrassed with you."
    scene 129 at topleft with dis
    menu:
        "Tell her the story about the night club":
            $ec_sarah_1_told_nightclub_story = True
            mc "Ugh, fine, I see I'm out of options here."
            s "Exactly!"
            call nightclub_flashback_1
            scene 136 at topleft with dis
            mc "So, there is that. That's what I was thinking about."
            s "That's really something, no wonder it made you squirm."
            scene 134 at topleft with dis
            mc "I know, right? But I guess that's part of the reason why my books even sell at all, much less well."
            scene 135 at topleft with dis
            mc "Just knowing that I can tap into this darker side of my mind when I need to, and that I have lived through some messed up stuff."
            mc "All my youth, I never really had much influence over what was happening to me, so I don't really mind anything I did back then."
            mc "But this is the kind of stuff that I did myself, willingly, and then again as soon as the shame washed off of me."
            scene 136 at topleft with dis
            s "Honestly, thank you for sharing that story with me."
            scene 135 at topleft with dis
            mc "Thanks for listening"
        "Tell her about that day you slept with your boss":
            $ec_sarah_1_told_her_about_affair_with_your_boss = True
            call boss_flashback_1
            scene 136 at topleft with dis
            mc "So, there is that. That's what I was thinking about."
            s "That's really something, no wonder it made you squirm."
            scene 134 at topleft with dis
            mc "I know, right? But I guess that's part of the reason why my books even sell at all, much less well."
            scene 135 at topleft with dis
            mc "Just knowing that I can tap into this darker side of my mind when I need to, and that I have lived through some messed up stuff."
            mc "All my youth, I never really had much influence over what was happening to me, so I don't really mind anything I did back then."
            mc "But this is the kind of stuff that I did myself, willingly, and then again as soon as the shame washed off of me."
            scene 136 at topleft with dis
            s "Honestly, thank you for sharing that story with me."
            scene 135 at topleft with dis
            mc "Thanks for listening"
        "Can we just...change the subject?":
            $ec_sarah_1_changed_subject = True
            s "Oh yes, of course, I didn't mean to pry."
            s "How about you tell me about something nice?"
            s "Something you enjoyed?"
            mc "Anything?"
            s "Just whatever comes to your mind when I say fun and enjoyable and relaxing."
            mc "Hah, okay."
            mc "There was this one day out by the lake..."
            s "Already selling me on it, I love hanging out by the lake."
            mc "Oh yeah, me too."
            mc "So, I was there with some friends..."
            mc "And we all just... had, you know, the atmosphere was...loaded."
            mc "Everyone was massaging each other, rubbing lotion on our backs even though we are already well lotioned up..."
            s "Mhm, that sounds steamy."
            mc "Yeah, but that's the thing. It wasn't really anything like that, you know?"
            mc "It was still a public lake, half of us had something going on with one of the others, and...you know, it just didn't amount to anything I would have written a book about."
            s "Hah, I get what you mean."
            mc "Right, in the evening, we collected sticks and made a fire, someone went to grab drinks, and we kinda just slept there under the light of the moon, on our towels with the backpacks for pillows."
            s "That does sound super nice."
            mc "It really was, a pretty special day."
            mc "One that I won't forget for a while."
            s "Yeah, I can imagine."
            s "That's good, you gotta tell me more stories like that."
            mc "We have all night."
    scene 137 at topleft with dis
    mc "But now, I really need some more wine."
    s "That, I can provide."
    scene 138 at topleft with dis
    s "But wait, before we keep talking, I need to show you something that will amaze you."
    scene 139 at topleft with dis
    s "Come on up, you need to see my little cozy nook up on the balcony."
    scene 140 at topleft with dis
    mc "Woah, that IS amazing."
    s "I know, right?"
    s "We can totally move the conversation there if you aren't afraid of my shoulder touching yours."
    menu:
        "Actually, as cozy as this looks...":
            $ec_sarah_1_said_no_to_balcony_cuddling = True
            scene 141 at topleft with dis
            s "Really? You are squeamish about cuddling?"
            s "Consider me surprised, but don't worry, I get it."
            s "Comfort zones and everything, then let's head back down."
            mc "Sorry, I don't mean to insult you, it's just..."
            s "Girl, I said don't worry, I really don't mind."
            s "Just wanted to make sure you aren't finding this spot by accident and berating me how I kept it from you."
            mc "Hah, okay, thanks."
            scene 161 at topleft with dis
            mc "Listen, I should probably head home now, before it gets too late."
            s "You sure you're okay to drive? You've had some wine."
            mc "Yeah, but not too much, I'm good."
            mc "Unless you wanna stop me, that is."
            s "I'm thinking I should, but I'm not in charge here."
            mc "Don't worry, I'll drive slowly and check my corners."
            s "Okay, have a safe trip."
            s "Actually, can you do me a favor and call me when you've made it home?"
            mc "That's cute."
            s "Pretty please?"
            mc "Oh, that wasn't an insult, of course I'll do that."
            s "Thank you."
            s "Good night, Ellen."
            mc "Good night. We should do this again sometime, that was fun."
            s "You think?"
            mc "Totes."
            s "Hah, I'm just kidding with you, it was great having you over."
            s "This house gets a bit too quiet sometimes."
            mc "Aye, I know the feeling."
            jump next_morning
        "You know how impossible it is to say no to that, don't you?":
            $ec_sarah_1_cuddled_on_balcony = True
            scene 142 at topleft with dis
            s "Hah, I know, right?"
            s "Okay, let me grab another bottle of wine, and we can make ourselves comfortable up here."
            scene 143 at topleft with dis
            s "And, how does it feel?"
            mc "Amazing, I'm not gonna lie."
            s "You want a refill?"
            mc "I swear, if I didn't know any better, I would say you were TRYING to get me drunk."
            s "Hah, I have read books that started like this, that much is sure."
            mc "Well, I have written some."
            s "And how does it feel, suddenly being a character in your own story?"
            scene 144 at topleft with dis
            mc "Are you...actually coming on to me?"
            s "Just a little bit, no need to worry."
            s "But you DID say you came here looking for inspiration, didn't you?"
            mc "Mh-hm."
            s "Well, I could be your muse tonight."
            s "I have nowhere else to be."
            menu:
                "Actually, I don't really think we should...":
                    $ec_sarah_1_said_no_to_sex = True
                    scene 144 at topleft with dis
                    s "Oh, don't worry, I really don't want to make you uncomfortable."
                    mc "You're not, this is...very comfortable."
                    scene 143 at topleft with dis
                    s "Then let's just stay here like this, what do you think?"
                    mc "That...would be great, thank you."
                    s "Just so you know, I won't run away just because you need some time to...adjust, if you catch my drift."
                    s "Anytime you think you need a muse, I'm here to do some musing."
                    mc "Hah, okay, thanks."
                    s "Do you want to still stay here tonight?"
                    s "There's really no need to drive home in the dark, the roads are tricky out here."
                    mc "That sounds tricky in its own right."
                    s "Oh, totally, I will wait until you are asleep, and then..."
                    mc "I'll call the cops."
                    s "Good, they already know my address."
                    s "All kidding aside, I have an extra blanket and a couch that misses being abused as a bed by friends sometimes."
                    s "And, like it or not, but you're my friend now, Miss Vague."
                    mc "I like it quite a lot."
                    mc "I've never been on friendly terms with the law."
                    s "Hah, good one."
                    s "What do you say, should we go to sleep?"
                    s "Or would you rather finish this bottle of wine with me?"
                    mc "God, I'm way too drunk already."
                    s "Another reason why you shouldn't be driving in the dark."
                    s "You never know if a cop might stop you."
                    mc "I don't know what you're talking about, officer, I am totally sober."
                    s "Oh yeah? Then why don't you show me that you can walk in a straight line, from here to the couch?"
                    mc "Watch me."
                    s "Closely."
                    scene 160 at topleft with dis
                    s "That went surprisingly smoothly."
                    mc "You mean I would be safe to drive home?"
                    s "I'm way too drunk to drive after you."
                    mc "Hah, the one night I'm actually trying to outrun the cops, the cop doesn't feel like running at all."
                    mc "Good night, Sarah, and thanks for letting me stay here tonight."
                    s "Always, this house is way too empty most nights."
                    s "Sleep tight, Miss Vague."
                    mc "Night, officer."
                    jump next_morning
                "I'm already starting to get ideas here...":
                    $ec_sarah_1_had_sex_with_sarah = True
                    scene 145 at topleft with dis
                    mc "I'm already starting to get ideas here..."
                    s "Really? Are you gonna write about me?"
                    mc "If you like."
                    s "Not a lot about you that I don't like."
                    scene 146 at topleft with dis
                    mc "Stop flirting!"
                    s "Make me."
                    scene 147 at topleft with dis
                    mc "Hah, okay, what should I call your character, then?"
                    s "I don't know."
                    s "That's, like, your job, isn't it?"
                    scene 148 at topleft with dis
                    mc "No preferences? I thought you wanted to be the muse?"
                    s "You are using my own words against me, that's pretty sexy."
                    scene 149 at topleft with dis
                    s "Okay, how about..."
                    s "Lisa. Do you think I could be a Lisa?"
                    scene 148 at topleft with dis
                    mc "Girl, you can be anything you like when you grow up."
                    s "Then Lisa it is."
                    s "I always wanted to be a Lisa."
                    mc "And what does this Lisa look like?"
                    scene 150 at topleft with dis
                    s "Slutty."
                    mc "Skimpy clothes?"
                    s "Everyday to the office."
                    scene 151 at topleft with dis
                    s "And smeared makeup when she comes out of the boss's office."
                    mc "Damn, the full nine yards, huh?"
                    s "And the full six inches."
                    mc "And then? You go right back to work?"
                    s "Gotta earn my living somehow, don't I?"
                    s "Straight to the next meeting, and nobody will dare to say a word about my makeup."
                    scene 153 at topleft with dis
                    mc "But they will think their part."
                    s "God, I hope so."
                    s "If none of them grab my ass or whisper something inappropriate into my ear before the day is over..."
                    scene 154 at topleft with dis
                    mc "I like the way you roll."
                    s "Then what do you say, should we roll over to my bedroom?"
                    mc "Lead the way."
                    scene 155 at topleft with dis
                    s "You wanna take some notes? Or do you reckon you'll remember everything tomorrow?"
                    mc "Hard to forget that cute little smile of yours."
                    scene 156 at topleft with dis
                    s "You know what I don't like about you?"
                    mc "No, tell me."
                    s "That you only use your lips for talking to me."
                    scene 157 at topleft with dis
                    mc "Then how about that?"
                    s "Better."
                    scene 158 at topleft with dis
                    mc "Now how am I supposed to see what I'm doing in this darkness?"
                    s "I, Sarah Fuse, hereby grant you permission to get all touchy-feely as you navigate through the darkness."
                    mc "I see, so that's how it is, huh?"
                    s "That's how it is between us, now, yes."
                    mc "If I didn't know any better, I would say you planned things this way."
                    s "That would give me a lot of credit for planning skills that I do not possess."
                    scene 159 at topleft with dis
                    mc "Girl, you are not fooling me."
                    s "Aye, but I'm feeling you."
                    mc "Stop it."
                    s "Make me."
                    mc "I'll make you do a lot of things before the night is over."
                    s "Big words, but can you back them up?"
                    mc "Let me see about that."
                    jump next_morning
    jump next_morning