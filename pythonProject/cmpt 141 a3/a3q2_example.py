# Will Bushell, abc123, 12345678, Jeffrey Long
# this is designed to help with question 2 of A3

import random       # need to import the libraries random

number = random.randint(1, 10000)               # this includes the number 1, and 10000
print("Your random number:", number)
if number % 2 == 0:                                  # number % 2 == 0 means number is
    print("Your number is even!")                    # divisible by 2 with 0 remainder (even)
else:
    print("Your number is odd.. yikes")

number = random.randint(1, 10000)           # I just have the code copied and
print("Your random number:", number)             # pasted to run twice
if number % 2 == 0:
    print("Your number is even!")
else:
    print("Your number is odd.. yikes")
