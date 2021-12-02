def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

test_arr = [0, 9, 8, 1, 2, 6, 7, 3, 4, 5]
bubble_sort(test_arr)
print(test_arr)