import random as r

def createNewFile(filename):    
    newFile = open(filename, "w")
    newFile.write("Here are a bunch of random arbitrary numbers: \n")
    
    randomNumbersDict = {}
    randomNumbersList = []
    sum = 0
    for i in range(50):
        number = r.randint(1, 100)
        randomNumbersList.append(number)
        if number in randomNumbersDict.keys():
            randomNumbersDict[number] += 1
        else:
            randomNumbersDict[number] = 1
        sum += number
    
    median = [x for x in randomNumbersDict.keys() if randomNumbersDict[x] == max(randomNumbersDict.values())]
    if len(median) > 1:
        newFile.write("Medians: " + str(median).strip("[]") + "   ")
    else:
        newFile.write("Median: " + str(median).strip("[]") + "   ")
    newFile.write("Mean: " + str(sum/50))
    
    for number in randomNumbersList:
        newFile.write(str(number) + "\n")
        
    return True