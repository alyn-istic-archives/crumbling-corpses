# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Jason")
define dis = Dissolve(0.1)
define v = Character("Valerie")
define yn = Character("Georgina")
define n1 = Character("NPC 1")
define n2 = Character("NPC 2")
define n3 = Character("NPC 3")
define z = Character("Zombie???")

image fridgean:
    "images/f1.png"
    pause.5
    "images/f2.png"
    pause.5
    "images/f3.png"
    pause.5

image chomp:
    "images/b1.png"
    pause.8
    "images/b2.png"
    pause.6
    "images/b3.png"
    pause.3
    "images/b4.png"
    pause.7
    "images/b5.png"
    pause.3
    "images/b6.png"
    pause.2

transform jump:
    pause .15
    yoffset 0
    easein .15 yoffset -10
    easeout .15 yoffset 0
    easein .15 yoffset -2
    easeout .15 yoffset 0
    yoffset 0

transform shake:
    linear 0.175 xoffset -5
    linear 0.175 xoffset +0
    linear 0.175 yoffset -5
    linear 0.175 yoffset +0
    repeat

default preferences.text_cps = 45
default preferences.afm_enable = False 

# The game starts here.

label start:
    scene bg bunker with Dissolve(0.5)

    # These display lines of dialogue.
    play sound "audio/we're cuit.mp3"
    "My name's -REDACTED-, and we're {b}so{/b} cooked."
    show j_closed with dis
    pause.01
    play sound "audio/jasonpmo.mp3"
    "And I hate Jason."
    show j_open with dis
    hide j_closed with dis
    j "Screw off."
    hide j_open with dis
    show j_closed with dis
    pause.025
    play sound "audio/jasoncallout.mp3"
    "See why I hate him?"
    hide j_closed with dis
    "It's been what... like a month into this whole 'living underground in a bunker' thing."
    "Would you believe how ordinary our lives were before things went south?"
    "And by south, I mean pretty bad considering... y'know... zombie apocalypse."
    play sound "audio/assholebunker.mp3"
    "Well, now, we're here. In this subpar bunker, surrounded by pretentious assholes and nosy rats."
    show j_closed with dis
    pause.025
    play sound "audio/jasonrat.mp3"
    "But Jason's really just both."
    
    "And it's my turn to make dinner, so I head to the fridge."
    "Out of hunger portable food."
    scene fridge with dis
    "what should I make?"
    menu:
        "a sandwich!!":
            jump fridge
        "soup.":
            jump fridge
        "pizzaaa":
            jump fridge
    label fridge:
        show fridgean with dis
        "Oh. {w=5}Hell. {w=5}Nah."
        play sound "audio/foodloss.mp3"
        "THERE'S NO FOOD." with vpunch
        play sound "audio/NOFOOD.mp3"
        "{cps=20}NOOOOOOOO." with pixellate
        scene fridge with dis
        "Valerie turns to me with clear disdain and confusion in her eyes for my sudden misery."
        show v_open with dis
        v "...{w} Are you okay?"
        show v_closed with dis
        hide v_open with dis
        yn "Of COURSE !!! {w} NOT, Valerie. {w} OBVIOUSLY."
        show v_open with dis
        hide v_closed with dis
        v "Damn, calm down."
        v "It is not that bad, I'm sure."
        play sound "audio/ITIS.mp3"
        "But it is."
        scene bg bunker with Dissolve(0.75)
        play sound "audio/oritwas.mp3"
        "Or it was."
        n1 "WE'RE OUT OF FOOD ???? NOOOOOO-"
        n2 "THIS CANNOT STAND WE NEED TO EATT"
        yn "I'M WELL AWARE AHHHH !!!"
        n3 "THAT'S IT, WE'RE INITIATING GREEN PROTOCOL"
        pause.1
        "WHAT."
        show trio with dis
        play sound "audio/wt.mp3"
        "what the."
        show imcooked with zoomin
        play sound "audio/wtf.mp3"
        "what the fuh."
        play sound "audio/ugly hoodie.mp3"
        "Yeah. {w} That's me. In the ugly hoodie right there."
        play sound "audio/food4surv.mp3"
        "I, OF ALL PEOPLE,{w} have been paired with Valerie to go for FOOD FOR SURVIVAL."
        "WORST OF ALL."
        pause.1
        show trio with zoomout
        play sound "audio/jasoncallout.mp3"
        "WITH JASON."
        "..."
    label explore:
        scene bunkergrowth with Dissolve(0.5)
        show v_closed at right with dis
        "And so I set forth into the perilous journey of scaling the bunker with Valerie."
        show j_closed at left with dis
        play sound "audio/jasoncallout.mp3"
        "...{w} and Jason."
        "..."
        hide j_closed
        show j_open at center
        show j_open at shake
        show z_open at left
        "{cps=80}{size=30}HOLY SHIT IS THAT A ZOMBIE-" with vpunch

        hide z_open
        show z_closed at left
        j "You guys see that, right..."
        hide j_open
        show j_closed at center
        show v_open at right
        v "...I do."
        hide v_open
        hide z_closed
        show z_open at left
        show v_closed at right
        yn "OH MY GOD KILL IT VRO PLEASE"
        hide j_closed
        show j_open
        j "WHO ME ??" with vpunch
        show j_closed
        hide j_open
        play sound "audio/jasoncallout.mp3"
        yn "YES YOU !! DID THEY NOT GIVE U A WEAPON OR SOMETHING?!"
        show j_open
        hide j_closed
        j "uh." with vpunch
        show j_closed
        hide j_open
        show v_open at right
        hide v_closed
        v "What do you mean 'uh', Jason?"
        pause.1
        v "I'll just do it myself."
        scene snipe with Dissolve(0.8)
        "With almost efficient speed, she drops into a quick stance, easily piercing through the zombie."
        "Oh my god.{w} That was...SO COOL !!!"
        j "SHOOT, GEORGINA, WATCH OUT!" with vpunch
        play sound "audio/hellnah.mp3"
        "hell nawh." with hpunch 
    label chomp:
        show chomp with dis
        yn "AHHHHHHHHHH !!!"
        j "GEORGINA SHUT UP YOU'RE ENDANGERING US !!"
        v "georgina, just hold on !!"
        j "she's DEAD valerie. LET HER DIE."
        j "we have MORE PRESSING ISSUES."
        z "grrrrr..."
        v "The horde, I know, I know."
        j "No thanks to someone."
        yn "IT HURTS HELP ME !! {w} HELP ME JASON!"
        play sound "audio/jasoncallout.mp3"
        "Pointedly ignoring me like a jackass, Jason turned to Valerie... I think?"
        j "I'll take the left hoard, you take the right. Damn it, I didn't want to fight."
        v "...So you knew how?"
        yn "DON'T LEAVE ME FOR DEAD OH MY GOD !!!!"
        "THE END? -  see part 2; DEAD AND DECAYED"   




        
        
        
        
    # This ends the game.