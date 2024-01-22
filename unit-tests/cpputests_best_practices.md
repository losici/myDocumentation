# CPPUTEST

## Comparators
We typically implement comparators for stubbed functions that take a pointer to a struct. We typically do not implement comparators for functions that take pointers to void or unsigned char, char, uint8_t, etc.
For that we use the built-in byte array comparators, or in some cases we just compare the pointer value (only rarely).
CppUTest has a built-in comparator for byte arrays that takes a pointer to unsigned char and a size.