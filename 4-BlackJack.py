from random import *
import sys

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
Money = 0
Bet = 0

# Define the ASCII art for each card
suits = [HEARTS, DIAMONDS, CLUBS, SPADES]
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10,
               'A': 10}

deck = []
fulldeck = []

for suit in suits:
    for value in values:
        space1 = " " if len(value) == 2 else "  "
        space2 = "    " if len(value) == 2 else "     "
        # f for formatting
        card = f"""
        ┌───────────┐
        │ {value}{space1}       │
        │           │
        │     {suit}     │
        │           │
        │  {space2}{value}   │
        └───────────┘
        """
        deck.append((card, card_values[value]))
        fulldeck.append((card, card_values[value]))


def Play():
    dealerpoints = 0
    playerpoints = 0
    global Money, deck, fulldeck, Bet
    if not deck:
        deck = fulldeck
    busted = False
    dealercard1 = choice(deck)
    deck.remove(dealercard1)
    dealercard2 = choice(deck)
    deck.remove(dealercard2)
    dealercard3 = (0, 0)
    dealercard4 = (0, 0)
    playercard3 = (0, 0)
    playercard4 = (0, 0)
    dealerhand = []
    playerhand = []

    print(f'''
Dealer's hand :
{dealercard1[0]}   
        ┌───────────┐
        │-----------│
        │-----------│
        │-----------│
        │-----------│
        │-----------│
        └───────────┘
''')
    playercard1 = choice(deck)
    deck.remove(playercard1)
    playercard2 = choice(deck)
    deck.remove(playercard2)
    print(f'''
    Your hand :
    {playercard1[0]}  {playercard2[0]}
    ''')
    dealerhand.append(dealercard1)
    dealerhand.append(dealercard2)
    playerhand.append(playercard1)
    playerhand.append(playercard2)

    while True:
        print('''
Make your move :
S -> Stand
H -> Hit
D -> Double Down   
Q -> Quit
''')
        move = input(">>").upper()
        while move not in ['S', 'H', 'D', 'Q']:
            print("Please enter a valid move")
            move = input(">>").upper()

        if not deck:
            deck = fulldeck
        if move == 'S':
            ##############
            print("Dealer's hand :")
            for card in dealerhand:
                print(card[0], end='')
            if int(dealercard1[1]) + int(dealercard2[1]) < 17:
                dealercard3 = choice(deck)
                deck.remove(dealercard3)
                dealerhand.append(dealercard3)
                print("Dealer's hand :")
                for card in dealerhand:
                    print(card[0], end='')
            if int(dealercard1[1]) + int(dealercard2[1]) + int(dealercard3[1]) < 17:
                dealercard4 = choice(deck)
                deck.remove(dealercard4)
                dealerhand.append(dealercard4)
                print("Dealer's hand :")
                for card in dealerhand:
                    print(card[0], end='')

            break
            #################
        if move == 'H':
            if playercard3 == 0:
                playercard3 = choice(deck)
                deck.remove(playercard3)
                playerhand.append(playercard3)
                print("Your hand :")
                for card in playerhand:
                    print(card[0], end='')
                if int(playercard1[1]) + int(playercard2[1]) + int(playercard3[1]) > 21:
                    busted = True
                    break
            else:
                playercard4 = choice(deck)
                deck.remove(playercard4)
                playerhand.append(playercard4)
                print("Your hand :")
                for card in playerhand:
                    print(card[0], end='')
                if int(playercard1[1]) + int(playercard2[1]) + int(playercard3[1]) + int(playercard4[1]) > 21:
                    busted = True
                    break

            #############
        if move == 'D':
            Money -= Bet
            Bet *= 2
            playercard3 = choice(deck)
            deck.remove(playercard3)
            playerhand.append(playercard3)
            print("Your hand :")
            for card in playerhand:
                print(card[0], end='')
            if int(playercard1[1]) + int(playercard2[1]) + int(playercard3[1]) > 21:
                busted = True
                break
            print("Dealer's hand :")
            for card in dealerhand:
                print(card[0], end='')
            if int(dealercard1[1]) + int(dealercard2[1]) < 17:
                dealercard3 = choice(deck)
                deck.remove(dealercard3)
                dealerhand.append(dealercard3)
                print("Dealer's hand :")
                for card in dealerhand:
                    print(card[0], end='')
            if int(dealercard1[1]) + int(dealercard2[1]) + int(dealercard3[1]) < 17:
                dealercard4 = choice(deck)
                deck.remove(dealercard4)
                dealerhand.append(dealercard4)
                print("Dealer's hand :")
                for card in dealerhand:
                    print(card[0], end='')
            break
            break
            #############
    if move == 'Q':
        print("Money = {}".format(Money))
        sys.exit()

    for i in dealerhand:
        dealerpoints += i[1]
    for i in playerhand:
        playerpoints += i[1]

    if busted:
        print("You busted!")
        print("Money = {}".format(Money))
        return 0
    if dealerpoints > 21:
        print("Dealer busted!")
        Money += Bet * 2
        print("Money = {}".format(Money))
        return 0
    if dealerpoints > playerpoints:
        print("You lost!")
        print("Money = {}".format(Money))
        return 0
    if dealerpoints < playerpoints:
        print("You won!")
        Money += Bet * 2
        print("Money = {}".format(Money))
        return 0
    if dealerpoints == playerpoints:
        print("It's a tie!")
        Money += Bet
        print("Money = {}".format(Money))
        return 0


def main():
    global Bet, Money
    Money = 5000
    print('''Rules :
• Try to get as close to 21 without going over.
• Kings, Queens, and Jacks are worth 10 points.
• Aces are worth 10 points.
• Cards 2 through 10 are worth their face value.
• (H)it to take another card.
• (S)tand to stop taking cards.
• On your first play, you can (D)ouble down to increase your bet
  but must hit exactly one more time before standing.
• In case of a tie, the bet is returned to the player.
• The dealer stops hitting at 17.
Money = {}'''.format(Money))
    Bet = int(input("Place your bet : "))
    while Bet <= 0 or Bet > Money:
        print("Please enter a valid number")
        Bet = int(input("Place your bet : "))
    while Money > 0:
        Money -= Bet
        Play()
    if Money <= 0:
        print("You're broke!")
        print("Good thing you weren't playing with real money.")
        return 0;
    return 0;


if __name__ == "__main__":
    main()
