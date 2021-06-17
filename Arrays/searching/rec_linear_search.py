value1 = 5
value2 = 7
array = [1, 2, 3, 4, 5, 6]
unsorted_array = [1, 2, 3, 4, 5, 6,4,3,2,6,7,8,0]

def rec_linear_search(index, array, value):
    if index <= len(array) - 1:
        if value == array[index]:
            print('rec_linear_search - Found value: ' + str(value))
        else:
            print('rec_linear_search - Value not found: ' + str(value))
            rec_linear_search(index + 1, array, value)
    else:
        print('rec_linear_search - Value not found array')
rec_linear_search(0,array,value1)
rec_linear_search(0,array,value2)