# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character("Kris")
define a = Character("Aurelia")
define q = Character("???")


# rooms
image frontdoor = "bg frontdoor.png"
image bedroom = "bg bedroom.png"
image fridgehallway = "bg fridgehallway.png"
image hallway = "bg hallwayflashlight.png"
image pool = "bg scarypool.png"
image stairway = "bg stairs.png"
image washroom = "bg washroom.png"
image corridoor = "bg hallway.png"



image fridge = "bg fridge.png"

#character
image aurelia back = "aureliaback.png"
image aurelia front = "aureliafront.png"
image aurelia taken = "aureliataken.png"
image monster = "monster.png"
#screens
image youwin = "bg youwin.png"
image beginning = "bg newspaper.png"
image youlose = "bg theend.png"
image black = "bg allblack.png"
image endscreen = "endscreen.png"
#animations


image keys = "keysobject.png"

# The game starts here.

label start:

    play music "cafe-noise-32940.mp3"
    scene beginning
    "..."
    "THREE CHILDREN GONE MISSING - HAUNTED HOUSE?"
    "Three children missing after venturing to alleged haunted house located in Ivy Woods."
    a "Hey Kris!"
    a "Come check this out!"

    k "Ivy Woods? Intresting... it has happened in our area, you wanna go take a peek there?"

    a "I don't know... I mean, sure... why not?"
    play music "intense-horror-music-01-14890.mp3"
    "..."
    jump frontdoor
label youwin:
    play music "leap-motiv-113893.mp3"
    scene bg youwin
    "..."
    return

label theend:
    play music "leap-motiv-113893.mp3"
    scene youlose
    "..."
    return


label frontdoor:

    scene bg frontdoor

    show aurelia back at center
    play sound "concrete-footsteps-1-6265.mp3"
    "..."
    a "I think this is it."
    k "Yeah, looks like the pictures in the newspaper."

    show aurelia front at center
    a "Should we go in?"
    "..."
    menu:
        "Go in":
            jump entrance
        "Leave":
            jump youwin

label entrance:
    
    scene corridoor
    show aurelia back at center
    "..."
    a "This place is giving me the creeps."
    a "I think we should just go home."
    k "You're just a little paranoid."
    k "We're together so you have nothing to be afraid of. Let's just go a little further."
    k "If you get too scared we can leave."
    "..."
    menu:
        "Go left":
            jump stairwaytohell
        "Leave":
            k "Okay, fine... we can go back home."
            play sound "concrete-footsteps-1-6265.mp3"
            show aurelia front at right
            play sound "door-slam-1-100245.mp3"
            "..."
            a "Wait... no no no no no!"
            k "Chill out everythings fine!"
            a "The door is locked! It won't open!"
            k "I guess we have to find another way out."
            menu:
                "Go left":
                    jump stairwaytohell


label stairwaytohell:
    scene stairway
    show aurelia back at center
    "..."
    k "Do you want to go up?"
    a "I don't really know."
    k "You can stay here, but I'm going. You could guard the stairs or something..."
    play sound "concrete-footsteps-1-6265.mp3"
    k "For monsters, you know?"
    show aurelia front at right
    a "Stop it Kris! Not funny! I'm going where you go."

    menu:
        "Explore upstairs":
            jump hallwayup
        "Back to entrance":
            jump mainentrance

label mainentrance:
    scene corridoor
    show aurelia back at center
    play sound "concrete-footsteps-1-6265.mp3"
    "..."
    a "Wait! There's another door Kris!"
    show aurelia front at right
    a "It's on the right, behind that corner."
    k "You're right Aurelia."
    show aurelia back at center
    a "But where to now?"
    menu:
        "Left":
            jump mainstairwaytohell
        "Right":
            jump hallwayfridge
label mainentranceb:
    scene corridoor
    show aurelia back at center
    "..."
    
    menu:
        "Left":
            jump mainstairwaytohell
        "Right":
            jump mainhallwayfridge

