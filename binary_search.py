def binary_search(arr, value, low, high):

    mid = (low + high) // 2

    if low <= high:
        if arr[mid] == value:
            return mid
        elif arr[mid] < value:
            return binary_search(arr, value, mid +1, high)
        else:
            return binary_search(arr, value, low, mid-1)
    else:
        return -1

arr = [1, 3, 5, 7, 9, 10, 12, 15, 18, 20]
value = int(input("Enter the value to search for : "))

result = binary_search(arr, value, 0, len(arr)-1)

if result != -1:
    print("The value is present at index : ", str(result))
else:
    print("The element is not present in the array")