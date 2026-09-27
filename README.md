# Interactive Campus Map

## About the Project

This project is an interactive map of the campus. It shows different campus locations and provides information about them. It also allows the user to search for locations and calculate the distance between two locations.

The project is made using Python, Pandas and Folium.

## Features

- Shows different campus locations on an interactive map
- Uses different marker colours for different categories
- Shows the description of each location
- Allows users to search for a location
- Calculates the distance between two locations
- Checks for invalid location numbers

## Requirements

- Python 3
- Pandas
- Folium

## Project Structure

interactive-campus-map/
│
├── data/
│   └── locations.csv
├── main.py
├── README.md
├── requirements.txt
├── campus_map.html
├── .gitignore
└── .gitattributes

## Setup and Installation

1. Clone the repository using:
git clone https://github.com/Anjali-Sharma23/interactive-campus-map

2. Open the project folder:
cd interactive-campus-map

3. Create a virtual environment:
python -m venv .venv

4. Activate the virtual environment on Windows:
.venv\Scripts\activate

5. Install the required libraries:
pip install -r requirements.txt

The required libraries are Pandas and Folium.

## Configuration

The campus location data is stored in the file:

data/locations.csv

The CSV file contains the following columns:

name,category,latitude,longitude,description

The CSV file should remain inside the data folder.

## Running the Project

Run the following command from the project folder:

python main.py

The program creates an interactive map named:

campus_map.html

After running the program, open campus_map.html in a web browser to view the map.

The program also asks the user whether they want to calculate the distance between two locations.

## Distance Calculation

The program calculates the approximate distance between two selected campus locations using their latitude and longitude values. The Haversine formula is used to calculate the distance in kilometres.

## Input Validation

The program checks whether the entered location numbers are valid. It also prevents the user from selecting the same location twice when calculating the distance.

## Technologies Used

- Python
- Pandas
- Folium

## Output

The main output of the project is an interactive HTML map containing the different campus locations, coloured markers, location descriptions and a search option.

## Conclusion

The Interactive Campus Map provides a simple way to find important campus locations, view their information, search for places and calculate the approximate distance between two locations.