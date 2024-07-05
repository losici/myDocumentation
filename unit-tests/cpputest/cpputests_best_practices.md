# CPPUTEST

[TOC]

## Comparators
We typically implement comparators for stubbed functions that take a pointer to a struct. We typically do not implement comparators for functions that take pointers to void or unsigned char, char, uint8_t, etc.
For that we use the built-in byte array comparators, or in some cases we just compare the pointer value (only rarely).
CppUTest has a built-in comparator for byte arrays that takes a pointer to unsigned char and a size.

## Mocking uint64_t functions


To successfully mock a function that returns a uint64_t in CppUTest when you don't have direct support for uint64_t or unsigned long long in MockSupport.h, there  is the need for a creative workaround (The maximum value that cpputest can return is UnsignedLongInt).

One method is to split the `uint64_t` value into two unsigned int values. This is more complex and requires careful handling to ensure correctness.

```
// Stub.c

/* Global Function Implementations*/

uint64_t nvs_getTime(void)
{
    uint32_t high = mock().actualCall("nvs_getTime").returnUnsignedLongIntValueOrDefault(0);
    uint32_t low = mock().actualCall("nvs_getTime").returnUnsignedLongIntValueOrDefault(0);
    return combineToUInt64(high, low);
}

/* Local Function Implementations*/

uint64_t combineToUInt64(uint32_t high, uint32_t low)
{
    return ((uint64_t)high << 32) | low;
}
```

In the test:
```
void splitFromUInt64(uint64_t value, uint32_t& high, uint32_t& low);

/* Global Function Implementations*/
TEST(DoSomethingGroup, TestDoSomething)
{
    uint32_t expectedHigh;
    uint32_t expectedLow;
    uint64_t expectedTime = 12345ULL;
    splitFromUInt64(expectedTime, expectedHigh, expectedLow);

    // Setup the mock for nvs_getTime to return the split 64-bit value
    mock().expectOneCall("nvs_getTime").andReturnValue(expectedHigh);
    mock().expectOneCall("nvs_getTime").andReturnValue(expectedLow);

    // Call the function under test
    do_something();

    // Optionally check results if do_something has observable effects
    // For example:
    // CHECK(someObservableCondition);

    // Verify that all expectations were met
    mock().checkExpectations();
}

/* Local Function Implementations*/
void splitFromUInt64(uint64_t value, uint32_t& high, uint32_t& low)
{
    high = (uint32_t)(value >> 32);
    low = (uint32_t)(value & 0xFFFFFFFF);
}
```

## Mocking functions with pointers parameters
When mocking a function that has pointer parameters, you need to handle the pointers correctly in both the mock function implementation and the test expectations. In our example, the function sl_bt_gatt_server_get_mtu has a pointer parameter uint16_t* mtu.
1. Pointers and Output Parameters: When mocking functions with pointer parameters, you must handle input and output pointers separately. Input pointers are passed directly, while output pointers are set using `withOutputParameterReturning`.
1. Using sizeof: The `sizeof` operator ensures you correctly specify the size of the data being set or used. This is particularly important for output parameters to avoid memory corruption or incorrect values. Using sizeof ensures that the correct amount of memory is used for the output parameter, which is crucial for properly simulating the behavior of the function.

```
// declaration
sl_status_t sl_bt_gatt_server_get_mtu(uint8_t connection, uint16_t* mtu);

...
// usage in code
uint16_t mtu = 0;
sc = sl_bt_gatt_server_get_mtu(event->connection, &mtu);

// mock stub
sl_status_t sl_bt_gatt_server_get_mtu(uint8_t connection, uint16_t* mtu)
    {
        mock()
            .actualCall("sl_bt_gatt_server_get_mtu")
            .withParameter("connection", connection)
            .withOutputParameter("mtu", mtu);
        
        return static_cast<sl_status_t>(mock().returnUnsignedIntValueOrDefault(0));
    }

// usage in unit test
...
    mock()
        .expectOneCall("sl_bt_gatt_server_get_mtu")
        .withParameter("connection", connection)
        .withOutputParameterReturning("mtu", &mtu, sizeof(mtu))
        .andReturnValue(SL_STATUS_OK);
...
```

