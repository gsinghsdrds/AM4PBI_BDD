Feature: Add the USA density index demographic reference layer to the map

  Scenario: I will add USA density index demographic reference layer to the map.
    Given I open the Analytics menu from the toolbar
    When  I select the Reference layer from the Analytics menubar
    And   I select the demographic USA density index reference layer
    Then  I see that USA demographic density index reference layer on the map
