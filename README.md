# Interactive Campus Map

## About the Project

The Interactive Campus Map is a Python-based project designed to help students, faculty members and visitors find important locations on the VIT Bhopal campus. The program uses a CSV file to store location data and uses Pandas to read and process the data. Folium is used to create an interactive map with different coloured markers for different categories of locations. The program also provides a simple menu in the terminal through which the user can select different options according to their requirement. The user can view the campus map, search for a location, calculate the distance between two locations, find nearby locations, filter locations by category, view details of a particular location and display all available locations. The project is written in Python and is designed to be simple and easy to use.

## Features
The project provides the following options:

1. **View Campus Map** – Opens the interactive campus map showing the available locations.
2. **Search for a Location** – Allows the user to search for a particular campus location.
3. **Calculate Distance** – Calculates the approximate distance between two selected locations.
4. **Find Nearby Locations** – Finds locations that are close to a selected location.
5. **Filter Locations by Category** – Displays locations belonging to a selected category such as Academic, Food, Hostel, Library or Medical.
6. **View Location Details** – Displays the name, category and description of a selected location.
7. **Show All Locations** – Displays all locations stored in the project.
8. **Exit** – Closes the program.

The interactive map also includes coloured markers, location descriptions, a search box and a map legend.

## Technologies Used
* Python
* Pandas
* Folium
* Folium Search Plugin
* Math module

## Requirements
Python must be installed on the computer. The required Python libraries are listed in `requirements.txt`.

The project requires:

* pandas
* folium

## Project Structure
```text
interactive-campus-map
│
├── data
│   └── locations.csv
│
├── main.py
├── map_module.py
├── search_module.py
├── distance_module.py
├── location_module.py
├── campus_map.html
├── requirements.txt
├── README.md
├── statement.md
├── .gitignore
└── .gitattributes
```

The `data/locations.csv` file contains the location information used by the program. The The project is divided into separate Python modules based on their responsibilities. The `main.py` file handles the main menu and user interaction. The `map_module.py` file creates the interactive campus map. The `search_module.py` file handles searching, nearby locations and category filtering. The `distance_module.py` file handles distance calculation. The `location_module.py` file handles location details and displaying all locations.The `campus_map.html` file is generated automatically by Folium when the program creates the interactive map. The `requirements.txt` file contains the required Python libraries.

## Installation
First, open the project folder in VS Code or another Python editor.

Install the required libraries using:

```text
pip install -r requirements.txt
```

If a virtual environment is being used, activate it before installing the libraries.

## Running the Program
Run the following command from the project folder:

```text
python main.py
```

The program will create the interactive campus map and display the main menu in the terminal.

The menu provides the following options:

```text
1. View Campus Map
2. Search for a Location
3. Calculate Distance
4. Find Nearby Locations
5. Filter Locations by Category
6. View Location Details
7. Show All Locations
8. Exit
```

The user can enter the number of an option to perform the required operation.

## Viewing the Campus Map
When the user selects **View Campus Map**, the program opens the generated `campus_map.html` file in the web browser. The map contains markers for different campus locations.

Different marker colours are used for different categories. The map also contains a search option and a legend explaining the marker colours.

## Searching for a Location
The user can enter the name of a campus location. The program searches the stored location data and displays the matching location information.

The interactive map also provides a search box that can be used to find locations directly on the map.

## Calculating Distance
The distance option allows the user to select two locations from the available list. The program calculates the approximate distance between them using their latitude and longitude values.

The calculation uses the Haversine formula to find the distance between the two geographical points.

The result is displayed in kilometres.

## Finding Nearby Locations
The user can select a location and specify a distance range. The program checks the stored coordinates and displays locations that are within the selected range.

This can help users find places that are close to a particular campus location.

## Filtering Locations by Category
The user can select a category and view the locations belonging to that category.

Examples of categories include:

* Academic
* Food
* Shopping
* Library
* Medical
* Hostel
* Fitness
* Recreation
* Administration
* Student Services

## Viewing Location Details
The user can select a location to view its details. The program displays information such as the location name, category and description.

## Showing All Locations
The **Show All Locations** option displays all the locations stored in the CSV file along with their available information.

## Input Validation
The program checks user inputs where required. For example, while calculating distance, the program checks whether the entered location numbers are valid and whether the two selected locations are different. Invalid inputs are handled by displaying an appropriate message instead of stopping the program unexpectedly.

## Data Storage
The location information is stored in `data/locations.csv`.

The CSV file contains the following fields:

* ID
* Name
* Category
* Latitude
* Longitude
* Description

Keeping the data in a separate CSV file makes it easier to add or update campus locations without changing the main Python program.

## Output
The main output of the project is the interactive campus map generated as `campus_map.html`.

The terminal provides the menu and displays results for operations such as searching, filtering, viewing details, listing locations and calculating distances.

## GitHub Repository
The complete project, including the Python source code, CSV data, requirements file, README and project statement, is maintained in a GitHub repository.

## Conclusion
The Interactive Campus Map provides a simple way to explore important locations on the VIT Bhopal campus. It combines Python programming, CSV data handling, location-based calculations and an interactive map. The menu-based system gives the user different options for finding and viewing campus information. The project also demonstrates the use of functions, loops, conditions, file handling, Pandas and external Python libraries in a practical application.