import pandas as pd
import folium
from folium.plugins import Search
import math
import webbrowser

data = pd.read_csv("data/locations.csv")

def distance(lat1, lon1, lat2, lon2):
    r = 6371
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1)
        * math.cos(lat2)
        * math.sin(dlon / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return r * c

def create_map():
    lat = data["latitude"].mean()
    lon = data["longitude"].mean()
    m = folium.Map(
        location=[lat, lon],
        zoom_start=17,
        tiles="https://tile.openstreetmap.de/{z}/{x}/{y}.png",
        attr="© OpenStreetMap contributors"
    )
    colors = {
        "Academic": "blue",
        "Food": "red",
        "Shopping": "orange",
        "Library": "green",
        "Medical": "darkred",
        "Hostel": "purple",
        "Fitness": "darkgreen",
        "Recreation": "cadetblue",
        "Administration": "black",
        "Student Services": "pink"
    }
    markers = folium.FeatureGroup(name="Locations")
    markers.add_to(m)

    for i in range(len(data)):
        cat = data["category"].iloc[i]
        if cat in colors:
            color = colors[cat]
        else:
            color = "gray"

        marker = folium.Marker(
            [ data["latitude"].iloc[i], data["longitude"].iloc[i]],
            popup=data["description"].iloc[i],
            tooltip=data["name"].iloc[i],
            icon=folium.Icon(color=color)
        )
        marker.add_to(markers)
    search = {"type": "FeatureCollection","features": [] }

    for i in range(len(data)):
        place = {"type": "Feature", "properties": { "name": data["name"].iloc[i]},"geometry": { "type": "Point", "coordinates": [data["longitude"].iloc[i],data["latitude"].iloc[i] ] } }
        search["features"].append(place)

    layer = folium.GeoJson(
        search,
        name="Search Locations",
        style_function=lambda x: {"opacity": 0, "fillOpacity": 0}
    )
    layer.add_to(m)

    Search(
        layer=layer,
        search_label="name",
        placeholder="Search location",
        collapsed=False
    ).add_to(m)

    legend = """
    <div style="
    position: fixed;
    bottom: 30px;
    left: 30px;
    background-color: white;
    padding: 10px;
    border: 2px solid grey;
    z-index: 9999;
    font-size: 14px;
    ">
    <b>Map Legend</b><br>
    <span style="color:blue;">●</span> Academic<br>
    <span style="color:red;">●</span> Food<br>
    <span style="color:orange;">●</span> Shopping<br>
    <span style="color:green;">●</span> Library<br>
    <span style="color:purple;">●</span> Hostel<br>
    <span style="color:darkred;">●</span> Medical<br>
    <span style="color:darkgreen;">●</span> Fitness<br>
    <span style="color:cadetblue;">●</span> Recreation<br>
    <span style="color:black;">●</span> Administration<br>
    <span style="color:pink;">●</span> Student Services
    </div>
    """
    m.get_root().html.add_child(folium.Element(legend))
    m.save("campus_map.html")
    print("\nMap created successfully.")

def search_location():
    name = input("\nEnter the location name: ").strip().lower()
    found = False
    for i in range(len(data)):
        location_name = str(data["name"].iloc[i])
        if name in location_name.lower():
            print("LOCATION FOUND")
            print("Name        :", data["name"].iloc[i])
            print("Category    :", data["category"].iloc[i])
            print("Description :", data["description"].iloc[i])
            found = True
    if not found:
        print("\nLocation not found.")

def display_locations():
    print("\nAvailable Locations:")
    for i in range(len(data)):
        print( f"{i + 1}. {data['name'].iloc[i]}"
            f" [{data['category'].iloc[i]}]" )

def calculate_distance():
    display_locations()
    try:
        a = int(input("\nEnter the number of the first location: "))
        b = int(input("Enter the number of the second location: "))
        if a < 1 or a > len(data) or b < 1 or b > len(data):
            print("\nInvalid location number.")
        elif a == b:
            print("\nPlease choose two different locations.")
        else:
            lat1 = data["latitude"].iloc[a - 1]
            lon1 = data["longitude"].iloc[a - 1]
            lat2 = data["latitude"].iloc[b - 1]
            lon2 = data["longitude"].iloc[b - 1]
            d = distance(lat1, lon1, lat2, lon2)
            print("DISTANCE RESULT")
            print("From       :",data["name"].iloc[a - 1]  )

            print( "To         :", data["name"].iloc[b - 1] )

            print( "Distance   :", round(d, 2), "km" )

    except ValueError:
        print("\nPlease enter valid numbers.")

def find_nearby_locations():
    display_locations()
    try:
        location_number = int( input("\nEnter the location number: ") )
        if location_number < 1 or location_number > len(data):
            print("\nInvalid location number.")
            return
        radius = float(input("Enter radius in km: ") )
        if radius <= 0:
            print("\nRadius must be greater than 0.")
            return
        selected_lat = data["latitude"].iloc[location_number - 1]
        selected_lon = data["longitude"].iloc[location_number - 1]
        selected_name = data["name"].iloc[location_number - 1]
        nearby = []
        for i in range(len(data)):
            if i == location_number - 1:
                continue
            lat = data["latitude"].iloc[i]
            lon = data["longitude"].iloc[i]
            d = distance(selected_lat,selected_lon,lat,lon )

            if d <= radius:
                nearby.append( ( data["name"].iloc[i], data["category"].iloc[i],  d )  )

        nearby.sort(key=lambda x: x[2])

        print("NEARBY LOCATIONS")
        print( "Location :", selected_name )

        print( "Radius   :", radius, "km" )

        if len(nearby) == 0:
            print("No locations found within this radius.")
        else:
            for i, item in enumerate(nearby, start=1):
                print( f"{i}. {item[0]}"
                    f" [{item[1]}]"
                    f" - {round(item[2], 2)} km" )

    except ValueError:
        print("\nPlease enter valid numbers.")

def filter_by_category():
    categories = sorted(
        data["category"].dropna().unique() )

    print("LOCATION CATEGORIES")
    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}")

    try:
        choice = int( input("Choose a category: ") )
        if choice < 1 or choice > len(categories):
            print("\nInvalid category.")
            return
        selected_category = categories[choice - 1]
        filtered = data[ data["category"] == selected_category ]
        print(selected_category.upper(), "LOCATIONS")
        for i, (_, row) in enumerate( filtered.iterrows(),start=1 ):
            print(f"{i}. {row['name']}" )

        print( "Total locations:", len(filtered) )

    except ValueError:
        print("\nPlease enter a valid number.")

