import pyperclip

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
x = input('''
What do you want to do ?
E -> Encrypt
D -> Decrypt\n''').upper()
key = int(input("Enter key of encryption : "))

message = input("enter message to encrypt/decrypt : ").upper()
output = ""

for letter in message:
    if letter in alphabet:
        if x == "E":
            output = output + alphabet[(alphabet.index(letter) + key) % len(alphabet)]
        elif x == "D":
            output = output + alphabet[(alphabet.index(letter) - key) % len(alphabet)]

    else:
        output = output + letter
pyperclip.copy(output)
print(output, "\nText copied to clipboard")
