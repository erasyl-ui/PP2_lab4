# Generator to yield squares of numbers from a to b
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input("Enter start number a: "))
b = int(input("Enter end number b: "))

print(f"Squares of numbers from {a} to {b}:")
for square in squares(a, b):
    print(square, end=" ")

# Example:
# If user inputs a=3, b=6, the output will be:
# Squares of numbers from 3 to 6:
# 9 16 25 36
