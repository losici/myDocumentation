# Structures and Functions

## How to organize data?
```
eEventType : E_EventType;
eEventSeverity : TcEventSeverity;
nEventIdentity : UDINT;
sEventText : STRING(255);
dtTimestamp : DATE_ANDTIME;
```

To create a new structure data unit type, right click on DUTs, select Add, next select DUT, enter the name "ST_Event" and use 'Structure'.

# Functions
Used to perform certain actions, define the code once and use them many times. 
![functions.png](/beckhoff/imgs/functions.png)

VAR_INPUT: input variables
VAR: interval variables
VAR_OUTPUT: 
VAR_IN_OUT: input output variables

POU-->POU--> Functions

you can pass parameters by value or reference. 
by value: no effect on the original data, I send a copy of the variable to the function, the value will change in the function, but the original data will be unchanged
by reference: you pass the member location, any change you do will affect the value and persist after the fucntion ended. 

Function blocks are like classes. And there can be many methods that describes the behaviour and then there can be states. 
You need to create an instance of the function block
```
VAR
    fbWinch : FB_Motor;
    fbConveyor : FB_Motor;
END_VAR
```
FB can have instance variables availble to every instance. 
Between VAR and END_VAR.
![fb_methods.png](/beckhoff/imgs/fb_methods.png)

Where to write code to change the state of an object? 
Function block body or using methods?
Calls that needs to be done in every plc cycle use the function block
Calls that needs to change a state and need to be called once use methods.

## Inheritance 
use the keyword "EXTEND"

## ST vs FB

In industrial automation and programmable logic controller (PLC) programming, "ST" and "FB" are often abbreviations for Structured Text and Function Blocks, respectively. These are two different programming languages or methods used for creating control logic in PLC systems. The choice between using ST and FB depends on the specific application and the programmer's preference or the programming standards of the organization. Here's a brief overview of when to use each:

### Structured Text (ST):
ST is a text-based language where you can write custom code and algorithms for specific control tasks in a PLC program.
Similarly, in Python and C, you can write custom functions or methods to perform specific tasks or calculations as needed.
ST allows you to define your control logic and algorithms in a flexible and tailored manner, just like writing functions in Python or C.

1. Use ST when you need more flexibility and control in your PLC programming.
1. ST is a high-level, text-based language that resembles traditional programming languages like C or Pascal.
1. It's suitable for complex algorithms, mathematical calculations, and custom logic that may not be easily represented using other PLC programming languages.
1. ST is ideal for applications where you need to implement unique, non-standard control sequences or handle complex data manipulation.

### Function Blocks (FB):
FBs in PLC programming are predefined, encapsulated blocks of code that encapsulate common control functions.
In Python and C, you can use pre-built libraries or modules (such as math, time, or third-party libraries) to access and utilize standardized functions or components.
FBs and pre-built libraries/modules both provide a way to modularize and reuse code, making it easier to maintain and share functionality across different parts of a program.
1. Use FB when you want to create reusable and modular code for commonly used control functions.
1. FBs are pre-defined, encapsulated blocks of code that can be easily integrated into your PLC program.
1. They promote a structured and organized approach to programming by breaking down the control logic into manageable blocks.
1. FBs are particularly useful for tasks that are repetitive or standardized, such as motor control, valve control, or communication protocols.
They can simplify maintenance and troubleshooting because errors or modifications only need to be addressed in one central location (the FB) rather than throughout the entire program.
Ultimately, the choice between using Structured Text (ST) and Function Blocks (FB) depends on the specific requirements of your automation project and your programming style. In many cases, a combination of both ST and FBs may be used in a PLC program to take advantage of the strengths of each approach and achieve a well-structured and efficient control system.

In essence, ST is comparable to writing custom code from scratch in Python or C, while FBs are similar to using ready-made functions or libraries to handle standard tasks. The choice between ST and FBs in industrial automation programming is often driven by the need for customization and modularity, much like how programmers in Python and C decide whether to write custom functions or leverage existing libraries/modules depending on their project requirements.