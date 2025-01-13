# Building
Declarations of the class goes to h.
Include files must be included where they are used.
Compiler checks functions are included int the declaration.
Thye compiler creates obj files-->  the Linker links all ocj together and creates the exe file. 

# Types

## Auto
Keyword that asks the compiler to deduce the type. The variable is still strongly typed.

## Casting
Compiler will convert types.
By casting you make your intention clear.

```
double d1 = 2.2;
int i1 = static_cast<int>(d1);
```
# User Defined Types
## Class
If you don't specify the access specifie, by default is private.
The order of **private, protected, public** doesn't matter and you can repeat them.
```
// Person.h
class Person
{
private:
	std::string firstname;
	std::string lastname;
	int arbitrarynumber;

public:
	Person(std::string first, std::string last, int arbitrary);
	Person();
	~Person();
	std::string getName();

};
// Person.c
#include "Person.h"

Person::Person(std::string first, std::string last, int arbitrary): // ":"constructor initializer
firstname(first),lastname(last), arbitraryname(arbitrary) //initializer list
{
    //empty
}
std::string Person::getName()
{
    return firstname + " " + lastname; 
}
```
### Constructor
- Don't have a return type:
- Same name of the class
- Initialization use "::" and ":"
- Always declare a default Constructor ```Person()=default;```
- Always declare a Destructor that destroyes the object ```~Person()```

### Scope
Objects were created as instance of the class. Objects have a lifetime.
When the constructor is called memory is allocated on the stack for the object. The object has a scope, it lasts until the close brace. And then the destructor runs. 
The resource acquisition is Initialization: Acquire in constructor and Release in destructor which is called automatically when the scope ends.



## Struct
By default is public.
## Namespaces
- Prevent name collisions
- Separate from class name with ::
- don't include `using` statements in the header files, but only in cpp so you prevent that the inport of the class is carried.

```
using std::cout;
using std::endl;

using namespace std; // not a good idea because you can 
...

cout<<"Hello world"<<endl;
```
## Inheritance
```
//h file
class Tweeter: public Person
{
    //list only what you are adding
};

//c file
Tweeter::Tweeter(std::string first,
		std::string last,
		int arbitrary,
		std::string handle)
	: 
	Person(first,last, arbitrary), //pass parameters to the base class initialization
	twitterhandle(handle)
{
	std::cout << "constructing tweeter " <<
		twitterhandle << std::endl;
}
```

## Enum
It give a name to a set of constans.
This is the old version c-style.
```
enum Status
{
	Pending,
	Approved, 
	Cancelled
};
```
## Scoped Enum
It is a class.
```
enumclass FileError
{
	notfound,
	ok
};
enumclass NetworkError
{
	disconnected,
	ok
};

Status s = Pending;s = Approved;
FileError fe= FileError::notfound;
fe= FileError::ok;
NetworkError ne = NetworkError::disconnected;
ne = NetworkError::ok;

```
## The Preprocessors
The line start with `#`. It controls what is compiled.
Use include guards in header files so that you don't recopile --> avoid to include multiple times the same header.

`#pragma once` : can also help in doing the same 