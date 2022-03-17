import folium
map = folium.Map(location=[50.404536445610404, 30.33755341976802], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[50.3, 30.4], popup="Hi I am a Marker", icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("Map1.html")
