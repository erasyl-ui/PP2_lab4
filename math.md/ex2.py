# Calculate the area of a trapezoid
def trapezoid_area(height, base1, base2):
    return 0.5 * (base1 + base2) * height

height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

print("Expected Output:", trapezoid_area(height, base1, base2))

# Example:
# Height: 5
# Base, first value: 5
# Base, second value: 6
# Expected Output: 27.5
