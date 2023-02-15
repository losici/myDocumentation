# Functions

Functions don't have to be part of a class.
```
int DoubleIt(int x)
{
    x = x*x;
    return x;
}
```
Header files contains the functions declaration.
The implementation is contained in a source fail.
The **Compiler** cares about the promises you make that you declared a function that exists. Tip: if you have an error Look at the header file.<br/>
The **Linker** cares that you keep those promises implementing the right function. Tip: if you have an error look at the source file.

## Some definitions
- Defining a function also declares it,
- inputs of a function are also called parameters;
Call by value: the value of the variable doesn't change, the function will operate on a copy of the variable.

Call by reference: the value of the variable will change in the calling scope.

Writing a function calling by reference:
- change the function in the scope of the function. For example the swap function,
- the parameter of the function is a large object and the  object is large and you want to avoid the waste memory on the copying. If you want to use it for this case, and the object doesn't need to change, use the `const&`. If you take something by reference only because you want to save space avoding the copy and you don't want to change the variable in the function scope, pass it by **const reference**.

Acthung! Never write a function with a return type which is a reference. This creates a mess. 

Returning by reference is dangerous. Returning by value is always safe.

## Member function
The member functions of a class must be declared in the header files and implemented in a .cpp file by using the full name.<br/>
```
Person::GetName()
```
You can also implement functions in the header file when hey are small by using the **inline** keywords. Moreover member function should be marked as **const** unless they are going to change the member variable of the class (both in the header file and in the implementation file).
Use the const keyword after the name of the function.
When the return type is **void**, it means that we are dealing with a subroutine.

# Understanding Error messages
## Linker
The linker makes sure that obj files are merged in exe. And that promises are fullfilled.
Typical errors:
- you can forget ot implement a function
- code for function is not in the cpp file
- the cpp file is not being linked
Linker questions:
- Have you ipplemented that function?
- usually in a.cpp
- it's about keeping the promises.
## Compiler
Typical errors:
- You can forget to declare a function before you call it
- Forget to include the header
- function is not declared in header
It doesn't care of the body.
Compiler questions:
- Have you declared that function?
- Usually in a.h
- making a promise


Other tips:
- solve the first error first;
- missing an include file --> compiler error.

> C++ is a strongly typed language. You mean what you declare. 

# Overloads
- function names can be used more than once. Overloading means that you can use the same function name as long as the compiler can distinguish among the different functions. This can happen with a different number of arguments. Taking the same number but of different type is risky. The return type can never be used to distringuish overloads this is because when calling a function you don't have to use (assign) the return type.