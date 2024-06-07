# Bit operations
## splitting a large value

```
uint64_t value = 123456UUL;
uint32_t high, low;
high = (uint32_t)(value >> 32);
low = (uint32_t)(value & 0xFFFFFFFF);
```
1. `high = (uint32_t)(value >> 32);` shift right by 32 bits effectively discards the lower 32 bits and moved the upper 32 bits to the position of the lower 32 bits.
The result is then cast to uint32_t, which is necessary to ensure that only the lower 32 bits are kept and any higher bits (if any existed, which they shouldn't) are discarded.
2. `low = (uint32_t)(value & 0xFFFFFFFF);`
This line performs a bitwise AND operation between value and the hexadecimal constant 0xFFFFFFFF (which has all 32 lower bits set to 1, and the rest set to 0).
The effect of the AND operation is to zero out any bits in value above the lowest 32, effectively isolating these bits.
