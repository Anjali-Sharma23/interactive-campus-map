import pandas as pd
import folium
from folium.plugins import Search
import json

locations = pd.read_csv("data/locations.csv")

lat = locations["latitude"].mean()
lon = locations["longitude"].mean()

campus_map = folium.Map(
    location=[lat, lon],
    zoom_start=17
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

marker_group = folium.FeatureGroup(name="Locations").add_to(campus_map)

for i in range(len(locations)):
    category = locations["category"][i]

    if category in colors:
        color = colors[category]
    else:
        color = "gray"

    folium.Marker(
        [locations["latitude"][i], locations["longitude"][i]],
        popup=locations["description"][i],
        tooltip=locations["name"][i],
        icon=folium.Icon(color=color)
    ).add_to(marker_group)

search_data = {
    "type": "FeatureCollection",
    "features": []
}

for i in range(len(locations)):

    feature = {
        "type": "Feature",
        "properties": {
            "name": locations["name"][i]
        },
        "geometry": {
            "type": "Point",
            "coordinates": [
                locations["longitude"][i],
                locations["latitude"][i]
            ]
        }
    }

    search_data["features"].append(feature)

search_layer = folium.GeoJson(
    search_data,
    name="Search Locations",
    style_function=lambda x: {
        "opacity": 0,
        "fillOpacity": 0
    }
)

search_layer.add_to(campus_map)

Search(
    layer=search_layer,
    search_label="name",
    placeholder="Search location",
    collapsed=False
).add_to(campus_map)

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

campus_map.get_root().html.add_child(folium.Element(legend))


campus_map.save("campus_map.html")

print("Map created successfully")