arr = list(map(int, input("Enter numbers: ").split()))

for i in range(len(arr)):
    min_index = i

    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j

    # Swap
    arr[i], arr[min_index] = arr[min_index], arr[i]

print("Sorted array:", arr)