def linear_search(arr, value, n):
    for i in range(0, n):
        if value == arr[i]:
            return i
    return -1

arr = [1, 3, 4, 5, 6, 8, 9, 11]
value = int(input("Enter value to search for : "))

result = linear_search(arr, value, len(arr))

if result != -1:
    print("the entered value is at index", result)
else:
    print("Entered value is not present in array")