Feature: Check the availability of different basemaps in Basemap Panel

  Scenario: Change basemap to streetmap basemap
    Given user visit the Basemap Panel
    When  select streetmap basemap from the Basemap Panel
    Then  user will see that existing basemap will change to streetmap basemap


  Scenario: User will change basemap from streetmap to lightcanvas basemap
    Given Basemap panel is open for the user
    When  select lightcanvas basemap from the Basemap Panel
    Then  user will see that existing basemap will change to lightcanvas basemap


  Scenario: User will change basemap from lightcanvas to darkgraycanvas basemap
    When  select darkgraycanvas basemap from the Basemap Panel
    Then  user will see that existing basemap will change to darkgraycanvas basemap
    Then  user will close the Basemap panel