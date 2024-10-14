Memory Management

**Contents**
[TOC]

## Basics
Computer memory or more common RAM (Random Access Memory)
The point of RAM's existence is to provide a fast means of data storage and retrieval throughout the life of a computer program. When your C program loads, a chunk of RAM is allocated to it, such that everything it needs to run is available close to the CPU. This is where the machine instructions that comprise your program will be run. Without memory or any other type of mechanism for housing fast, volatile data, your C program would have to be fetched all the way from the storage disk. 



Every C program will have four key memory segments. These memory segments roughly comprise the total memory space allocated to a C program. 
1. Code or Text segment: This segment is where the compiled machine code for your program lives. The CPU runs the machine code located within the code segment. Usually, the code segment is read only so that your program won't be modified after compilation.
Usually the **Code Memory** can be called also **ROM** or **FLASH**

1. Data segment: This segment can be further broken up into smaller segments, but for our purposes, it's fine to regard this segment as a whole. The data segment is where all of the **global variables** for your program live. Any variables that you declare outside of a function, as well as **static variables** will live in this memory segment.

1. Stack segment: It is where all **local variables** and **arguments within a function** live. With **every function call**, space is allocated on the stack for all the variables and arguments needed for the function to run. You may have heard of the term stack overflow. This is actually the error that occurs when you run out of available memory on the stack.

1. Heap segment: it is where all of the dynamically allocated memory for your program lives. This is the memory segment that we will be most concerned with in this course. The stack and heap segments grow towards each other. This means that as your program dynamically allocates memory on the heap, its used address space will grow upwards towards the stack. Correspondingly, as the number of function calls that your program makes increases or, to put it another way, as the call stack grows in size, the allocated memory on the stack will grow downwards towards the heap. In this course, we will be focusing almost exclusively on the heap segment as this is where memory is dynamically allocated in C.

In general RAM memory takes into account STACK and HEAP segment.
FLASH Memory contains Code and Data segment.

