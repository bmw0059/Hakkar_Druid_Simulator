# 4 cards in deck, 1 corrupted blood
# play tog + 2 naturalize -> 5 card draw. What are the odds it kills at 30hp?

import random

DAMAGE = 3

# Change these as needed
HP = 30
FATIGUE = 1
CARDS = 3
BLOODS = 1

hp = HP
fatigue = FATIGUE
cards = CARDS
bloods = BLOODS


def draw():
    global hp
    global fatigue
    global cards
    global bloods

    if cards <= 0:
        takeFatigue()
        return
    else:
        r = random.randint(1, cards)
        if r <= bloods:
            hp = hp - 3
            cards = cards - 1
            bloods = bloods - 1
            draw()
            cards = cards + 2
            bloods = bloods + 2
    if cards != bloods:
        cards = cards - 1
    return

def takeFatigue():
    global hp
    global fatigue
    hp = hp - fatigue
    fatigue = fatigue + 1
    return

fail = 0
success = 0

for x in range(100000):
    for i in range(5):
        draw()
        #print hp
    print hp
    if hp > 0:
        fail = fail + 1
    else:
        success = success + 1
    hp = HP
    fatigue = FATIGUE
    cards = CARDS
    bloods = BLOODS

print ("\n\nFAILURES: %s", fail)
print ("\nSUCCESS: %s", success)
