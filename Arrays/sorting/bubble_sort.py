value1 = 5
value2 = 7
array = [1, 2, 3, 4, 5, 6]
unsorted_array = [1, 2, 3, 4, 5, 6, 4, 3, 2, 6, 7, 8, 0]


def bubble_sort(array):
    array_length = len(array)
    for i in range(array_length - 1):
        for j in range(0, array_length - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


print(bubble_sort(unsorted_array))
print(bubble_sort(array))
