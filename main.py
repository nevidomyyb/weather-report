from apscheduler.schedulers.background import BackgroundScheduler
from telethon.sync import TelegramClient
from telethon import events
from app import *
from decouple import config
import asyncio
from telethon import errors

token = config('TOKEN')
api_hash = config('API_HASH')
api_id = config('API_ID')

try:
    client = TelegramClient('anon', api_id, api_hash)

    @client.on(events.NewMessage)
    async def my_event_handler(event):
        cidade = event.raw_text
        try:
            dados = return_geolocation(cidade)
            await asyncio.sleep(1)
            dados_1 = get_data(dados[0], dados[1])
            await asyncio.sleep(1)
            await event.reply(f"Olá, em {dados[2]} foram registrados:\nÚltima temperatura registrada foi de {dados_1[0]}°C\nE a probabilidade de chuva está em {dados_1[1]}%")
        except Exception as e:
            print(e)
            await event.reply(f"Essa cidade não existe amigo, tente novamente")

    client.start(bot_token=token)
    client.run_until_disconnected()
except errors.FloodWaitError as e:
    # Wait for the specified number of seconds before retrying
    wait_time = e.seconds
    print(f"Got FloodWaitError, waiting for {wait_time} seconds...")
    while wait_time > 0:
        print(f"Got FloodWaitError, waiting for {wait_time} seconds...")
        wait_time.sleep(30)
        wait_time -= 30
    print("Gotta!")
