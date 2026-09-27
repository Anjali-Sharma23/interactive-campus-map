import pandas as pd
import folium
from folium.plugins import Search
import math

data = pd.read_csv("data/locations.csv")

def distance(lat1, lon1, lat2, lon2):
    r = 6371
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return r * c

lat = data["latitude"].mean()
lon = data["longitude"].mean()

m = folium.Map(location=[lat, lon], zoom_start=17)

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
    cat = data["category"][i]
    if cat in colors:
        color = colors[cat]
    else:
        color = "gray"

    marker = folium.Marker(
        [data["latitude"][i], data["longitude"][i]],
        popup=data["description"][i],
        tooltip=data["name"][i],
        icon=folium.Icon(color=color)
    )

    marker.add_to(markers)

search = {
    "type": "FeatureCollection",
    "features": []
}

for i in range(len(data)):
    place = {
        "type": "Feature",
        "properties": {
            "name": data["name"][i]
        },
        "geometry": {
            "type": "Point",
            "coordinates": [
                data["longitude"][i],
                data["latitude"][i]
            ]
        }
    }
    search["features"].append(place)

layer = folium.GeoJson(
    search,
    name="Search Locations",
    style_function=lambda x: {
        "opacity": 0,
        "fillOpacity": 0
    }
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

print("Map created successfully")

ch = input("\nDo you want to calculate the distance between two locations? (yes/no): ")

if ch.lower() == "yes":
    print("\nAvailable locations:")

    for i in range(len(data)):
        print(i + 1, data["name"][i])

    a = int(input("\nEnter the number of the first location: "))
    b = int(input("Enter the number of the second location: "))

    if a < 1 or a > len(data) or b < 1 or b > len(data):
        print("\nInvalid location number.")
    elif a == b:
        print("\nPlease choose two different locations.")
    else:
        lat1 = data["latitude"][a - 1]
        lon1 = data["longitude"][a - 1]
        lat2 = data["latitude"][b - 1]
        lon2 = data["longitude"][b - 1]
        d = distance(lat1, lon1, lat2, lon2)
        print("\nDistance between", data["name"][a - 1],
              "and", data["name"][b - 1],
              "is", round(d, 2), "km")