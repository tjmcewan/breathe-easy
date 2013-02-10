Feature: driving the API

  Scenario: load the index
    Given we have our app bootstrapped
    when we hit the index page
    then we get a successful response
