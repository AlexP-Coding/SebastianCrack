# The script of the game goes in this file.

```
To add:
- Music
- Sound
- Timing
- Text color and size
```
# Text comment

# CHARACTER COLORS
define bgCharColorA = "#1d53a5"
define bgCharColorB = "#aaaaaa"

# TEXT COLORS
define baddieColor = "#ff00ea"
define deathColor = "#ca0a0a"

$ nrBaddieChoices = 0
$ nrEvilChoices = 0
$ nrObnoxiousChoices = 0

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
define charGfKaren = Character("Kar Enn", color = "#ffcccc")
define charSweater = Character("Wooly whisper", size=15, color="#ca0a0a")

# BackgroundCharacters
define charArmy = Character("Army", color = bgCharColorA, what_size=34)
define charBMom = Character("Bass’s Mom Who Is Visiting", color = bgCharColorA)
define charBDad = Character("Bass’s Dad Who Is Visiting", color = bgCharColorB)
define charNews = Character("Journalist", color=bgCharColorA)
define charMail = Character("Maiman", color=bgCharColorA)

define currentGfriend = charGfPsycho


# SCRIPT 

# The game starts here.
label start:
    $ nrBaddieChoices = 0
    $ nrEvilChoices = 0
    $ nrObnoxiousChoices = 0


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    ##### INTRO SEB #####

    "A long time ago, far far deep into the lands of Morocco a portuguese king was acting like a teenage brat."
    
    "This king was 24 years old."

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

    "In 1548, Sebastian and his army (including his 10yo cousin) marched into a really complicated and stupid battle."

    charSeb "Let’s go brave warriors! This crusade-like war will totally work out in our favor, like all the other crusades did!"

    "..."

    charSeb "We will {=slayBig}SLAAAAAAAY{/slayBig}… {w=1.2}{space=15} Our enemies!"

    charArmy "Chargeee! Ahhh!"

    "However, Sebastian did not {=slay}slay{/slay}, he was {=death}slayed{/death}…"
    "Probably."

    "As the shores in Portugal filled with fog, and the population prayed for Sebastian’s return, his beautiful garments were lost forever..."

    "{cps=2}Until…{/cps}"


    ##### INTRO BASS #####

    charBass "Holy monarchy, is that the long lost 1548 D.Sebastian hot crop top?"

    "Bass has been tenderly stealing D.Sebastian-related artifacts from museums all his life"
    "They’re one of his few possessions, beyond his ten-dollar Nokia phone, his novelty D.Sebastian poster, and his bathtub-slash-toilet-slash-bed."

    charBass "I can’t believe it! I don’t even have to incapacitate a guard for this one!"

    menu:
        "Buy the sweater":
            jump pt1_choice01_BuySweaterYes

        "Heck yeah, buy the sweater":
            jump pt1_choice01_BuySweaterYes

label pt1_choice01_BuySweaterYes:
    $ flag_BuySweater = True
    jump pt1_choice01_Done
        

label pt1_choice01_Done:
    
    "Bass buys the sweater. He receives five cents in his bank account."

    charBass "Whoop!"

    "The package then gets held hostage in customs."
    "He’s forced to pay up a whole six dollars."

    charBass "Son of Aviz!"

    "After a not-so-grueling two-hour-turned-twelve-hour trip, the hot crop top not-so-soon reaches Bass’ stingy hands."

    charBass "Ok, let’s see how I look."

    charBass "…"
    charBass_loud "{=slayBig}Perfect!{/slay}"
    charBass "Hot as an inbred king. I don't even need pants!"

    charBass "And it came just at the right time, too.\nI bet my date tonight will love it!"

    charBass "I’d better get ready.\nI’ll go out and see if the local park has some flowers I can…er…borrow."

    charBass "Should I say goodbye to my parents?"

    menu:
        "Say goodbye":
            jump pt1_choice02_ByeParentsYes

        "Do not":
            jump pt1_choice02_ByeParentsNo


# CHOICE: Say goodbye to visiting parents
label pt1_choice02_ByeParentsYes:
    $ flag_sayBye = True

    charBass "Bye, world-renowned geneticists mom-and-dad!"

    charBMom "…Why does he always have to say it like that?"

    charBDad "Weird-ass kid."

    jump pt1_choice02_Done


label pt1_choice02_ByeParentsNo:
    $ flag_sayBye = False

    charBass "Nah." 
    charBass "They’re on thin ice after cloning my dead dog during their crazy scientist phase."

    jump pt1_choice02_Done


