value1 = 5
value2 = 7
array = [1, 2, 3, 4, 5, 6]
unsorted_array = [1, 2, 3, 4, 5, 6, 4, 3, 2, 6, 7, 8, 0]


def binary_search(array, value):
    low = 0
    high = len(array) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if array[mid] < value:
            low = mid + 1
        elif array[mid] > value:
            high = mid - 1
        else:
            return mid
    return -1


print(binary_search(array, value1))
print(binary_search(array, value2))
