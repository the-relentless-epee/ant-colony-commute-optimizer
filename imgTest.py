import geopy.geocoders
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.patches import Rectangle
import geopy

def get_coordinates(city_name):
    geolocator = geopy.geocoders.GoogleV3("AIzaSyBfojVOxAdn0XgNRvTNQd5FxLdIkiTxlpM")
    location = geolocator.geocode(city_name)
    return (location.latitude, location.longitude) if location else None

city_names = ["Delta, BC, CA", "Vancouver, BC, CA", "Langley, BC, CA", "Surrey, BC, CA", "Richmond, BC, CA", "Burnaby, BC, CA"]

cities = {}
for i in city_names:
    coordinates = get_coordinates(i)
    if coordinates:
        cities[i] = coordinates
    else:
        print(f"Could not find coordinates for {i}")

latitudes = [coord[0] for coord in cities.values()]
longitudes = [coord[1] for coord in cities.values()]

fig, ax = plt.subplots(figsize=(10, 8))

# Display the image as background
img = mpimg.imread('map.png')
ax.imshow(img, extent=[-123.2, -122.6, 49, 49.4], zorder=0)

# Plot the scatter plot
sc = ax.scatter(longitudes, latitudes, color='blue', marker='o', zorder=1)
ax.set_aspect('equal', adjustable='box')

# Annotate cities
for city, coord in cities.items():
    ax.annotate(city, (coord[1], coord[0]), textcoords="offset points", xytext=(0,10), ha='center', zorder=2)

# Set title and labels
plt.title('City Locations on a 2D Plot')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.axis([-123.2, -122.6, 49, 49.4])

# Add interactive features
plt.grid(True)  # Optional: adds a grid to the plot

# Ensure interactive mode is set correctly
plt.show()
