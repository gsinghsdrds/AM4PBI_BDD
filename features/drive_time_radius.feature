Feature: create a drive time and radius around a location in USA

	Scenario Outline: I will create a drive time and radius around a location in USA
		Given I load the USA_Cities dataset to the Esri Viz
		When  I select a single city feature point on the map
		When  Click on the Analytics in the ToolBar
		When  Click on Analytcs menu from the Maps for PowerBI toolbar
        When  I created <drivetimetype> of <mins> minutes around a location in USA
        Then  I will see <drivetimetype> of <mins> minutes on the map
		Then  zoom to extent and close the drive time panel of <mins> minutes


	Examples:
		| drivetimetype | mins   |
        | Drive time    | 10     |
        | Radius        | 10     |
        | Radius        | 30     |
        | Radius        | 101    |
        | Drive time    | 31     |
		| Radius        | -10    |
        | Drive time    | -10    |
        | Radius        | *$@    |
        | Drive time    | #&@    |







