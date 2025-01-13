# Quick look up

## size of array
By dividing the total size of the array by the size of a single element, you get the number of elements in the array.
```
datatype size = sizeof(array_name) / sizeof(array_name[index])
```

## find the element with smallest index 

#include <stdio.h>
#include <stdint.h> // For uint32_t
#include <stdlib.h> // For abs() function

// Function to find the index of the element with the smallest difference
int findClosestIndex(uint32_t times[], int size, uint32_t currentTime) {
    int closestIndex = 0;
    uint32_t minDifference = abs((int32_t)(times[0] - currentTime)); 

    for (int i = 1; i < size; i++) {
        uint32_t difference = abs((int32_t)(times[i] - currentTime));
        if (difference < minDifference) {
            minDifference = difference;
            closestIndex = i;
        }
    }

    return closestIndex;
}

int main() {
    uint32_t times[] = {1200, 1230, 1300, 1400, 1500};
    uint32_t currentTime = 1330;
    int size = sizeof(times) / sizeof(times[0]);

    int index = findClosestIndex(times, size, currentTime);

    printf("The index of the closest time is: %d\n", index);
    printf("The closest time is: %u\n", times[index]);

    return 0;
}