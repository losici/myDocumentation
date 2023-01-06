"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    pivot = array[-1]
    i = 0
    while(True):
        element = array[i]
        if element>pivot:
            temp = array[-i-2]
            array[-i-2]=array[-i-1]
            array[-i-1] = array[i]
            array[i] = temp
        else:
            i += 1
            




    # for i in range(len(array)):
    #     element = array[i]
    #     if element>pivot:
    #         temp = array[-i-2]
    #         array[-i-2]=array[-i-1]
    #         array[-i-1] = array[i]
    #         array[i] = temp
        
        
    return array

test1 = [8,3,1,7,0,10,2]
test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
# print (quicksort(test))
print (quicksort(test1))