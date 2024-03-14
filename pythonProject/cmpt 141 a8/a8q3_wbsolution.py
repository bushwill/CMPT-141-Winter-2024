def read_data(filename):
    """ reads in data about treasures.
    Each treasure has a name, value, and weight
    
    filename: string. Name of a CSV file where treasures
        are listed 1 per line.
    return: a list of records (dictionaries). Each record
        has the keys "name", "value", and "weight"
    """
    f = open(filename, 'r')
    L = []
    for line in f:
        line = line.rstrip().split(",")
        treasure = {"name": line[0],
                    "value": int(line[1][1:]),
                    "weight": int(line[2]) }
        L.append(treasure)
    return L

def best_profit(remaining_treasures, remaining_space):
    if len(remaining_treasures) == 0:
        return 0
    if remaining_treasures[0]['weight'] > remaining_space:
        return best_profit(remaining_treasures[1:], remaining_space)
    return max(remaining_treasures[0]['value'] + best_profit(remaining_treasures[1:], remaining_space-remaining_treasures[0]['weight']),
               best_profit(remaining_treasures[1:], remaining_space))

file = "room1.txt"    
treasures = read_data(file)
print('Room1 with 100 space:', best_profit(treasures, 100))

file = "room2.txt"    
treasures = read_data(file)
print('Room2 with 100 space:', best_profit(treasures, 100))

file = "room3.txt"    
treasures = read_data(file)
print('Room3 with 100 space:', best_profit(treasures, 100))

file = "room3.txt"    
treasures = read_data(file)
print('Room3 with 300 space:', best_profit(treasures, 300))

