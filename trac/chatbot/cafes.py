import time
import requests
from colorama import Fore, Style
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from .constants import *

class CafeLogic:
    def __init__(self, max_results=20, user_agent="location_lookup"):
        self.max_results = max_results
        self.geolocator = Nominatim(user_agent=user_agent)

    def get_location_from_postal_code(self, postal_code):
        try:
            location = self.geolocator.geocode(postal_code)
            if location:
                return location.latitude, location.longitude
            print(LOCATION_NOT_FOUND.format(postal_code))
        except Exception as e:
            print(LOCATION_ERROR.format(e))
        return None, None

    def find_nearby_cafes(self, lat, lon, radius):
        overpass_url = "http://overpass-api.de/api/interpreter"
        radius_meters = int(radius * 1609.34)
        query = f"""
        [out:json];
        node["amenity"="cafe"](around:{radius_meters},{lat},{lon});
        out;
        """
        try:
            response = requests.get(overpass_url, params={'data': query})
            response.raise_for_status()
            data = response.json()
            cafes_found = 0
            elements = data.get('elements', [])
            if not elements:
                print(NO_CAFES_IN_RADIUS)
                return False
            print(CAFES_WITHIN_RADIUS.format(radius, self.max_results))
            for element in elements:
                if cafes_found >= self.max_results:
                    break
                place_lat = element.get('lat')
                place_lon = element.get('lon')
                place_name = element.get('tags', {}).get('name')
                if place_name and place_lat and place_lon:
                    distance_km = geodesic((lat, lon), (place_lat, place_lon)).kilometers
                    distance_miles = distance_km * 0.621371
                    print(CAFE_INFO.format(place_name, distance_miles))
                    cafes_found += 1
            if cafes_found == 0:
                print(NO_NAMED_CAFES)
                return False
            return True
        except requests.RequestException as e:
            print(CAFE_FETCH_ERROR.format(e))
            return False

    def run(self):
        while True:
            postal_code = input(ENTER_POSTAL_CODE)
            lat, lon = self.get_location_from_postal_code(postal_code)
            if lat is not None and lon is not None:
                try:
                    radius = float(input(ENTER_RADIUS))
                    return self.find_nearby_cafes(lat, lon, radius)
                except ValueError:
                    print(INVALID_RADIUS_INPUT)
            else:
                print(INVALID_POSTAL_CODE)