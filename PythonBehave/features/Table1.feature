Feature: Showing off behave
@smoke
  Scenario: Run a simple test
    Given we have behave installed
     When we implement numOf tests
     |num|
     |5  |
     Then behave will test them for us!