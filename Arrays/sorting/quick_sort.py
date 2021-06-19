value1 = 5
value2 = 7
array = [1, 2, 3, 4, 5, 6]
unsorted_array = [1, 2, 3, 4, 5, 6, 4, 3, 2, 6, 7, 8, 0]


def quick_sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[-1]
        for x in array:
            if x > pivot:
                greater.append(x)
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return array


print(quick_sort(unsorted_array))
print(quick_sort(array))
