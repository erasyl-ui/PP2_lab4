# Generator to iterate numbers divisible by 3 and 4 between 0 and n
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter the upper limit n: "))

print("Numbers divisible by 3 and 4 between 0 and", n, ":")
for num in divisible_by_3_and_4(n):
    print(num, end=" ")

# Example:
# If user inputs 30, the output will be:
# Numbers divisible by 3 and 4 between 0 and 30:
# 0 12 24
