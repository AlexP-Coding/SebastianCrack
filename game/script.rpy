# The script of the game goes in this file.

```
To add:
- Music
- Sound
- Timing
- Text color and size
```
# Text comment

## Img position

transform middle:
    yalign 0.25
    xalign 0.5
    zoom 1.20

define fastDissolve = Dissolve(0.3)
define slowDissolve = Dissolve(0.8)
define slowishDissolve = Dissolve(0.5)

# CHARACTER COLORS
define bgCharColorA = "#1d53a5"
define bgCharColorB = "#28c7bc"

# TEXT COLORS
define baddieColor = "#ff00ea"
define deathColor = "#ca0a0a"


# STYLES

define gui.dialogue_text_outlines = [(1, "#0000", 0, 0)]

style slay:
    color baddieColor
    outlines [ (1,  "#ffffff", 0.5, 0.5) ]

style slayBig is slay:
    take slay
    size 65

style death:
    color deathColor
    outlines [( 1, "#ffffff", 0, 0)]

style loud:
    size 34

style quiet:
    size 10


# CHARACTERS

# Main characters
define narrator = Character(what_italic=True)
define charSeb = Character("King D.Sebastian", color="#ca0a0a")
define charBass = Character("Bass", color = "#df7233")
define charBass_loud = Character(kind=charBass, what_size=34)
define charGfPsycho = Character("Charlie Mason", color = "#43cc19")
define charGfKaren = Character("Kar Enn", color = "#bd4ae0")
define charSweater = Character("Wooly whisper", size=25, color="#ca0a0a")

# BackgroundCharacters
define charArmy = Character("Army", color = bgCharColorA, what_size=34)
define charBMom = Character("Bass’s Mom Who Is Visiting", color = bgCharColorA)
define charBDad = Character("Bass’s Dad Who Is Visiting", color = bgCharColorB)
define charNews = Character("Journalist", color=bgCharColorA)
define charMail = Character("Mailman", color=bgCharColorA)

define currentGfriend = charGfPsycho

# SCRIPT 

