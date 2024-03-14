# Will Bushell
# This is meant to help with assignment 8 question 4
# This is a fairly challenging question for everyone, don't lose motivation, give this question some time

# This question employs something called tree recursion, where a function makes multiple recursive calls, creating tree-like branches


# Example book:
"""
"eevee" : ["jolteon", "flareon", "vaporeon"],
    "jolteon" : ["zapdos"],
    "vaporeon" : ["articuno"],
    "flareon" : ["moltres"]
"""
#             eevee
#          /    |    \
#       /       |       \
# jolteon     flareon     vaporean
#    |          |            |
#    |          |            |
# zapdos      moltres     articuno
"""
This shows the tree structure you need to recursively follow,
if you wanted to find the evolution from eevee to moltres, you'd 
have to search each branch until you find it.
"""
### You will have to have a loop inside the recursive function to check each available branch ###
