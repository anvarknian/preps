value1 = 5
value2 = 7
array = [1, 2, 3, 4, 5, 6]
unsorted_array = [1, 2, 3, 4, 5, 6,4,3,2,6,7,8,0]

def rec_binary_search(low, high, array, value):
    if low <= high:
        mid = (high + low) // 2
        if array[mid] == value:
            return mid
        elif array[mid] > value:
            return rec_binary_search(low, mid - 1, array, value)
        elif array[mid] < value:
            return rec_binary_search(mid + 1, high, array, value)
        else:
            return -1


print(rec_binary_search(0, len(array) - 1, array, value1))
print(rec_binary_search(0, len(array) - 1, array, value2))