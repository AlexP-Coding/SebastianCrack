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

# BackgroundCharacters
define charArmy = Character("Army", color = bgCharColorA, what_size=34)
define charBMom = Character("Bass’s Mom Who Is Visiting", color = bgCharColorA)
define charBDad = Character("Bass’s Dad Who Is Visiting", color = bgCharColorB)


# SCRIPT 

# The game starts here.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

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

    "GAME END. FOR NOW..."




    # This ends the game.

    return
