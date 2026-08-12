5n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    num = int(input(f"Enter element {i + 1}: "))
    arr.append(num)


for i in range(n - 1):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted array:", arr)