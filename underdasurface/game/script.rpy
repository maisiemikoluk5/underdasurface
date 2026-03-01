# script.rpy — Mole Man: Storyboard Line Game (Ren'Py)

define p = Character("You")
define m = Character("MoleMan", color="#c8d6ff")
define n = Character(None)  # narrator

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
            text "Animal cheese fries: [has_animalstylecheesefries]" size 18

label start:
    # Use a HUD overlay (comment out if you don't want it)
    show screen hud

    # Solid color background (no image needed)
    scene black with dissolve

    n "Rain stitches the street into silver lines."
    n "You lift the sewer hatch and climb down, lantern trembling in your hand."
    p "Emergency blockage. Sewer line 7B. Fix it or you’re done."
    n "You hear scritch-scritch... and then a polite cough."
    n "A voice: “Down here, we prefer guests who knock.”"

    menu:
        "Call out: Sorry, I didn’t know another division was cleaning this section…":
            jump meet_mole
        "Hide behind the pipe and watch.":
            jump deodorant_needed
        "Climb back up. Nope.":
            jump leave

label leave:
    scene black with dissolve
    n "You climb back up into the rain."
    n "Boss isn't gonna be happy about this."
    n "THE END (Coward’s Cut)."
    return

label deodorant_needed:
    scene black with dissolve
    n "He smells you."
    p "i would recognize that scent anywhere… the scent ive been dreaming about→(beefy, girthy)"
    m "s-senpai? Is that you?"

    menu:
        "“s-senpai? Is that you?”":
            jump meet_mole
        "“S-stop! Dont come any closer!”":
            jump meet_mole

label meet_mole:
    scene black with dissolve
    n "Mermories flash back to you."
    p "oh..i think thats my ex on foenem"
    m "y-youve changed…"
    p "“i could say the same for you…”"
    n "You both blush."

    menu:
        "Ask him why he wants u":
            jump why_me
        "Go left":
            jump taco_bell
        "Go right":
            jump inn_out

label why_me:
    scene black with dissolve
    p "“Why do YOU still want me?! YOU FREAK! YOU BROKE MY HEART!?"
    m "w-wait calm down, we can talk about this-"
    p "NO! YOU LEFT ME!!! YOU LEFT ME WHEN I NEEDED YOU THE MOST!!! I shouldve known. You’ve always been like this *tears well  up in his eyes *"
    m "i was meant for the tunnels. you were meant for the surface. We were never meant to be. :("
    n "THE END (Too desperate)."
    return

label taco_bell:
    scene black with dissolve
    m "You know… our old taco bell is close to the metro line."
    n "You think: h-he remembered my favourite spot…" 

    menu:
        "Order a Beefy 5-Layer Burrito with extra cheese and beans":
            if not has_burrito:
                $ has_burrito= True
            jump oh_no
        "Order a salad":
            if not has_salad:
                $ has_salad = True
            jump salad
        "Tell him you don’t like taco bell any more":
            jump meet_mole

label oh_no:
    scene black with dissolve
    n "Server: Order 714? 714?"
    n "The cashier lazily draws out. Wait- you are order 713! Before you could react, he storms up to the cashier and taps the counter."
    n "You take a look and realise there is no extra, just a regular serving of cheese. D:"

    menu:
        "Take it anyway":
            jump too_much_fibre
        "Correct server and ask to make another":
            $ hp -= 1
            if hp <= 0:
                jump slimed_out
        

label salad:
    scene black with dissolve
    m "A salad… huh? I still remember your old order… I can’t believe how much you’ve changed”."
    n "You look at the plastic tray of leafy greens in your hand. Inside, you feel guilty."
    p "It’s still my favourite. The extra cheese. I can’t believe I tried to change myself to impress him. I’ve changed so much, yet he stayed so familiar…"

    menu:
        "Try again with him.":
            jump try_again
        "Nuh uh.":
            jump nuh_uh
    

label inn_out:
    scene black with dissolve
    m "“You know… the route chamber is close to the eat-it-out- UHH i mean in-and-out where we first met."
    n "you think: h-he remembered where we first met…" 

    menu:
        "Order a four-by-four with extra cheese and animal style fries" if not has_animalstylecheesefried:
            $ has_animalstylecheesefried = True
            jump self_respect
        "Order a salad" if not has_salad:
            $ has_salad = True
            jump salad
       
label slimed_out:
    scene black with dissolve
    n "Server: Yeah, that’s not my problem?"
    n "The cashier rolls her eyes further than her eyebrow piercing goes."
    n "Server: Maybe if you weren’t so caught up dating that ugly… thing… over there, maybe you wouldn’t have missed your number."
    p "Now you’ve really crossed the line…"
    n "He grows, getting ready to pounce on you."
    n "Before he bares his sharp teeth, he jumps in front of you."
    m "This cashier has no idea what he just got himself into."
    p "You got a damn problem with me?"
    n "The cashier to roll his eyes again."
    n "Server: You asked for it."
    n "He jumps over the counter, scratching you face and killing you."
    n "THE END (Beat up by service worker Ending)."
    return

label self_respect:
    scene black with dissolve
    m "Cheese fries, huh?"
    n "He chuckles."
    m "I remember when you would go crazy for these."
    n "Your face burns a little red, embarrassed to admit you still remember that."
    p "Yeah… some things never change right?"
    n "You look down at the floor embarassed, shuffling your feet a little."
    m "Yeah. Some things never change."
    n "He looks at you, a satisfied grin on his face."
    n "THE END (Self respect Ending)."
    return

label nuh_uh:
    scene black with dissolve
    n "You don’t become a hero."
    n "You become something rarer: a caretaker."
    m "Welcome to the line beneath the lines."
    n "THE END (It's not you it's me Ending)."
    return

label try_again:
    scene black with dissolve
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
    n "Slowly you melt into his arms."
    n "THE END (Back together ending <3)."
    return

label too_much_fibre:
    scene black with dissolve
    p "OH NO! MY STOMACH IS ABOUT TO BUUUUSST"
    n "Then you lowkey get crazy style gas and fart everryyywheereee.."
    n "Then you lowkey get crazyyyyy sloppy greasy slick diarrhea……. And the door hinges blow off and he sees you smearing poo on the walls."
    n "THE END (Explosive Ending)."
    return