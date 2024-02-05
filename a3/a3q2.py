def cube(number):
    # Calculate the cube root of the number
    cube_root = round(number ** (1/3))
    
    # Check if the cube root raised to the power of 3 is equal to the original number
    return cube_root ** 3 == number

x = 125
print("Is", x, "a perfect cube? ", cube(x))
