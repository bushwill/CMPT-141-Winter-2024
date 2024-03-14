def spaceTime(distance_in_meters):
    if distance_in_meters<=1:
        return 1
    return spaceTime(distance_in_meters/2)+1



print(spaceTime(10))