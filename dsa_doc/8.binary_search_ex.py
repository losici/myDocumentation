"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    temp = input_array
    while True:
        array_len = len(temp)
        if array_len > 1:
            array_middle = array_len//2
            comparison = temp[array_middle-1]
            if value > comparison:
                temp = temp[array_middle:]
            elif temp[array_middle] == value:
                return input_array.index(value)
            else:
                temp = temp[:array_middle]
        else:
            if value in temp:
                return input_array.index(value)
            else:
                break
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print (binary_search(test_list, test_val1))
print (binary_search(test_list, test_val2))