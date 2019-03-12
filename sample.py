import folium
import pandas
data=pandas.read_csv("low.csv")
data1=pandas.read_csv("medium.csv")
data2=pandas.read_csv("high.csv")
data3=pandas.read_csv("deep.csv")
dir(folium)
map=folium.Map(location=[14.67,77.58],zoom_start=10)
fg=folium.FeatureGroup(name="My Map")
lat=list(data["latitute"])
latm=list(data1["latitute"])
lath=list(data2["latitute"])
latd=list(data3["latitute"])
print(lat)


lan=list(data["Longitude"])
lanm=list(data1["Longitude"])
lanh=list(data2["Longitude"])
land=list(data3["Longitude"])

loc=list(data["Location"])
loc1=list(data1["Location"])
loc2=list(data2["Location"])
loc3=list(data3["Location"])

for lt,ln,lc in zip(lat,lan,loc):
    fg.add_child(folium.Marker(location=[lt,ln],popup=str(lc),icon=folium.Icon(color='green')))
    
for ltm,lnm,lc1 in zip(latm,lanm,loc1):
    fg.add_child(folium.Marker(location=[ltm,lnm],popup=str(lc1),icon=folium.Icon(color='orange')))
for lth,lnh,lc2 in zip(lath,lanh,loc2):
    fg.add_child(folium.Marker(location=[lth,lnh],popup=str(lc2),icon=folium.Icon(color='red')))
for ltd,lnd,lc3 in zip(latd,land,loc3):
    fg.add_child(folium.Marker(location=[ltd,lnd],popup=str(lc3),icon=folium.Icon(color='blue')))

map.add_child(fg)
map.save("Map.html")
