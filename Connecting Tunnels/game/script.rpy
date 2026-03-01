# Fade-in animation
transform menu_fade:
    alpha 0.0
    yoffset 20
    linear 0.8 alpha 1.0 yoffset 0


# Modern Button Style
style pretty_button:
    background "#FFFFFF15"
    hover_background "#FFFFFF35"
    padding (18, 12)
    xminimum 260

style pretty_button_text:
    size 32
    color "#FFFFFF"
    xalign 0.5


screen main_menu():

    tag menu

    # Background
    add "main.png"

    # Soft dark overlay for readability
    add Solid("#00000080")

    # Centered Content
    vbox:
        spacing 35
        xalign 0.5
        yalign 0.5
        at menu_fade

        # Game Title
        text "Connecting Tunnels":
            size 90
            color "#FFFFFF"
            outlines [(3, "#000000", 0, 0)]
            xalign 0.5

        null height 20

        # Buttons
        textbutton "Start" style "pretty_button":
            action Start()

        textbutton "Load" style "pretty_button":
            action ShowMenu("load")

        textbutton "Settings" style "pretty_button":
            action ShowMenu("preferences")

        textbutton "Quit" style "pretty_button":
            action Quit(confirm=True)

# script.rpy — Mole Man: Storyboard Line Game (Ren'Py)

define p = Character("You")
define m = Character("Mole Man", color="#c8d6ff")
define n = Character(None)  # narrator
define s = Character("Server")
define h = Character("???")
define b = Character("Boss")

init:
    image bg end = "bg_end.png"
    image bg inout = "bg_inout.png"
    image bg sewer = "bg_sewer.png"
    image bg tacobell = "bg_taco.png"
    image you = "yn.png"
    image moleman = "Mole Man.png"
    image server inout = "server_inout"
    image server taco = "server_taco.png"
    image street = "street.PNG"
    image silhouette = "silhouette.png"
    image bg tacobell poo = "poo.PNG"
    image kiss = "kiss.PNG"
    image bg dark = "dark sewer.png"

default hp = 1
default has_salad = False
default has_burrito = False
default has_animalstylecheesefries = False


# ---- Optional: simple UI / HUD in the corner ----
screen hud():
    frame:
        xalign 0.02
        yalign 0.02
        padding (12, 10)
        background "#0008"
        vbox:
            text "HP: [hp]" size 20
            text "Burrito: [has_burrito]" size 18
            text "Salad: [has_salad]" size 18
            text "Animal Style Cheese Fries: [has_animalstylecheesefries]" size 18

label start:
    # Use a HUD overlay (comment out if you don't want it)
    show screen hud

    # Solid color background (no image needed)
    scene street with dissolve
    n "Rain stitches the street into silver lines."
    n "You lift the sewer hatch and climb down, lantern trembling in your hand."
    b "Emergency blockage. Sewer line 7B. Fix it or else you're DONE!"
    n "You sigh, knowing that you have no choice but to go down there and fix it."
    n "After all, you are just a measly sewer cleaner intern. You have no choice but to follow orders and do your job."
    scene bg dark with dissolve
    show silhouette at left
    n "You hear a scritch-scritch... and then a polite cough."
    h "Down here, we prefer guests who knock."
    hide silhouette

    menu:
        "Call out: Sorry, I didn’t know another division was cleaning this section…":
            jump meet_mole
        "Hide behind the pipe and watch.":
            jump deodorant_needed
        "Climb back up. No way are you doing this today.":
            jump leave

label leave:
    scene street with dissolve
    n "You trudge back up the manhole into the pouring rain."
    b "Where do you think you're going? GET BACK IN THE SEWER, OR YOU'RE FIRED!"
    n "All of a sudden, the phone cuts out. You lost signal."
    p "Oh no... boss isn't gonna be happy about this..."
    n "THE END (Coward’s Cut)."
    return

label deodorant_needed:
    scene bg dark
    show silhouette at left
    n "He comes up close, and sniffs you."
    m "I would recognize that scent anywhere…"
    n "He chokes. Huh?"
    m "The scent that plagues my dreams at night... that sharp and fragrant smell... that I will never get enough of..."
    m "B-baka? Is that you?"
    hide silhouette

    menu:
        "W-what? Senpai?! Is that you?":
            jump meet_mole
        "S-stop! Don't come any closer!":
            jump meet_mole

