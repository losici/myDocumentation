# Operators

## Arithmetic
They are: +,-,*,/ and their shortcuts +=, -=, *=, /=. There are also increment and decrement operators: i++, ++i, i--, --i. Additionally there is the *%* modulo operator and there is not the exponential operator.

## Comparison
They are: <,<=,=>,>, !=. To combine more comparisons use boolean operators: ||  and &&, ! not.

## Bitwise
They operate bit by bit.
- or | :
- and & :
- xor ^:
- not ~:

## Bit shift operators
- Left Shift <<: Multiplico per la potenza di 2. Example: `6<<1` means `6*(2^1)=6*2=12`. Example: `6<<3` means `6*(2^3)=6*8=48`
- Right Shift >>: Divido per la potenza di 2.
```
N = N>>k; // N=N/(2^k)
N = N<<i; // N=N*(2^i)
```
## Opertor Overloading
They are one of the central aspect of Cpp. All of the operators can be overloaded.
- write a function that defines the operator
- usually is  amember function
- occasionally a free function
