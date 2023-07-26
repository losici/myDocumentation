# Scope

## Static
Using static in front of a variable influences two things:
1. lifetime: variable lives for the duration of the program
1. linkage: access from other files
A global variable lives for the duration of the program. If you use static inside a function, then the linkage is not really a concern, but the duration of the lifetime is.
When you design tests be mindful of the static keyword.