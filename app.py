from decouple import config
import requests
token = config('TOKEN')

   
def get_data():
    url = 'https://api.open-meteo.com/v1/forecast?latitude=-9.65&longitude=-35.73&hourly=temperature_2m,precipitation_probability,&forecast_days=1'
    request = requests.get(url)
    response = request.json()
    last_temperature_index = len(response["hourly"]["temperature_2m"]) - 1
    last_temperature = response["hourly"]["temperature_2m"][last_temperature_index]
    last_preciptation_probability_index = len(response["hourly"]["precipitation_probability"]) -1 
    last_preciptation_probability = response["hourly"]["precipitation_probability"][last_preciptation_probability_index]
    return [last_temperature, last_preciptation_probability]
    
def send_message():
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    temperature, precipitation_chance = get_data()
    text_ola = f"Olá!"
    text_temperatura = f"A ultima temperatura registrada foi de {temperature}°C"
    text_probabilidade = f"E a probabilidade de chance está em {precipitation_chance}%"
    params_ola = get_params(text_ola)
    params_temperatura = get_params(text_temperatura)
    params_probabilidade = get_params(text_probabilidade)
    response = requests.get(url, params=params_ola)
    response = requests.get(url, params=params_temperatura)
    response = requests.get(url, params=params_probabilidade)

def get_params(text):
    params = {
        "chat_id": -992332908,
        "text": text,
        "parse_mode": "HTML"
    }
    return params

send_message()