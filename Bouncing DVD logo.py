from random import *
import bext, os, time, random

os.system('cls')
#### NOTE : Run this code in terminal not in an IDE :)####
width, height = bext.size()
direction = "downright"
x = random.randint(0, width - 4)
y = random.randint(0, height - 4)
colors = ['red', 'green', 'yellow', 'blue', 'purple', 'cyan', 'white']
while True:
    bext.clear()
    bext.hide_cursor()
    bext.goto(x, y)
    print('DVD', end='')
    time.sleep(0.2)
    if y == height - 1:
        bext.fg(choice(colors))
        if direction == "downright":
            direction = "upright"
        elif direction == "downleft":
            direction = "upleft"
    if x == width - 4 or x == width - 3 or x == width - 2 :
        bext.fg(choice(colors))
        if direction == "upright":
            direction = "upleft"
        elif direction == "downright":
            direction = "downleft"
    if y == 0:
        bext.fg(choice(colors))
        if direction == "upright":
            direction = "downright"
        elif direction == "upleft":
            direction = "downleft"
    if x == 0 or x == 1 or x == 2:
        bext.fg(choice(colors))
        if direction == "downleft":
            direction = "downright"
        elif direction == "upleft":
            direction = "upright"

    if direction == "downright":
        x += 2
        y += 1
    elif direction == "upleft":
        x -= 2
        y -= 1
    elif direction == "upright":
        x += 2
        y -= 1
    elif direction == "downleft":
        x -= 2
        y += 1
