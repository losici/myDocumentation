# Notation
In general when talking about asymptotyc analysis we talk about:
- operations: number of times we need to perform some operations
- memory: how much memory is consumed by the algorithms
- others: network transfer, compression ratios, disk usage.

To understand the maximum look at the domain and its limits.

Efficiency is described by Big O notation O(n). Inside O there is an algebric expression where n represents the length of your input.<br/>
```
//pseudocode

function decode(input):
    create output_string //--> 1
    for each letter in input: //--> n
        get new_letter from letters location in cipher // --> n
        add new_letter to output // --> n
    return output //--> 1

```
**O(n) = 3n+2**
Depending on the data structures that we use this can increase.

### Worst case
It puts an upper bound to the code.

## Time Efficiency
Time efficiency - a measure of amount of time for an algorithm to execute.

## Space Efficiency
Space efficiency - a measure of the amount of memory needed for an algorithm to execute.


## How to do quick estimates?
### O(logn)
O(logn) means that the domain space is reduced and reduced during the search. It means ad the input size grows the cost of the algorithm doesn't increase at the same rate (it's like bisection method in calculus.)

### O(n^2)
Doubly-nested loop is an indication of it.

### O(nm)
A nested loop that iterates over two distinct collections of data might indicate an O(nm) algorithm.

# Resources
dsa google: https://techdevguide.withgoogle.com/paths/data-structures-and-algorithms/#sequence-7