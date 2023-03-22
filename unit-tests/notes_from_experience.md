# Notes from experience
Some notes from experience and gathered in mixed order:
- When coding unit-tests, think about the test cases to implement, keep them simple. 
- Unit-tests return void and have void input parameters, inside the unit-tests the function to actually test is called. 
- When to mock functions: If the function under test has other functions inside, those that are inside the same file of the funcions under tests do not have to be mocked, otherwise we are introducing a behaviour which could not match the behaviour produced by the tests. The functions to be mocked are those that are called inside the function under test and that are defined outside the file that contains the function under test.