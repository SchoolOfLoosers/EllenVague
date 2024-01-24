label dream_masturbation_witch_2:
    $completed_dream_masturbation_witch_2 = True
    na "As soon as I started touching myself, I could already feel my mind slipping..."
    na "And I was transported back to the place I already knew so well..."
    na "And this time, I was ready to meet her..."
    na "Or, I mean, play along with the tricks my own mind insisted on playing on me..."
    na "But in the moment, it all felt so real..."
    na "Like I was actually in that weird place with the statues, and there was really that weird woman in the tribal paint and tattoos..."
    na "Like such things really existed, in the real world..."
    na "So I decided to just play along."
    na "After all, what could really happen to me here, in my own dreams?"
    q "Welcome back, Ellen."
    mc "How do you know my name?"
    q "I know about everything that happens in my forest."
    q "The ravens tell me everything that I don't see myself."
    if ec_jay_2_had_sex_with_jay:
        q "Where trees were once cut down, you spread your legs for the last descendant of the Killhides."
        q "As have many women before you."
        q "But no matter how much he may try to produce an heir to his empire, his will be the last generation to soil this forest with his footsteps."
    if dc_cock_lady_2_why_the_heck_not:
        q "And I was there when you first opened your mind to the forest at Cecilia's palace."
        q "I could not reach you then, but I was there to catch a glimpse of you."
    mc "Of course."
    q "I see you still struggle to believe me."
    mc "How could I not?"
    q "The real question to ask is \"how could you trust me\"."
    q "Tell me a word, or a thing, and I will make sure it happens to you when you are awake again."
    menu:
        "I might believe you if I win the lottery.":
            $dream_masturbation_witch_2_i_might_believe_you_if_i_win_the_lottery = True
            mc "I might believe you if I win the lottery."
            #todo unlock a little scene where mary tells us that we won the lottery, only a small prize of a few bucks, even though we never played.

            pass #todo fill choice
        "The word is Spanish Inquisition.":
            $dream_masturbation_witch_2_the_word_is_spanish_inquisition = True
            mc "The word is Spanish Inquisition."
            #todo unlock a little scene where Patty says the word on the radio, and that then unlocks the next queen scene
            pass #todo fill choice
        "There is this FBI agent who is becoming a problem..." if 1!=1:#todo activate this once we have completed robert_2or3
            $dream_masturbation_witch_2_there_is_this_fbi_agent_who_is_becoming_a_problem_ = True
            mc "There is this FBI agent who is becoming a problem..."
            pass #todo fill choice



    #todo
    return