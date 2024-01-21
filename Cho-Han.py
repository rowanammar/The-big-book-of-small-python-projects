import random
from random import *

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN', 4: 'SHI', 5: 'GO', 6: 'ROKU'}
Money = 5000

print(f'''
In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.
Betting on snake eyes(two ones) pays 6 times the original bet.
You have : {Money} won
''')
while True:
    while True:
        try:
            bet = int(input("How much do you bet? "))
            if 0 < bet <= Money:
                break
            else:
                print("Please enter a valid bet")
        except ValueError:
            print("Please enter a number")

    Money -= bet
    dice1 = randint(1, 2)
    dice2 = randint(1, 2)
    choice = input("What is your bet ?\n\t\tCHO (even) or HAN (odd) ?\n").upper()
    while choice != "CHO" and choice != "HAN":
        choice = input("Please enter a valid bet\n\t\tCHO (even) or HAN (odd) ?\n").upper()
    snake = ''
    if Money >= bet:
        snake = input("Do you want to bet on a snake's eye? Yes/No ").upper()

    print(f"THE DICE :\n\t\t{JAPANESE_NUMBERS[dice1]} - {JAPANESE_NUMBERS[dice2]}\n\t\t {dice1} - {dice2}")
    if snake == "YES":
        Money -= bet
        snakes = True if (dice1 + dice2 == 2) else False
        if snakes:
            Money += bet * 6
            print(f"It was a snake's eye!\nMoney = {Money}")

    if (((dice1 + dice2) % 2 == 0) and choice == "CHO") or (((dice1 + dice2) % 2 != 0) and choice == "HAN"):
        Money += bet * 2
        print(f"You won the bet!\nMoney= {Money}")
    else:
        print(f"You lost the bet!\nMoney= {Money}")

    if Money == 0:
        print("You're broke!")
        break
