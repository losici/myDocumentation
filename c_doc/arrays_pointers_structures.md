# Arrays
In C, memory spaces are not automatically cleared from the previous values. Therefore array must always be initialized. 
The array can be initialized in 2 ways:
1. Within the array declaration
    ```c
    int array[5] = {0, 1, 2, 3, 4};
    int array[5] = {0}; // quickly initialization with a single array value
    ```
1. Outside the array declaration
    ```c
    // using looping structures
    int array_size = 5;
    int array[array_size];
    int i;
    for (i = 0, i<array_size5, i++)
    {
        array[i] = 0
    }
    ```
## characters array
Characters array should always be initialized before using them. Elements in a character array holds characters plus  a special termination character '/0'. Remember to allocate enough room also for the null character.
```c
char name[] = {'E','v','a','\0'}; // method 1
char name2[] = 'Eva' // array of size 4 with null character
```
# Pointers
Pointers are variable that most often contain a memory address as their value. In other words, a pointer variable contains a memory address that points to another variable.
```c
int x = 0;
int age = 30;
int* pAge;
pAge = &age; // to indirectly reference a value through a pointer we must assign an address to the pointer
```
I assigned the memory address of the age variable to the pointer variable pAge. 
I can assign the contents of what my pointer variables points-to to a non-pointer variable.
```c
x = *pAge; // x=30
```
Info graphics

Step 1:
```c
int x = 0;
int age = 30;
int* pAge = NULL;
```
Name: x
address: 0xHH
value: 0

Name: age
address: 0xFF
value: 30

Name: pAge
address: 0x22
value: NULL

Step 2:
```c
pAge = &age; // the value is updated with the address
```

Name: pAge
address: 0x22
value: 0xFF

Step 3:
```c
x = *pAge;
```
Name: x
address: 0xHH
value: 30

>Note! Pointers variables should always be initialized with one of the following:
- a memory address
- 0
- NULL

AGAIN: pointer variables can only be assigned with memory addresses, 0, or NULL.
You can assign non-addresses value to pointers with the `*` *indirection operator* 
```c
*pAge = 7;
```
## Passing by value
When passing by values C reserves extra memory space to make a copy of the variables that are arguments of the function. When passing by value there are two main concerns:
1. making copies degrades performances
1. When arguments are passed by value we are unable to modify the original contents of the incoming parameters. This is because C makes a copy of the original variable and only the copy is modified. 

## Passing by reference
Using pointers we can actually modify the original content of the variables. We pass the address of the variable (argument) to the function using indirection `*` *indirection operator*

```c
void demoPassByReference(int *x) // I tell C that my function will take a pointer
{
    *x += 5; //increment the value by 5, modify original content of the variable
    printf("\n The value of the variable is : %d", *x); // shows the actual value incremented by 5
    printf("\n The address of the pointer is : %d", x); // print the numeric representation of the pointer address
}

...
int y = 0;
demoPassByReference(&y); // I pass the memory address of the variable nby placing the unary operator (&)
```
### Passing arrays to functions

# Data structures

