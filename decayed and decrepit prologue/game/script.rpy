# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Jason")


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
    show j_closed
    pause.01
    "And I fucking hate Jason."
    hide j_closed
    show j_open with Dissolve(0.5)
    j "Fuck off."
    # This ends the game.

    return
