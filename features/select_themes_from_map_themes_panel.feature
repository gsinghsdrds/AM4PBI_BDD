Feature: Customer will switch between different available Map themes in Map Themes Panel

	Scenario Outline: Test map themes for Heat Map, Location Only, Clustering
		Given Customer opens the Map themes Panel
		When  Customer go to  "<mapthemes>" Map theme
        Then  Customer expects "<mapthemes>" map theme will open


	Examples:
		| mapthemes	|
		| Heat Map 	|
		| Clustering  |
        | Location Only     |