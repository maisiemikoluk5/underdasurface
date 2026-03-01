#!/usr/bin/env python3
"""
Under da surface: second chances with the mole
- Node/scene-based "storyboard" structure
- Branching choices
- Simple inventory + flags
"""

from dataclasses import dataclass, field
from typing import Callable, Dict, List, Optional, Tuple

# ---------- Game State ----------

@dataclass
class GameState:
    inventory: set = field(default_factory=set)
    flags: Dict[str, bool] = field(default_factory=dict)
    hp: int = 3  # tiny "tension" meter; not a full combat system


# ---------- Helpers ----------

def say(lines: List[str]) -> None:
    """Print storyboard lines with spacing."""
    for line in lines:
        print(line)
    print()

def prompt_choice(options: List[Tuple[str, str]]) -> str:
    """
    options: list of (key, description)
    returns chosen key
    """
    while True:
        for i, (_, desc) in enumerate(options, start=1):
            print(f"{i}. {desc}")
        choice = input("\nChoose: ").strip()
        print()
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(options):
                return options[idx][0]
        # allow typing the key directly too
        keys = [k for k, _ in options]
        if choice in keys:
            return choice
        print("Invalid choice. Try again.\n")

def has(state: GameState, item: str) -> bool:
    return item in state.inventory

def flag(state: GameState, name: str) -> bool:
    return state.flags.get(name, False)

def set_flag(state: GameState, name: str, value: bool = True) -> None:
    state.flags[name] = value

def add_item(state: GameState, item: str) -> None:
    state.inventory.add(item)

def remove_item(state: GameState, item: str) -> None:
    state.inventory.discard(item)


# ---------- Storyboard Scene Model ----------

@dataclass
class Choice:
    text: str
    next_scene: str
    condition: Optional[Callable[[GameState], bool]] = None
    effect: Optional[Callable[[GameState], None]] = None

@dataclass
class Scene:
    title: str
    lines: List[str]
    choices: List[Choice] = field(default_factory=list)
    on_enter: Optional[Callable[[GameState], None]] = None


# ---------- Scenes ----------

