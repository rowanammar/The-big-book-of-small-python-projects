from random import *
import random
OBJECT_PRONOUNS = ['Her', 'Him', 'Them']
POSSESIVE_PRONOUNS = ['Her', 'His', 'Their']
PERSONAL_PRONOUNS = ['She', 'He', 'They']
STATES = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania',
'Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan']
NOUNS = ['Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent',
'Cat', 'Dog', 'Chicken', 'Robot', 'Video Game', 'Avocado',
'Plastic Straw','Serial Killer', 'Telephone Psychic']
PLACES = ['House', 'Attic', 'Bank Deposit Box', 'School', 'Basement',
'Workplace', 'Donut Shop', 'Apocalypse Bunker']
WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week']
verbs = [
    "announce",
    "reveal",
    "report",
    "discuss",
    "explain",
    "present",
    "share",
    "promote",
    "celebrate",
    "introduce",
    "highlight",
    "emphasize",
    "underscore",
    "proclaim",
    "declare",
    "affirm",
    "expose",
    "unveil",
    "demonstrate",
    "show"
]

while True:
    numHeadlines = input('Enter the number of headlines to generate: ')
    if numHeadlines.isdecimal() and (0 < int(numHeadlines)):
        break
    print('Please enter a number greater than 0.')

for i in range(int(numHeadlines)) :
    print(f'''
    headline #{i+1} {choice(NOUNS) + 's'} {choice(verbs)} {choice(STATES)} {choice(PLACES)} {choice(WHEN)}?
    ''')