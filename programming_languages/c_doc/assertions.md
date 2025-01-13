**Index of Contents**
[TOC]

# Assertions
# C11
From C11 use the [assertion library](https://en.cppreference.com/w/c/language/_Static_assert).
# C90/C99
Static Analysis checker like `splint` are not compatible with C11. Therefore a work around to implement a static assertion must be used.

```h
#define STATIC_ASSERT(condition, message) typedef char static_assertion_##message[(condition) ? 1 : -1]
```
1. `#define STATIC_ASSERT(condition, message)`
    - `#define`: This is the C preprocessor directive that defines a macro.
    - `STATIC_ASSERT(condition, message)`: This is the macro name STATIC_ASSERT with two arguments: condition and message.
    - `condition`: A boolean expression that is evaluated at compile time. If it evaluates to true (non-zero), the assertion passes. If it evaluates to false (zero), the assertion fails, causing a compiler error.
    - `message`: A user-defined name or identifier that is used in the typedef name, providing context in the compiler error message when the assertion fails.

2. `typedef char static_assertion_##message[(condition) ? 1 : -1];`

    This is the actual code that the macro expands to when it is used. Let's break it down:

    - `typedef char`: This declares a new type, which is an array of char. The array's size will be determined by the expression following it.
    - `static_assertion_##message`:static_assertion_: This is a prefix used to name the typedef.
    - `##`: This is the token-pasting operator in C, which concatenates the token static_assertion_ with the message argument passed to the macro. This means that the typedef will be named something like `static_assertion_TemperatureRecord_size_mismatch` if TemperatureRecord_size_mismatch is passed as the message.
    - `[(condition) ? 1 : -1]`: This is the array size specification. It uses the ternary operator to decide the size of the array based on the value of the condition. 
        - (condition): This is the expression that evaluates to either true (non-zero) or false (zero).
        - `? 1 : -1`: If the condition is true, the array size will be 1. If the condition is false, the array size will be -1.
        
        > Note: In C, having an array size of -1 is illegal, and this triggers a compile-time error if the condition is false.

## How it Works:
If the condition is true (non-zero), the array size is valid (1), and the typedef declaration will compile successfully.

If the condition is false (zero), the array size becomes -1, which is illegal, and the compiler will produce an error.

This error helps simulate the behavior of a static_assert and enforces the condition at compile time.

### Example of usage
```
typedef PACKSTRUCT(struct TemperatureLogRecord_tag {
    uint64_t unixTime;
    float temperature_c;
}) TemperatureLogRecord;

STATIC_ASSERT(sizeof(TemperatureLogRecord) == TEMPERATURE_LOG_RECORD_SIZE, TemperatureLogRecord_size_mismatch);
```
