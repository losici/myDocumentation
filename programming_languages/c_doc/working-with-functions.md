# Working with functions in C
A function is an abstraction that receives input(s) and produce an output. When the inputs are defined, the fucntion can be defined and it will do some processing to produce an output. A function is a means by which you can encapsulate instructions. 

There are two groups of functions:
1. User defined functions: created by the programmer using C and its library functions
1. Library: functions that are included with C programming language (C standard library API are a bunch of header files)

Benefits of using functions:
1. Increase the `Modulary` maintainin gthe separation of concerns
1. Reusable code: cut down on duplicating code by encapsulating
1. Maintainability
1. Easy to test systems
1. Less bugs

## Anatomy of a Function in C
There are four primary parts:
- Return Type
- Function name
- Parameters (inputs) 
- Function Body
The function signature is composed by the return type, the name and the parameters.
> Note: there is a distinction between function parameters and arguments. A function parameter is part of the function signature and it is relevant to the function definition. A function argument is the value used when calling the function. 

## User-defined functions
> All prototypes are declarations but not all declarations are prototypes.
### Function declaration
Any goruping of statement that declare a function
### Function Prototype 
A function declaration that include parameter types. Prototypes defines API, external API define a public interface and should be put in a header file. Internal API must be put at the top of the source file.
```
//declaration
void perform_task();
//prototype
void perform_task(void);

void performa_task2(int size. char **out);
```
# Standard Library Part 1
# Standard Library Part 2