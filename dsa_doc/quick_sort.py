"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

def qs(arr,left,right):
    if left < right: # it contains at least 2 elements
        partition_pos = partition(arr, left, right)
        qs(arr,left,partition_pos-1)
        qs(arr, partition_pos +1, right)
    return arr



def partition(arr, left, right):
    i = left
    j = right -1
    pivot = arr[right]

    while i < j:
        while i<right and arr[i]<pivot:
            i+=1
        while j>left and arr[j]>=pivot:
            j -= 1
        if i<j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i]>pivot:
        arr[i], arr[right] = arr[right], arr[i]
    
    return i



test1 = [8,3,1,7,0,10,2]
test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print (qs(test, 0, len(test)-1))
print (qs(test1,  0, len(test1)-1))
