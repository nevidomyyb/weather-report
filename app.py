from decouple import config
import requests

token = config('TOKEN')
chat_code = config('CHAT_CODE')
google_code = config('API_GOOGLE')

def return_geolocation(city):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address=${city}&key={google_code}"
    response = requests.get(url)
    response = response.json()
    latitude = response["results"][0]["geometry"]["location"]["lat"]
    longitude = response["results"][0]['geometry']["location"]["lng"]
    name = response["results"][0]["formatted_address"]
    print(latitude, longitude, name)
    return latitude, longitude, name

def get_data(latitude, longitude):
    urlz = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,precipitation_probability,&forecast_days=1'
    responsez = requests.get(urlz)
    responsez = responsez.json()
    last_temperature_index = len(responsez["hourly"]["temperature_2m"]) - 1
    last_temperature = responsez["hourly"]["temperature_2m"][last_temperature_index]
    last_preciptation_probability_index = len(responsez["hourly"]["precipitation_probability"]) -1 
    last_preciptation_probability = responsez["hourly"]["precipitation_probability"][last_preciptation_probability_index]
    print(last_temperature, last_preciptation_probability)
    return last_temperature, last_preciptation_probability
    