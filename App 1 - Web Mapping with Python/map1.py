import folium
from folium.plugins import MarkerCluster
import pandas


data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation <3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[44.05423792776983, -121.318977164173], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(el)+ " m",
    fill_color=color_producer(el), color = 'gray', fill_opacity=0.7))

map.add_child(fg)

map.save("Map1.html")
