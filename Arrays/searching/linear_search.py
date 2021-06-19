value1 = 5
value2 = 7
array = [1, 2, 3, 4, 5, 6]
unsorted_array = [1, 2, 3, 4, 5, 6, 4, 3, 2, 6, 7, 8, 0]


def linear_search(array, value):
    for i in array:
        if i == value:
            print('linear_search - Found value ' + str(value))
        else:
            print('linear_search - Value not found array')


linear_search(array, value1)
linear_search(array, value2)
