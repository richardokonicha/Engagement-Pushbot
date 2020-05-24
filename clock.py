from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
scheduler = BlockingScheduler()
from features.round import round_func
import os
from dotenv import load_dotenv
load_dotenv()

minute = os.getenv("MINUTE")
hour=os.getenv("HOUR")

# knowit = datetime.datetime.now() + datetime.timedelta(seconds=10)
# @scheduler.scheduled_job('cron', id="run_every_2_min", minute='*/2' , args=['yougo'])
# def hello(text):
#     print("hello world yess", text)

@scheduler.scheduled_job('cron', id="run_every_2_min", minute=minute, hour=hour )
def triggerround():
    print("triggering round")
    round_func()

scheduler.start()
