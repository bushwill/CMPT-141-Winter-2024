# Lab 5 Checkpoint

# Write a program that asks the user to INPUT any string. Then, it counts
# how many of the characters in that string are VOWELS (i.e. a, e, i, o or u) 
# and prints out that count.

# user INPUT any string
str_input = input("Enter a string: ")

vowels = "AeIOUaeiou"
vowel_count = 0

for char in str_input:
    if char in vowels:
        vowel_count += 1

print("There are", vowel_count, "vowels in", str_input)