# CHOICE END
label pt1_choice02_Done:
    charBass "The guys at Wishy-Washy are insane…I'll bet this sweater-top isn't even THAT haunted."


    ##### CHOICES #####

    "As Bass leaves his luxurious condo, (no, there’s no sarcasm there, this is what counts as luxury in Lisbon in 2023 if you’re a local) he is greeted with only the freshest air the city can provide."

    charBass "Mmm…I love the smell of piss in the morning."

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
            jump pt3_choice01_DontHelpEvil

        "Ignore them.":
            jump pt3_choice01_DontHelpObnoxious

        "Redirect them to somewhere more fun.":
            jump pt3_choice01_DontHelpBaddie

label pt3_choice01_DontHelpEvil:
    $ nrBaddieChoices += 1

    "Bass isn’t in the mood to play tour guide so he directs them in the opposite direction, up a long steep cobblestone street."
    "The tourists smile and thank him."
    "While climbing the street, one of them slips on the worn stones, tumbling onto the road."
    "A tram happens to be passing by and murders the man instantly." 
    "This leads to the further decay of the relations between olive oil europe and butter europe. The UN has to get involved so the situation doesn’t escalate."

    jump pt3_choice01_Done


label pt3_choice01_DontHelpObnoxious:
    $ nrObnoxiousChoices += 1

    "Bass pulls out his phone, flipping it on queue. The mountain of charms just about misses their lobster red faces."
    "He cosplays as a productive member of society."

    charBass "Who the fuck dares to call me when I’m so busy?"

    jump pt3_choice01_Done

label pt3_choice01_DontHelpBaddie:
    $ nrBaddieChoices += 1

    "Bass greets the strangers with a cheshire grin, looking at the destination on their phone."
    "He scoffs, convinces them it’s not worth their time. Instead, he suggests somewhere better, more fun he says."
    "The tourists thank him for his time and help and go down a shady street. They are later mugged and the loot is redistributed among locals."
    "Sunscreen is nowhere to be found among the treasure."

    jump pt3_choice01_Done

label pt3_choice01_Done:
    "Bass continues on. He’s on a mission of the utmost importance...For iced coffee."

    "On his way, his phone dings twice."
    "Both of his dates text him. Who should be blessed with his attention?"

    menu:
        "Text [charGfPsycho.name].":
            jump pt3_choice02_TextDateEvil

        "Text [charGfKaren.name].":
            jump pt3_choice02_TextDateObnoxious
        
        "Block both.":
            jump pt3_choice02_TextDateBaddie


label pt3_choice02_TextDateEvil:
    $ nrEvilChoices += 1
    charBass "(text) Can’t wait to kick a puppy with u l8r 2nite. <3 u."
    jump pt3_choice02_Done

label pt3_choice02_TextDateObnoxious:
    $ nrObnoxiousChoices += 1
    charBass "(text) I’ve been thinking about you all day." 
    charBass "(text) The way you verbally abuse people who earn minimum wage and nitpick everything…it just gets me going."
    jump pt3_choice02_Done

label pt3_choice02_TextDateBaddie:
    $ nrBaddieChoices += 1
    "Bass doesn't have time for this. There are more important things to life than a romantic partner he can’t use for clout." 
    "He blocks both dates before deleting their contacts. C U NVR."
    jump pt3_choice02_Done


label pt3_choice02_Done:

    "Bass arrives at the coffee shop. The place is packed, the counter and cashier blocked by an endless sea of people."
    "Bass rolls his eyes. What does a guy have to do to get a cup of coffee?"
    charSweater "You know what to do…"

    menu:
        "Call in a bomb threat.":
            jump pt3_choice03_CoffeeShopEvil

        "Steal it.":
            jump pt3_choice03_CoffeeShopObnoxious

        "Call the tabloids.":
            jump pt3_choice03_CoffeeShopBaddie

label pt3_choice03_CoffeeShopEvil:
    $ nrEvilChoices +=1
    "Bass sneaks away to the bathroom, logs onto his burner account and tweets anonymously about a suspicious looking man in jorts sipping his drink by the window."
    "Anyone just hanging out at a coffee shop without a single Instagram tab open is reason enough for suspicion."
    
    "He waits two minutes before making the actual call. Bass hears the symphony of screams and gas and people being trampled."
    "When the coast is clear he skips over to the counter and collects his rightful, free and well earned cup of coffee. "

    jump pt3_choice03_Done

