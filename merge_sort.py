def merge_sort(arr):

    mid = len(arr) // 2

    if len(arr) > 1:
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        #recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        #index
        i = 0
        j = 0
        k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

test_arr = [1, 9, 8, 4, 5, 3, 2, 6, 7]
merge_sort(test_arr)
print(test_arr)