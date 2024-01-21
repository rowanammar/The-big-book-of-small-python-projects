import random
from random import *

print('''
This is a bluffing game for two human players. Each player has a box.
One box has a carrot in it. To win, you must have the box with the
carrot in it.

This is a very simple and silly game.

The first player looks into their box (the second player must close
their eyes during this). The first player then says "There is a carrot
in my box" or "There is not a carrot in my box". The second player then
gets to decide if they want to swap boxes or not.

''')

player1 = input("Enter first player's name  : ")
player2 = input("Enter second player's name : ")

print('''
   +-----------+      +----------+ 
  /           /|     /          /|
 /           / |    /          / |
+-----------+  +   +----------+  +
|  Red Box  | /   | Gold Box |  /
|           |/    |          | / 
+-----------+     +----------+
''')

print(f"{player1}, you have the red box. {player2}, you have the gold box.\n {player2} please close your eyes.")
input("Press enter to continue...")

carrot = randint(1, 2)
if carrot == 1:
    print('''
       +___________+
       |           |
       |           |
       |           |
       +---_V_----+      +----------+ 
      /    \ /    /|     /          /|
     /      v     / |    /          / |
    +-----------+  +   +----------+  +
    |  Red Box  | /   | Gold Box |  /
    |           |/    |          | / 
    +-----------+     +----------+

    ''')
else:
    print('''

             +___________+
             |           |
             |           |
             |           |
             +-----------+      +----------+ 
            /           /|     /          /|
           /           / |    /          / |
          +-----------+  +   +----------+  +
          |  Red Box  | /   | Gold Box |  /
          |           |/    |          | / 
          +-----------+     +----------+

          ''')

input("Press enter to continue...")
print('\n' * 100)
x = input(f"{player2}, do you want to swap boxes? (y/n) : ").upper()
swap = True if x == 'Y' else False
if carrot == 1 and not swap:
    print(f"{player1} wins!")
elif carrot == 1 and swap:
    print(f"{player2} wins!")
elif carrot == 2 and not swap:
    print(f"{player2} wins!")
else:
    print(f"{player1} wins!")
