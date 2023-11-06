# Recursive Function


# def factorail(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorail(n - 1)


# print(factorail(3))

# Fibonacci numbers
# f0=0
# f1=1

# fn = f(n-1)+f(n-2)


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter the number of Fibonacci numbers to print: "))
for i in range(n):
    print(fibonacci(i), end=" ")
