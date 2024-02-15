from readFileFunction import readFile

def readAverages(filename):
    averages = readFile(filename)[1]
    averages = averages.rsplit("Mean")
    median = averages[0]
    mean = averages[-1]
    mean = "Mean" + mean    
    return median, mean
