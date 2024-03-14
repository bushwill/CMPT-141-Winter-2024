# Will Bushell
# This is meant to help with assignment 8 question 2

# The first function will take a string representing a sentence and prepare it for your recursive function.
# I would convert the sentence into a list of words, 
# then have the recursive function place the first word of the list at the end of the return value

# Pseudocode example:

'''
function1(sentence):
    convert sentence(string) to list(list of words)
    recursion(list)

recursion(list):
    if list is empty:
        return empty string
    if list has one item:
        return one item
    else:
        return recursion(rest of list) + first word of list
''' 

# Hand tracing an example:

# sentence = "DO I CHOOSE YOU PIKACHU"
# after first function = ["DO", "I", "CHOOSE", "YOU", "PIKACHU"]
# after first recursive iteration(else statement) = ["I", "CHOOSE", "YOU", "PIKACHU"] + "DO"
# after second recursive iteration(else statement) = ["CHOOSE", "YOU", "PIKACHU"] + "I" + "DO"
# after third recursive iteration(else statement) = ["YOU", "PIKACHU"] + "CHOOSE" + "I" + "DO"
# after fourth recursive iteration(else statement) = ["PIKACHU"] + "YOU" + "CHOOSE" + "I" + "DO"
# after fifth recursive iteration(second if statement) = "PIKACHU" + "YOU" + "CHOOSE" + "I" + "DO"
# then everything returns and evaluates, giving "PIKACHU YOU CHOOSE I DO"