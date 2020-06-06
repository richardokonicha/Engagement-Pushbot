from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
import datetime
scheduler = BlockingScheduler(timezone='utc')
from features.round import round_func
import os
from dotenv import load_dotenv
load_dotenv()

CRON = os.getenv("CRON")

# @scheduler.scheduled_job('cron', CronTrigger.from_crontab(CRON), id="cron", )


def triggerround():
    print("triggering round")
    round_func()

scheduler.add_job(triggerround, CronTrigger.from_crontab(CRON))
scheduler.print_jobs()
scheduler.start()
