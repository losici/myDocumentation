# Understanding C Structure
## Structure Basics

### Initialize structures to 0

```c
struct Point p4;
memset(&p4, 0, sizeof(p4));  // Set all members to 0
```

# Using C Structures
tbd
# Managing memory with Bit Fields
## How is RAM allocated to structure members?
When you create an object based on a structure, the memory is contiguously allocated to the members of the structure.

### Example
```
struct jersey{
    char sponsor; // 1 byte
    char designer; // 1 byte
    int number; // 4 bytes
}shirt;
```
What is the size of the shirt object? <br>
It might be easy to think it is 6 bytes. But this is wrong because of the **Structure Padding**. The CPU doesn't read one byte at a time but one "word" per time. The size of the word depends on the CPU bits.<br/>
Word size:
- 4 bytes (32 bit)
- 8 bytes (64 bit)

So at each CPU cycle, the CPU reads one word, the structure padding acts so that there is no waste of CPU, so that there will be the least number of cycles to fetch a variable.<br/>
Without structure padding the number variable would be split as follows and therefore there would be 2 CPU cycle to fetch "number":
![Bad Structure Padding](/c_doc/img/bad_structure_padding.png "Bad Structure Padding")<br/>
Structure padding acts so that there is only one cycle to access the varible number. 
![Good Structure Padding](/c_doc/img/good_structure_padding.png "Good Structure Padding")<br/>
It is a compromise between memory and cpu cycles. The order in structure padding matters, changing the order of the members it will change the total size. 
The directive #pragma pack(1) helps to reduce the memory waste.

## Bit fields
They are a way to access to specific bits. They aloow to work with data smaller than 8 bits. They cna help memory optimization and hardware control. They cannot be used with characters but only with **INTEGERS**.
```
struct {
    int shirtNumber :5; // 5 bits + 1 for the sign
    int heightPlayer:3; // 3 bits + 1 for the sign
}
```
In integer one bit is used to mantain the sign. Otherwise better use ***unsigned integer**.
```
struct {
    unsigned int shirtNumber :5; // 5 bits 
    unsigned int heightPlayer:3; // 3 bits 
}
```
