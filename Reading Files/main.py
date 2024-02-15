# This program makes a file of 50 numbers, and at the beginning prints the mean and median averages.

from createNewFileFunction import createNewFile
from readAveragesFunction import readAverages
from updateFileFunction import updateFile
from readFileFunction import readFile
from graphFileFunction import graphFile

from os.path import exists

print("Welcome to this weird numbers program!")
filename = "Reading Files/" + input("What's the name of the file you'd like to open? ") + ".txt"

while True:
    if not exists(filename):
        print("File doesnt exist, creating new file named " + filename + "...")
        createNewFile(filename)
    print("What would you like to do?")
    print("[New] Create new file!")
    print("[A] Read the averages from " + filename)
    print("[B] Update the numbers in " + filename)
    print("[C] Read " + filename + " file")
    print("[D] Graph file " + filename)
    print("[Quit] Quit the program")
    
    decision = input("Select a function: ")

    if decision == "New" or decision == "new":
        filename = "Reading Files/" + input("What's the name of the new file? ") + ".txt"
        result = createNewFile(filename)
        if result:
            print("\n~~~~~~~~~~~~~~~~~~~~| File created successfully! |~~~~~~~~~~~~~~~~~~~~\n")

    elif decision == "A" or decision == "a":
        median, mean = readAverages(filename)
        print("~~~~~~~~~~~~~~~~~~~~|", median)
        print("~~~~~~~~~~~~~~~~~~~~|", mean)
        
    elif decision == "B" or decision == "b":
        result = updateFile(filename)
        if result:
            print("\n~~~~~~~~~~~~~~~~~~~~| File updated successfully! |~~~~~~~~~~~~~~~~~~~~\n")
        else:
            print("~~~~~~~~~~~~~~~~~~~~| Error!", filename, "does not exist |~~~~~~~~~~~~~~~~~~~~")
        
    elif decision == "C" or decision == "c":
        result = readFile(filename)
        print("\n~~~~~~~~~~~~~~~~~~~~", filename, "~~~~~~~~~~~~~~~~~~~~~~~")
        for line in result:
            print(line)
        print("~~~~~~~~~~~~~~~~~~~~| end of file |~~~~~~~~~~~~~~~~~~~~~~~\n")
        
    elif decision == "D" or decision == "d":
        if graphFile(filename):
            print("\n~~~~~~~~~~~~~~~~~~~~| file graphed successfully! |~~~~~~~~~~~~~~~~~~~~~~~\n")
        
    elif decision == "Quit" or decision == "quit":
        print("See ya later")
        print("Program ended successfully.")
        break
        
    else:
        print("Invalid decision, try again.")
        
