# Will Bushell, abc123, 12345678, Jeffrey Long
# this is designed to help with question 1 of A4
def fibonacci(n):
    # Two mathematical special cases that must be considered
    if n == 1:
        return 1
    elif n == 2:
        return 1
    # Follows is the correct fibonacci sequence formula:
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


result = 0
n = 1

while result < 144:
    result = fibonacci(n)
    print(f"The", n, "number in the Fibonacci sequence is:", result)
    n = n+1

print("Goodbye!")
