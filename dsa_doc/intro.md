# Notation

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

# Resources
dsa google: https://techdevguide.withgoogle.com/paths/data-structures-and-algorithms/#sequence-7