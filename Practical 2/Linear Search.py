arr = list(map(int, input("Enter numbers: ").split()))

key = int(input("Enter the number to search: "))

found = False

for i in range(len(arr)):
    if arr[i] == key:
        print("Element found at position", i + 1)
        found = True
        break

if not found:
    print("Element not found")