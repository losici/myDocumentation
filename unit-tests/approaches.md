# Approaches to writing unit-tests
There are two approaches to write unit-tests:
- TLD: Test Last Developemnt - Writing the unit tests at the end aftwer you wrote the new features or you have done bug fixes.
- TDD: Test Driven Development - More common and also known as "Test First Development", where developers begin development by writing a test that fails and then they implement the new features, or bug fix. The developer is supposed to write minimal code to pass thwe test and refactor to improve the code design.

## TLD: Test Last Developemnt
Writing the unit tests at the end aftwer you wrote the new features or you have done bug fixes. It involves to code and desgin first, then test at the end. A disadvantage is that we write production code that is not testable because we didn't follow some design priciples. Also we might not use an exhaustive enough scenarios for laziness or lack of time.<br/> 

![TLD](/unit-tests/imgs/tld.png "TLD")<br/> 

## TDD: Test Driven Development
For each requirement for a specific feature you follow these steps:
1. Start with a failing test
1. Write minimal code to pass the test
1. Refactor code to improve the code design (applying design principles for clean coding, separate public behaviours from implementation details)<br/> 

![TDD](/unit-tests/imgs/tdd.png "TDD")<br/> 



