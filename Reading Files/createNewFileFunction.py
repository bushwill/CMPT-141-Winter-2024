# This function creates a brand new file named filename!

import random as r

def createNewFile(filename):    
    newFile = open(filename, "w")
    newFile.write("Here are a bunch of random arbitrary numbers: \n")
    
    # A dictionary that maps a number key to a instance number value. If the number '50' is in
    # the file 3 times, 3 will be mapped to 50. 
    # This is important to collect the median(s)
    randomNumbersDict = {}
    
    # This list collects all numbers in their original order
    randomNumbersList = []
    sum = 0
    for i in range(51):
        number = r.randint(1, 100)
        randomNumbersList.append(number)
        if number in randomNumbersDict.keys():
            randomNumbersDict[number] += 1
        else:
            randomNumbersDict[number] = 1
        sum += number
    
    # This for comprehension makes the median list named "median"
    median = [x for x in randomNumbersDict.keys() if randomNumbersDict[x] == max(randomNumbersDict.values())]
    
    # If there are more than one median, we appropriately make the word plural
    if len(median) > 1:
        newFile.write("Medians: " + str(median).strip("[]") + "   ")
    else:
        newFile.write("Median: " + str(median).strip("[]") + "   ")
    newFile.write("Mean: " + str(sum/50))
    
    for number in randomNumbersList:
        newFile.write(str(number) + "\n")
        
    return True