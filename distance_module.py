import math


def distance(lat1, lon1, lat2, lon2):

    radius = 6371

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

    return radius * c


def calculate_distance(data):

    print("\nAvailable locations:")

    for i in range(len(data)):
        print(i + 1, data["name"][i])

    try:
        first = int(input("\nEnter the number of the first location: "))
        second = int(input("Enter the number of the second location: "))

        if first < 1 or first > len(data) or second < 1 or second > len(data):
            print("\nInvalid location number.")

        elif first == second:
            print("\nPlease choose two different locations.")

        else:
            lat1 = data["latitude"][first - 1]
            lon1 = data["longitude"][first - 1]

            lat2 = data["latitude"][second - 1]
            lon2 = data["longitude"][second - 1]

            result = distance(lat1, lon1, lat2, lon2)

            print(
                "\nDistance between",
                data["name"][first - 1],
                "and",
                data["name"][second - 1],
                "is",
                round(result, 2),
                "km"
            )

    except ValueError:
        print("\nPlease enter valid numbers.")