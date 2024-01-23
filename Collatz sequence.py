def collatz(number):
    if number == 1:
        return number
    else:
        if number % 2 == 0:
            print(int(number), end=' , ')
            return collatz(number / 2)
        else:
            print(int(number), end=' , ')
            return collatz(number * 3 + 1)


def main():
    print('''
The Collatz sequence is a sequence of numbers produced from a starting number n, following three rules:
1) If n is even, the next number n is n / 2.
2) If n is odd, the next number n is n * 3 + 1.
3) If n is 1, stop. Otherwise, repeat.
    ''')
    n = input("Enter a number: ")
    try:
        print(int(collatz(int(n))))
    except ValueError:
        print("Please enter an integer.")


main()
