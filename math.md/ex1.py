# Convert degree to radian
import math

def degree_to_radian(degree):
    return degree * (math.pi / 180)

degree = float(input("Input degree: "))
print("Output radian:", round(degree_to_radian(degree), 6))

# Example:
# Input degree: 15
# Output radian: 0.261799
