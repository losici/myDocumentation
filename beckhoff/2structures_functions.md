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
VAR_IN_OUT: 

POU-->POU--> Functions

you can pass parameters by value or reference. 
by value: no effect on the original data, I send a copy of the variable to the function, the value will change in the function, but the original data will be unchanged
by reference: you pass the member location, any change you do will affect the value and persist after the fucntion ended. 
