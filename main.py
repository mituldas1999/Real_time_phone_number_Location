import phonenumbers
import opencage
import folium
from myphone import number

from phonenumbers import geocoder

pepnumber=phonenumbers.parse(number)

location=geocoder.description_for_number(pepnumber,"en")
print(location)

from phonenumbers import carrier

service_provider= phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, 'en'))

from opencage.geocoder import OpenCageGeocode

key='f8ef1c43991c4d6595d0eb370f0002b8'
geocoder=OpenCageGeocode(key)

quary=str(location)
results=geocoder.geocode(quary)
#print(results)

lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']

print(lat,lng)

myMap=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(myMap)

myMap.save("myLocation.html")


