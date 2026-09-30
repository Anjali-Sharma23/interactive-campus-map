import pandas as pd
import webbrowser

from map_module import create_map
from search_module import search_location, find_nearby, filter_category
from distance_module import calculate_distance
from location_module import location_details, show_all_locations


data = pd.read_csv("data/locations.csv")


while True:
    print("\n========================================")
    print("        INTERACTIVE CAMPUS MAP")
    print("========================================")
    print("1. View Campus Map")
    print("2. Search for a Location")
    print("3. Calculate Distance")
    print("4. Find Nearby Locations")
    print("5. Filter Locations by Category")
    print("6. View Location Details")
    print("7. Show All Locations")
    print("8. Exit")
    print("========================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_map(data)
        webbrowser.open("campus_map.html")
        print("\nCampus map opened successfully.")

    elif choice == "2":
        search_location(data)

    elif choice == "3":
        calculate_distance(data)

    elif choice == "4":
        find_nearby(data)

    elif choice == "5":
        filter_category(data)

    elif choice == "6":
        location_details(data)

    elif choice == "7":
        show_all_locations(data)

    elif choice == "8":
        print("\nThank you for using the Interactive Campus Map.")
        break

    else:
        print("\nInvalid choice. Please select a number from 1 to 8.")