Feature: Explaining example in behave
@smoke
  Scenario Outline: Run a simple test
    Given we have behave installed
     When we implement <num> tests
     Then behave will test them for us!
 Examples: Numbers
    |num|
    |5  |
    |4  |