label pt3_choice03_CoffeeShopObnoxious:
    $ nrObnoxiousChoices +=1
    "Bass pushes past the crowd, elbowing people left and right."
    "The barista starts to call out the next name but doesn’t finish before Bass slips it from his hand and makes a run for it."
    "The barista does crossfit in his free time though: he jumps over the counter but underestimates the length of the jump."
    "That, coupled with a few missed leg days, makes him hit his ankle on the counter on the way down."
    "People gather around him, too distracted by the scene to go after the iced coffee thief."
    "The corporation worth millions doesn’t offer him health insurance. Poor guy."
    jump pt3_choice03_Done

label pt3_choice03_CoffeeShopBaddie:
    $ nrBaddieChoices +=1
    "A swarm of amateur journalists descend upon the small shop, shoving microphones in the baristas’ faces."

    charNews "Is it true your oat milk is just regular milk with oats mixed in?"

    "Using his contacts, several Instagram stories and tweets Bass had successfully emptied the place of customers."
    "While the underpaid workers are bombarded and distracted, Bass goes behind the counter to make his own personalized and perfect drink…"
    "He also slips a few cartons of milk into his tote bag for good measure."

    jump pt3_choice03_Done


label pt3_choice03_Done:
    "It’s almost time for his date and he’s starting to get nervous."
    "Bass stands outside the restaurant. What should he do?"

    charSweater "Do it. You know you want to."

    menu:
        "Start a rumor.":
            jump pt3_choice04_RestaurantEvil

        "Cyber stalk the restaurant staff.":
            jump pt3_choice04_RestaurantObnoxious

        "Ghost them.":
            jump pt3_choice04_RestaurantBaddie


label pt3_choice04_RestaurantEvil:
    $ nrEvilChoices +=1
    "Bass starts a rumour about banks being shady in relation to credit and debit cards, forcing them to withhold those services for some hours while they investigate."
    "Now when the bill comes Bass can say he doesn’t carry cash and his date will be forced to pay for everything."
    jump pt3_choice04_Done

label pt3_choice04_RestaurantObnoxious:
    $ nrObnoxiousChoices +=1
    "Bass stalks every member of staff as he watches them rush through the restaurant on their shifts."
    "One by one. Tinder. Linkedin. Tumblr. That one Youtube channel they made when they were a teenager."
    "Perfect. Now he had everything he needed to terrorize the staff and impress his date."
    jump pt3_choice04_Done

label pt3_choice04_RestaurantBaddie:
    $ nrBaddieChoices +=1
    "Bass ghosts both of his dates and assumes his true destiny."
    "In order to become the biggest baddie youtuber there ever was, he needs to make some big sacrifices…like ghosting the psychopath groupie and karen."
    "Woe is he. Such acts of martyrdom truly deserve recognition…from the algorithm."
    jump endingBaddie


label pt3_choice04_Done:
    jump temp_ending



##### ENDINGS #####

label endingEvil:
    "The rumor about cards and banks goes beyond what Bass could’ve imagined."
    "The banks are mysteriously drained of their assets. They all file for bankruptcy."
    "People start rioting. They turn on each other. Crucial means of communication are lost as cell towers go out."
    "There’s blood in the streets. Planes start dropping like flies. "
    "There are fires everywhere. This causes the Earth to heat up so significantly it speeds up the climate crisis. The ground begins to physically boil."
    "The Earth was literally shaken to its core. It’s too much. In one instant, it’s all gone."
    "Atmosphere popped. Thousands of years of existence sprinkled throughout the cosmos as if it were mere decoration."
    "And the only proof any of it ever mattered...is a sweater."
    jump temp_ending


label endingBaddie:
    "Bass blows up overnight." 
    "People just can’t get enough of him. He’s on the cover of every magazine still in print and his name is on everybody’s lips."
    "Plastic surgeons are booked for months on end with people desperate to recreate his juicy lips."
    "He’s uncancelable. When he sits down in a gray hoodie, fake tears bottle in hand, and PR statement just off screen the internet forgives their favorite white man."
    "Youtube has to beef up their website just to handle the amount of traffic he generates."
    "He’s unstoppable."
    jump temp_ending


label endingDateDisappears:
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

    jump endingDateDisappearsTwo

label endingDateDisappearsTwo:
    "Bass goes home to wallow in peace. He cries himself to sleep and wonders if he should try again."

    charBass "Maybe in another life..."

    jump temp_ending


