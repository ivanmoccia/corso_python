import random
import json
import os

with open("C:\\Users\\Ivan\\Desktop\\Projects\\flash_cards\\inglese.json") as dizionario_lingua:
    flash_cards = dict(json.loads(dizionario_lingua.read()))

list_keys = list(flash_cards.keys())
random.shuffle(list_keys)

for i in list_keys:
    answer = ""

    while answer != flash_cards[i]:
        answer = input(f"Cosa vuol dire {i}: ")

        if answer == flash_cards[i]:
            print('Giusto!')
        else:
            print('Sbagliato!')
