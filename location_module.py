def location_details(data):

    print("\nAvailable locations:")

    for i in range(len(data)):
        print(i + 1, data["name"][i])

    try:
        choice = int(input("\nEnter the location number: "))

        if choice < 1 or choice > len(data):
            print("\nInvalid location number.")
            return

        i = choice - 1

        print("\n==============================")
        print("Location Details")
        print("==============================")
        print("Name:", data["name"][i])
        print("Category:", data["category"][i])
        print("Latitude:", data["latitude"][i])
        print("Longitude:", data["longitude"][i])
        print("Description:", data["description"][i])

    except ValueError:
        print("\nPlease enter a valid number.")


def show_all_locations(data):

    print("\n==============================")
    print("All Campus Locations")
    print("==============================")

    for i in range(len(data)):

        print("\n", i + 1, ".", data["name"][i])
        print("Category:", data["category"][i])
        print("Description:", data["description"][i])