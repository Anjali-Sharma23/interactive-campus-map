from distance_module import distance


def search_location(data):

    name = input("\nEnter the location name: ").strip().lower()

    found = False

    for i in range(len(data)):

        if name in data["name"][i].lower():

            print("\nLocation:", data["name"][i])
            print("Category:", data["category"][i])
            print("Description:", data["description"][i])

            found = True

    if not found:
        print("\nLocation not found.")


def find_nearby(data):

    print("\nAvailable locations:")

    for i in range(len(data)):
        print(i + 1, data["name"][i])

    try:
        choice = int(input("\nEnter the number of the location: "))
        limit = float(input("Enter distance range in km: "))

        if choice < 1 or choice > len(data):
            print("\nInvalid location number.")
            return

        lat1 = data["latitude"][choice - 1]
        lon1 = data["longitude"][choice - 1]

        found = False

        print("\nLocations within", limit, "km:")

        for i in range(len(data)):

            if i == choice - 1:
                continue

            lat2 = data["latitude"][i]
            lon2 = data["longitude"][i]

            d = distance(lat1, lon1, lat2, lon2)

            if d <= limit:
                print(
                    data["name"][i],
                    "-",
                    round(d, 2),
                    "km"
                )
                found = True

        if not found:
            print("No nearby locations found.")

    except ValueError:
        print("\nPlease enter valid numbers.")


def filter_category(data):

    categories = data["category"].unique()

    print("\nAvailable categories:")

    for i in range(len(categories)):
        print(i + 1, categories[i])

    try:
        choice = int(input("\nEnter the category number: "))

        if choice < 1 or choice > len(categories):
            print("\nInvalid category number.")
            return

        selected = categories[choice - 1]

        print("\nLocations in", selected, "category:")

        found = False

        for i in range(len(data)):

            if data["category"][i] == selected:
                print(
                    i + 1,
                    data["name"][i]
                )
                found = True

        if not found:
            print("\nNo locations found.")

    except ValueError:
        print("\nPlease enter a valid number.")