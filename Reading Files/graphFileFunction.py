import matplotlib.pyplot as plt
from readFileFunction import readFile

def graphFile(filename):
    numbers = readFile(filename)[2:]
    plt.figure()
    plt.title("Graph Title! XD")
    plt.xlabel("Number Order")
    plt.ylabel("Number Magnitude")
    for number in range(0, 50):
        plt.plot(number, int(numbers[number]), "g.")
    plt.show()
    return True