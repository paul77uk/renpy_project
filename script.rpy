# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image mohappy = "momohappy.png"
image mosmile = "momosmile.png"
image moangry = "momounimpressed.png"
image moneutral = "momoneutral.png"

define kai = Character("Kayoki")
define momo = Character("Momoshi")
define kita = Character("Kitaki")
define r = Character("You")
define ANNOUNCE = Character("ANNOUNCEMENT!")
define ALERT = Character("ALERT!")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    ALERT "Run this code if you have a Micro:bit and put it on your wrist to have a SUPA WATCH-O-2000! on your wrist! Don't touch your face!!! https://makecode.microbit.org/_fLxhEm48YcDW "
    # These display lines of dialogue.
    "Hello, and WELCOME, to CORONAVIRUS⚡STRIKE!"
    "We will soon begin a journey...
    to save ourselves... and others..."
    "FROM CORONA!!!"
    "We will soon begin our journey, and find our way to make an end to this COVID-19⚡STRIKE! before time runs out..."
    "And you all die!"
    "You will have to choose your path to try and save everyone from this CORONAVIRUS⚡STRIKE! by choosing choices when they come."
    "You have to use strategy and intelligence!"
    r "B-but won't this be too hard for me?! I mean, I am just a kid."
    "*laughter* Not at all, kid! This is especially for you. We believe you are the only one able to save us here."
    r "M-Me?!"
    "Yes. You."
    r "T-The only o-one?!?!?!"
    "Yes. You are the only one."
    r "W-WHaT..."
    "I know, I know, it seems a little overwhelming, doesn't it?!"
    r "(What is going on.)"
    r "(I mean, I don't even have any superpowers-- wait a minute! Maybe he's mistaken me for someone else........?!)"
    r "Ummm, sorry mister, but I think you've mistaken me for someone else......"
    "Oh no I haven't!"
    r "...(seriously?!?!?!)..."
    "You love heros, right?!"
    r "Y-Yeah, it depends which, though."
    "And you love adventure?!"
    r "H-HEY--"
    "And you always feel like you are helpless to everything?!"
    r "H-HOW DO YOU K-KNOW ALL THAT--"
    "*chuckles* What you don't realize, kid, you don't realize you are already a hero."
    r "WH-"
    "You can do anything."
    r "HU-"
    "You are so special."
    r "HO-"
    "You mean everything, absolutely EVERYTHING, to the world."
    r "B-BU-"
    "Listen, kid, don't let anyone put yourself down. Even yourself."
    r "(Even myself... what's he talking about?!)"
    "You talk to yourself all the time."
    r "(I TALK TO MYSELF?!?!?!?!?! WHA--)"
    "You are doing it right now."
    r "(HEY CAN THIS GUY READ MY MIND?!)"
    "I know what you are thinking. And that's it. Thinking. It's basicly talking to yourself. If you only knew how to use thought the well way..."
    r "(The well way?! This guy doesn't know how to speak.)"
    "It's a saying here."
    r "*You roll your eyes.*"
    "Anyways, you use it the wrong way. You use it against yourself, to make yourself feel worse."
    r "(worse?!) Mister I do not understand a single thing."
    "You soon will. You just need to use thought the well way."
    "Anyways, enough talk, I'd better introduce you to your new friends."
    "They are valuable people, you know."
    r "(valuable people...)"
    "Hey, Kai!"
    "Come over here a sec!"

    kai "What is it?!"
    "Our hero arived!"
    kai "Oh, they have indeed?! "
    kai "*Kai bends down with his hands behind his back and seems to be scanning your whole body...* (hmm this kid is one unique, strong kid...)"
    kai "Hello, kid!"
    r "(ummmmmmm.......)"
    kai "Don't worry, I am a friendly person! My name is Kayoki, by the way, but you can call me Kai for short."
    ANNOUNCE "YOU ARE ABOUT TO MAKE YOUR FIRST CHOICE!

    Remember, you can only choose once, unless you click the 'Back' button below.

    CHOOSE WISELY!!!"

    menu:
         r "How should I respond?!"

         "Step back":
             r "You step back."
             kai "*laughs* You are a shy person! Don't be scared, I am a best friend to--"

         "H-Hello.":
             r "H-Hello k-kai..."
             kai "You are a good little kid!"

         "Silent":
             r "You do not respond in any way, you just put down your eyes"
             kai "*chuckles* It's ok, kid--"

    label after_menu:

         "Just then, somebody steps into the room."

         show mohappy

         momo "Hello, my dear child! I am Momoshi, but you can call me Momo for short!"

         show moneutral

         kai "I was talking."

         show moangry

         momo "And I wanted to talk, too, you know."

         kai "Ok, ok."

         r "You look from face to face as they talk."

    menu:
         r "What should I do?!"

         "Say Hi to Momo":
             r "H-Hello M-Momo..."
             kai "seems to be bursting inside."

             show mohappy
         "Ask Kai to talk a bit more.":
             r "Umm... kai?!"
             kai "Yeah, actually, I don't have much else to say."
             kai "But be brave, kid. That CORONAVIRUS⚡STRIKE! is deadly, trust me."
             show moneutral
             momo "Yeah, definitely."


         "Silent":
             r "You do not respond in any way, you just put down your eyes again."
             kai "Looks at you."
             momo "Gasps, sighs and makes a quick stern look at Kai, before looking at you."

    momo "Anyway, hello there, my dear child."

    ANNOUNCE "This is how far the programme went yet. You will see more later. We hope you enjoyed!"

    # This ends the game.

    return
