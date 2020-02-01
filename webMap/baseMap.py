import pandas
import folium
from folium import FeatureGroup, Popup, Icon, CircleMarker, GeoJson, LayerControl

map  = folium.Map(location=[41.935475, -99.648585], zoom_start=5, tiles = "Stamen Terrain")

fgv = FeatureGroup(name = "Volcanoes")
fgp = FeatureGroup(name = "Population")

data = pandas.read_csv("Volcanoes.txt")
# data.columns # would return columns in data
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

html = """<h4>Volcano information:</h4>
Height: %s m
"""
def color_selector(elevation):
    if 3000 <= elevation  :
        return 'red'
    elif 1200 <= elevation < 3000:
        return 'orange'
    else:
        return 'green'
for latitude, longtitude, elevation in zip(lat, lon, elev):
    iframe = folium.IFrame(html=html % str(elevation), width=200, height=100)   
    
    fgv.add_child(CircleMarker(location = [latitude, longtitude], radius = 7, popup = Popup(iframe), fill_color= color_selector(elevation), 
        color = 'white', fill_opacity = 0.6))

fgp.add_child(GeoJson(data = open("world.json", "r", encoding = "utf-8-sig").read(), 
    style_function = lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 
    'orange' if 10000000 <= x['properties']['POP2005'] < 30000000  else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
# You need to add layer control after other layers
map.add_child(LayerControl())
map.save("Map1.html")
