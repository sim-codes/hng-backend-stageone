from rest_framework.response import Response
from rest_framework.views import APIView
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv() 

GEOLOCATION_KEY=os.getenv('GEOLOCATION_KEY')
WEATHER_KEY=os.getenv('WEATHER_KEY')



# Return json response
def data_to_json(url):
    response = requests.get(url)
    data = json.loads(response.text)
    return data

class CityTemperatureView(APIView):
    def get(self, request):
        location_request_url = 'https://ipgeolocation.abstractapi.com/v1/?api_key=' + GEOLOCATION_KEY       
        loc_data = data_to_json(location_request_url)

        weather_request_url = f'https://api.openweathermap.org/data/2.5/weather?q={loc_data["city"]}&appid={WEATHER_KEY}'
        weather_data = data_to_json(weather_request_url)
        temp_in_celsius = int(weather_data['main']['temp'] - 273.15)

        visitor_name = request.query_params.get('visitor_name')

        print(int(weather_data['main']['temp'] - 273.15))
        return Response({
            "client_ip": loc_data['ip_address'],
            "location": loc_data['city'],
            "greeting": f"Hello, {visitor_name}! the temperature is {temp_in_celsius} degrees Celsius in {loc_data['city']}!"
            })
    