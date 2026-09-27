# Interactive Campus Map

## About the Project

This project is an interactive map of the campus. It helps users find different locations on the campus and view information about them.

The project is made using Python and uses the Folium and Pandas libraries.

## Features

* Shows different campus locations on an interactive map
* Uses different marker colours for different categories
* Shows the description of a location when its marker is clicked
* Allows users to search for a location
* Calculates the distance between two selected locations
* Checks for invalid location numbers

## Technologies Used

* Python
* Pandas
* Folium

## Project Files

* `main.py` - Main Python program
* `data/locations.csv` - Contains the location names, categories, coordinates and descriptions
* `campus_map.html` - Generated interactive map
* `README.md` - Project information

## How to Run

1. Open the project folder in VS Code.
2. Make sure the required libraries are installed.
3. Run `main.py`.
4. The program creates `campus_map.html`.
5. Open the HTML file to view the interactive map.
6. The program also gives an option to calculate the distance between two locations.

## Distance Calculation

The distance between two locations is calculated using the Haversine formula. The latitude and longitude of the two locations are used to calculate the approximate distance in kilometres.

## Conclusion

The Interactive Campus Map makes it easier to locate important places on the campus and find the distance between different locations.
# interactive-campus-map
A Python-based interactive campus navigation and information system.