def build_scenes() -> Dict[str, Scene]:
    scenes: Dict[str, Scene] = {}

    scenes["start"] = Scene(
        title="SEWER HATCH @ MIDNIGHT",
        lines=[
            "Rain stitches the street into silver lines.",
            "You lift the sewer hatch and climb down, lantern trembling in your hand.",
            "",
            "You hear *scritch-scritch*… and then a polite cough.",
            "",
            "A voice: “Down here, we prefer guests who knock.”",
        ],
        choices=[
            Choice("Call out: “Sorry, I didn’t know another division was cleaning this section…”", "meet_mole"),
            Choice("Hide behind the pipe and watch.", "spy_mole"),
            Choice("Climb back up. Nope.", "leave"),
        ],
    )

    scenes["leave"] = Scene(
        title="RETREAT",
        lines=[
            "You climb back up into the rain.",
            "Boss is not gonna be happy about this.",
            "",
            "THE END (Coward’s Cut).",
        ],
    )

    scenes["spy_mole"] = Scene(
        title="DEODORANT NEEDED",
        lines=[
            "You press into the pipe-shadow and hold your breath.",
            "A figure shuffles into the light of the lantern: beefy, girthy, .",
            "His nose twitches. He’s sniffing the air like he can smell intentions.",
            "",
            "He stops. “i would recognize that scent anywhere… the scent ive been dreaming about.”",
        ],
        choices=[
            Choice("“s-senpai? Is that you?”", "meet_mole"),
            Choice("STOP! DON'T COME ANY CLOSER!", "meet_mole"),
        ],
    )

    scenes["meet_mole"] = Scene(
        title="FIRST CONTACT?",
        lines=[
            "Mermories flash back to you.",
            "You whisper,“oh..i think thats my ex on foenem.”",
            "He looks you up and down. ““y-you've changed…””",
            "",
            "“i could say the same for you…”",
            "You both blush."
            "“You know our old Taco Bell is near the metro line to our left. You know… the route chamber is close to the eat-it-out- UHH i mean in-and-out where we first met.”",
        ],
        choices=[
            Choice("Ask why he still wants you", "why_guard"),
            Choice("Taco Bell (LEFT).", "metro_line"),
            Choice("In-and-Out (RIGHT).", "root_chambers"),
        ],
    )

    scenes["why_guard"] = Scene(
        title="AGAIN?",
        lines=[
            "“Why do YOU still want me?! YOU IDIOT! YOU BROKE MY HEART!?"
            "w-wait calm down, we can talk about this-"
            "NO! YOU LEFT ME!!! YOU LEFT ME WHEN I NEEDED YOU THE MOST!!! I shouldve known. You’ve always been like this "
            "*tears well  up in his eyes *"
            "THE END (Too Desperate).",
        ]
    )

    scenes["metro_line"] = Scene(
        title="TACO BELL",
        lines=[
            "you think: h-he remembered my favourite spot…"
        ],
        choices=[
            Choice("Try the keypad (guess the code).", "keypad"),
            Choice("Search the posters for clues.", "poster_clue"),
            Choice("Turn back to the fork.", "meet_mole"),
        ],
    )

    scenes["keypad"] = Scene(
        title="THE KEYPAD",
        lines=[
            "The keypad blinks: [ _ _ _ _ ].",
            "A smeared label reads: “LINE—B / MAINT.”",
            "",
            "You can try three times before the lock sulks.",
        ],
        choices=[
            Choice("Enter code 1974 (a year on a poster).", "keypad_try_1974"),
            Choice("Enter code 0420 (spray-painted nearby).", "keypad_try_0420"),
            Choice("Enter code 1312 (scratched into the frame).", "keypad_try_1312"),
            Choice("Back away slowly.", "metro_line"),
        ],
    )

    def keypad_fail(state: GameState) -> None:
        state.hp -= 1

    scenes["keypad_try_1974"] = Scene(
        title="CODE: 1974",
        lines=[
            "*beep* *beep*",
            "The light goes red.",
            "The lock makes a disappointed whirr.",
            "You feel the tunnel watching you.",
        ],
        choices=[
            Choice("Try again.", "keypad", effect=keypad_fail),
            Choice("Stop messing with it.", "metro_line"),
        ],
    )

    scenes["keypad_try_0420"] = Scene(
        title="CODE: 0420",
        lines=[
            "*beep*",
            "Green light.",
            "The door clicks open like it’s been waiting for someone to remember.",
            "",
            "Inside is a maintenance room with a dusty map tube and a sealed canteen.",
        ],
        choices=[
            Choice("Take the map tube.", "maintenance_loot",
                   effect=lambda s: add_item(s, "tunnel_map")),
            Choice("Take the sealed canteen.", "maintenance_loot",
                   effect=lambda s: add_item(s, "canteen")),
            Choice("Take both.", "maintenance_loot",
                   effect=lambda s: (add_item(s, "tunnel_map"), add_item(s, "canteen"))),
        ],
    )

    scenes["keypad_try_1312"] = Scene(
        title="CODE: 1312",
        lines=[
            "*beep* *beep* *beep*",
            "Red light.",
            "The keypad emits a loud buzz that echoes down the line.",
            "",
            "Somewhere, metal scrapes metal. Something heard you.",
        ],
        choices=[
            Choice("Run back toward the fork.", "meet_mole",
                   effect=lambda s: (set_flag(s, "stalker_awake", True), keypad_fail(s))),
            Choice("Hold still and listen.", "listen_scrape", effect=keypad_fail),
        ],
    )

    scenes["poster_clue"] = Scene(
        title="POSTER CLUES",
        lines=[
            "You scan the posters with your lantern.",
            "One advert screams: “B-LINE OPENS 04/20!”",
            "Another shows a faded mayor pointing at the words: “REMEMBER THE CODE.”",
            "",
            "Well. That seems… helpful.",
        ],
        choices=[
            Choice("Return to the keypad.", "keypad"),
            Choice("Ignore it and go back.", "metro_line"),
        ],
    )

    scenes["maintenance_loot"] = Scene(
        title="MAINTENANCE ROOM",
        lines=[
            "The room smells like cold pennies and old paperwork.",
            "You pocket what you can. The door clicks shut behind you—then stays ajar.",
            "",
            "Back on the line, the hum feels slightly quieter.",
        ],
        choices=[
            Choice("Proceed down the metro line.", "deep_line"),
            Choice("Go back to the fork.", "meet_mole"),
        ],
    )

    scenes["listen_scrape"] = Scene(
        title="LISTENING",
        lines=[
            "You kill your breath.",
            "The scraping stops.",
            "Then—two taps on the wall, exactly like Morrow did earlier.",
            "",
            "A message in sound: *you are not alone*.",
        ],
        choices=[
            Choice("Back away toward the fork.", "meet_mole",
                   effect=lambda s: set_flag(s, "stalker_awake", True)),
            Choice("Call out: “Morrow?”", "call_morrow"),
        ],
    )

    scenes["call_morrow"] = Scene(
        title="ECHO NAME",
        lines=[
            "Your voice rides the rails and returns thinner.",
            "No answer. But you hear a *soft laugh*—not Morrow’s.",
            "",
            "Bad timing. Great atmosphere.",
        ],
        choices=[
            Choice("Run.", "meet_mole", effect=lambda s: set_flag(s, "stalker_awake", True)),
        ],
    )

    scenes["deep_line"] = Scene(
        title="THE DEEP LINE",
        lines=[
            "You follow the track into a wider chamber where the ceiling arches like a ribcage.",
            "A mural covers the wall: a giant mole holding up the city with both hands.",
            "",
            "In front of the mural sits a steel door labeled: “FOUNDATION VALVE.”",
        ],
        choices=[
            Choice("Use the tunnel map (if you have it).", "valve_room",
                   condition=lambda s: has(s, "tunnel_map")),
            Choice("Try to brute-force the steel door.", "brute_force"),
            Choice("Go back.", "metro_line"),
        ],
    )

    scenes["brute_force"] = Scene(
        title="BRUTE FORCE",
        lines=[
            "You shoulder the door. It doesn’t care.",
            "You shoulder again. The door continues not caring.",
            "",
            "You gain: a bruised ego.",
            "You lose: time.",
        ],
        choices=[
            Choice("Look for another route.", "deep_line",
                   effect=lambda s: (s.__setattr__("hp", max(1, s.hp - 1)), None)),
            Choice("Go back.", "metro_line"),
        ],
    )

    scenes["valve_room"] = Scene(
        title="FOUNDATION VALVE",
        lines=[
            "The map shows a hidden latch behind the mural’s cracked tile.",
            "You pry it open and slip inside.",
            "",
            "A valve wheel the size of a car tire sits in the center.",
            "A note: “TURN ONLY IF YOU MEAN IT.”",
        ],
        choices=[
            Choice("Turn the valve RIGHT (drain the lower tunnels).", "valve_right"),
            Choice("Turn the valve LEFT (flood the line to seal it).", "valve_left"),
            Choice("Don’t touch it. Leave.", "deep_line"),
        ],
    )

    scenes["valve_right"] = Scene(
        title="RIGHT TURN",
        lines=[
            "You turn the wheel. It fights you like a stubborn planet.",
            "Water begins to drain, revealing carved symbols in the concrete.",
            "",
            "One symbol matches a sketch on your map: “ROOT GATE.”",
            "A new route opens.",
        ],
        choices=[
            Choice("Follow the newly revealed route.", "root_gate",
                   effect=lambda s: set_flag(s, "tunnels_drained", True)),
        ],
    )

    scenes["valve_left"] = Scene(
        title="LEFT TURN",
        lines=[
            "You turn the wheel LEFT.",
            "The hum rises into a warning whine.",
            "Water surges down the track like the city exhaling.",
            "",
            "Whatever was moving out there… stops moving.",
            "You might’ve sealed something in—or out.",
        ],
        choices=[
            Choice("Return to the chamber.", "deep_line",
                   effect=lambda s: set_flag(s, "line_flooded", True)),
        ],
    )

    scenes["root_chambers"] = Scene(
        title="ROOT-CHAMBERS",
        lines=[
            "You take the right tunnel and the air changes—damp soil, green rot, life.",
            "Tree roots lace the ceiling like black veins.",
            "",
            "A small altar of stones sits beside a candle stub.",
            "On it: a rusted compass and a clean, sharp trowel.",
        ],
        choices=[
            Choice("Take the compass.", "root_chambers",
                   effect=lambda s: add_item(s, "compass"),
                   condition=lambda s: not has(s, "compass")),
            Choice("Take the trowel.", "root_chambers",
                   effect=lambda s: add_item(s, "trowel"),
                   condition=lambda s: not has(s, "trowel")),
            Choice("Leave the altar alone and move on.", "fungus_fork"),
            Choice("Go back to Morrow.", "meet_mole"),
        ],
    )

    scenes["fungus_fork"] = Scene(
        title="THE FUNGUS FORK",
        lines=[
            "Bioluminescent fungus paints the tunnel walls in dim constellations.",
            "Three paths split like a claw mark:",
            "  (1) Downward: a cold draft and distant dripping.",
            "  (2) Flat: a warm breeze that smells like smoke.",
            "  (3) Upward: root-lattice and faint daylight.",
        ],
        choices=[
            Choice("Go downward.", "cold_draft"),
            Choice("Go flat toward the warm breeze.", "smoke_breeze"),
            Choice("Go upward toward faint daylight.", "daylight_exit"),
        ],
    )

    scenes["cold_draft"] = Scene(
        title="COLD DRAFT",
        lines=[
            "The tunnel narrows. Your lantern gutter-flares.",
            "A hiss slides across the stone.",
            "",
            "A pale, eyeless thing—like a sewer eel made of mist—drifts toward you.",
        ],
        choices=[
            Choice("Use chalk to mark a retreat line (if you have chalk).", "marked_retreat",
                   condition=lambda s: has(s, "chalk"),
                   effect=lambda s: set_flag(s, "marked_path", True)),
            Choice("Use the trowel to strike the stone and scare it (if you have trowel).", "scare_mist",
                   condition=lambda s: has(s, "trowel")),
            Choice("Back away slowly.", "fungus_fork",
                   effect=lambda s: (s.__setattr__("hp", max(1, s.hp - 1)), None)),
        ],
    )

    scenes["marked_retreat"] = Scene(
        title="CHALK LINE",
        lines=[
            "You draw a bold chalk line on the wall—your own storyboard panel border.",
            "The mist-thing pauses, confused by human certainty.",
            "You retreat along your line and the tunnel feels less eager to swallow you.",
        ],
        choices=[
            Choice("Return to the fungus fork.", "fungus_fork"),
        ],
    )

    scenes["scare_mist"] = Scene(
        title="STONE SONG",
        lines=[
            "You strike stone with the trowel: *CLANG!*",
            "The sound rings sharp and bright.",
            "The mist-thing recoils like it hates music.",
            "",
            "It melts backward into cracks you didn’t see before.",
        ],
        choices=[
            Choice("Continue downward, now that it’s gone.", "root_gate",
                   effect=lambda s: set_flag(s, "mist_cleared", True)),
            Choice("Return to the fungus fork.", "fungus_fork"),
        ],
    )

    scenes["smoke_breeze"] = Scene(
        title="SMOKE BREEZE",
        lines=[
            "The warm air leads you to a hidden camp: coffee tin, blanket, a tiny stove.",
            "Morrow sits there, sipping something that smells like burnt dreams.",
            "",
            "“Told you darkness has teeth,” he says, nodding at your lantern.",
            "“You planning to bite back or run?”",
        ],
        choices=[
            Choice("Ask Morrow to guide you to the Root Gate.", "root_gate",
                   effect=lambda s: set_flag(s, "morrow_guided", True)),
            Choice("Rest for a moment (restore 1 hp).", "smoke_breeze",
                   effect=lambda s: s.__setattr__("hp", min(3, s.hp + 1))),
            Choice("Return to the fungus fork.", "fungus_fork"),
        ],
    )

    scenes["daylight_exit"] = Scene(
        title="FAINT DAYLIGHT",
        lines=[
            "You climb toward the pale promise of daylight.",
            "Roots thin out. Concrete cracks. You find an iron grate.",
            "",
            "Above: the city. Below: the story you haven’t finished.",
        ],
        choices=[
            Choice("Leave now (end the adventure).", "leave_good"),
            Choice("Go back. You’re not done.", "fungus_fork"),
        ],
    )

    scenes["leave_good"] = Scene(
        title="SURFACE",
        lines=[
            "You slip out into daylight, blinking like a newborn rumor.",
            "The city looks ordinary, which is the biggest lie it tells.",
            "",
            "THE END (You lived. For now.)",
        ],
        choices=[],
    )

    scenes["root_gate"] = Scene(
        title="THE ROOT GATE",
        lines=[
            "You arrive at a circular stone door braided with thick roots.",
            "At the center is a handprint-shaped depression, like the door wants a promise.",
            "",
            "A whisper comes from the roots: “FOUNDATION… KEEPER…”",
        ],
        choices=[
            Choice("Place your hand in the depression.", "handprint"),
            Choice("Use the compass to align a hidden notch (if you have compass).", "compass_align",
                   condition=lambda s: has(s, "compass")),
            Choice("Back away.", "fungus_fork"),
        ],
    )

    scenes["handprint"] = Scene(
        title="THE PROMISE",
        lines=[
            "The stone is cold enough to sting.",
            "Roots tighten, not to hurt—just to test you.",
            "",
            "A voice, not quite Morrow’s: “Will you keep what the city forgets?”",
        ],
        choices=[
            Choice("Say yes. Accept the role.", "ending_keeper",
                   effect=lambda s: set_flag(s, "keeper", True)),
            Choice("Say no. You’re just passing through.", "ending_witness",
                   effect=lambda s: set_flag(s, "witness", True)),
        ],
    )

    scenes["compass_align"] = Scene(
        title="TRUE NORTH, TRUE DOWN",
        lines=[
            "The compass needle spins once, then points *down*.",
            "You rotate a hidden notch to match it.",
            "",
            "The Root Gate loosens, impressed by your weird sense of direction.",
        ],
        choices=[
            Choice("Enter the Root Gate.", "inside_gate",
                   effect=lambda s: set_flag(s, "gate_open", True)),
        ],
    )

    scenes["inside_gate"] = Scene(
        title="INSIDE THE GATE",
        lines=[
            "Beyond the door is a chamber filled with quiet technology—old pumps, new cables.",
            "This isn’t just tunnels. It’s infrastructure. A hidden skeleton.",
            "",
            "Morrow steps from the shadows. “So you found it.”",
            "“One last choice. What do we do with what we know?”",
        ],
        choices=[
            Choice("Expose it to the surface world (risk chaos).", "ending_expose"),
            Choice("Help Morrow maintain it (protect the city quietly).", "ending_keeper"),
        ],
    )

    scenes["ending_expose"] = Scene(
        title="THE DISCLOSURE",
        lines=[
            "You take photos. Notes. Coordinates.",
            "Truth spreads fast when it’s spicy, not when it’s important.",
            "",
            "Soon the tunnels fill with curious feet and careless hands.",
            "Some doors should be opened. Some should be understood first.",
            "",
            "THE END (Disclosure Ending).",
        ],
        choices=[],
    )

    scenes["ending_keeper"] = Scene(
        title="KEEPER OF THE FOUNDATION",
        lines=[
            "You don’t become a hero.",
            "You become something rarer: a caretaker.",
            "",
            "Morrow nods once, solemn as a bolt tightened properly.",
            "“Welcome to the line beneath the lines.”",
            "",
            "THE END (Keeper Ending).",
        ],
        choices=[],
    )

    scenes["ending_witness"] = Scene(
        title="JUST A WITNESS",
        lines=[
            "You step back. The roots release you with a soft sigh.",
            "The door seals again, content to remain a rumor.",
            "",
            "Morrow watches you go. “Fair,” he says. “Not everyone wants a second job.”",
            "",
            "THE END (Witness Ending).",
        ],
        choices=[],
    )

    return scenes


