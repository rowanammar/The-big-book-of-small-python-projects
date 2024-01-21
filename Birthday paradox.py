from random import *
from datetime import *

x = 0
MatchingCounter = 0


def generateBirthdays():
    duplicate = False
    birthdays = []
    global x, MatchingCounter
    for i in range(0, int(x)):
        YearStart = datetime(2005, 1, 1)
        # Get a random number of days into the year
        randomNumberOfDays = timedelta(randint(0, 364))
        # Add the random number of days to the start of the year
        birthday = YearStart + randomNumberOfDays
        birthdays.append(birthday)

    if len(birthdays) != len(set(birthdays)):
        # puts the elements in a set , therefore removing the duplicates , so if the length is the same , no duplicates
        duplicate = True

    if duplicate:
        MatchingCounter += 1


def main():
    global x

    print('''
    The Birthday Paradox shows us that in a group of N people, the odds
    that two of them have matching birthdays is surprisingly large.
    This program does a Monte Carlo simulation (that is, repeated random  simulations) to explore this concept.
    (It's not actually a paradox, it's just a surprising result.) ''')

    x = input("Enter number of dates to be generated : ")

    s = input("Enter number of simulations to run an analysis : ")
    for i in range(int(s)):
        generateBirthdays()

    probability = round(MatchingCounter / int(s) * 100, 2)
    print("Matching birthdays were found {} times!".format(MatchingCounter))
    print("That means there is a {}% chance!".format(probability))


if __name__ == "__main__":
    main()
