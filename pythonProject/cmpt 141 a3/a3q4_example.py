# Will Bushell, abc123, 12345678, Jeffrey Long
# this is designed to help with question 4 of A3

import random       # need to import the library random

print("Let's simulate a fun game with dice!")
user_input = input("[y/n] ")

while user_input == "y":
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    print("Player 1's roll:", roll1)
    print("Player 2's roll:", roll2)

    if roll1 > roll2:
        print("Player 1 wins!")
    elif roll1 == roll2:
        print("Both players tied!")
    else:
        print("Player 2 wins!")

    user_input = input("Play again? [y/n] ")

    