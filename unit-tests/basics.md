# Basics
Test-suits are useful to group unit-tests into a project, test-suits are set up with tests-frameworks. Some example of tests-frameworks are:<br/>
- cmock
- QTtest
- unity

Test classes should only be testing public behaviours.<br/>
Each test method is a test and the name should provide information about what the test is testing and the expected results.<br/>
There is a *3A Structure* to keep in mind when setting up a unit-test.<br/>
* Arrange
* Act
* Assert

A good unit test should be *readable, concise, fast and isolated*.<br/>
A unit-test should only test one method under test (MUT) and we should avoid conditional statemens in the unit-tests because they compromise the clarity and also the consistent running of the unit-tests (we are introducing branches). The unit-tests should verify the MUT outputs or the states of specific objects.

## Sharing setup
Some unit tests have the same setup code duplicated in the code. Duplicated code makes maintenance a pain. A solution can be to create a setup method that it is fired before any unit tests: `public void init()`.</br>
We can also setup at the beginning of each unit-test a private method to setup the unit test. In the test we just call a local instance of the public method.
## Using Parametrized Data
Most unit-tests provede functionalities of parametrized data. We create a method that has in unputs the parametrized data and use the framework where we specify the data `TestCase(1.1,2.1)`:
```
public void exampleFunction_InputIsX_ReturnInY(expected_output, provided_input)
``` 