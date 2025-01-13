# From experience

## Invalid Syntax for Struct Initialization:


```
    static DummyLogRecord logRecord[] = {
        { .unixTime = 78234, .dummy.time= 150, .dummy.thing= 10},
        { .unixTime = 9348592, .dummy.time = 250 , .dummy.thing = 20 },
    };

where I have 
PACKSTRUCT(structDummy_tag
           {
               uint32_t time;
               uint8_t thing;
           });
typedef struct Dummy_tag Dummy;

typedef PACKSTRUCT(struct DummyLogRecord_tag{
    uint64_t unixTime;
    Dummy dummy;
})DummyLogRecord;
```
C++ does not support the . operator for nested struct member initialization directly in aggregate initialization lists. Instead, you should use brace-enclosed lists.
In your initialization list, dummy.time and dummy.thing are invalid in this context.

Incorrect Member Access Syntax:
In your initialization list, dummy.time and dummy.thing are invalid in this context.

Correct version
```
static DummyLogRecord logRecord[] = {
    { .unixTime = 78234, .dummy = { .time = 150, .thing = 10 } },
    { .unixTime = 9348592, .dummy = { .time = 250, .thing = 20 } },
};
```