label endingLoveYourself:
    " Bass, naked once more on the cold cobbled streets, begins to head home, while avoiding the gaze of the drunk men in sad beige trousers."
    "Once at home, Bass gazed once more upon his precious poster."

    charBass "Oh, why can’t I be hot and sexy like you… Your luscious lips, your creamy, inbred skin…"
    charBass "*sigh* How many ladies must you have pulled in your hay day. Why can’t I just be you!"

    "Once more, our dear Bass cried himself to sleep. However, in the next morning, an even worse surprise awaited him."
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
    "Although the train would be much, much, much faster, Bass decided he didn't want to spend a single penny more than he had to."
    "He decided to send himself to Leiria by mail."
    "This choice led to a journey of multiple years, sealed inside a tiny box, but Bass persevered."

    "Upon arrival, Bass noticed a small detail."
    "Leiria wasn't real. All this time, it had been a wormhole! "

    charBass " Oooh, my head…Where…where am I?"

    charBass "Something is wrong…Am I dead?"

    "Bass was in fact, not dead, just a bit groggy from the journey."
    "All along, Leiria had been a secret portal to Morocco."
    "He was now in a strange van, somewhere in this foreign country."
    "Somewhere…familiar."

    charBass "Nuh uh. I’m not doing this. I just want my sweater and…love."

    charSeb "Ahhh!"
    charSeb "O.M.G. Did that thing just like, explode?"
    charSeb "Who? Get off me, filthy peasant! *cough* I mean, filthy similar social class man. "

    charBass "Everything hurts… Wait. Is this… the post office!"
    charBass "Hey, you. Give me my sweater."

    charSeb "*sigh* Another one looking for some lost package…"
    charSeb "When will anyone look for good old Seby *sob*."

    charBass "It’s not some lost package! It’s a priceless arti… Did…did you just say Seby?"

    charSeb "I got separated from my besties when I came here, and they never came back for meeee…"
    charSeb "I had to piss…"
    charSeb "And…they all thought I was bleeding to death, because I had royal coloured pee. Now I’m stuck here… forever."

    charBass "Are you..."

    menu:
        "…the Seby?":
            jump endingLoveYourself_choice02_Done

        "…D. Sebastian the first?":
            jump endingLoveYourself_choice02_Done
        
        "…His incestuous grace in person?":
            jump endingLoveYourself_choice02_Done

label endingLoveYourself_choice02_Done:
    charSeb "Don’t call me that… those days…are over."
    charSeb "My pee isn't even red anymore… What king I am…"

    charBass "I’m your biggest fan!!!"
    charBass "Please, please…Give me an autograph or I die."

    charSeb "C’mon then. Die."
    charSeb "I double dare you."
    charSeb "Do you know who I am? Well, was…"
    charSeb "I bet they put my stupid little cousin on the throne, didn't they. Pff, can’t even do a manicure on his own."

    charBass "Uh, about that… he kinda died…with you. The Spaniards took it…"

    charSeb "What? Double Uncle - slash - Cousin Phi Phi? He’s like a… 4 at best. He kinda looks like a thumb."
    charSeb "Oh, then I have nothing to worry about. He can’t reach dearest Seby’s heels. Old man liked slaying people too much, like, literally."

    charBass "How are you alive? You should be-"

    charSeb "Like, chop, chop, chop, chop. If the french revolution had happened back then. They would’ve loooved him."
    charSeb "Like, forget Robespierre, it would have been Thumbpierre. Then he would have been a queen."

    charBass "But, how-"

    charSeb "But he wasn't one, and sadly, neither was I."
    charSeb "I’m stuck here, eternally. There’s nothing left to slaaaay."
    charSeb "Wait. Omg, don’t tell me I gave the kingdom to…the spanish?"
    charSeb "Oh noo, my unsoiled reputation as the straigh…greatest king ever…is ruined."
    charSeb "Am I not remembered as the best King of Portugal?"

    charBass "Uh, you’re not remembered as the worst…maybe."

    charSeb "Nooooo! My incestuous kingdom! My great realm of hotness.I’m so stupid. *sob*"

    charBass "Hey, what are you saying? To me you’re the greatest king to have ever lived!"
    charBass "You’re not stupid, you’re brave. Who would march into cannons like you did?"
    charBass "Also, you’re the only one who ended a dynasty with style."

    charSeb "You’re just lying to make me feel better. It’s not worth it…"

    charBass "You deserve love. Do you know why?"
    charBass "Because I love you. With all my heart."
    charBass "I would… pay for your lunch! (if it’s less than 1.50 euros)."
    charBass "Oh Sebastian, you are the love of my life!"

    charSeb "Do you…do you mean that?"

    charBass "Of course. You are m-m-my world. I don’t need a sweater when I can have you!"

    charSeb "You should put some clothes one though. Or you’ll have a nasty burn where my divine kind power does not reach. But the sun will."

    jump temp_ending







label temp_ending:
    "Oh dear. Maybe you'd like to try and give him a happier ending? (THANKS FOR PLAYING!)"


    # This ends the game.

    return
