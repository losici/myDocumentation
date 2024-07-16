# Scope
[TOC]

## Static
Using static in front of a variable influences two things:
1. lifetime: variable lives for the duration of the program
1. linkage: access from other files
A global variable lives for the duration of the program. If you use static inside a function, then the linkage is not really a concern, but the duration of the lifetime is.
When you design tests be mindful of the static keyword.

- static function: it restricts the visibility of the function to the file in which is defined. The function cannot be called from other source files.
- static variable: when used with variable inside a function, static ensures the variables retains its value between function calls. A static variable can  only be initialized once. 

## inline
It is a hint to the compiler to replace the function call with the function code itself to avoid the overhead of a function call. The compiler is free to ignore this hint.

