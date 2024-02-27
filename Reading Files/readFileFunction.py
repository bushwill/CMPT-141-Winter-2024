# This function reads all the data from a file (nothing too special)

def readFile(filename):
    file = open(filename, "r")
    fileContents = []
    for line in file:
        # Stripping the \n prevents it from being appended to the list of lines
        fileContents.append(line.strip("\n"))
        
    return fileContents