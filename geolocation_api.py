import requests
import json

class GeolocationAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://maps.googleapis.com/maps/api/geocode/json'

    def get_location(self, address):
        params = {
            'address': address,
            'key': self.api_key
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def handle_errors(self, response):
        if response.status_code == 400:
            return 'Invalid request'
        elif response.status_code == 401:
            return 'Unauthorized'
        elif response.status_code == 500:
            return 'Internal server error'
        else:
            return 'Unknown error'
