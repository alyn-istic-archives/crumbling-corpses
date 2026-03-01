# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Jason")
define dis = Dissolve(0.1)
define v = Character("Valerie")

image fridgean:
    "images/f1.png"
    pause.3
    "images/f2.png"
    pause.2
    "images/f3.png"
    pause.2

default preferences.text_cps = 45
default preferences.afm_enable = False 

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg bunker

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "I'm -REDACTED-, and we're so fucking cooked."
    show j_closed with dis
    pause.01
    "And I fucking hate Jason."
    show j_open with dis
    j "Fuck off."
    show j_closed with dis
    pause.025
    "See why I hate him?"
    hide j_closed with dis
    "It's been what... like a month into this whole 'living underground in a bunker' thing."
    "Would you believe how ordinary our lives were before we got here?"
    "Well, now, we're here. In this subpar bunker, surrounded by pretentious assholes and rates."
    show j_closed with dis
    pause.025
    "But Jason's really both."
    
    "And it's my turn to make dinner, so I head to the fridge."
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
        "Oh. {w=5}Fuck. {w=5}Nah."
        "THERE'S NO FUCKING FOOD." with vpunch
        "{cps=20}NOOOOOOOO." with pixellate
        "Valerie turns to me with clear disdain and confusion in her eyes for my sudden misery."
        show v_open with dis
        v "...{w} Are you okay?"
        
    # This ends the game.

    return
