from geopy.geocoders import Nominatim # from animal.dog import Dog와 같음
geolocator = Nominatim(user_agent="hong")
location = geolocator.geocode("Incheon, South Korea")

# pip install geopy -> geopy 설치 (터미널에서)

print(location.address)
print(location.latitude)
print(location.longitude)
print(location.raw)