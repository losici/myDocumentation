# Errors cpputest

error: expected primary-expression before ‘.’ token
  828 |         { .unixTime = 78234, .dummy.time = 150, .dummy.thing = 10},

Invalid Syntax for Struct Initialization:
C++ does not support the . operator for nested struct member initialization directly in aggregate initialization lists. Instead, you should use brace-enclosed lists.

correct:

static DummyLogRecord logRecord[] = {
    { .unixTime = 78234, .dummy = { .time = 150, .thing = 10 } },
    { .unixTime = 9348592, .dummy = { .time = 250, .thing = 20 } },
};