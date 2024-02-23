# Delegates

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