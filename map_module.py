import folium
from folium.plugins import Search


def create_map(data):

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

        category = data["category"][i]

        if category in colors:
            color = colors[category]
        else:
            color = "gray"

        marker = folium.Marker(
            [data["latitude"][i], data["longitude"][i]],
            popup=data["description"][i],
            tooltip=data["name"][i],
            icon=folium.Icon(color=color)
        )

        marker.add_to(markers)

    search_data = {
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

        search_data["features"].append(place)

    layer = folium.GeoJson(
        search_data,
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

    print("\nMap created successfully.")