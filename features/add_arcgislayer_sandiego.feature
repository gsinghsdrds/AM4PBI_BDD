Feature: add the arcgis layer from san diego about places to visit

  Scenario: I will add the arcgis layer from the san diego
    Given I go to the Analytics menu
    When  I click on the Reference layer from the Analytics menu
    And   I select the ArcGIS label in the Reference layer window
    And   I enter the text San Diego in the search box
    And   I select the san diego layer from the panel
    And   I close the reference layer panel
    Then  I see San Diego layer about places to go on the map
