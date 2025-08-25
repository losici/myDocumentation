# Week 1 - C
## Introduction
Programming is about input becoming output.
The source code is written in C, and it is the input and the machine code is the output and it is written in 1 and 0. 

make is a program that runs the compiler for you. The compiler we are using is clang for c program. Clang can be used very simply but it is not user friendly. 
```sh
code hello.c
make hello # run the compiler - trigger the compilation
./hello # run the machine code       
ls # list

$ hello* hello.c # the * means it is an executable
```

```sh
clang -o hello hello.c
./hello
```

make is useful because it just prevent us to run the tedious command of above.

If you use a third part library you have to tell the compiler. I have to tell the compiler to `link` the library cs50

```sh
clang -o hello hello.c -lcs50

```

Make uses for us -o and -l 

# Steps in turning source code in 0 and 1
## Preprocessing
They look for the libraries and it's like copying and pasting the prototypes of the functions before the compiler. 
#include <stdio.h>
#include is a preprocessor command. The libraries contain the prototypes of the functions.
it converts the hash include lines to the prototypes within the file
## Compiling
After the preprocessing, in the computer memory the code gets converted into assembler language.
## Assembling
Takes the assembly code and it converts to 0 and 1.
clang uses a.o : assembly output
## Linking
The compiler converts all the files to o and 1 and they are still separate, the linker combines the files intelligently everything into one. 

### Compiler collections
1. clang
1. gcc

# Other tools
## Decompiling
Reverse engineer the 0 and 1 into source code. 

## Debugging
It is a rare thing to get a program 100% right at the first time. Bugs are always omnipresent.

```c
#include <stdio.h>
printf("i is %i\n", i);
```

Step over: execute the function without going inside
Step into: inside the function

# Attributes of code
1. Correctness, tested with reviews, unit tests, other tests
1. Design
1. Style, vscode extensions can do that

