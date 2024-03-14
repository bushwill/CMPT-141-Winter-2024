# Will Bushell, abc123, 12345678, Jeffrey Long
# this is designed to help with question 3 of A4

user_input = ""
bug_list = []
while(user_input != "ladybug"):
    user_input = input("Enter a bug that is not a ladybug: ")
    if user_input != "ladybug":
        bug_list.append(user_input.upper())
print("You entered a ladybug.")
print("Here are the cool bugs you entered: ", bug_list)

loved_bugs = []
hated_bugs = []
print("Here is your remaining list of bugs:", bug_list)
response = input("Do you love any of these bugs? (y/n) ")
while response == 'y':
    user_input = input("Which bug do you love: ")
    bug_list.remove(user_input.upper())
    loved_bugs.append(user_input.upper())
    print("Here is your remaining list of bugs:", bug_list)
    response = input("Do you love any more of these bugs? (y/n) ")
response = 'y'
while response == 'y':
    user_input = input("Which bug do you hate: ")
    bug_list.remove(user_input.upper())
    hated_bugs.append(user_input.upper())
    print("Here is your remaining list of bugs:", bug_list)
    response = input("Do you hate any more of these bugs? (y/n) ")
hated_bugs.append("LADYBUG")
print("Here are your loved bugs:", loved_bugs)
print("Here are your hated bugs:", hated_bugs)
print("Here are your unsorted bugs:", bug_list)