label meet_mole:
    scene bg sewer with dissolve
    n "Mermories of the past come flooding back to you."
    p "I think..."
    p "No, it can't be."
    p "It’s been so long since I’ve seen him. I thought I’d never see him again."
    n "You swallow, trying to find the words to say, and you’re not even sure if he still remembers you."
    p "My ex-boyfriend? No, that’s not right. He was more than that. He was my best friend. My soulmate. My universe."
    show moleman at left with dissolve
    m "Y-you've changed… In a good way, of course!"
    n "He gets shy, trying to play it cool, but you can tell he’s just as flustered as you are."
    p "I could say the same for you…"
    n "You look him up and down, and notice his build is a little wider, muscles a little stronger."
    n "He’s all grown up, and yet he still feels the same. The same breathtakingly gorgeous eyes, the same wide smile, the same smell."
    n "You both blush, an heavy air of tension hanging between you two."
    hide moleman
    menu:
        "Ask him why he had to leave.":
            jump why_me
        "Go left.":
            jump taco_bell
        "Go right.":
            jump inn_out

label why_me:
    scene bg end with dissolve
    p "Why did you have to leave me?! YOU FREAK! YOU BROKE MY HEART!? Why would I EVER want to be with you again?!"
    show moleman at center
    m "Huh?! W-wait calm down, I never said anything abou-"
    p "NO! YOU ABANDONNED ME!!! BACK THEN, YOU LEFT ME WHEN I NEEDED YOU THE MOST!!! I should've known. You’ve always been like this. Pathetically selfish."
    m "I... was meant for the tunnels. You knew that."
    n "He swallows, tripping over his words. Tears wallow in his eyes, and you can tell he’s trying to choke back a sob."
    m "You were meant for the surface. In the very first place, we were never meant to be. :("
    hide moleman with dissolve
    n "THE END (Too DESPERATE)."
    return

label taco_bell:
    show moleman at left
    m "You know… our old taco bell is close to the metro line. I-if you wouldn't mind going with me...?"
    n "He blushes, looking sheepish and scratching his head. He nervously awaits your response."
    n "*H-he remembered my favourite comfort takeout food...*" 
    scene bg tacobell with dissolve
    hide moleman

    menu:
        "Order a Beefy 55-Layer Burrito with extra cheese.":
            if not has_burrito:
                $ has_burrito= True
            jump oh_no
        "Order a salad.":
            if not has_salad:
                $ has_salad = True
            jump saladt
        "Tell him you don’t like taco bell anymore.":
            jump meet_mole

label inn_out:
    show moleman at right
    m "“You know… the route chamber is close to the eat-it-out-"
    m "UHHHH- I meant, the in-and-out where we first met...? I-if you wouldn't mind going with me...?”"
    n "He blushes, looking sheepish and scratching his head. He nervously awaits your response."
    p "*H-he remembered where we first met…*" 
    scene bg inout with dissolve
    hide moleman 
    menu:
        "Order a four-by-four with extra cheese and animal style fries." if not has_animalstylecheesefries:
            $ has_animalstylecheesefries = True
            jump self_respect
        "Order a salad." if not has_salad:
            $ has_salad = True
            jump saladi

label oh_no:
    scene bg tacobell with dissolve
    show server taco at truecenter
    s "Order 714? 714? A 55-Layer Burrito with extra beans?"
    n "The cashier lazily calls out orders, clearly being underpaid. But wait- she got your order wrong!"
    n "Before you could react, he storms up to the cashier and knocks on the counter angrily."
    show moleman at left
    m "Hey! That's not what-"
    n "You stop him before he escalates the situation, and decide to just make do with what she gave you."
    n "You don’t want to cause a scene in public, and you most certainly don't want to make him look bad."
    n "You take a look and realize that there was extra beans in your burrito, which you *really* don't like."
    hide server taco
    hide moleman
    menu:
        "Take it anyway.":
            jump too_much_fibre
        "Correct the server and ask her to make another one.":
            $ hp -= 1
            if hp <= 0:
                jump slimed_out
        

label saladt:
    scene bg tacobell with dissolve
    show moleman at left
    m "A salad… huh? I still remember your old order… I can’t believe how much you’ve changed."
    n "He looks a little surprised, and then a look of hurt flashes across his face."
    n "You look at the plastic tray of leafy greens in your hand. Inside, you feel a little guilty."
    n "In fact, the burrito is still your favourite."
    n "The extra cheese. The extra beef."
    n "You used to go crazy for those, and now you're trying to change yourself to impress someone who liked you as you were in the first place."
    hide moleman
    menu:
        "Try again with him.":
            jump try_again
        "Nuh uh. Mole men don't deserve second chances.":
            jump nuh_uh

