# This function reads the averages on line 2 of the file
# Important to note it utilizes the readFile() function!

from readFileFunction import readFile

def readAverages(filename):
    averages = readFile(filename)[1]
    averages = averages.rsplit("Mean")
    median = averages[0]
    mean = averages[-1]
    mean = "Mean" + mean    
    return median, mean
