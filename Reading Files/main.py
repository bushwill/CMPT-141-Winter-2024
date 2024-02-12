# This program makes a file of 50 numbers, and at the beginning prints the mean and median averages.

from createNewFileFunction import createNewFile
from readAveragesFunction import readAverages
from updateFileFunction import updateFile
from readFileFunction import readFile

filename = "Reading Files/numbers.txt"

print("Welcome to this weird numbers program!")
while True:
    print("What would you like to do?")
    print("[New] Create new file!")
    print("[A] Read the averages from " + filename)
    print("[B] Update the numbers in " + filename)
    print("[C] Read all values from " + filename)
    print("[Quit] Quit the program")
    
    decision = input("Select a function: ")

    if decision == "New" or decision == "new":
        result = createNewFile(filename)
        if result:
            print("~~~~~~~~~~~~~~~~~~~~| File created successfully! |~~~~~~~~~~~~~~~~~~~~")

    elif decision == "A" or decision == "a":
        median, mean = readAverages(filename)
        print("~~~~~~~~~~~~~~~~~~~~|", median)
        print("~~~~~~~~~~~~~~~~~~~~|", mean)
        
    elif decision == "B" or decision == "b":
        result = updateFile(filename)
        if result:
            print("~~~~~~~~~~~~~~~~~~~~| File updated successfully! |~~~~~~~~~~~~~~~~~~~~")
        else:
            print("~~~~~~~~~~~~~~~~~~~~| Error!", filename, "does not exist |~~~~~~~~~~~~~~~~~~~~")
        
    elif decision == "C" or decision == "c":
        result = readFile(filename)
        print("\n~~~~~~~~~~~~~~~~~~~~", filename, "~~~~~~~~~~~~~~~~~~~~~~~")
        for line in result:
            print(line)
        print("~~~~~~~~~~~~~~~~~~~~| end of file |~~~~~~~~~~~~~~~~~~~~~~~\n")
        
    elif decision == "Quit" or decision == "quit":
        print("See ya later")
        print("Program ended successfully.")
        break
        
    else:
        print("Invalid decision, try again.")
        
