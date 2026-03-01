# script.rpy — Mole Man: Storyboard Line Game (Ren'Py)

define p = Character("You")
define m = Character("MoleMan", color="#c8d6ff")
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
    image mole = "Mole Man.png"
    image server inout = "server_inout"
    image server taco = "server_taco.png"
    image street = "street.PNG"
    image silhouette = "moleman silhouette.PNG"
    image bg tacobell poo = "poo.PNG"

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
    scene bg sewer with dissolve
    n "You hear scritch-scritch... and then a polite cough."
    h "Down here, we prefer guests who knock."

    menu:
        "Call out: Sorry, I didn’t know another division was cleaning this section…":
            jump meet_mole
        "Hide behind the pipe and watch.":
            jump deodorant_needed
        "Climb back up. Nope.":
            jump leave

label leave:
    scene bg end with dissolve
    show you at left
    n "You trudge back up the manhole into the pouring rain."
    n "Boss isn't gonna be happy about this..."
    hide you
    n "THE END (Coward’s Cut)."
    return

label deodorant_needed:
    scene bg sewer
    show silhouette at left
    n "He smells you."
    m "I would recognize that scent anywhere…"
    n "He chokes."
    m "The scent ive been dreaming about→(beefy, girthy)"
    m "B-baka? Is that you?"
    hide silhouette

    menu:
        "“s-senpai? Is that you?”":
            jump meet_mole
        "“S-stop! Dont come any closer!”":
            jump meet_mole

label meet_mole:
    scene bg sewer with dissolve
    n "Mermories flash back to you."
    p "oh..i think thats my ex on foenem"
    show moleman with dissolve at left
    m "Y-youve changed… In a good way, of course!"
    p "“i could say the same for you…”"
    n "You both blush, an air of heaviness hanging between you two."
    hide moleman
    menu:
        "Ask him why he still wants you":
            jump why_me
        "Go left":
            jump taco_bell
        "Go right":
            jump inn_out

label why_me:
    scene bg end with dissolve
    p "“Why do YOU still want me?! YOU FREAK! YOU BROKE MY HEART!?"
    show moleman at center
    m "W-wait calm down, we can talk about this-"
    p "NO! YOU LEFT ME!!! YOU LEFT ME WHEN I NEEDED YOU THE MOST!!! I shouldve known. You’ve always been like this *tears well  up in his eyes *"
    m "I... was meant for the tunnels. You were meant for the surface. We were never meant to be. :("
    hide moleman with dissolve
    n "THE END (Too desperate)."
    return

label taco_bell:
    scene bg tacobell with dissolve
    show moleman at left
    m "You know… our old taco bell is close to the metro line."
    n "You think: H-he remembered my favourite spot…" 
    hide moleman

    menu:
        "Order a Beefy 5-Layer Burrito with extra cheese and beans.":
            if not has_burrito:
                $ has_burrito= True
            jump oh_no
        "Order a salad.":
            if not has_salad:
                $ has_salad = True
            jump saladt
        "Tell him you don’t like taco bell anymore.":
            jump meet_mole

label oh_no:
    scene bg tacobell with dissolve
    show server taco at right
    n "Server: Order 714? 714?"
    n "The cashier lazily draws out. Wait- you guys are order 713! Before you could react, he storms up to the cashier and taps the counter angrily."
    show moleman at left
    n "You take a look and realise there is no extra, just a regular serving of cheese. D:"
    hide server taco
    hide moleman
    menu:
        "Take it anyway":
            jump too_much_fibre
        "Correct server and ask to make another":
            $ hp -= 1
            if hp <= 0:
                jump slimed_out
        

label saladt:
    scene bg tacobell with dissolve
    show moleman at left
    m "A salad… huh? I still remember your old order… I can’t believe how much you’ve changed”."
    n "You look at the plastic tray of leafy greens in your hand. Inside, you feel guilty."
    p "It’s still my favourite. The extra cheese. I can’t believe I tried to change myself to impress him. I’ve changed so much, yet he stayed so familiar…"
    hide moleman
    menu:
        "Try again with him.":
            jump try_again
        "Nuh uh.":
            jump nuh_uh

label saladi:
    scene bg inout with dissolve
    show moleman at left
    m "A salad… huh? I still remember your old order… I can’t believe how much you’ve changed”."
    n "You look at the plastic tray of leafy greens in your hand. Inside, you feel guilty."
    p "It’s still my favourite. The extra cheese. I can’t believe I tried to change myself to impress him. I’ve changed so much, yet he stayed so familiar…"
    hide moleman
    menu:
        "Try again with him.":
            jump try_again
        "Nuh uh.":
            jump nuh_uh
    

label inn_out:
    scene bg inout with dissolve
    show moleman at right
    m "“You know… the route chamber is close to the eat-it-out- UHH i mean in-and-out where we first met."
    n "you think: h-he remembered where we first met…" 
    hide moleman 
    menu:
        "Order a four-by-four with extra cheese and animal style fries" if not has_animalstylecheesefried:
            $ has_animalstylecheesefried = True
            jump self_respect
        "Order a salad" if not has_salad:
            $ has_salad = True
            jump saladi
       
label slimed_out:
    scene bg end with dissolve
    show server inout at left
    s "Yeah, that’s not my problem?"
    hide server_inout
    n "The cashier rolls her eyes further than her eyebrow piercing goes."
    show server inout at left
    s "Maybe if you weren’t so caught up dating that ugly… thing… over there, maybe you wouldn’t have missed your number."
    hide server_inout
    p "Now you’ve really crossed the line…"
    n "He growls, getting ready to pounce on her."
    n "But before he bares his sharp teeth, you jump in front of him."
    show moleman at left
    m "This cashier has no idea what she just got himself into."
    hide moleman 
    p "You got a damn problem with me?"
    n "The cashier to roll her eyes again."
    show server_inout at right
    s "You asked for it now, rat!"
    hide server_inout
    n "She jumps over the counter, scratching you face and killing you."
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
    n "THE END (Self respect Ending)."
    return

label nuh_uh:
    scene bg end with dissolve
    show moleman at left
    m "Oh by the way I'm going to war soon."
    p "That's good for you.. I guess."
    n "He's kinda awkward and chopped anyway."
    hide moleman
    n "THE END (It's not you it's me Ending)."
    return

label try_again:
    scene bg_end with dissolve
    show moleman at left
    n "He smiles softly."
    m "I know what you’re trying to do."
    n "tears unwillingly drip down your face."
    m "You don’t have to change yourself. Not for me. Not for yourself. For nobody. I never wanted you to change."
    n "Tears keep streaming into your now soggy salad."
    p "But you left me."
    n "You were choked out."
    m "I never left."
    n "He holds you."
    m "You just never looked back."
    n "Slowly you melt into his arms, and the world seems to fade into "
    hide moleman
    n "THE END (Back together ending <3)."
    return

label too_much_fibre:
    scene bg tacobell poo with dissolve
    p "OH NO! MY STOMACH IS ABOUT TO BUUUUSST!!!"
    n "Then you lowkey get crazy style gas and fart everryyywheereee.."
    n "Then you lowkey get crazyyyyy sloppy greasy slick diarrhea……. And the door hinges blow off and he sees you smearing poo on the walls."
    n "THE END (Explosive Ending)."
    return