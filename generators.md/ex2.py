# Generator to print even numbers between 0 and n in comma-separated form
def even_generator(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input("Enter the upper limit n: "))

print("Even numbers between 0 and", n, ":")
print(",".join(map(str, even_generator(n))))

# Example:
# If user inputs 10, the output will be:
# Even numbers between 0 and 10:
# 0,2,4,6,8,10
