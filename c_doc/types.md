# TYPES
This section goes in depth to the c types

[TOC]

## typedef __SIZE_TYPE__ size_t;
The exact type of size_t can vary between different platforms and compilers. By using typedef __SIZE_TYPE__ size_t;, the C standard library abstracts away these differences, ensuring that size_t will always be the appropriate type for the target platform. This abstraction allows code to be portable across different systems without needing to worry about the underlying type of size_t.
By defining size_t using __SIZE_TYPE__, the standard library ensures consistency in how sizes are represented. This consistency is crucial for the correct functioning of library functions that deal with sizes of objects and memory allocation (e.g., malloc, sizeof).
The __SIZE_TYPE__ macro is not a part of any standard library per se; rather, it is a compiler-specific internal definition used by some compilers to define the size_t type. It is most commonly associated with GCC (GNU Compiler Collection) and Clang, which are both widely used C and C++ compilers.
__SIZE_TYPE__ is chosen to be the most efficient type for representing sizes on a given platform. This typically means that size_t will be an unsigned integer type that matches the word size of the architecture (e.g., unsigned int on 32-bit systems, unsigned long on many 64-bit systems).