def view_location_details():
    display_locations()
    try:
        choice = int(input("\nEnter the location number: "))
        if choice < 1 or choice > len(data):
            print("\nInvalid location number.")
            return
        row = data.iloc[choice - 1]

        print("LOCATION DETAILS")
        print("Name        :", row["name"])
        print("Category    :", row["category"])
        print("Description :", row["description"])
        print("Latitude    :", row["latitude"])
        print("Longitude   :", row["longitude"])

    except ValueError:
        print("\nPlease enter a valid number.")

def show_all_locations():
    print("ALL CAMPUS LOCATIONS")

    for i in range(len(data)):
        print(f"{i + 1}. "
            f"{data['name'].iloc[i]}"
            f" [{data['category'].iloc[i]}]" )

    print( "Total locations:",len(data))

create_map()

while True:
    print("       INTERACTIVE CAMPUS MAP")
    print("1. View Campus Map")
    print("2. Search for a Location")
    print("3. Calculate Distance")
    print("4. Find Nearby Locations")
    print("5. Filter Locations by Category")
    print("6. View Location Details")
    print("7. Show All Locations")
    print("8. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        webbrowser.open("campus_map.html")
        print("\nOpening campus map...")
    elif choice == "2":
        search_location()
    elif choice == "3":
        calculate_distance()
    elif choice == "4":
        find_nearby_locations()
    elif choice == "5":
        filter_by_category()
    elif choice == "6":
        view_location_details()
    elif choice == "7":
        show_all_locations()
    elif choice == "8":
        print( "\nThank you for using the " "Interactive Campus Map.")
        break
    else:
        print(  "\nInvalid choice. " "Please select 1-8." )