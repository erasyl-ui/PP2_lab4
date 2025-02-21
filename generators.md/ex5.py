# Generator to return all numbers from n down to 0
def countdown(n):
    for i in range(n, -1, -1):
        yield i

n = int(input("Enter start number n: "))

print("Countdown from", n, "to 0:")
for num in countdown(n):
    print(num, end=" ")

# Example:
# If user inputs 5, the output will be:
# Countdown from 5 to 0:
# 5 4 3 2 1 0
