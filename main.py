from apscheduler.schedulers.background import BackgroundScheduler
from app import send_message
from time import sleep

scheduler = BackgroundScheduler()
scheduler.add_job(send_message, 'interval', hours=1)

scheduler.start()

while True:
    sleep(1)