# ---------- Main Loop ----------

def run_game():
    scenes = build_scenes()
    state = GameState()

    current = "start"

    print("\n=== MOLE MAN: STORYBOARD LINE GAME ===\n")
    while True:
        if current not in scenes:
            print(f"Missing scene: {current}. Game over.")
            return

        scene = scenes[current]

        # run on_enter
        if scene.on_enter:
            scene.on_enter(state)

        # HUD-ish info (lightweight)
        inv = ", ".join(sorted(state.inventory)) if state.inventory else "—"
        print(f"[{scene.title}]   HP:{state.hp}   Inventory:{inv}\n")

        say(scene.lines)

        # end scenes
        available = []
        for ch in scene.choices:
            if ch.condition is None or ch.condition(state):
                available.append(ch)

        if not available:
            # no choices -> end
            return

        # Build menu
        menu = [(str(i), c.text) for i, c in enumerate(available, start=1)]
        picked_key = prompt_choice(menu)
        picked_index = int(picked_key) - 1
        choice = available[picked_index]

        # apply effect
        if choice.effect:
            choice.effect(state)

        # losing condition (optional)
        if state.hp <= 0:
            print("[YOU’RE OVERWHELMED]\n")
            say([
                "Your lantern sputters out.",
                "The tunnel doesn’t rush you—just patiently lets you forget which way is up.",
                "",
                "THE END (Lost Ending)."
            ])
            return

        current = choice.next_scene


if __name__ == "__main__":
    run_game()