label saladi:
    scene bg inout with dissolve
    show moleman at left
    m "A salad… huh? I still remember your old combo… I can’t believe how much you’ve changed."
    n "He looks a little surprised, and a look of hurt momentarily flashes across his face."
    n "You look at the plastic tray of leafy greens in your hand. Inside, you feel a little guilty."
    n "In fact, the burger combo is still your favourite."
    n "The extra cheese. The extra fries."
    n "You used to go crazy for those, and now you're trying to change yourself to impress someone who liked you as you were in the first place."
    hide moleman
    menu:
        "Try again with him.":
            jump try_again
        "Nuh uh. Mole men don't deserve second chances.":
            jump nuh_uh
    
label slimed_out:
    scene bg tacobell with dissolve
    show server taco at truecenter
    p "Excuse me, but I think you got my order wrong. I ordered a Beefy 55-Layer Burrito with extra cheese, but this has extra beans in it..."
    s "Yeah, that’s not my problem?"
    hide server taco
    n "The cashier sneers and sarcastically rolls her eyes further than her eyebrow piercing."
    n "You can see the veins in his neck bulging as he tries to contain his rage."
    show server taco at truecenter
    s "Yeah, well maybe if you weren’t so caught up chatting with that ugly… thing… over there, maybe you wouldn’t have missed your number."
    hide server taco
    show moleman at left
    m "Now you’ve really crossed the line…"
    n "He growls, getting ready to pounce on her."
    n "But before he bares his sharp teeth, you jump in front of him."
    m "This cashier has no idea what she just got himself into."
    n "He growls animalistically at her, rolling his shoulders and flexing his biceps."
    hide moleman 
    p "You got a damn problem with us?"
    n "The cashier to roll her eyes again."
    show server taco at truecenter
    s "You asked for it now, you rats!"
    hide server taco
    scene black with dissolve
    n "She jumps over the counter, scratching you two in the face and killing you."
    n "THE END (Beat up by service worker ending)."
    return

label self_respect:
    scene bg end with dissolve
    show moleman at right
    m "Cheese fries, huh?"
    n "He chuckles."
    m "I remember when you used to go crazy for those."
    n "Your face burns a little red, embarrassed to admit you still remember that."
    p "Yeah… some things never change right?"
    n "You look down at the floor embarassed, shuffling your feet a little."
    m "Yeah. Some things never change."
    n "He looks at you, a satisfied grin on his face."
    hide moleman
    n "THE END (Self Respect Ending)."
    return

label nuh_uh:
    scene bg end with dissolve
    show moleman at left
    m "Oh, by the way I might be going to war soon."
    n "He says it so firmly, and you can tell he's trying to sound tough, but it just comes off as awkward and sad."
    p "That's good for you... I guess."
    n "You couldn't feel less indifferent about this news. He seems hurt, but that's not your business anyway."
    n "He's kinda awkward, and way too chopped anyway."
    hide moleman
    n "THE END (It's Not You, It's Me Ending)."
    return

label try_again:
    scene bg_end with dissolve
    show moleman at left
    n "He smiles softly."
    m "I know what you’re trying to do."
    n "Tears unwillingly drip down your face, and unsuspecting sobs leave your lips."
    m "You don’t have to change yourself. Not for me. Not for society. For nobody."
    m "I never wanted you to change. Just stay the way you are, won't you?"
    n "Tears were now streaming into your soggy salad."
    p "But... I left you. I *hurt* you. I thought you hated me."
    n "You were choked up, trying to find the right words to say."
    m "I never left."
    n "He holds you tightly, and your hearts beat together as one."
    m "You just never looked back."
    n "Slowly you melt into his arms, and suddenly everything feels as though it's right again."
    hide moleman
    show kiss at truecenter
    n "THE END (Back Together Ending <3)."
    return

label too_much_fibre:
    scene bg tacobell poo with dissolve
    p "OH NO! MY STOMACH IS ABOUT TO BUUUUSST!!!"
    n "Then you lowkey get crazy style gas and fart everryyywheereee.."
    n "Then you lowkey get crazyyy sloppy greasy slick diarrhea. To make things worse,  the door hinges blow off while you drop a generational brown as he sees you painting the walls brown."
    n "THE END (Explosive Ending)."
    return