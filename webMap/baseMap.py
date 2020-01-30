import folium
from folium import FeatureGroup, Popup, Icon 

map  = folium.Map(location=[33.086561, -96.829191], zoom_start=11, tiles = "Stamen Terrain")

fg = FeatureGroup(name = "My Map")
fg.add_child(folium.Marker(location = [33.086561, -96.829191], popup = Popup("I used to work here! ", max_width=300), icon = Icon(color = "green")))

map.add_child(fg)
map.save("Map1.html")
