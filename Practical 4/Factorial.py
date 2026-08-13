def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative(n):
    factorial = 1

    for i in range(1, n + 1):
        factorial *= i

    return factorial


n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial using recursion :", factorial_recursive(n))
    print("Factorial using iteration :", factorial_iterative(n))