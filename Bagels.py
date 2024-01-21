from random import *

GuessCounter = 0


def play():
    global GuessCounter
    CorrectNumber = str(randint(100, 999))
    GuessCounter = 0
    solution = False
    for i in range(0, 10):
        print("Guess #{}".format(GuessCounter + 1))
        Guess = str(input())
        if Guess == CorrectNumber:
            print("Correct!!!")
            solution = True
            break
        CorrectDigit = False
        for j in range(len(CorrectNumber)):
            if Guess[j] == CorrectNumber[j]:
                print("Fermi")
                CorrectDigit = True
            elif Guess[j] in CorrectNumber:
                print("Pico")
                CorrectDigit = True
        if not CorrectDigit:
            print("Bagels")
        GuessCounter += 1

    if not solution:
        print("The correct number was {}! Better luck next time!".format(CorrectNumber))


def main():
    print('''I am thinking of a 3-digit number. Try to guess what it is.
    Here are some clues:
    When I say:          That means:
    Pico                  One digit is correct but in the wrong position.
    Fermi                 One digit is correct and in the right position.
    Bagels                No digit is correct.
    I have thought up a number.
    You have 10 guesses to get it.''')
    while True :
        play()
        x = input("Do u want to play again? Y/N\n")
        if x.lower() != 'y':
            break


if __name__ == "__main__":
    main()
