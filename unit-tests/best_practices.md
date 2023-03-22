# Best Practices
## Avoid Shared Dependencies
What is a shared dependencies?<br/>
Avoid to interact with csv, database and clouds, because some unit-tests may fail because they expect different data then those stored by other unit-tests.
![Shared Dependencies](/unit-tests/imgs/shared-dependencies.png "Shared Dependencies")<br/> Use instead **test doubles** which mock the dependencies and they are completely isolated, and the unit test will interact with the test double instead of the shared dependencies. Test dubble avoids interacting with our shared dependencies by supplying our system under test with dummy data
![Test Doubles](/unit-tests/imgs/test-doubles.png "Test Doubles")<br/> 
<br/>
There are many names for test doubles:
- dummies
- stubs
- spies
- mocks
- fakes

But in practise they can be all grouped in 2 categories **stubs** and **mocks**, but most of the frameworks they just call everything **mocks**. The difference is that"
- Stubs supply data to the system under tests, it fakes data taken from the shared dependencies and it supply that data to a system under test. It takes care of incoming data interactions 
- mocks when a test double is used to verify that our system under test has tried to communicate with a shared dependencied. It takes care of outgoing communications. 

## Unit test vs integration test
One of the purpose of integration tests is to provide automaiton testing for things like shared dependencies under code associated. <br/>
Integraiton tests access to the shared dependencies, for example they actually read and write to csv files.<br/>
Integration tests have their test-suit and they are managed differently from unit-tests also because they are slower since they setup a shared dependency for each test. 
![Integration Test](/unit-tests/imgs/integration-tests.png "Integration Test")<br/> 
### In Summary
Unit-tests, aim to test the business logic that can be isolated and they should be used the majority of the time. They should be:
- readable - always
- concise - always
- isolated - always
- fast - always
Integration tests aim to test shared dependencies, out-of-process dependencies, third-party libraries and niche scenarios. The should be used sparingly to confirm infrastructure, to test frameworks and shared/out-of-process dependencies. They should be:
- readable
- concise - not always
- isolated - not always
- fast - not always

## Avoid Brittle unit-tests
They are unit-tests that fail for wrong reasons, they cause false alarms. Unit-tests should test the function behaviour and not coding details.

## Writing Testable Code
To design good unit-tests you need testable code.<br/>
Code design impacts testability and design principles matter. The **design priciples** are:
- Separation of concerns: we keep business logic separate from user-interface logic and also different from the infrastructure code(data layers); 
- Have seams in the application: it is all about separating funcionalities and behaviours of the applications. There are specific classes for specific behaviours functionalities;
- Single Responsability (SOLID): the code containing each production class aim to achieve one specific behaviour and there is no secret behaviour;
- Encapsulation: only expose as public have those methods that the application needs. And those are the methods to unit-tests, the rest are provate methods, and so implementation details, hence helper methods. 
- Dependency injection: we supply the dependencies as part of the constructors;
- Depoendency inversion (SOLID): referencing the dependencies using interfaces.
The aim of these design principles is to create a **loosely coupled code**: all functionalities and behaviours within our application can be easily isolated so that we can unit-test them individually.

## Code Coverage
This is a percentage measure to work out how much unit-testing coverage you've got of your production code. The formula is:
```
Coverage = (lines executed)/(total number of lines)
```
The formula is calculated after you run your unit-tests. And it is basically the total lines od production code executed because you run your unit tests divided by the total number of production code lines and then it is converted to a percentage that state exactly how much test coverage you have got of your production code. <br/>
100% testing coverage is **NOT** the aim, otherwise developers will start to convert private methods to public methods only for the sake of unit-testing and they will test coding details, hence this will lead to brittle unit-tests. And we want to avoid that. 
