Feature: Test the add lat and long feature

  Scenario: The user adds features to the map using latitude and longitude.
    Given I have loaded PowerBI and signed in as a free user
    When  User drag the latitude field into the Latitude field well
    And   I drag the longitude field into the Longitude field well
    And   I will make sure that latitude and longitude fields are not summarized
    Then  points should appear on the map in the correct lat/long position
    When  I go into edit mode
    Then the toolbar should not have the Location type button


