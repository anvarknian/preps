## Merge sort, quick sort , bubble sort, insertion sort, selection sort
## binary search,  linear search
## rec binary search, rec linear search
value1 = 5
value2 = 7
array = [1, 2, 3, 4, 5, 6]
unsorted_array = [1, 2, 3, 4, 5, 6,4,3,2,6,7,8,0]


def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]
        mergeSort(left)
        mergeSort(right)
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                myList[k] = left[i]
                i += 1
            else:
                myList[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1
        return myList

print(mergeSort(unsorted_array))
print(len(unsorted_array))
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
#print(quick_sort(unsorted_array))

def bubble_sort(array):
    array_length = len(array)
    for i in range(array_length-1):
        for j in range(0 , array_length-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] =array[j+1], array[j]
    return array
#print(bubble_sort(unsorted_array))


def insertion_sort(array):
    for i in range(1,len(array)):
        selected_value = array[i]
        j = i-1
        while j>=0 and selected_value<array[j]:
            array[j+1]=array[j]
            j-=1
        array[j+1] = selected_value

    return array
#print(insertion_sort(unsorted_array))


def selection_sort(A):
    for i in range(len(A)):
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]
    return A
#print(selection_sort(unsorted_array))

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


# print(binary_search(array,value1))
# print(binary_search(array,value2))


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


#print(rec_binary_search(0, len(array) - 1, array, value1))
#print(rec_binary_search(0, len(array) - 1, array, value2))


def linear_search(array, value):
    for i in array:
        if i == value:
            print('linear_search - Found value ' + str(value))
        else:
            print('linear_search - Value not found array')


# linear_search(array,value1)
# linear_search(array,value2)

def rec_linear_search(index, array, value):
    if index <= len(array) - 1:
        if value == array[index]:
            print('rec_linear_search - Found value: ' + str(value))
        else:
            print('rec_linear_search - Value not found: ' + str(value))
            rec_linear_search(index + 1, array, value)
    else:
        print('rec_linear_search - Value not found array')
# rec_linear_search(0,array,value1)
# rec_linear_search(0,array,value2)
