# Calculate the area of a parallelogram
def parallelogram_area(base, height):
    return base * height

base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

print("Expected Output:", parallelogram_area(base, height))

# Example:
# Length of base: 5
# Height of parallelogram: 6
# Expected Output: 30.0
