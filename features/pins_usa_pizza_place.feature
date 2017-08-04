Feature: Test the Pins features of Power BI

  Scenario: I search for usa pizza place Pins
    Given I select the Analytics menu from the toolbar
    When  I select the Pins from the Analytics Menu
    And   In the search box, I enter this text - Pizza place in USA
    Then  One Pin will be display on the map area