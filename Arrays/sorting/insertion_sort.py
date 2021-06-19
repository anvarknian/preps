value1 = 5
value2 = 7
array = [1, 2, 3, 4, 5, 6]
unsorted_array = [1, 2, 3, 4, 5, 6, 4, 3, 2, 6, 7, 8, 0]


def insertion_sort(array):
    for i in range(1, len(array)):
        selected_value = array[i]
        j = i - 1
        while j >= 0 and selected_value < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = selected_value

    return array


print(insertion_sort(unsorted_array))
print(insertion_sort(array))
