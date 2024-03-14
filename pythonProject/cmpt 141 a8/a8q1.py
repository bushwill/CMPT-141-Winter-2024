# Will Bushell
# This script is meant to help understand recursion for assignment 8 question 1

def fact(number):
    # Stop condition
    if (number == 0 or number == 1):
        return 1
    # Recursive condition (this is where you would divide the distance in half)
    else:
        return number * fact(number - 1)


print(fact(5))