label hallwayfridge:

    scene bg fridgehallway
    show aurelia back at center
    "..."
    show aurelia front at right
    a "I wonder what happened to those kids."
    a "They must've been here, I have this weird feeling."
    k "I'm also a little at unease, which concerns me even more."
    show aurelia back at center
    "..."
    k "I just hope that we aren't the ones who find them."
    "..."
    menu:
        "Back to entrance":
            "..."
            jump mainentranceb
        "Continue onwards":
            "..."
            jump scarypool

label mainhallwayfridge:

    scene bg fridgehallway
    "..."
    menu:
        "Back to entrance":
            "..."
            jump mainentranceb
        "Continue to pool":
            "..."
            jump scarypool

label hallwayup:

    scene bg hallwayflashlight
    show aurelia back at center
    a "I don't know about this Kris... How could the doors just close like that?"
    a "There's something seriously off about this place."
    "..."
label mainhallwayup:

    scene bg hallwayflashlight
    "..."
    menu:
        "Stairway":
            jump mainstairwaytohell
        "Go deeper":
            jump bedroom 
label mainstairwaytohell:
    scene stairway
    "..."
    menu:
        "Downstairs":
            jump mainentrance
        "Upstairs":
            jump mainhallwayup 

    menu:
        "Explore upstairs":
            jump hallwayup
        "Back to entance":
            jump mainentrance

label bedroom:
    scene bg bedroom
    play sound "concrete-footsteps-1-6265.mp3"
    "..."
    menu:
        "Look around":
            k "This place is giving me chills."
            menu:
                "Back to hallway":
                    jump mainhallwayup
        "Back to hallway":
            jump mainhallwayup
label scarypool:
    scene pool
    show aurelia back at center
    "..."
    menu:
        "Go back":
            show aurelia front at right
            a "This is seriously freaking me out Kris. Can we go somewhere else?"
            play sound "concrete-footsteps-1-6265.mp3"
            k "Alright, we can look for an exit somewhere else."
            "..."
            jump mainhallwayfridge 
        "Go deeper":
            show aurelia front at right
            play sound "concrete-footsteps-1-6265.mp3"
            a "I don't think we should do this Kris."
            k "You always worry too much Aurelia. Everything will be fine."
            "..."
            jump sacrifice
label sacrifice:
    show aurelia front at right
    "..."
    q "You must come closer"
    play sound "horror-sound-effect-212573.mp3"
    show monster at truecenter

    q "Ah... I see.. you must be terrified Kris..."
    q "Where is my beautiful Aurelia?"
    k "No you can't take her!"
    q "I must take someone..."
    q "It is the rules..."
    menu:
        "Sacrifice Aurelia":
            "..."
            jump aureliagone
        "Sacrifice yourself":
            "..."
            k "No! Take me instead! She doesn't deserve this!"
            jump krisgone
label aureliagone:
    k "NO!"
    play sound "horror-sound-effect-212573.mp3"

    scene aureliataken
    a "Help me Kris!"
    scene black
    a "AHhhahhaaAAAAhaaa!"
    "*blub blub"
    k "Aurelia no! Nooooooo!"
    q "Go on Kris, you wouldn't want to be next, right?"
    "..."
    menu:
        "RUN":
            jump runhallwayfridge
label runhallwayfridge:

    scene fridgehallway  
    menu:
        "..."
        "RUN":
            jump runentrance
label runentrance:
    scene corridoor
    "..."
    menu:
        "RUN":
            scene black
            "..."
            "Kris makes a run for it."
            "He'll never be seen again."
            "Small price to pay to not feel the guilt of a lost loved one."
            "Someone could say: sacrifices must be made."
            jump theend
label krisgone:
    scene endscreen
    a "Kris... please don't leave me..."
    a "Kris? Please say something."
    a "Kris... No..."

    jump theend
    

