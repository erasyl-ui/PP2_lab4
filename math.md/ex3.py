# Calculate the area of a regular polygon
import math

def polygon_area(sides, side_length):
    return (sides * side_length ** 2) / (4 * math.tan(math.pi / sides))

sides = int(input("Input number of sides: "))
side_length = float(input("Input the length of a side: "))

print("The area of the polygon is:", round(polygon_area(sides, side_length), 2))

# Example:
# Input number of sides: 4
# Input the length of a side: 25
# The area of the polygon is: 625
