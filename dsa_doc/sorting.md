# Bubble Sort
Naive approach based on comparisons. It got 4 comparisons for 5 elements to move the biggest element at the end. So there are n-1 comparisons. The largest element of the array will bubble up till the end.
## Efficiency
There were n-1 iterations for n-1  comparison.<br/>
The complexity is (n-1)(n-1) = n^2 -2n +1 = O(n^2).<br/>
Worst case = O(n^2)<br/>
Average case = O(n^2)<br/>
Best case = O(n)<br/>

# Merge Sort
it is based on divide and conquer. 
The array is broken up is a bunch of array of 1 element each. We do a comparison of pairs, and swap the biggest on the right. We count the comparisons for efficiency.
At the next iteration we join two couples of array and we do the comparisons.
The comparison is always with the left extremes of the arrays.
## Efficiency
At each step we did one less comparison of the array we were building.
If n is the size of the array the number of comparison is n-1.
approximately we are going to do max n comparisons. Number of iterations x number of comparisons.
In order to sort an array of 7 we needed to do 3 steps. <br/>
**Time efficiency:**<br/>
Worst case = O(nlog(n)): n comparisons for log(n) steps<br/>
**Space efficiency:**<br/>
For Merge sort you need an auxillary space of O(n) because we got read of the old ones. We need two different arrays at each step. The array where the numbers were in and the new array that we're copying the values into.

# Quick Sort
you pick a random value in the array and move all values larger than it above it and all values below it lower than it. The value that you pick initially is called a **pivot**.The convention is pick the last element as a pivot.
## Efficiency 
The efficiency is pretty complicated. First let's look to the quick sort.<br/>
Worst case: O(n^2)
Average case = O(nlog(n))<br/>
Best case = O(nlog(n))<br/>
If we know we are getting arrays that are near sorted we don't want to use quick sort. We can do some optimizations:
- We can run the comparisons at both time;
-  