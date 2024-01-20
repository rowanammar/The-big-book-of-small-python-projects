alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
message = input("Enter the encrypted Caesar cipher message to hack :\n").upper()

for key in range(0, 27):
    output = ""
    for letter in message:
        if letter in alphabet:
            output = output + alphabet[(alphabet.index(letter) - key) % len(alphabet)]
        else:
            output = output + letter
    print("key #{}:  ".format(key), output)
