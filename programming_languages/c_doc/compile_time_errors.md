# Compile Time Errors
They are typically errors that violate the syntax rules and therefore they are caught at compile time, so the compiler will detect them before creating an executable file.
These errors are generated by the compiler such as gcc, clang and msvc and they enforce rules about uniqye identifiers within structures, unions,enums and other constructs. 

## duplicate designator is not allowed
The "duplicate designator is not allowed" error typically arises when there are repeated identifiers within structures, unions, or other definitions where each field or label is expected to be unique.
Some examples:
1. Duplicate field in a structure or union
1. Duplicate case label in a switch
1. typedef or enum redefinition
