def readFile(filename):
    file = open(filename, "r")
    fileContents = []
    for line in file:
        fileContents.append(line.strip("\n"))
        
    return fileContents