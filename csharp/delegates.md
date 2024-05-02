# Delegates
It acts like a traditional function pointer, which is a way to point to a particular method. You can have a method that accepts a function pointer so that we can extend this behaviour or receive a callback.
A delegate is a type that represents references to methods with a particular parameter list and return type.

## What is  a delegate?
1. Defines the required method signature
1.  Whenever you define that you want to use a delegate, the consumer of the delegate knows exactly what the function you will point to will return, as well as what the expected parameters are. You can construct a delegate by introducing the delegate keyword.

- contravariance and covariance in C#

## When to use a delegates?
- When you need a callback
- events for WPF
- extensability

### Creating, Users and Invoking a delegate

## Introduciton to Func and Actions
Func and Action delegates in C# are powerful tools used  to define and pass around functions as parameters or return values.

### Understanding the Difference: Func vs. Action
The main difference between Func and Action lies in their return types. The Func delegate allows you to specify a return type, whereas the Action delegate does not return a value. Both delegates can have up to 16 parameters.


Sys.Func<int> repetitionsProvider, Sys.Action<string> reportConsumer

() => procedureRepetitions
result => report = result 

Func = provider: takes a parameter and returns a value
Action = consumer
	- It represents a method that takes no parameters and returns void.
	- It's commonly used for defining and passing around actions or operations that don't produce a result.
It is equivalent to a function pointer