# The game starts here.
label start:
    
    "Hi. Do you want to cheat and get the True Ending right away?"

    menu:
        "Yes":
            $ datedEvil = True
            $ datedObnoxious = True
            "Well, you still gotta play the game to get it...except now it's just the one time."
        
        "No":
            $ datedEvil = False
            $ datedObnoxious = False
            "Good for you. Have fun!"
    
    $ nrBaddieChoices = 0
    $ nrEvilChoices = 0
    $ nrObnoxiousChoices = 0
    $ nrChoicesTotal = 4
    
    $ nrMaxDateOptions = 3
    $ minGoodDateOptions = -(nrMaxDateOptions // - 2)
    
    jump fake_start


label fake_start:
    $ endingId = ""

    $ nrBaddieChoices = 0
    $ nrEvilChoices = 0
    $ nrObnoxiousChoices = 0
    $ nrGoodDateOptions = 0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    ##### INTRO SEB #####
    show sebastiao
    "A long time ago, far far deep into the lands of Morocco a portuguese king was acting like a teenage brat."
    
    "This king was 24 years old."

    play sound "Shared Audio Themes and Leitmotifs/funny-eastern-short-music-vlog-background-hip-hop-beat-29-sec-148905 (1) (1).mp3"

    charSeb "Yes! Victory will be super mine."
    charSeb "I am going to go head first into this like, super dangerous war and leave no heirs behind! Yaaaay!!"

    "This war was a very complicated affair, that takes a really long time to explain…soo, I won’t. Our great king wore the most beautiful and illustrious garments of the land."

    "D. Sebastian was a bastion of hope and dreams for the Kingdom of Portugal. His father passed before he was born and his grandfather when he was a mere three years old." 
    "There was no one else to rule! Should Sebastian die, the kingdom would go to sh…the spaniards!"

    charSeb "Actually! I had two cousins, and an-"

    "Shh! *cough*"

    "Moving on." 
    "Sebastian was heavily traumatized at court and was under a lot of pressure, from literally everyone. His reign wasn't all bad, but he kinda made a kingdom lose independence soo…."
    "Yeah… He made some stupid, stupid choices."

    play sound "Intro/Intro Pt1 Seb/the-glorious-army-cinematic-epic-battle-music-warhammer-inspired-155892 (1).mp3"

    "In 1548, Sebastian and his army (including his 10yo cousin) marched into a really complicated and stupid battle."

    charSeb "Let’s go brave warriors! This crusade-like war will totally work out in our favor, like all the other crusades did!"

    "..."

    charSeb "We will {=slayBig}SLAAAAAAAY{/slayBig}… {w=1.2}{space=15} Our enemies!"

    charArmy "Chargeee! Ahhh!"

    play sound "Intro/Intro Pt1 Seb/battle-screaming-36126 (1).mp3" 
    play sound "Intro/Intro Pt1 Seb/bloody-blade-103593 (1).mp3"



    "However, Sebastian did not {=slay}slay{/slay}, he was {=death}slayed{/death}…"
    "Probably."

    "As the shores in Portugal filled with fog, and the population prayed for Sebastian’s return, his beautiful garments were lost forever..."

    play sound "Intro/Intro Pt2 Bass/harp-glissando-with-chimes-sound-effect-128349.mp3"
    "{cps=2}Until…{/cps}"


    hide sebastiao
    show cg_wishywash


    ##### INTRO BASS #####

    play sound "Intro/Intro Pt2 Bass/eco-technology-145636.mp3"

    charBass "Holy monarchy, is that the long lost 1548 D.Sebastian hot crop top?"

    "Bass has been tenderly stealing D.Sebastian-related artifacts from museums all his life"
    "They’re one of his few possessions, beyond his ten-dollar Nokia phone, his novelty D.Sebastian poster, and his bathtub-slash-toilet-slash-bed."

    charBass "I can’t believe it! I don’t even have to incapacitate a guard for this one!"

    stop sound fadeout 1

    menu:
        "Buy the sweater":
            jump pt1_choice01_Done

        "Heck yeah, buy the sweater":
            jump pt1_choice01_Done

        

label pt1_choice01_Done:
    play sound "Intro/Intro Pt2 Bass/cash-register-141427.mp3" 
    
    "Bass buys the sweater. He receives five cents in his bank account."

    play sound "Intro/Intro Pt2 Bass/success fanfare trumpets 6185.mp3"
    charBass "Whoop!"

    "The package then gets held hostage in customs."

    play sound "Intro/Intro Pt2 Bass/wrong buzzer 6268.mp3"
    "He’s forced to pay up a whole six dollars."
    charBass "Son of Aviz!"

    "After a not-so-grueling two-hour-turned-twelve-hour trip, the hot crop top not-so-soon reaches Bass’ stingy hands."
    
    hide cg_wishywash
    scene bg_bass_house
    
    charBass "Ok, let’s see how I look."

    play sound "Intro/Intro Pt2 Bass/camera-13695.mp3" 

    charBass "…"

    show bass_covered_full at middle

    play sound "Intro/Intro Pt2 Bass/ohoh-yeh-91690.mp3"
    charBass_loud "{=slayBig}Perfect!{/slay}"
    charBass "Hot as an inbred king. I don't even need pants!"

    charBass "And it came just at the right time, too.\nI bet my date tonight will love it!"

    charBass "I’d better get ready.\nI’ll go out and see if the local park has some flowers I can…er…borrow."

    charBass "Should I say goodbye to my parents?"

    hide bass_covered_full

    play sound "Intro/Intro Pt2 Bass/futuristic-logo-3-versions-149429.mp3"
    menu:
        "Say goodbye":
            jump pt1_choice02_ByeParentsYes

        "Do not":
            jump pt1_choice02_ByeParentsNo


# CHOICE: Say goodbye to visiting parents
label pt1_choice02_ByeParentsYes:

    charBass "Bye, world-renowned geneticists mom-and-dad!"

    charBMom "…Why does he always have to say it like that?"

    charBDad "Weird-ass kid."

    jump pt1_choice02_Done


label pt1_choice02_ByeParentsNo:

    charBass "Nah." 
    charBass "They’re on thin ice after cloning my dead dog during their crazy scientist phase."

    jump pt1_choice02_Done


# CHOICE END
label pt1_choice02_Done:
    play sound "Intro/Intro Pt2 Bass/door creaking 01.mp3" 
    play music "Intro/Intro Pt2 Bass/sinister 156638.mp3"
    charBass "The guys at Wishy-Washy are insane…"
    stop sound fadeout 1
    charBass "I'll bet this sweater-top isn't even THAT haunted."

    play sound "Intro/Intro Pt2 Bass/door close 9.wav"
    stop music fadeout 1

    ##### CHOICES #####
    
    scene bg_lisboa
    with slowDissolve

    "As Bass leaves his luxurious condo, (no, there’s no sarcasm there, this is what counts as luxury in Lisbon in 2023 if you’re a local) he is greeted with only the freshest air the city can provide."
    
    show bass_covered_full at middle

    charBass "Mmm…I love the smell of piss in the morning."

    hide bass_covered_full

    "While on his merry way to do his chores a strange couple steps in his path, flailing their phones around."
    "They’re red as can be and wearing the most hideous hiking shoes known to man. It looks like they’re carrying their entire house on their back."
    "Bass couldn’t help but appreciate the dedication to refusing to pay for a hotel."
    "They seem to be trying to find the nearest metro line."
    "His skin begins to tingle, maybe it’s the wool…maybe it’s the traces of lead…either way Bass can feel it calling to him."

    charSweater "Don’t. Help. Don’t…help."

    "Bass can't help but obey."

## PT3 CHOICE 1
    menu:
        "Send them in the wrong direction":
            $ nrEvilChoices += 1
            jump pt3_choice01_DontHelpEvil

        "Ignore them.":
            $ nrObnoxiousChoices += 1
            jump pt3_choice01_DontHelpObnoxious

        "Redirect them to somewhere more fun.":
            $ nrBaddieChoices += 1
            jump pt3_choice01_DontHelpBaddie

label pt3_choice01_DontHelpEvil:
    "Bass isn’t in the mood to play tour guide so he directs them in the opposite direction, up a long steep cobblestone street."
    "The tourists smile and thank him."
    "While climbing the street, one of them slips on the worn stones, tumbling onto the road."
    "A tram happens to be passing by and murders the man instantly." 
    "This leads to the further decay of the relations between olive oil europe and butter europe. The UN has to get involved so the situation doesn’t escalate."

    jump pt3_choice01_Done


label pt3_choice01_DontHelpObnoxious:

    "Bass pulls out his phone, flipping it on queue. The mountain of charms just about misses their lobster red faces."
    "He cosplays as a productive member of society."

    charBass "Who the fuck dares to call me when I’m so busy?"

    jump pt3_choice01_Done

label pt3_choice01_DontHelpBaddie:
    
    show bass_covered_short at middle

    play sound "Shared Audio Themes and Leitmotifs/baddie decision (nokia bitchy ringtone).mp3"
    
    "Bass greets the strangers with a cheshire grin, looking at the destination on their phone."
    "He scoffs, convinces them it’s not worth their time. Instead, he suggests somewhere better, more fun he says."
    "The tourists thank him for his time and help and go down a shady street. They are later mugged and the loot is redistributed among locals."
    "Sunscreen is nowhere to be found among the treasure."
   
    hide bass_covered_short
    
    jump pt3_choice01_Done
    
label pt3_choice01_Done:

    "Bass continues on. He’s on a mission of the utmost importance...For iced coffee."
    
    show cg_phone_message
    
    "On his way, his phone dings twice."
    "Both of his dates text him. Who should be blessed with his attention?"

    menu:
        "Text [charGfPsycho.name].":
            $ nrEvilChoices += 1 
            jump pt3_choice02_TextDateEvil

        "Text [charGfKaren.name].":
            $ nrObnoxiousChoices += 1 
            jump pt3_choice02_TextDateObnoxious
        
        "Block both.":
            $ nrBaddieChoices += 1 
            jump pt3_choice02_TextDateBaddie


label pt3_choice02_TextDateEvil:
    charBass "(text) Can’t wait to kick a puppy with u l8r 2nite. <3 u."
    jump pt3_choice02_Done

label pt3_choice02_TextDateObnoxious:
    charBass "(text) I’ve been thinking about you all day." 
    charBass "(text) The way you verbally abuse people who earn minimum wage and nitpick everything…it just gets me going."
    jump pt3_choice02_Done

label pt3_choice02_TextDateBaddie:
    show cg_phone_turnedoff

    play sound "Shared Audio Themes and Leitmotifs/baddie decision (nokia bitchy ringtone).mp3"

    "Bass doesn't have time for this. There are more important things to life than a romantic partner he can’t use for clout." 
    "He blocks both dates before deleting their contacts. C U NVR."
    
    hide cg_phone_turnedoff

    jump pt3_choice02_Done


label pt3_choice02_Done:
    hide cg_phone_message
    scene bg_coffeeshop

    "Bass arrives at the coffee shop. The place is packed, the counter and cashier blocked by an endless sea of people."
    "Bass rolls his eyes. What does a guy have to do to get a cup of coffee?"
    charSweater "You know what to do…"

    menu:
        "Call in a bomb threat.":
            $ nrEvilChoices += 1 
            jump pt3_choice03_CoffeeShopEvil

        "Steal it.":
            $ nrObnoxiousChoices += 1 
            jump pt3_choice03_CoffeeShopObnoxious

        "Call the tabloids.":
            $ nrBaddieChoices += 1 
            jump pt3_choice03_CoffeeShopBaddie

label pt3_choice03_CoffeeShopEvil:
    "Bass sneaks away to the bathroom, logs onto his burner account and tweets anonymously about a suspicious looking man in jorts sipping his drink by the window."
    "Anyone just hanging out at a coffee shop without a single Instagram tab open is reason enough for suspicion."
    
    "He waits two minutes before making the actual call. Bass hears the symphony of screams and gas and people being trampled."
    "When the coast is clear he skips over to the counter and collects his rightful, free and well earned cup of coffee. "
    
    
    jump pt3_choice03_Done

label pt3_choice03_CoffeeShopObnoxious:
    "Bass pushes past the crowd, elbowing people left and right."
    "The barista starts to call out the next name but doesn’t finish before Bass slips it from his hand and makes a run for it."
    "The barista does crossfit in his free time though: he jumps over the counter but underestimates the length of the jump."
    "That, coupled with a few missed leg days, makes him hit his ankle on the counter on the way down."
    "People gather around him, too distracted by the scene to go after the iced coffee thief."
    "The corporation worth millions doesn’t offer him health insurance. Poor guy."
    
    
    jump pt3_choice03_Done

label pt3_choice03_CoffeeShopBaddie:

    play sound "Shared Audio Themes and Leitmotifs/baddie decision (nokia bitchy ringtone).mp3"

    "A swarm of amateur journalists descend upon the small shop, shoving microphones in the baristas’ faces."

    charNews "Is it true your oat milk is just regular milk with oats mixed in?"

    show bass_covered_croptop at middle

    "Using his contacts, several Instagram stories and tweets Bass had successfully emptied the place of customers."
    "While the underpaid workers are bombarded and distracted, Bass goes behind the counter to make his own personalized and perfect drink…"
    "He also slips a few cartons of milk into his tote bag for good measure."
    
    hide bass_covered_croptop
    
    jump pt3_choice03_Done


label pt3_choice03_Done:

    scene bg_restaurant_outside
    with fastDissolve

    "It’s almost time for his date and he’s starting to get nervous."
    "Bass stands outside the restaurant. What should he do?"

    charSweater "Do it. You know you want to."

    menu:
        "Start a rumor.":
            $ nrEvilChoices += 1 
            jump pt3_choice04_RestaurantEvil

        "Cyber stalk the restaurant staff.":
            $ nrObnoxiousChoices += 1 
            jump pt3_choice04_RestaurantObnoxious

        "Ghost them.":
            $ nrBaddieChoices += 1 
            jump pt3_choice04_RestaurantBaddie


label pt3_choice04_RestaurantEvil:
    "Bass starts a rumour about banks being shady in relation to credit and debit cards, forcing them to withhold those services for some hours while they investigate."
    "Now when the bill comes Bass can say he doesn’t carry cash and his date will be forced to pay for everything."
    jump pt3_choice04_Done

label pt3_choice04_RestaurantObnoxious:
    "Bass stalks every member of staff as he watches them rush through the restaurant on their shifts."
    "One by one. Tinder. Linkedin. Tumblr. That one Youtube channel they made when they were a teenager."
    "Perfect. Now he had everything he needed to terrorize the staff and impress his date."
    jump pt3_choice04_Done

label pt3_choice04_RestaurantBaddie:

    play sound "Shared Audio Themes and Leitmotifs/baddie decision (nokia bitchy ringtone).mp3"

    "Bass ghosts both of his dates and assumes his true destiny."
    "In order to become the biggest baddie youtuber there ever was, he needs to make some big sacrifices…like ghosting the psychopath groupie and karen."
    "Woe is he. Such acts of martyrdom truly deserve recognition…from the algorithm."
    jump endingBaddie


label pt3_choice04_Done:
    if nrEvilChoices >= nrChoicesTotal:
        jump endingEvil

    if nrBaddieChoices >= nrChoicesTotal:
        jump endingBaddie

    if nrEvilChoices >= nrObnoxiousChoices:
        $ currentGfriend = charGfPsycho
        jump dateevil

    if nrEvilChoices < nrObnoxiousChoices:
        $ currentGfriend = charGfKaren
        jump dateObnoxious


label dateevil:
    "Bass’ date approaches him. He feels the sweater tingle against his skin again but…it’s not tempting him. Hmmm…"  
    
    show love_a_happy at middle
    
    charGfPsycho "Hey! You must be Bass, I’m Charlie!" 
    
    hide love_a_happy
    
    menu:
        "Compliment her":
            jump dateEvil_choice01_Compliment

        "Go to dinner":
            $ nrGoodDateOptions += 1
            jump dateEvil_choice01_Dinner

label dateEvil_choice01_Compliment:
    show love_a_normal at middle

    
    charBass "You’re very…punctual."

    "Bass is trying to be something he’s not - civil. She can smell it a mile away."
    "You’re trying to be something you’re not, she’s suspicious of you."

    hide love_a_normal
    show love_a_bored at middle
   
    charGfPsycho "I don’t like guys who are observant…that’s my job."

    charBass "(Yeah…I’m not getting a good vibe from her)."

    play sound "Intro/Intro Pt2 Bass/wrong buzzer 6268.mp3"

    jump dateEvil_choice01_Done
    

label dateEvil_choice01_Dinner:
    charBass "Well then, we should head in for our totally budget friendly I can afford this this is totally worth every penny and priced reasonably dinner."
    
    "Bass opens the door and goes in first, not even waiting for her. It swings backwards and smacks her in the face. Her nose starts bleeding."
    "She licks the blood and smiles before following him inside."
    
    scene bg_restaurant_inside
    with fastDissolve
   
    "Dinner is going smoothly, with Bass uncharacteristically ordering the most expensive thing on the menu, fully planning on making his date pay for it."
    "Charlie orders the steak so rare it’s practically raw, and mentions something about the redness of the blood being oh so vibrant."
    
    show love_a_normal at middle
    
    "As the waiter goes to switch the cutlery, Charlie refuses. The waiter is uneasily uncomfortable and backs away."
   
    charGfPsycho "Don’t worry, I brought my own."
    
    hide love_a_normal
    show love_a_happy_knife at middle

    play sound "Dates/Date Evil/knife-slice-41231 (1).mp3"
    
    "She whips out a gigantic kitchen, shiny and sparkling and omg…is that dried blood on the handle?"

    charGfPsycho "It’s a priceless relic, I bought it on eBay for ssssuuuper cheap."
    charGfPsycho "People just don’t appreciate the classics."

    charBass "The classics?"
    
    hide love_a_happy_knife
    show love_a_knife at middle
   
    charGfPsycho "Murder weapons, silly!"

    play sound "Shared Audio Themes and Leitmotifs/ping-82822.mp3"
    
    hide love_a_knife
    jump dateEvil_choice01_Done


label dateEvil_choice01_Done:
    scene bg_restaurant_inside
    with fastDissolve

    charBass "..."

    charSweater "We should probably get to know her weaknesses."
    charSweater "You know. In case she tries to kill you."

    menu:
        "Ask about her interests.":
            jump dateEvil_choice02_Ask

        "Dismiss her interests.":
            $ nrGoodDateOptions +=1
            jump dateEvil_choice02_Dismiss    


label dateEvil_choice02_Ask:
    charBass "So Charlie, tell me more about your…interests."
    
    show love_a_normal at middle
    
    "Charlie scowls."
    
    hide love_a_normal
    show love_a_bored at middle

    charGfPsycho "Why don’t you tell me more about yourself hmm? Like who you work for or why you’re so interested in me."
    charGfPsycho "Did someone hire you?"

    charBass "What? No!"

    "She angles the knife towards Bass."
    
    hide love_a_bored
    show love_a_knife at middle

    play sound "Dates/Date Evil/knife-slice-41231 (1).mp3"
    
    charGfPsycho "Only someone with secrets to hide would be so defensive. Your body language says it all."

    "... Isn’t body language a pseudoscience?"

    charBass "(I don’t know man at this point I just want to leave this interaction with everything intact.)"
    
    hide love_a_knife
    show love_a_normal at middle
    
    "Bass is able to get [charGfPsycho] to calm down but she’s watching him closely, knife at the ready."
   
    hide love_a_normal
    play sound "Intro/Intro Pt2 Bass/wrong buzzer 6268.mp3"
   
    jump dateEvil_choice02_Done


label dateEvil_choice02_Dismiss:
    charBass "Well I’m an artifact collector myself, of much more interesting items if I do say so myself…"

    "Bass recounts the tales of the beloved poster of his idol, his Y2K plastic mace of a flip phone but not his sweater…"
   
    show love_a_happy at middle
    
    "[charGfPsycho] listens happily: he doesn’t care about her!"
    "He doesn’t care that she’s been labelled a psychopath by everyone!"
    "Including every medical professional she’s seen! And member of law enforcement!"
    
    hide love_a_happy
    show love_a_evil at middle
    
    "That makes her like him more."
    
    hide love_a_evil

    play sound "Shared Audio Themes and Leitmotifs/ping-82822.mp3"

    jump dateEvil_choice02_Done

label dateEvil_choice02_Done:
    
    charSweater "This is going well."
    charSweater "Some murder would really spice things up, you know."

    charBass "(I'll kill her with laughter!)"

    menu:
        "Tell a joke":
            jump dateEvil_choice03_JokeNo

        "Tell a joke":
            $ nrGoodDateOptions += 1
            jump dateEvil_choice03_JokeYes


label dateEvil_choice03_JokeNo:
    charBass "What does royalty wear during stormy weather?"
    charBass "A Reign Coat."
   
    show love_a_normal at middle
    
    "Charlie rolls her eyes."
   
    hide love_a_normal
    show love_a_bored at middle
    
    charGfPsycho "Ugh. Lame."

    hide love_a_bored

    play sound "Intro/Intro Pt2 Bass/wrong buzzer 6268.mp3"
   
    jump dateEvil_choice03_Done


label dateEvil_choice03_JokeYes:
    "Bass laughs to himself."
   
    show love_a_normal at middle
    
    charGfPsycho "Why are you laughing?"

    charBass "I’m just thinking of all the ways I’d get rid of that waiter, if you catch my drift."
   
    hide love_a_normal
    show love_a_evil at middle
    
    "Charlie did catch his drift, except she interpreted it in a completely different way."
    
    hide love_a_evil
    show love_a_happy at middle
   
    "You know."
   
    hide love_a_happy
    show love_a_knife at middle
    
    play sound "Dates/Date Evil/knife-slice-41231 (1).mp3"
    
    "The murder-y way."

    play sound "Shared Audio Themes and Leitmotifs/ping-82822.mp3"
    
    hide love_a_knife
    jump dateEvil_choice03_Done


label dateEvil_choice03_Done:
    if nrGoodDateOptions > minGoodDateOptions:
        $ datedEvil = True
        $ currentGfriend = charGfPsycho
        jump endingDateDisappears

    if nrGoodDateOptions <= minGoodDateOptions:
        jump endingRejected





label dateObnoxious:
    "Bass’ date approaches him."
    "He feels the sweater tingle against his skin again but…it feels different, somehow."
   
    show love_b_normal at middle
    
    charGfKaren "Hi! Bass, right? It's [charGfKaren]."
    charBass "Pleasure to meet you."
    
    hide love_b_normal
    show love_b_bored at middle
    
    "[charGfKaren] looks at the line that's been forming."
   
    hide love_b_bored
    show love_b_normal_thinking at middle
    
    charGfKaren "We'll have a long time for meeting each other, it seems."
   
    hide love_b_normal_thinking
    show love_b_happy_evil at middle
    
    charGfKaren "These people have some nerve, making us wait like this."
    
    hide love_b_happy_evil
    
    "Bass gulps."
    "He had forgone making a reservation to spare cash, but now there's a line of exactly three people."
    "They are looking at possibly twenty minutes of boredom unless they somehow disappear."

    charSweater "I think we should {i}get rid of the problem{/i}."

    "Bass steadies himself."

    charBass "Don't worry, babe, I got this."

    menu:
        "Make a scene.":
            $ nrGoodDateOptions += 1
            jump dateObnoxious_choice01_Scene

        "Propose a game.":
            jump dateObnoxious_choice01_Game


label dateObnoxious_choice01_Scene:
    "Bass scoffs so loud some spit jumps out and into his date's face."
    
    show love_b_bored at middle
   
    charGfKaren "Dude."
    
    hide love_b_bored
    
    charBass "Un. Be. Lie. Va. Ble."
    charBass "This is an OUTRAGE!"
    charBass "We've brought our good, hard-earned money to this establishment..."
    charBass "And you repay us with a NON-ZERO WAITING TIME??"
   
    show love_b_normal at middle
    
    "[charGfKaren] looks at [charBass] with stars in his eyes."
   
    hide love_b_normal
    show love_b_happy at middle
    
    charGfKaren "I know, right?!"
    charBass "I will not stand for this! You'll be getting the worst Welp review of your lives, I tell you."
    
    hide love_b_happy
    
    "The guy at reception ushers them in, face red. The people still in line give both of them the stink-eye as you pass."

    play sound "Shared Audio Themes and Leitmotifs/ping-82822.mp3"

    jump dateObnoxious_choice01_Done


label dateObnoxious_choice01_Game:
    
    "Bass pull out a ratty pack of cards he'd found on the ground."
    
    charBass "How about some 'Go Fish'?"
    
    show love_b_normal at middle
    
    charGfKaren "..."
    
    hide love_b_normal
    show love_b_bored at middle
    
    charGfKaren "I'm sorry. Are we five?"

    charBass "...No, babe."
    
    hide love_b_bored
    
    "Bass stands in silence for the long ten minutes it takes them to get in."
    "[charGfKaren] rants about poor customer service the whole time."
    "Bass adores him."

    play sound "Intro/Intro Pt2 Bass/wrong buzzer 6268.mp3"

    jump dateObnoxious_choice01_Done


label dateObnoxious_choice01_Done:
    scene bg_restaurant_inside
    with fastDissolve
    
    "Bass and his date finally make it inside the restaurant."

    "It's packed. Servers sprint at speeds unknown to even Sanic the Porcupine."

    "The loverbirds order: Bass frowns at the prices - "
    charBass "40 cents for bottled water! Disgusting!"
    "- and [charGfKaren] frowns at the menu options."
    
    show love_b_bored at middle
    
    charGfKaren "They don't even have non-salt options. Disgusting!"
    
    hide love_b_bored
   
    "Dinner comes and goes. It tastes as good as Bass (barely) paid."
    
    show love_b_normal_thinking at middle
    
    charGfKaren "That bacon tasted so raw I could hear it mooing."
    
    hide love_b_normal_thinking
    
    "Bass does not have the heart to tell him it's pork bacon...pre-cooked."

    "He should probably avenge his date regardless."

    charSweater "Ruin the staff's day. Do it. They deserves it."

    menu:
        "Trip the incoming waiter.":
            jump dateObnoxious_choice02_Trip

        "Ask for the manager.":
            $ nrGoodDateOptions += 1
            jump dateObnoxious_choice02_Manager


label dateObnoxious_choice02_Trip:
    "Bass trips the waiter once she goes to show them the bill (1000 cents! Outrageous!)."
    "The waiter spills the tray full of food on [charGfKaren]'s shoes."
    "Bass sees his past lives flash before his eyes."
    
    show love_b_bored at middle
    
    charGfKaren "I-  I-"
    
    hide love_b_bored
    
    charBass "Oh dear. Oh no. Oh no. I'm so sorry."
    charBass "...I don't have to pay for that, right?"

    "They get kicked out instantly."

    play sound "Intro/Intro Pt2 Bass/wrong buzzer 6268.mp3"

label dateObnoxious_choice02_Manager:

    charBass "I'd like to call the manager, please."
    
    show love_b_happy at middle
    
    charGfKaren "You tell 'em, babe!"

    "The manager shows up, eventually. She is a woman almost twice Bass' size, and thrice as muscly."
   
    hide love_b_happy
    show love_b_normal_thinking at middle
   
    charGfKaren "..."
    charBass "..."
   
    hide love_b_normal_thinking
    
    "They quietly pay the bill and leave."

    play sound "Shared Audio Themes and Leitmotifs/ping-82822.mp3"

    jump dateObnoxious_choice02_Done
    

label dateObnoxious_choice02_Done:
    scene bg_restaurant_outside
    show love_b_normal at middle
    
    charGfKaren "Well. That was that."
    
    hide love_b_normal
    scene bg_sweetdrop
    with fastDissolve
    
    "They end up going for a walk, pausing near the local Sweet Drop supermarket."
    
    show love_b_normal_thinking at middle
    
    charGfKaren "What now?"
    
    hide love_b_normal_thinking
    
    charSweater "Let's finish this date with a bang, shall we?"
    
    menu:
        "Leave a -5 stars Welp review...together.":
            $ nrGoodDateOptions += 1
            jump dateObnoxious_choice03_Review

        "Go for a kiss":
            jump dateObnoxious_choice03_Kiss

label dateObnoxious_choice03_Review:
    show love_b_happy_evil at middle
    
    charGfKaren "I thought you'd never ask!"
    
    hide love_b_happy_evil
    
    "Their joint disregard for workers' rights helps them write such a poor review even the Definetly-Not-Haunted-Sweater cringes."
    "The restaurant is to close the very next day."
    "The staff hires a hitman for the couple as soon as they get the notice."

    play sound "Shared Audio Themes and Leitmotifs/ping-82822.mp3"

    jump dateObnoxious_choice03_Done

label dateObnoxious_choice03_Kiss:
    show love_b_normal at middle
    
    "You close in on each other."
    "Closer...."
    
    hide love_b_normal
    show love_b_happy at middle
    
    "And closer..."
    
    hide love_b_happy
    show love_b_bored at middle
    
    "Until [charGfKaren] pushes you back."
    
    charGfKaren "You wish! Dude...we are SO not there yet."
    
    hide love_b_bored

    play sound "Intro/Intro Pt2 Bass/wrong buzzer 6268.mp3"
    
    jump dateObnoxious_choice03_Done


label dateObnoxious_choice03_Done:
    if nrGoodDateOptions > minGoodDateOptions:
        $ datedObnoxious = True
        $ currentGfriend = charGfKaren
        jump endingDateDisappears

    if nrGoodDateOptions <= minGoodDateOptions:
        jump endingRejected


##### ENDINGS #####

label endingEvil:
    $ endingId = "Evil"

    play sound "Endings/Evil/chaosmp3-14692.mp3"
    scene bg_evil_end_world
    with slowDissolve

    
    "The rumor about cards and banks goes beyond what Bass could’ve imagined."
    "The banks are mysteriously drained of their assets. They all file for bankruptcy."
    "People start rioting. They turn on each other. Crucial means of communication are lost as cell towers go out."
    "There’s blood in the streets. Planes start dropping like flies. "
    "There are fires everywhere. This causes the Earth to heat up so significantly it speeds up the climate crisis. The ground begins to physically boil."
    
    play sound "Endings/Love Yourself/explosion-42132 (1).mp3"
    scene bg_explosion
    with slowDissolve
    
    "The Earth was literally shaken to its core. It’s too much. In one instant, it’s all gone."

    
    scene bg_fog
    with slowishDissolve
    
    "Atmosphere popped. Thousands of years of existence sprinkled throughout the cosmos as if it were mere decoration."
    
    show main_menu
    
    "And the only proof any of it ever mattered...is a sweater."
    hide main_menu
    jump game_end


label endingBaddie:
    $ endingId = "Baddie"

    
    scene bg_fog
    with fastDissolve

    show bass_covered_croptop at middle

    play sound "Endings/Baddie/crowd-screaming-6850 (mp3cut.net).mp3"

    "Bass blows up overnight." 
    "People just can’t get enough of him. He’s on the cover of every magazine still in print and his name is on everybody’s lips."
    "Plastic surgeons are booked for months on end with people desperate to recreate his juicy lips."
    
    hide bass_covered_croptop
    show cg_apology video

    play sound "Endings/Baddie/apocalypse-128378.mp3"
    
    "He’s uncancelable. When he sits down in a gray hoodie, fake tears bottle in hand, and PR statement just off screen the internet forgives their favorite white man."
    "Youtube has to beef up their website just to handle the amount of traffic he generates."
    "He’s unstoppable."
    jump game_end


label endingDateDisappears:
    $ endingId = "Date Disappears"

    scene bg_fog
    with fastDissolve

    currentGfriend "So. It's cold...ish."
    currentGfriend "You know what a good boyfriend does to help his date when it's cold."

    "[currentGfriend.name] looks pointedly at the single piece of clothing Bass is wearing."

    charBass "You want my...sweater?"
    charBass "You mean my precious D.Sebastian long lost now found hot crop top?!"
    charBass "But, [currentGfriend.name], it's all I have!"

    "Bass' date giggles. It sounds slightly deranged."

    "Bass gives his date the D.Sebastian long lost now found hot crop top." 
    "Unfortunately, he truly does have nothing else on him - and finds himself completely naked."

    "He's moderately okay with this."

    "Bass looks at his date." 
    "A bright light surrounds the sweater, nearly blinding him."
    "His date doesn't seem to notice."

    charBass "Hey, are you okay?"

    "[currentGfriend.name] stares -"

    currentGfriend "Huh, I guess the carpet does match the dra - aaaaaaaaaaaaaaaaaaaaaaaapes!"

    "- and disappears in a flash, taking the D.Sebastian long lost now found hot crop top along, leaving only the faint stench of nutmeg behind."

    charBass "........"

    charBass "............................."

    charBass "This is what I get for giving people things."
    charBass "No love, and no wearable historical artifacts I had to pay customs for."
    charBass "I'm going back to bed. At least my D.Sebastian poster won't disappear on me."

    if datedEvil and datedObnoxious:
        jump endingLoveYourself
 
    "Bass goes home to wallow in peace. He cries himself to sleep and wonders if he should try again."

    charBass "Maybe in another life..."

    jump game_end


label endingLoveYourself:
    $ endingId = "Love Yourself"
    
    scene bg_lisboa

    play sound "Endings/Love Yourself/dark-piano-more-on-spotify-bruno-magic-152569 (mp3cut.net) (1).mp3"
    
    " Bass, naked once more on the cold cobbled streets, begins to head home, while avoiding the gaze of the drunk men in sad beige trousers."
    scene bg_bass_house
    
    "Once at home, Bass gazed once more upon his precious poster."

    charBass "Oh, why can’t I be hot and sexy like you… Your luscious lips, your creamy, inbred skin…"
    charBass "*sigh* How many ladies must you have pulled in your hay day. Why can’t I just be you!"


    "Once more, our dear Bass cried himself to sleep. However, in the next morning, an even worse surprise awaited him."
    
    scene bg_bass_house

    "On that Friday morning, the mailman appeared for the first time that week. Bass believed it was his treasured sweater."
    "But alas, his sweater had been kidnapped by a nefarious being: the post office!"

    charBass "What!? What do you mean?! Why do I have to pay 60 euros for MY sweater?!"

    charMail "It’s the customs fee. Nothin’ you can do about it."

    charBass "Why do I have to go to Leiria!?"

    charMail "Look, weird-looking kiddo, I just deliver the mail. Sort it out yourself."

    charBass "*sigh* Should I go to Leiria and pay this robbery of a fee or just…stay home and be depressed?"

    menu:
        "Stay home and be depressed":
            jump endingLoveYourself_choice01_StayHomeYes
        
        "Go to Leiria":
            jump endingLoveYourself_choice01_Done

        "Go to Leiria (dramatically)":
            play sound "Endings/Love Yourself/risk-136788 (1) (mp3cut.net) (1).mp3"
            jump endingLoveYourself_choice01_Done


label  endingLoveYourself_choice01_StayHomeYes:
    "Bass grabbed his things and embarked on the treacherous path to Leiria!"

    charBass "What? No! I said I want to stay home! *snif* At least my Seby's poster won’t hurt my feelings…"

    "C’mon dude. Don’t be like that."
    "You almost considered spending money on that sweater. That’s like, a lot of thoughts."

    charBass "I. Want. To. Stay. Home."

    "Well, too bad. You’re going to Leiria and you will like it!"
    "If you don’t go, I’ll burn your dear Seby and all of his incestuous beauty!"

    charBass "Noo! Please, anything but that. Fine… I’ll go."
    
    jump endingLoveYourself_choice01_Done


label endingLoveYourself_choice01_Done:
    

    play sound "Endings/Love Yourself/epic-travel-on-celtic-roads-version-60s-10819 (1).mp3"
   
    "Although the train would be much, much, much faster, Bass decided he didn't want to spend a single penny more than he had to."
    "He decided to send himself to Leiria by mail."
    "This choice led to a journey of multiple years, sealed inside a tiny box, but Bass persevered."
    
    play sound "Endings/Love Yourself/PORTAL (1).mp3"
    scene bg_portal
    with fastDissolve
    
    "Upon arrival, Bass noticed a small detail."
    "Leiria wasn't real. All this time, it had been a wormhole! "
    
    
    charBass " Oooh, my head…Where…where am I?"

    
    play sound "Endings/Love Yourself/truckrunningwav-14613 (1).mp3"

    charBass "Something is wrong…Am I dead?"

    "Bass was in fact, not dead, just a bit groggy from the journey."
    
    scene bg_mss
    with fastDissolve

    "All along, Leiria had been a secret portal to Morocco."
    "He was now in a strange van, somewhere in this foreign country."
    "Somewhere…familiar."

    charBass "Nuh uh. I’m not doing this. I just want my sweater and…love."
    
   
    play sound "Endings/Love Yourself/oh-no-the-car-exploded-10632.mp3"

    charSeb "Ahhh!"
    
    scene bg_explosion
    
    play sound "Shared Audio Themes and Leitmotifs/funny-eastern-short-music-vlog-background-hip-hop-beat-29-sec-148905 (1) (1).mp3"

    scene bg_mss
    

    charSeb "O.M.G. Did that thing just like, explode?"
    
    show sebby_uncovered at middle
    
    charSeb "Who? Get off me, filthy peasant! *cough* I mean, filthy similar social class man. "
    
    hide sebby_uncovered
    
    charBass "Everything hurts… Wait. Is this… the post office!"
    charBass "Hey, you. Give me my sweater."
    
    show sebby_uncovered at middle
    
    charSeb "*sigh* Another one looking for some lost package…"
    charSeb "When will anyone look for good old Seby *sob*."

    hide sebby_uncovered

    charBass "It’s not some lost package! It’s a priceless arti… Did…did you just say Seby?"
    
    show sebby_uncovered at middle

    charSeb "I got separated from my besties when I came here, and they never came back for meeee…"
    charSeb "I had to piss…"
    charSeb "And…they all thought I was bleeding to death, because I had royal coloured pee. Now I’m stuck here… forever."

    hide sebby_uncovered

    charBass "Are you..."

    menu:
        "…the Seby?":
            jump endingLoveYourself_choice02_Done

        "…D. Sebastian the first?":
            jump endingLoveYourself_choice02_Done
        
        "…His incestuous grace in person?":
            jump endingLoveYourself_choice02_Done

label endingLoveYourself_choice02_Done:
    show sebby_uncovered at middle
    
    charSeb "Don’t call me that… those days…are over."
    charSeb "My pee isn't even red anymore… What king I am…"

    hide sebby_uncovered
    show bass_censored_ at middle

    charBass "I’m your biggest fan!!!"
    charBass "Please, please…Give me an autograph or I die."

    hide bass_censored_
    show sebby_uncovered at middle

    charSeb "C’mon then. Die."
    charSeb "I double dare you."
    charSeb "Do you know who I am? Well, was…"
    charSeb "I bet they put my stupid little cousin on the throne, didn't they. Pff, can’t even do a manicure on his own."

    hide sebby_uncovered
    show bass_censored_ at middle

    charBass "Uh, about that… he kinda died…with you. The Spaniards took it…"

    hide bass_censored_
    show sebby_uncovered at middle

    charSeb "What? Double Uncle - slash - Cousin Phi Phi? He’s like a… 4 at best. He kinda looks like a thumb."
    charSeb "Oh, then I have nothing to worry about. He can’t reach dearest Seby’s heels. Old man liked slaying people too much, like, literally."

    hide sebby_uncovered
    show bass_censored_ at middle

    charBass "How are you alive? You should be-"

    hide bass_censored_
    show sebby_uncovered at middle

    charSeb "Like, chop, chop, chop, chop. If the french revolution had happened back then. They would’ve loooved him."
    charSeb "Like, forget Robespierre, it would have been Thumbpierre. Then he would have been a queen."

    hide sebby_uncovered
    show bass_censored_ at middle

    charBass "But, how-"

    hide bass_censored_
    show sebby_uncovered at middle

    play sound "Endings/Love Yourself/dark-piano-more-on-spotify-bruno-magic-152569 (mp3cut.net) (1).mp3"

    charSeb "But he wasn't one, and sadly, neither was I."
    charSeb "I’m stuck here, eternally. There’s nothing left to slaaaay."
    charSeb "Wait. Omg, don’t tell me I gave the kingdom to…the spanish?"
    charSeb "Oh noo, my unsoiled reputation as the straigh…greatest king ever…is ruined."
    charSeb "Am I not remembered as the best King of Portugal?"

    hide sebby_uncovered
    show bass_censored_ at middle

    charBass "Uh, you’re not remembered as the worst…maybe."

    hide bass_censored_
    show sebby_uncovered at middle
    
    charSeb "Nooooo! My incestuous kingdom! My great realm of hotness.I’m so stupid. *sob*"

    hide sebby_uncovered
    show bass_censored_ at middle

    charBass "Hey, what are you saying? To me you’re the greatest king to have ever lived!"
    charBass "You’re not stupid, you’re brave. Who would march into cannons like you did?"
    charBass "Also, you’re the only one who ended a dynasty with style."

    hide bass_censored_
    show sebby_uncovered at middle

    play sound "Endings/Love Yourself/romantic-episode-139730 (1).mp3"

    charSeb "You’re just lying to make me feel better. It’s not worth it…"

    hide sebby_uncovered
    show bass_censored_blush at middle

    charBass "You deserve love. Do you know why?"
    charBass "Because I love you. With all my heart."
    charBass "I would… pay for your lunch! (if it’s less than 1.50 euros)."
    charBass "Oh Sebastian, you are the love of my life!"

    hide bass_censored_blush
    show sebby_uncovered_blush at middle
    
    charSeb "Do you…do you mean that?"

    hide sebby_uncovered_blush
    show bass_censored_blush at middle

    charBass "Of course. You are m-m-my world. I don’t need a sweater when I can have you!"

    hide bass_censored_blush
    show sebby_uncovered_blush at middle

    charSeb "You should put some clothes on though. Or you’ll have a nasty burn where my divine kind power does not reach. But the sun will."
    
    hide sebby_uncovered_blush
    play sound "Endings/Love Yourself/explosion_01-6225 (1).mp3"

    jump game_end_nice


label endingRejected:
    $ endingId = "Rejected"
    scene bg_restaurant_outside
    with fastDissolve

    play sound "Endings/Rejected/the-wait-138639 (2).mp3"

    "As the date kept getting longer and longer, Bass’ date began moving frantically. Desperately looking around, searching for something to help them escape."

    charBass "Ohh did the date food also touch your innards? You look like you’re about to produce a very nasty surprise."
    charBass "Well, why don’t you go relieve yourself, while I prepare an even bigger surprise for you."

    currentGfriend "YES! Bathroom! That 's what I need!"

    charBass "Don’t you dare use the ones that you have to pay for!"
    
    scene bg_sweetdrop
    with fastDissolve
    
    "Awaiting the return of his date, Bass had spent the last 5 hours behind the local Sweet Drop supermarket."
    "As the poor soulless employees left, they stared with pity into the eyes of someone who had even less soul. "
    "Heartbroken, Bass decided to become one with the Sweet Drop."
    play sound "Endings/Rejected/evil-mouth-ensemble-78778 (2).mp3"
    
    scene bg_sweetdrop_sacrifice
    with fastDissolve
    
    
   
    "Even to this day, the employees perform paganic rituals around all that remains of him."
    "A simple sweater."

    jump game_end




label game_end_nice:
    scene bg_explosion_heart
    with fastDissolve

    "What a masterful show of love!"
    "Still. Maybe you'd like to try a different route? \n(Ending: [endingId])\nTHANKS FOR PLAYING!!! <3 )"

    menu:
        "End Game":
            jump end

        "Try your hand at love once more":
            jump fake_start



label game_end:
    "Oh dear. Maybe you'd like to try and get a happier ending? \n(Ending: [endingId])\n(THANKS FOR PLAYING!)"

    menu:
        "End Game":
            jump end

        "Try again":
            jump fake_start



label end:
    # This ends the game.

    return
