# This main.py script is the beginning point of the program; it is the "landing page" of the program

# To run this Reading Files program, press run on this file!

# All the below import statements import the functions from the other files and make them available in this function
from createNewFileFunction import createNewFile
from readAveragesFunction import readAverages
from updateFileFunction import updateFile
from readFileFunction import readFile
from graphFileFunction import graphFile

# This is a library present in the operating system (os) that detects if a filepath exists
from os.path import exists

print("Welcome to this weird numbers program!")

# The "Reading Files/" addon is for if this program is located in a file named Reading Files
# Change it accordingly!
filename = "Reading Files/" + input("What's the name of the file you'd like to open? ") + ".txt"

while True:
    # If the file does not exist, it uses the createNewFile function to make it exist
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
        
