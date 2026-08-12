
print("================================")
print("       BIG FACTORIAL")
print("================================")

n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")

else:
    factorial = 1

    for i in range(1, n + 1):
        factorial = factorial * i

    print()
    print("Number =", n)
    print("Factorial =", factorial)

    print()
    print("Number of digits:", len(str(factorial)))