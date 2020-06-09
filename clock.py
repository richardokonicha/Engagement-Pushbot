from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
import datetime
from features.round import round_func
import os
from dotenv import load_dotenv
from rq import Queue
from worker import conn

scheduler = BlockingScheduler(timezone='utc')
q = Queue(connection=conn)

load_dotenv()
CRON = os.getenv("CRON")


def triggerround():
    result = q.enqueue(round_func)
    print("triggering round", result)


scheduler.add_job(triggerround, CronTrigger.from_crontab(CRON))
scheduler.print_jobs()
scheduler.start()