# Unions
The {0} initializer is intended to initialize all elements of the structure (or union) to zero. This works because in C, a zero-initialized structure or union sets all scalar members (like integers) to 0, pointers to NULL, and floating-point numbers to 0.0.

For a structure, {0} will set all its members to 0.
For a union, {0} will typically zero out the first member of the union.
Some compilers can complain because for the union it can be unclear which part is initialized.
Therefore an explicit initialization is recommended.

Example
```c
// in .h
typedef union
{
    SystemEventA systemEventA;
    SystemEventB systemEventB;
    uint16_t systemEventSimpleCode;
} SystemEventRecord;

typedef PACKSTRUCT(struct SystemEventLogRecord_tag {
    uint64_t unixTime;
    SystemEventRecord systemEvent;
}) SystemEventLogRecord;

// in .c
SystemEventLogRecord logRecord = { 
    .unixTime = 0, 
    .systemEvent.systemEventSimpleCode = 0 
};

```
