farm = [['F', '_', 'G'], ['_', 'W', '_'], ['_', 'J', '_']]

def spring(farm):
    copy_farm = deep_copy(farm)
    for y in range(len(copy_farm)):
        for x in range(len(copy_farm)):
            if copy_farm[y][x] == '_':
                neighbours = set()
                if y-1 != -1:
                    neighbours.add(copy_farm[y-1][x])
                if y+1 != len(copy_farm):
                    neighbours.add(copy_farm[y+1][x])
                if x-1 != -1:
                    neighbours.add(copy_farm[y][x-1])
                if x+1 != len(copy_farm):
                    neighbours.add(copy_farm[y][x+1])
                neighbours.discard('_')
                neighbours.discard('M')
                if len(neighbours) == 0:
                    farm[y][x] = '_'
                elif len(neighbours) == 4:
                    farm[y][x] = 'M'
                elif 'J' in neighbours:
                    farm[y][x] = 'J'
                elif len(neighbours) == 1:
                    farm[y][x] = neighbours.pop()
                elif len(neighbours) == 3:
                    farm[y][x] = '_'
                elif 'F' in neighbours and 'G' in neighbours:
                    farm[y][x] = 'F'
                elif 'F' in neighbours and 'W' in neighbours:
                    farm[y][x] = 'W'
                elif 'W' in neighbours and 'G' in neighbours:
                    farm[y][x] = 'G'
    return farm

def deep_copy(farm):
    copy_farm = []
    for row in farm:
        copy_farm.append(row.copy())
    return copy_farm

print(farm)
print(spring(farm))