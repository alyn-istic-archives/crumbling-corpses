# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Jason")
define dis = Dissolve(0.1)
define v = Character("Valerie")
define yn = Character("me")
define n1 = Character("NPC 1")
define n2 = Character("NPC 2")
define n3 = Character("NPC 3")

image fridgean:
    "images/f1.png"
    pause.5
    "images/f2.png"
    pause.5
    "images/f3.png"
    pause.5

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

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    jump explore
    scene bg bunker with Dissolve(0.5)

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

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
        "THERE'S NO FOOD." with vpunch
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
        "But it is."
        scene bg bunker with Dissolve(0.75)
        "Or it was."
        n1 "WE'RE OUT OF FOOD ???? NOOOOOO-"
        n2 "THIS CANNOT STAND WE NEED TO EATT"
        yn "I'M WELL AWARE AHHHH !!!"
        n3 "THAT'S IT, WE'RE INITIATING GREEN PROTOCOL"
        pause.1
        "WHAT."
        play audio "audio/sum.mp3"
        show trio with dis
        "what the."
        show imcooked with zoomin
        "what the fuh."
        "Yeah. {w} That's me. In the ugly hoodie."
        "I, OF ALL PEOPLE,{w} have been paired with Valerie to go for FOOD FOR SURVIVAL."
        "WORST OF ALL."
        pause.1
        show trio with zoomout
        "WITH JASON."
        "..."
    label explore:
        scene bunkergrowth with Dissolve(0.5)
        show v_closed at right with dis
        "And so I set forth into the perilous journey of scaling the bunker with Valerie."
        show j_closed at left with dis
        "...{w} and Jason."
        "..."
        "HOLY SHIT IS THAT A ZOMBIE-" with vpunch
        hide j_closed
        show j_open at shake
        j "You guys see that, right..."
        show j_closed
        hide j_open
        show v_open at right
        v "...I do."
        hide v_open
        show v_closed
        yn "OH MY GOD KILL IT VRO PLEASE"
        hide j_closed
        show j_open
        j "WHO ME ??" with vpunch
        show j_closed
        hide j_open
        yn "YES YOU !! DID THEY NOT GIVE U A WEAPON OR SOMETHING?!"
        show j_open
        hide j_closed
        j "uh." with vpunch
        show j_closed
        hide j_open
        show v_open
        hide v_closed
        v "What do you mean 'uh', Jason?"
        pause.1
        v "I'll just do it myself."
        "With almost efficient speed, she drops into a quick stance, easily piercing through the zombie. "
        
        
        
        
    # This ends the game.

    return
