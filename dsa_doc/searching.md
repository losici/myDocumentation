# What is an algorithm?
It is the high level description of a trick to solve a problem.<br/>
**See if a number exist in an array**
If we start looking from the front or from the back the complexity will be O(n).<br/>
**if the array is sorted**
Check if the number is greater than the middle element and then move forward.

# Binary search
Given a sorted array, look if a certain element is contained in the array.
Start from the middle number, if it higher we take the higher side and we move on.
The number of iteration increase every time the size doubles.
O(log(n)+1) = O(logn)

Create a table: array size and iterations to spot the patterns.

# Recursion
A recursive function needs:
1. To call itself;
2. Base case: exit condition to avoid being stucked in the infinite recursion;
3. Alter the input parameter;

# Sorting
You change the the order of the array.

## Naive approach
Compare every element with every element. But for sure there is a smarter way to solve it.

