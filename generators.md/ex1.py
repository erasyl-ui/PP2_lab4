# Generator that generates the squares of numbers up to some number N
def square_generator(N):
    for i in range(N + 1):
        yield i ** 2

N = int(input("Enter the upper limit N: "))

print("Squares up to", N, ":")
for square in square_generator(N):
    print(square, end=" ")

# Example:
# If user inputs 5, the output will be:
# Squares up to 5:
# 0 1 4 9 16 25
