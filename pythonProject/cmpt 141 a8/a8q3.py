# Will Bushell
# This is meant to help with assignment 8 question 3

# This is a simpler question than you might think, don't overcomplicate it
# It has a lot of comparisons, and you will essentially be trying every treasure combination possible.

# The recursive function should return the best possible value that can fit in the available space

# For each treasure in the list...

"""
If treasure list length is 0, return 0
Test the first treasure, if it cant fit, recurse with the rest of the list excluding this first treasure
If it can:
    Compare the current treasure value with the return value of recursively calling the function again 
    with the rest of the list excluding the first treasure

    Return the greater value
"""

