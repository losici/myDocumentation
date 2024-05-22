# Quick guide for dumb errors in C

## Static
1. The **static** keyword can make the difference between something that works and something that doesn't.

## Pointers
1. Watch out for function that return pointers but are not memorized. Sometimes when doing a subroutine doing:
```
// wrong results: this happens when the subroutine is called and the value opcode will not be updated but will stay the old one from a previous function call

static void test_med_deliverTestingDose(opcode, ccpResponseCode)
{
    static uint8_t expectedResponse[] = { ResponseCodeOpCode, opcode, ccpResponseCode };
    ...
}
```
```
// correct: it forces the reinitialization of the variables
static void test_med_deliverTestingDose(opcode, ccpResponseCode)
{
    static uint8_t expectedResponse[] = { ResponseCodeOpCode, 0, 0 };
    expectedResponse[1] = opcode;
    expectedResponse[2] = ccpResponseCode;
}
```