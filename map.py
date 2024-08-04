import geopy.geocoders
import matplotlib.pyplot as plt
import geopy

imgWidth = 0 #in pixels
imgHeight = 0

l = -123.2
r = -122.6
t = 49.4
b = 49

imgScale = 839/1149750
img_x_offset = -0.0980 #coordinate values
img_y_offset = -0.0510



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





fig, map = plt.subplots(figsize=(10, 8))

img= plt.imread("map.png")
imgHeight, imgWidth = img.shape[:2]

imgL = l+img_x_offset
imgR = imgWidth*imgScale+imgL
imgB = b+img_y_offset
imgT = imgHeight*imgScale+imgB

map.imshow(img, extent=[imgL, imgR, imgB, imgT])
plt.scatter(longitudes, latitudes, color='blue', marker='o')
plt.gca().set_aspect('equal', adjustable='box')


for city, coord in cities.items():
    plt.annotate(city, (coord[1], coord[0]), textcoords="offset points", xytext=(0,10), ha='center')

plt.title('City Locations on a 2D Plot')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.axis([l, r, b, t])


#plt.grid(True)
plt.show()
