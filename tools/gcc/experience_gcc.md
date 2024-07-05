# From Experience
A collection of learning experience with gcc

[TOC]
## Switch off the error variable set but not used
When calling functions that return a variable, in case you do not use that variable you get the following error.
```
error: variable ‘sc’ set but not used [-Werror=unused-but-set-variable]
```
This can be switched off defining the variable in the following way:
```
sl_status_t sc __attribute__((unused));
bool isSuccess __attribute__((unused));
```