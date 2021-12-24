# def quick_sort(arr, left, right):
#     if left < right:
#         partition_pos = partition(arr, left, right)
#         quick_sort(arr, left, partition_pos - 1)
#         quick_sort(arr, partition_pos + 1, right)

# def partition(arr, left, right):
#     i = left
#     j = right - 1
#     piviot = arr[right]

#     while i < j:
#         while i < right and arr[i] < piviot:
#             i += 1
#         while j > left and arr[j] >= piviot:
#             j -= 1
        
#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]
        
#     if arr[i] > piviot:
#         arr[i], arr[right] = arr[right], arr[i]
    
#     return i

# test_arr = [0, 9, 2, 7, 8, 3, 4, 6, 5, 1]
# quick_sort(test_arr, 0, len(test_arr)-1)
# print(test_arr)

def quick_sort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quick_sort(arr, left, partition_pos - 1)
        quick_sort(arr, partition_pos + 1, right)

def partition(arr, left, right):
    i = left
    j = right - 1
    piviot = arr[right]

    while i < j:
        while i < right and arr[i] < piviot:
            i += 1
        while j < right and arr[j] >= piviot:
            j -= 1
        
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    if arr[i] > piviot:
        arr[i], arr[right] = arr[right], arr[i]
    
    return i

test_arr = [0, 9, 1, 3, 2, 7, 8, 4, 5, 6]
quick_sort(test_arr, 0, len(test_arr)-1)
print(test_arr)